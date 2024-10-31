import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import sqlite3

# Ruta de la base de datos
db_path = './Database/NFL_database.db'

# Función para obtener los datos de la base de datos
def get_data(query, params=None):
    conn = sqlite3.connect(db_path)
    if params:
        df = pd.read_sql(query, conn, params=params)
    else:
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

# Diccionario de conversión de nombres de estados de español a abreviaturas en inglés
state_conversion = {
    'Arizona': 'AZ',
    'Georgia': 'GA',
    'Maryland': 'MD',
    'Nueva York': 'NY',
    'Carolina del Norte': 'NC',
    'Illinois': 'IL',
    'Ohio': 'OH',
    'Texas': 'TX',
    'Colorado': 'CO',
    'Michigan': 'MI',
    'Wisconsin': 'WI',
    'Indiana': 'IN',
    'Florida': 'FL',
    'Misuri': 'MO',
    'Nevada': 'NV',
    'California': 'CA',
    'Minnesota': 'MN',
    'Massachusetts': 'MA',
    'Luisiana': 'LA',
    'Pensilvania': 'PA',
    'Washington': 'WA',
    'Tennessee': 'TN'
}

# Crear un diccionario inverso para mostrar los nombres completos en la tabla
state_full_name = {v: k for k, v in state_conversion.items()}

# Función para convertir los nombres de los estados a abreviaturas
def convert_state_names(df):
    df['Estado'] = df['Estado'].replace(state_conversion)
    return df



app = dash.Dash(__name__)
app.title = "NFL Dashboard" 


app._favicon = 'nfl_logo.ico' 

