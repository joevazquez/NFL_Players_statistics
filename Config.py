from sqlalchemy import create_engine
import pandas as pd

# Configuración de la conexión a la base de datos PostgreSQL
DATABASE_URI = 'postgresql://umefzpbv8c084ijirrmy:q7AXb6qsBEB1EgTbMvYSVieYUbSOnM@b1bua5kvmbuvwgwxle7r-postgresql.services.clever-cloud.com:50013/b1bua5kvmbuvwgwxle7r'

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URI)

# Función para obtener los datos desde la base de datos
def get_data(query):
    with engine.connect() as connection:
        return pd.read_sql(query, connection)
