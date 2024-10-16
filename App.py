import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import sqlite3

# Ruta de la base de datos
db_path = './Database/NFL_database.db'

# Función para obtener los datos de la base de datos
def get_data(query):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Diccionario de colores para cada posición
color_discrete_map = {
    'QB': '#636EFA',
    'WR': '#EF553B',
    'RB': '#00CC96',
    'TE': '#AB63FA',
    'FB': '#FFA15A',
    'P': '#19D3F3',
    'K': '#FF6692',
    'LB': '#B6E880',
    'CB': '#FF97FF',
    'S': '#FECB52',
    'DT': '#D3D3D3',
    'OT': '#8B0000',
    'C': '#B8860B',
    'G': '#7FFF00',
}

# Consultas para los datos de Passing, Rushing y Receiving, obteniendo también el año desde Player_season
query_passing = """
    SELECT ps.Posicion AS Position, COUNT(*) AS Count, ps.Anio AS Year
    FROM Statistics s
    JOIN Player_season ps ON s.Player_ID = ps.Player_ID
    WHERE s.Type_ID = 1
    GROUP BY ps.Posicion, ps.Anio
"""
query_rushing = """
    SELECT ps.Posicion AS Position, COUNT(*) AS Count, ps.Anio AS Year
    FROM Statistics s
    JOIN Player_season ps ON s.Player_ID = ps.Player_ID
    WHERE s.Type_ID = 2
    GROUP BY ps.Posicion, ps.Anio
"""
query_receiving = """
    SELECT ps.Posicion AS Position, COUNT(*) AS Count, ps.Anio AS Year
    FROM Statistics s
    JOIN Player_season ps ON s.Player_ID = ps.Player_ID
    WHERE s.Type_ID = 3
    GROUP BY ps.Posicion, ps.Anio
"""

# Inicializar la aplicación Dash con título personalizado y favicon
app = dash.Dash(__name__)
app.title = "NFL Stats Dashboard"  # Cambia esto al nombre que deseas mostrar


app._favicon = 'nfl_logo.ico'  # Asegúrate de que el archivo 'favicon.ico' esté en la carpeta 'assets'

# Layout del dashboard
app.layout = html.Div([
    html.H1("Estadísticas de la NFL", style={'text-align': 'center', 'padding-top': '30px'}),
    
    html.Div([
        dcc.Dropdown(
            id='year-pie-chart',
            placeholder='Filtrar por año',
            style={'width': '30%', 'margin-left': 'auto'}
        )
    ], style={'display': 'flex', 'justify-content': 'flex-end', 'padding': '20px'}),
    
    html.Div([
        html.Div(dcc.Graph(id='passing-pie-chart'), style={'width': '33%', 'padding': '10px'}),
        html.Div(dcc.Graph(id='rushing-pie-chart'), style={'width': '33%', 'padding': '10px'}),
        html.Div(dcc.Graph(id='receiving-pie-chart'), style={'width': '33%', 'padding': '10px'}),
    ], style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center'}),
])

@app.callback(
    Output('year-pie-chart', 'options'),
    Input('year-pie-chart', 'value')
)
def update_year_options(selected_year):
    df = get_data(query_passing)
    years = df['Year'].unique()
    return [{'label': str(year), 'value': str(year)} for year in sorted(years)]

@app.callback(
    [Output('passing-pie-chart', 'figure'),
     Output('rushing-pie-chart', 'figure'),
     Output('receiving-pie-chart', 'figure')],
    [Input('year-pie-chart', 'value')]
)
def update_pie_charts(selected_year):
    data_passing = get_data(query_passing)
    data_rushing = get_data(query_rushing)
    data_receiving = get_data(query_receiving)

    if selected_year:
        data_passing = data_passing[data_passing['Year'] == int(selected_year)]
        data_rushing = data_rushing[data_rushing['Year'] == int(selected_year)]
        data_receiving = data_receiving[data_receiving['Year'] == int(selected_year)]

    fig_passing = px.pie(
        data_passing, 
        names='Position', 
        values='Count',
        title=f'Estadísticas de pases por posición - {selected_year if selected_year else "All Years"}',
        hole=0.4,
        color='Position',
        color_discrete_map=color_discrete_map
    )
    fig_passing.update_traces(textinfo='percent+label', textposition='inside')
    fig_passing.update_layout(showlegend=True, height=500)

    fig_rushing = px.pie(
        data_rushing, 
        names='Position', 
        values='Count',
        title=f'Estadísticas de carreras por posición - {selected_year if selected_year else "All Years"}',
        hole=0.4,
        color='Position',
        color_discrete_map=color_discrete_map
    )
    fig_rushing.update_traces(textinfo='percent+label', textposition='inside')
    fig_rushing.update_layout(showlegend=True, height=500)

    fig_receiving = px.pie(
        data_receiving, 
        names='Position', 
        values='Count',
        title=f'Estadísticas de recepción por posición - {selected_year if selected_year else "All Years"}',
        hole=0.4,
        color='Position',
        color_discrete_map=color_discrete_map
    )
    fig_receiving.update_traces(textinfo='percent+label', textposition='inside')
    fig_receiving.update_layout(showlegend=True, height=500)

    return fig_passing, fig_rushing, fig_receiving

if __name__ == '__main__':
    app.run_server(debug=True)
