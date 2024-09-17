from sqlalchemy import create_engine
import pandas as pd

# Configuración de la conexión a la base de datos PostgreSQL
DATABASE_URI = 'postgresql://username:password@localhost:5432/nombre_base_datos'

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URI)

# Función para obtener los datos desde la base de datos
def get_data(query):
    with engine.connect() as connection:
        return pd.read_sql(query, connection)
