import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('NFL_database.db')
cursor = conn.cursor()

# Crear la tabla 'Teams'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Teams (
        Team_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Team_name TEXT NOT NULL,
        Team_initials TEXT
    )
''')

# Crear la tabla 'Player'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Player (
        Player_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Team_ID INTEGER,
        Name TEXT NOT NULL,
        Posicion TEXT,
        FOREIGN KEY (Team_ID) REFERENCES Teams (Team_ID)
    )
''')

# Crear la tabla 'Seasons'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Seasons (
        Season_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Team_ID INTEGER,
        Anio INTEGER,
        FOREIGN KEY (Team_ID) REFERENCES Teams (Team_ID)
    )
''')

# Crear la tabla 'Season_players'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Season_players (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Player_ID INTEGER,
        Season_ID INTEGER,
        FOREIGN KEY (Player_ID) REFERENCES Player (Player_ID),
        FOREIGN KEY (Season_ID) REFERENCES Seasons (Season_ID)
    )
''')

# Crear la tabla 'Type'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Type (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL
    )
''')

# Crear la tabla 'Statistics'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Statistics (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Player_Season_ID INTEGER,
        Type_ID INTEGER,
        Games_played INTEGER,
        ATT INTEGER,
        Yards INTEGER,
        Touchdowns INTEGER,
        FOREIGN KEY (Player_Season_ID) REFERENCES Season_players (ID),
        FOREIGN KEY (Type_ID) REFERENCES Type (ID)
    )
''')

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Base de datos y tablas creadas exitosamente.")
