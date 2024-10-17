import dash
from dash import dcc, html, dash_table
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

# Querys para mostrar los datos en el dashboard
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

query_passing_top = ('''
    WITH RankedData AS (
        SELECT
            ps.Name,
            t.Team_name AS Team,
            ps.Posicion AS Position,
            ps.Anio AS Year,
            SUM(s.Yards) AS Total_Yards,
            SUM(s.Touchdowns) AS Total_Touchdowns,
            ROW_NUMBER() OVER (PARTITION BY ps.Anio ORDER BY SUM(s.Yards) DESC) AS rank
        FROM
            Statistics s
        JOIN
            Player_season ps ON s.Player_ID = ps.Player_ID
        JOIN
            Teams t ON ps.Team_ID = t.Team_ID
        WHERE
            s.Type_ID = 1
        GROUP BY
            ps.Anio, ps.Name, t.Team_name, ps.Posicion
    )
    SELECT
        Name, Team, Position, Year, Total_Yards, Total_Touchdowns
    FROM
        RankedData
    WHERE
        rank <= 10
    ORDER BY
        Year, Total_Yards DESC;
''')

query_rushing_top = ('''
    WITH RankedData AS (
        SELECT
            ps.Name,
            t.Team_name AS Team,
            ps.Posicion AS Position,
            ps.Anio AS Year,
            SUM(s.Yards) AS Total_Yards,
            SUM(s.Touchdowns) AS Total_Touchdowns,
            ROW_NUMBER() OVER (PARTITION BY ps.Anio ORDER BY SUM(s.Yards) DESC) AS rank
        FROM
            Statistics s
        JOIN
            Player_season ps ON s.Player_ID = ps.Player_ID
        JOIN
            Teams t ON ps.Team_ID = t.Team_ID
        WHERE
            s.Type_ID = 2
        GROUP BY
            ps.Anio, ps.Name, t.Team_name, ps.Posicion
    )
    SELECT
        Name, Team, Position, Year, Total_Yards, Total_Touchdowns
    FROM
        RankedData
    WHERE
        rank <= 10
    ORDER BY
        Year, Total_Yards DESC;
''')

query_receiving_top = ('''
    WITH RankedData AS (
        SELECT
            ps.Name,
            t.Team_name AS Team,
            ps.Posicion AS Position,
            ps.Anio AS Year,
            SUM(s.Yards) AS Total_Yards,
            SUM(s.Touchdowns) AS Total_Touchdowns,
            ROW_NUMBER() OVER (PARTITION BY ps.Anio ORDER BY SUM(s.Yards) DESC) AS rank
        FROM
            Statistics s
        JOIN
            Player_season ps ON s.Player_ID = ps.Player_ID
        JOIN
            Teams t ON ps.Team_ID = t.Team_ID
        WHERE
            s.Type_ID = 3
        GROUP BY
            ps.Anio, ps.Name, t.Team_name, ps.Posicion
    )
    SELECT
        Name, Team, Position, Year, Total_Yards, Total_Touchdowns
    FROM
        RankedData
    WHERE
        rank <= 10
    ORDER BY
        Year, Total_Yards DESC;
''')

query_passing_efficiency =('''
    WITH RankedData AS (
        SELECT
            ps.Name AS Name,
            t.Team_name AS Team,
            ps.Anio AS Year,
            SUM(s.ATT) AS ATT,
            SUM(s.Touchdowns) AS Touchdowns,
            CASE WHEN SUM(s.Touchdowns) > 0 THEN ROUND(CAST(SUM(s.ATT) AS REAL) / SUM(s.Touchdowns), 2) ELSE NULL END AS Attempts_Per_TD,
            ROW_NUMBER() OVER (PARTITION BY ps.Anio ORDER BY CASE WHEN SUM(s.Touchdowns) > 0 THEN ROUND(CAST(SUM(s.ATT) AS REAL) / SUM(s.Touchdowns), 2) ELSE NULL END ASC) AS rank
        FROM
            Statistics s
        JOIN
            Player_season ps ON s.Player_ID = ps.Player_ID
        JOIN
            Teams t ON ps.Team_ID = t.Team_ID
        WHERE
            s.Type_ID = 1 
        GROUP BY
            ps.Name, t.Team_name, ps.Anio
        HAVING
            SUM(s.Touchdowns) > 0 
            AND SUM(s.ATT) >= 100 
    )
    SELECT
        Name,
        Team,
        Year,
        ATT,
        Touchdowns,
        Attempts_Per_TD
    FROM
        RankedData
    WHERE
        rank <= 10
    ORDER BY
        Year ASC,
        Attempts_Per_TD ASC;

''')

