import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import pandas as pd
import sqlite3

# Ruta de la base de datos
db_path = './Database/NFL_database.db'

# Función para ejecutar el query y obtener los datos
def get_data(query):
    conn = sqlite3.connect(db_path)
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Querys para Passing, Rushing y Receiving
query_passing = ('''
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

query_rushing = ('''
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

query_receiving = ('''
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

# Inicializar la aplicación Dash
app = dash.Dash(__name__)

# Layout de la aplicación
app.layout = html.Div([
    html.H1("Top 10 NFL Players by Statistics Type", style={'text-align': 'center'}),
    
    # Dropdown para seleccionar el tipo de estadísticas
    dcc.Dropdown(
        id='stat-type',
        options=[
            {'label': 'Passing', 'value': 'passing'},
            {'label': 'Rushing', 'value': 'rushing'},
            {'label': 'Receiving', 'value': 'receiving'}
        ],
        value='passing',
        style={'width': '50%', 'margin': '0 auto'}
    ),

    # Dropdown para filtrar por año
    dcc.Dropdown(
        id='year-filter',
        placeholder='Select a Year',
        style={'width': '50%', 'margin': '10px auto'}
    ),
    
    # Tabla para mostrar los resultados
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
        style_table={'overflowX': 'auto'},
        style_cell={
            'textAlign': 'left',
            'padding': '5px',
            'whiteSpace': 'normal',
        },
        page_size=10
    ),
])

# Callback para actualizar el filtro de años basado en el tipo de estadísticas
@app.callback(
    Output('year-filter', 'options'),
    Input('stat-type', 'value')
)
def update_year_filter_options(selected_type):
    if selected_type == 'passing':
        df = get_data(query_passing)
    elif selected_type == 'rushing':
        df = get_data(query_rushing)
    else:
        df = get_data(query_receiving)

    years = df['Year'].unique()
    return [{'label': year, 'value': year} for year in years]

# Callback para actualizar la tabla basada en la selección del dropdown
@app.callback(
    Output('top-10-table', 'data'),
    [Input('stat-type', 'value'), Input('year-filter', 'value')]
)
def update_table(selected_type, selected_year):
    if selected_type == 'passing':
        df = get_data(query_passing)
    elif selected_type == 'rushing':
        df = get_data(query_rushing)
    else:
        df = get_data(query_receiving)

    if selected_year:
        df = df[df['Year'] == selected_year]

    return df.to_dict('records')

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
