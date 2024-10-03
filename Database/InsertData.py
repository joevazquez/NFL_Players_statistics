import os
import sqlite3
import pandas as pd

# Obtener la ruta del directorio actual donde se encuentra el script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Definir la ruta de la base de datos relativa al script actual
db_path = os.path.join(script_dir, 'NFL_database.db')

# Verificar que la ruta es correcta (opcional, para depuración)
print(f"Ruta de la base de datos: {db_path}")

# Conectar a la base de datos
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Carga del archivo nfl_teams.csv a la tabla de Teams 
"""
# Leer el archivo CSV
csv_file_path = os.path.join(script_dir, '..', 'Dataset', 'nfl_teams.csv')  # Subimos un nivel para acceder a 'Dataset'
teams_data = pd.read_csv(csv_file_path)

# Insertar los datos en la tabla Teams
for index, row in teams_data.iterrows():
    cursor.execute("INSERT INTO Teams (Team_name, Team_initials) VALUES (?, ?)", 
                   (row['Equipo'], row['Iniciales']))
"""

# Incerta los tipos de stadistics que se tienen en los datasets
"""
# Insertar los valores Passing, Rushing, Receiving
cursor.execute('''
INSERT INTO Type (Name)
VALUES 
    ('Passing'),
    ('Rushing'),
    ('Receiving');
''')
"""


# Insertar los jugadores en la tabla Player_season
"""
# Ruta al archivo CSV dentro del proyecto (ajusta esta ruta a tu estructura)
csv_file_path = os.path.join(os.getcwd(), 'Dataset', 'nfl_players.csv')

# Cargar el archivo CSV
nfl_players_df = pd.read_csv(csv_file_path)

# Insertar los jugadores y sus temporadas en la tabla Player_season
for index, row in nfl_players_df.iterrows():
    jugador = row['Nombre']
    equipo = row['Team']
    posicion = row['POS']
    anio = row['Season']  # Se asume que hay una columna 'Anio' en el CSV
    
    # Obtener el Team_ID usando las iniciales del equipo
    cursor.execute('''
    SELECT Team_ID FROM Teams WHERE Team_initials = ?
    ''', (equipo,))
    
    team_id = cursor.fetchone()
    
    # Si se encuentra el Team_ID, insertar el jugador en Player_season
    if team_id:
        cursor.execute('''
        INSERT INTO Player_season (Team_ID, Name, Posicion, Anio)
        VALUES (?, ?, ?, ?)
        ''', (team_id[0], jugador, posicion, anio))
"""
# Confirmar los cambios
conn.commit()

# Cerrar la conexión
conn.close()

print("Datos insertados correctamente.")