query_rushing_efficiency = ('''
    WITH RankedData AS (
        SELECT
            ps.Name AS Name,
            t.Team_name AS Team,
            ps.Anio AS Year,
            SUM(s.ATT) AS ATT,
            SUM(s.Touchdowns) AS Touchdowns,
            CASE WHEN SUM(s.Touchdowns) > 0 THEN ROUND(CAST(SUM(s.ATT) AS REAL) / SUM(s.Touchdowns), 2) ELSE NULL END AS Attempts_Per_TD,
            ROW_NUMBER() OVER (PARTITION BY ps.Anio ORDER BY CASE WHEN SUM(s.Touchdowns) > 0 THEN ROUND(CAST(SUM(s.ATT) AS REAL) / SUM(s.Touchdowns), 2) ELSE NULL END ASC) AS rank
        FROM
            Statistics s
        JOIN
            Player_season ps ON s.Player_ID = ps.Player_ID
        JOIN
            Teams t ON ps.Team_ID = t.Team_ID
        WHERE
            s.Type_ID = 2 
        GROUP BY
            ps.Name, t.Team_name, ps.Anio
        HAVING
            SUM(s.Touchdowns) > 0 
            AND SUM(s.ATT) >= 200 
    )
    SELECT
        Name,
        Team,
        Year,
        ATT,
        Touchdowns,
        Attempts_Per_TD
    FROM
        RankedData
    WHERE
        rank <= 10
    ORDER BY
        Year ASC,
        Attempts_Per_TD ASC;
''')

query_receiving_efficiency = ('''
    WITH RankedData AS (
        SELECT
            ps.Name AS Name,
            t.Team_name AS Team,
            ps.Anio AS Year,
            SUM(s.ATT) AS ATT,
            SUM(s.Touchdowns) AS Touchdowns,
            CASE WHEN SUM(s.Touchdowns) > 0 THEN ROUND(CAST(SUM(s.ATT) AS REAL) / SUM(s.Touchdowns), 2) ELSE NULL END AS Attempts_Per_TD,
            ROW_NUMBER() OVER (PARTITION BY ps.Anio ORDER BY CASE WHEN SUM(s.Touchdowns) > 0 THEN ROUND(CAST(SUM(s.ATT) AS REAL) / SUM(s.Touchdowns), 2) ELSE NULL END ASC) AS rank
        FROM
            Statistics s
        JOIN
            Player_season ps ON s.Player_ID = ps.Player_ID
        JOIN
            Teams t ON ps.Team_ID = t.Team_ID
        WHERE
            s.Type_ID = 3 
        GROUP BY
            ps.Name, t.Team_name, ps.Anio
        HAVING
            SUM(s.Touchdowns) > 0 
            AND SUM(s.ATT) >= 50 
    )
    SELECT
        Name,
        Team,
        Year,
        ATT,
        Touchdowns,
        Attempts_Per_TD
    FROM
        RankedData
    WHERE
        rank <= 10
    ORDER BY
        Year ASC,
        Attempts_Per_TD ASC;
''')

app = dash.Dash(__name__)
app.title = "Dashboard NFL" 


app._favicon = 'nfl_logo.ico' 

