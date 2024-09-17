import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
from Config import get_data

# Crear la aplicación Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Obtener datos iniciales (modifica las consultas según tus tablas)
passing_data = get_data("SELECT * FROM PassingStats")
receiving_data = get_data("SELECT * FROM ReceivingStats")
rushing_data = get_data("SELECT * FROM RushingStats")

# Crear los gráficos iniciales utilizando Plotly
fig_passing = px.bar(passing_data, x='PlayerID', y='YDS', title='Yardas de Pase por Jugador')
fig_receiving = px.bar(receiving_data, x='PlayerID', y='YDS', title='Yardas de Recepción por Jugador')
fig_rushing = px.bar(rushing_data, x='PlayerID', y='YDS', title='Yardas de Acarreo por Jugador')

# Diseño del Dashboard
app.layout = dbc.Container([
    html.H1('Dashboard de Estadísticas de Jugadores'),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='data-selector',
                options=[
                    {'label': 'Pase', 'value': 'passing'},
                    {'label': 'Recepción', 'value': 'receiving'},
                    {'label': 'Acarreo', 'value': 'rushing'}
                ],
                value='passing',
                clearable=False,
                style={'margin-bottom': '20px'}
            ),
            dcc.Graph(id='main-graph')
        ], width=12),
    ]),
])

# Callback para actualizar el gráfico
@app.callback(
    Output('main-graph', 'figure'),
    [Input('data-selector', 'value')]
)
def update_graph(selected_data):
    if selected_data == 'passing':
        return fig_passing
    elif selected_data == 'receiving':
        return fig_receiving
    elif selected_data == 'rushing':
        return fig_rushing

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)
