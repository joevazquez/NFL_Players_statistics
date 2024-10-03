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

# Incerta las temporadas por equipo que se tienen en los datasets
"""
cursor.execute('''
INSERT INTO Seasons (Team_ID, Anio)
VALUES
    -- Año 2019
    (1, 2019), (2, 2019), (3, 2019), (4, 2019), (5, 2019), (6, 2019), (7, 2019), (8, 2019), (9, 2019), 
    (10, 2019), (11, 2019), (12, 2019), (13, 2019), (14, 2019), (15, 2019), (16, 2019), (17, 2019), 
    (18, 2019), (19, 2019), (20, 2019), (21, 2019), (22, 2019), (23, 2019), (24, 2019), (25, 2019), 
    (26, 2019), (27, 2019), (28, 2019), (29, 2019), (30, 2019), (31, 2019), (32, 2019),

    -- Año 2020
    (1, 2020), (2, 2020), (3, 2020), (4, 2020), (5, 2020), (6, 2020), (7, 2020), (8, 2020), (9, 2020), 
    (10, 2020), (11, 2020), (12, 2020), (13, 2020), (14, 2020), (15, 2020), (16, 2020), (17, 2020), 
    (18, 2020), (19, 2020), (20, 2020), (21, 2020), (22, 2020), (23, 2020), (24, 2020), (25, 2020), 
    (26, 2020), (27, 2020), (28, 2020), (29, 2020), (30, 2020), (31, 2020), (32, 2020),

    -- Año 2021
    (1, 2021), (2, 2021), (3, 2021), (4, 2021), (5, 2021), (6, 2021), (7, 2021), (8, 2021), (9, 2021), 
    (10, 2021), (11, 2021), (12, 2021), (13, 2021), (14, 2021), (15, 2021), (16, 2021), (17, 2021), 
    (18, 2021), (19, 2021), (20, 2021), (21, 2021), (22, 2021), (23, 2021), (24, 2021), (25, 2021), 
    (26, 2021), (27, 2021), (28, 2021), (29, 2021), (30, 2021), (31, 2021), (32, 2021),

    -- Año 2022
    (1, 2022), (2, 2022), (3, 2022), (4, 2022), (5, 2022), (6, 2022), (7, 2022), (8, 2022), (9, 2022), 
    (10, 2022), (11, 2022), (12, 2022), (13, 2022), (14, 2022), (15, 2022), (16, 2022), (17, 2022), 
    (18, 2022), (19, 2022), (20, 2022), (21, 2022), (22, 2022), (23, 2022), (24, 2022), (25, 2022), 
    (26, 2022), (27, 2022), (28, 2022), (29, 2022), (30, 2022), (31, 2022), (32, 2022),

    -- Año 2023
    (1, 2023), (2, 2023), (3, 2023), (4, 2023), (5, 2023), (6, 2023), (7, 2023), (8, 2023), (9, 2023), 
    (10, 2023), (11, 2023), (12, 2023), (13, 2023), (14, 2023), (15, 2023), (16, 2023), (17, 2023), 
    (18, 2023), (19, 2023), (20, 2023), (21, 2023), (22, 2023), (23, 2023), (24, 2023), (25, 2023), 
    (26, 2023), (27, 2023), (28, 2023), (29, 2023), (30, 2023), (31, 2023), (32, 2023);
''')
"""

# Ruta al archivo CSV dentro del proyecto
csv_file_path = os.path.join(os.getcwd(), 'Dataset', 'nfl_players.csv')  # Ajusta esta ruta según tu estructura

# Cargar el archivo CSV
nfl_players_df = pd.read_csv(csv_file_path)

# Insertar los jugadores en la tabla Player
for index, row in nfl_players_df.iterrows():
    jugador = row['Nombre']
    equipo = row['Team']
    posicion = row['POS']
    
    # Obtener el Team_ID usando las iniciales del equipo
    cursor.execute('''
    SELECT Team_ID FROM Teams WHERE Team_initials = ?
    ''', (equipo,))
    
    team_id = cursor.fetchone()
    
    if team_id:
        # Si se encuentra el Team_ID, insertar el jugador
        cursor.execute('''
        INSERT INTO Player (Team_ID, Name, Posicion)
        VALUES (?, ?, ?)
        ''', (team_id[0], jugador, posicion))

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
conn.close()

print("Datos insertados correctamente.")