# Layout del dashboard
app.layout = html.Div([
    html.H1("Estadísticas de la NFL", id='Title'),
    
    # Muestra las gráficas de barras de las proporciones de las posiciones en las estadísticas
    html.Div([
        dcc.Dropdown(
        id='year-bar-chart',
        placeholder='Filtrar por año'
        ),

    ], style={'display': 'flex', 'justify-content': 'flex-end', 'gap': '10px', 'padding': '20px'}),
    
    html.Div([
        html.Div(dcc.Graph(id='passing-bar-chart'), style={'width': '33%', 'padding': '10px'}),
        html.Div(dcc.Graph(id='rushing-bar-chart'), style={'width': '33%', 'padding': '10px'}),
        html.Div(dcc.Graph(id='receiving-bar-chart'), style={'width': '33%', 'padding': '10px'}),
    ], id='graph'),

    # Muestra la tabla del top 10 de jugadores por estadística
    html.H1("Top 10 Jugadores Por Estadística", style={'text-align': 'center'}),
    html.Div([
        dcc.Dropdown(
        id='stat-type-top',
        options=[
            {'label': 'Passing', 'value': 'passing'},
            {'label': 'Rushing', 'value': 'rushing'},
            {'label': 'Receiving', 'value': 'receiving'}
        ],
        value='passing'
        ),
        dcc.Dropdown(
            id='year-filter-top',
            placeholder='Select a Year'
        ),
    ]),
    # Contenedor para la tabla y la gráfica, colocados en la misma línea
    html.Div([
    
    # Columna de la tabla del top 10
    html.Div([
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
            row_selectable='single',
            selected_rows=[],
            style_table={'overflowX': 'auto', 'height': '400px'},  # Limitar la altura de la tabla
            style_cell={
                'textAlign': 'center',
                'whiteSpace': 'normal',
            },
            page_size=10
        ),
    ], style={'width': '45%', 'display': 'inline-block', 'padding': '10px', 'vertical-align': 'top'}),
    
    # Columna para la gráfica de trayectoria del jugador seleccionado
    html.Div([
        html.Div(id='player-detail'),
    ], id='chart-eficency')

], style={'display': 'flex', 'justify-content': 'space-around'}),

    html.H1("Mapa de campeonatos ganados por estado"),
    html.Div([
        html.Div([
            dcc.Graph(id='heatmap-states'),
        ], id='map'),
        
        html.Div([
            dash_table.DataTable(
                id='state-table-titles',
                columns=[
                    {"name": "Inicial del Estado", "id": "Estado"},
                    {"name": "Nombre Completo", "id": "Nombre Completo"}
                ],
                data=[],
                row_selectable='single',  # Permitir seleccionar una fila
                selected_rows=[],  # Para manejar las filas seleccionadas
                style_table={'overflowX': 'auto', 'height': '400px', 'overflowY': 'auto'},
                style_cell={'textAlign': 'center'},
            )
        ], id='table-map-titles'),
    ], id='content-map'),

        html.Div(id='team-detail-champ', style={'padding-top': '20px'}),

    html.H1("Mapa de subcampeonatos por estado"),
    html.Div([
        html.Div([
            dcc.Graph(id='heatmap-subtitles'),
        ], id='map-subtitles'),
        
        html.Div([
            dash_table.DataTable(
            id='state-table-subtitles',
            columns=[
                {"name": "Inicial del Estado", "id": "Estado"},
                {"name": "Nombre Completo", "id": "Nombre Completo"},
            ],
            data=[],
            row_selectable='single',  # Permitir seleccionar una fila
            selected_rows=[],  # Para manejar las filas seleccionadas
            style_table={'overflowX': 'auto', 'height': '400px', 'overflowY': 'auto'},
            style_cell={'textAlign': 'center'},
            )
        ], id='table-map-subtitles'),
    ], id='content-map-subtitles'),

    html.Div(id='team-detail', style={'padding-top': '20px'}),

    # Mostrar tabla de eficiencia
    html.H1("Juagdores Más Eficientes Por Estadística"),
    html.Div([
        dcc.Dropdown(
        id='stat-type-efficiency',
        options=[
            {'label': 'Passing', 'value': 'passing'},
            {'label': 'Rushing', 'value': 'rushing'},
            {'label': 'Receiving', 'value': 'receiving'}
        ],
        value='passing'
        ),
        dcc.Dropdown(
            id='year-filter-efficiency',
            placeholder='Select a Year',
        ),
    ]),

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

# Callback para actualizar las opciones de años
@app.callback(
    Output('year-bar-chart', 'options'),
    Input('year-bar-chart', 'value')
)
def update_year_options(selected_year):
    df = get_data(query_passing)
    years = df['Year'].unique()
    return [{'label': str(year), 'value': str(year)} for year in sorted(years)]

# Callback para actualizar las gráficas de barras con el filtro por año 
@app.callback(
    [Output('passing-bar-chart', 'figure'),
     Output('rushing-bar-chart', 'figure'),
     Output('receiving-bar-chart', 'figure')],
    [Input('year-bar-chart', 'value')]  
)
def update_bar_charts(selected_year):
    # Obtener los datos
    data_passing = get_data(query_passing)
    data_rushing = get_data(query_rushing)
    data_receiving = get_data(query_receiving)

    # Filtrar por año
    if selected_year:
        data_passing = data_passing[data_passing['Year'] == int(selected_year)]
        data_rushing = data_rushing[data_rushing['Year'] == int(selected_year)]
        data_receiving = data_receiving[data_receiving['Year'] == int(selected_year)]


    # Ordenar los datos por la columna 'Count' de mayor a menor
    data_passing = data_passing.sort_values(by='Count', ascending=False)
    data_rushing = data_rushing.sort_values(by='Count', ascending=False)
    data_receiving = data_receiving.sort_values(by='Count', ascending=False)

    # Crear las gráficas
    fig_passing = px.bar(
        data_passing, 
        x='Position', 
        y='Count',
        title=f'Estadísticas de pases por posición-{selected_year if selected_year else "All Years"}',
        color='Position',
        color_discrete_map=color_discrete_map
    )

    fig_rushing = px.bar(
        data_rushing, 
        x='Position', 
        y='Count',
        title=f'Estadísticas de carreras por posición-{selected_year if selected_year else "All Years"}',
        color='Position',
        color_discrete_map=color_discrete_map
    )

    fig_receiving = px.bar(
        data_receiving, 
        x='Position', 
        y='Count',
        title=f'Estadísticas de recepción por posición-{selected_year if selected_year else "All Years"}',
        color='Position',
        color_discrete_map=color_discrete_map
    )

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

# Mostrar información de los jugadores top 10
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


# Mostrar información de los jugadores seleccionados del top 10
@app.callback(
    Output('player-detail', 'children'),
    [Input('top-10-table', 'selected_rows'), Input('top-10-table', 'data')]
)
def display_player_trajectory(selected_rows, data):
    # Comprobar si hay una fila seleccionada
    if selected_rows is not None and len(selected_rows) > 0:
        player_name = data[selected_rows[0]]['Name']

        query_player_trajectory = '''
            SELECT ps.Anio AS Year, SUM(s.Yards) AS Total_Yards, SUM(s.Touchdowns) AS Total_Touchdowns, SUM(s.ATT) AS Intentos_Totales
            FROM Statistics s
            JOIN Player_season ps ON s.Player_ID = ps.Player_ID
            WHERE ps.Name = ?
            GROUP BY ps.Anio
            ORDER BY ps.Anio ASC;
        '''

        df = get_data(query_player_trajectory, (player_name,))
        df['Year'] = df['Year'].astype(str)

        # Crear la gráfica de trayectoria del jugador
        fig = px.line(df, x='Year', y=['Total_Yards', 'Intentos_Totales', 'Total_Touchdowns'], 
                      title=f'Trayectoria de {player_name}', markers=True)

        return dcc.Graph(figure=fig)

    # Si no hay una selección activa, devolver un contenido vacío o un mensaje
    return html.Div("Selecciona un jugador de la tabla para ver su trayectoria.", id='Select-player-text')


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

# -------------------------------------------------------------------------------------------------------------

# Callback para los campeonatos
@app.callback(
    [Output('heatmap-states', 'figure'), Output('state-table-titles', 'data')],
    Input('heatmap-states', 'id')
)
def update_heatmap_and_table_titles(id):
    query = "SELECT Estado, Titulos, Team_name FROM Teams"
    df_teams = get_data(query)
    df_teams = convert_state_names(df_teams)
    
    df_teams_grouped = df_teams.groupby('Estado').agg({
            'Titulos': 'sum',  
            'Team_name': lambda x: ', '.join(x)  
        }).reset_index()
    
    fig = px.choropleth(
        df_teams,
        locations='Estado',
        locationmode="USA-states",
        color='Titulos',
        color_continuous_scale="Greens",
        scope="usa",
        labels={'Titulos': 'Títulos ganados'},
    )
    
    table_data = [{
            "Estado": row['Estado'],
            "Nombre Completo": state_full_name[row['Estado']],
            "Equipos": row['Team_name']
        } for index, row in df_teams_grouped.iterrows()]

    return fig, table_data

@app.callback(
    Output('team-detail-champ', 'children'),
    [Input('state-table-titles', 'selected_rows'), Input('state-table-titles', 'data')]
)
def display_teams(selected_rows, data):
    if selected_rows is not None and len(selected_rows) > 0:
        selected_state = data[selected_rows[0]]['Estado']
        equipos = data[selected_rows[0]]['Equipos']
        return html.Div([
            html.H3(f"Equipos del estado: {selected_state}"),
            html.P(f"Equipos: {equipos}",id='Lista-equipos-champ')
        ],id='Texto-equipo-map-champ')
    return html.Div("Selecciona un estado de la tabla para ver los equipos.", id='Select-player-text')

# -------------------------------------------------------------------------------------------------------------

# Callback para los subcampeonatos
@app.callback(
    [Output('heatmap-subtitles', 'figure'), Output('state-table-subtitles', 'data')],
    Input('heatmap-subtitles', 'id')
)
def update_heatmap_and_table_subtitles(id):
    try:
        query = "SELECT Estado, Subtitulos, Team_name FROM Teams"
        df_teams = get_data(query)
        df_teams = convert_state_names(df_teams)
        
        df_teams_grouped = df_teams.groupby('Estado').agg({
            'Subtitulos': 'sum',  # Sumar los subcampeonatos por estado
            'Team_name': lambda x: ', '.join(x)  # Concatenar nombres de equipos
        }).reset_index()

        # Crear el mapa de calor de subcampeonatos
        fig = px.choropleth(
            df_teams_grouped,
            locations='Estado',
            locationmode="USA-states",
            color='Subtitulos',
            color_continuous_scale="Reds",
            scope="usa",
            labels={'Subtitulos': 'Subcampeonatos'},
        )
        
        table_data = [{
            "Estado": row['Estado'],
            "Nombre Completo": state_full_name[row['Estado']],
            "Equipos": row['Team_name']
        } for index, row in df_teams_grouped.iterrows()]
        
        # Devolver el gráfico y la tabla
        return fig, table_data
    
    except Exception as e:
        # Si algo falla, devuelve un gráfico y tabla vacíos para evitar errores
        print(f"Error: {e}")
        fig = px.choropleth(locations=[], locationmode="USA-states", scope="usa")
        return fig, []

@app.callback(
    Output('team-detail', 'children'),
    [Input('state-table-subtitles', 'selected_rows'), Input('state-table-subtitles', 'data')]
)
def display_teams(selected_rows, data):
    if selected_rows is not None and len(selected_rows) > 0:
        selected_state = data[selected_rows[0]]['Estado']
        equipos = data[selected_rows[0]]['Equipos']
        return html.Div([
            html.H3(f"Equipos del estado: {selected_state}"),
            html.P(f"Equipos: {equipos}",id='Lista-equipos')
        ],id='Texto-equipo-map')
    return html.Div("Selecciona un estado de la tabla para ver los equipos.", id='Select-player-text')

if __name__ == '__main__':
    app.run_server(debug=True)
