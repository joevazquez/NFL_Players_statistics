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

# Crear la tabla 'Player_season'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Player_season (
        Player_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Team_ID INTEGER,
        Name TEXT NOT NULL,
        Posicion TEXT,
        Anio INTEGER,
        FOREIGN KEY (Team_ID) REFERENCES Teams (Team_ID)
    )
''')

# Crear la tabla 'Type'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Type (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL
    )
''')

"""
# Borrar tablas
cursor.execute('''
DROP TABLE Statistics;
''')

"""
# Crear la tabla 'Statistics'
cursor.execute('''
CREATE TABLE  Statistics (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT,
    Team_ID TEXT,
    Position TEXT,
    Games_played INTEGER,
    ATT INTEGER,
    Yards INTEGER,
    Long_Play INTEGER,
    Touchdowns INTEGER,
    Player_ID INTEGER,
    Type_ID INTEGER,
    FOREIGN KEY (Team_ID) REFERENCES Teams (Team_ID),
    FOREIGN KEY (Player_ID) REFERENCES Player_season (Player_ID),
    FOREIGN KEY (Type_ID) REFERENCES Type (ID)
);
''')

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

#print("Tabla borrada exitosamente.")
print("Base de datos y tablas creadas exitosamente.")