# Layout del dashboard
app.layout = html.Div([
    html.H1("Estadísticas de la NFL", style={'text-align': 'center', 'padding-top': '30px'}),
    
    # Muestra las gráficas de pie de las proporciones de las posiciones en las estadísticas
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

    # Tabla del top 10 de jugadores por estadística
    html.H1("Top 10 jugadores por estadística", style={'text-align': 'center'}),

    dcc.Dropdown(
        id='stat-type-top',
        options=[
            {'label': 'Passing', 'value': 'passing'},
            {'label': 'Rushing', 'value': 'rushing'},
            {'label': 'Receiving', 'value': 'receiving'}
        ],
        value='passing',
        style={'width': '50%', 'margin': '0 auto'}
    ),

    dcc.Dropdown(
        id='year-filter-top',
        placeholder='Select a Year',
        style={'width': '50%', 'margin': '10px auto'}
    ),

    dash_table.DataTable(
        id='top-10-table',
        columns=[
            {"name": "Team", "id": "Team"},
            {"name": "Position", "id": "Position"},
            {"name": "Name", "id": "Name"},
            {"name": "Total Yards", "id": "Total_Yards"},
            {"name": "Total Touchdowns", "id": "Total_Touchdowns"}
        ],
        data=[],
        style_table={'overflowX': 'auto', 'padding-bottom': '25px'},
        style_cell={
            'textAlign': 'center',
            'padding-bottom': '5px',
            'whiteSpace': 'normal',
        },
        page_size=10
    ),

    # Tabla de los jugadores más eficientes por estadística
    html.H1("Top 10 jugadores más eficientes por estadística", style={'text-align': 'center'}),

    dcc.Dropdown(
        id='stat-type-efficiency',
        options=[
            {'label': 'Passing', 'value': 'passing'},
            {'label': 'Rushing', 'value': 'rushing'},
            {'label': 'Receiving', 'value': 'receiving'}
        ],
        value='passing',
        style={'width': '50%', 'margin': '0 auto'}
    ),

    dcc.Dropdown(
        id='year-filter-efficiency',
        placeholder='Select a Year',
        style={'width': '50%', 'margin': '10px auto'}
    ),

    dash_table.DataTable(
        id='top-10-table-efficiency',
        columns=[
            {"name": "Name", "id": "Name"},
            {"name": "Team", "id": "Team"},
            {"name": "ATT", "id": "ATT"},
            {"name": "Touchdowns", "id": "Touchdowns"},
            {"name": "Attempts Per TD", "id": "Attempts_Per_TD"}
        ],
        data=[],
        style_table={'overflowX': 'auto', 'padding-bottom': '25px'},
        style_cell={
            'textAlign': 'center',
            'padding-bottom': '5px',
            'whiteSpace': 'normal',
        },
        page_size=10
    ), 
])

# --------------------------------------------------------------------------------------------------------------------
# Llamados para que muestre las tablas y funcionen los filtros

# Gráfica de pie
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

# Callback para actualizar el filtro de años basado en el tipo de estadísticas
@app.callback(
    Output('year-filter-top', 'options'),
    Input('stat-type-top', 'value')
)
def update_year_filter_options_top(selected_type):
    if selected_type == 'passing':
        df = get_data(query_passing_top)
    elif selected_type == 'rushing':
        df = get_data(query_rushing_top)
    else:
        df = get_data(query_receiving_top)

    years = df['Year'].unique()
    return [{'label': str(year), 'value': str(year)} for year in years]

@app.callback(
    Output('top-10-table', 'data'),
    [Input('stat-type-top', 'value'), Input('year-filter-top', 'value')]
)
def update_top_10_table(selected_type, selected_year):
    if selected_type == 'passing':
        df = get_data(query_passing_top)
    elif selected_type == 'rushing':
        df = get_data(query_rushing_top)
    else:
        df = get_data(query_receiving_top)

    if selected_year:
        df = df[df['Year'] == int(selected_year)]

    return df.to_dict('records')

# Tabla de eficiencia
@app.callback(
    Output('year-filter-efficiency', 'options'),
    Input('stat-type-efficiency', 'value')
)
def update_year_filter_options_efficiency(selected_type):
    if selected_type == 'passing':
        df = get_data(query_passing_efficiency)
    elif selected_type == 'rushing':
        df = get_data(query_rushing_efficiency)
    else:
        df = get_data(query_receiving_efficiency)

    years = df['Year'].unique()
    return [{'label': str(year), 'value': str(year)} for year in years]

@app.callback(
    Output('top-10-table-efficiency', 'data'),
    [Input('stat-type-efficiency', 'value'), Input('year-filter-efficiency', 'value')]
)
def update_top_10_efficiency_table(selected_type, selected_year):
    if selected_type == 'passing':
        df = get_data(query_passing_efficiency)
    elif selected_type == 'rushing':
        df = get_data(query_rushing_efficiency)
    else:
        df = get_data(query_receiving_efficiency)

    if selected_year:
        df = df[df['Year'] == int(selected_year)]

    return df.to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True)
