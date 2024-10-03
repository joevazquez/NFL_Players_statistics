import os
from sqlalchemy import create_engine
import pandas as pd

# Obtener la ruta absoluta del directorio del proyecto
project_dir = os.path.dirname(os.path.abspath(__file__))

# Definir la ruta relativa hacia el archivo de la base de datos
db_path = os.path.join(project_dir, 'Database', 'NFL_database.db')

# Configuración de la conexión a la base de datos SQLite
DATABASE_URI = f'sqlite:///{db_path}'

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URI)

# Función para obtener los datos desde la base de datos
def get_data(query):
    with engine.connect() as connection:
        return pd.read_sql(query, connection)
