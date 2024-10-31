import sys
import os

# Agregar el directorio principal a sys.path para que se pueda encontrar Config.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Ahora se puede importar Config
from Config import get_data

#Querys de validación de los datos
query = "SELECT * FROM Teams"
df = get_data(query)
if df.empty:
    print("La tabla 'Teams' está vacía.")
else:
    print(df)
print("----------------------------------------------------------------------------------------")

query = "SELECT * FROM Type"
df = get_data(query)
if df.empty:
    print("La tabla 'Type' está vacía.")
else:
    print(df)
print("----------------------------------------------------------------------------------------")

query = ('''SELECT * 
         FROM Player_season''')
df = get_data(query)
if df.empty:
    print("La tabla 'Player_season' está vacía.")
else:
    print(df)
print("----------------------------------------------------------------------------------------")

query = ('''SELECT * 
         FROM Statistics ''')
df = get_data(query)
if df.empty:
    print("La tabla 'Statistics' está vacía.")
else:
    print(df)
print("----------------------------------------------------------------------------------------")

"""
    Saca el top 10 con respecto a las Yardas totales de cada uno de los jugadores y
    se saca de todos los jugadores de este tipo de estadística el número total de yardas
    se ordenan de forma desendente y se saca el top 10 haciendo la agrupación por año, así 
    se asegura regresar el top 10 por año de cada tipo de estadística
    
"""

print('Top 10 por año de Passing')
query = ('''
   WITH RankedData AS (
        SELECT
            ps.Name,
            t.Team_name AS Team,
            ps.Posicion AS Position,
            ps.Anio AS Year,
            SUM(s.Yards) AS Total_Yards,
            SUM(s.ATT) AS Total_Attempts,
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
        Name,
        Team,
        Position,
        Year,
        Total_Yards,
        Total_Attempts,
        Total_Touchdowns
    FROM
        RankedData
    WHERE
        rank <= 10
    ORDER BY
        Year, Total_Yards DESC;
''')

df = get_data(query)
if df.empty:
    print("No se puede mostrar la información")
else:
    print(df)


print("----------------------------------------------------------------------------------------")

print('Top 10 por año de Rushing')
query = ('''
   WITH RankedData AS (
        SELECT
            ps.Name,
            t.Team_name AS Team,
            ps.Posicion AS Position,
            ps.Anio AS Year,
            SUM(s.Yards) AS Total_Yards,
            SUM(s.ATT) AS Total_Attempts,
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
        Name,
        Team,
        Position,
        Year,
        Total_Yards,
        Total_Attempts,
        Total_Touchdowns
    FROM
        RankedData
    WHERE
        rank <= 10
    ORDER BY
        Year, Total_Yards DESC;
''')

df = get_data(query)
if df.empty:
    print("No se puede mostrar la información")
else:
    print(df)

print("----------------------------------------------------------------------------------------")

print('Top 10 por año de Reciving')
query = ('''
   WITH RankedData AS (
        SELECT
            ps.Name,
            t.Team_name AS Team,
            ps.Posicion AS Position,
            ps.Anio AS Year,
            SUM(s.Yards) AS Total_Yards,
            SUM(s.ATT) AS Total_Attempts,
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
        Name,
        Team,
        Position,
        Year,
        Total_Yards,
        Total_Attempts,
        Total_Touchdowns
    FROM
        RankedData
    WHERE
        rank <= 10
    ORDER BY
        Year, Total_Yards DESC;
''')

df = get_data(query)
if df.empty:
    print("No se puede mostrar la información")
else:
    print(df)


print("----------------------------------------------------------------------------------------")

print('Jugadores más eficiente en pases')
query = ('''
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

df = get_data(query)
if df.empty:
    print("No se puede mostrar la información")
else:
    print(df)

print("----------------------------------------------------------------------------------------")

print('Jugadores más eficiente en carrera')
query = ('''
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

df = get_data(query)
if df.empty:
    print("No se puede mostrar la información")
else:
    print(df)

print("----------------------------------------------------------------------------------------")

print('Jugadores más eficiente en recepción')
query = ('''
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

df = get_data(query)
if df.empty:
    print("No se puede mostrar la información")
else:
    print(df)

print("----------------------------------------------------------------------------------------")

print('Trayectoria de los jugadores')
query = ('''
    SELECT
        ps.Name AS Name,
        t.Team_name AS Team,
        ps.Anio AS Year,
        SUM(s.ATT) AS ATT,
        SUM(s.Touchdowns) AS Touchdowns,
        CASE WHEN SUM(s.Touchdowns) > 0 THEN ROUND(CAST(SUM(s.ATT) AS REAL) / SUM(s.Touchdowns), 2) ELSE NULL END AS Attempts_Per_TD
    FROM
        Statistics s
    JOIN
        Player_season ps ON s.Player_ID = ps.Player_ID
    JOIN
        Teams t ON ps.Team_ID = t.Team_ID
    WHERE
        s.Type_ID = 3 -- Tipo de estadística (3 para recepciones, puedes cambiar según el tipo)
    GROUP BY
        ps.Name, t.Team_name, ps.Anio
    HAVING
        SUM(s.Touchdowns) > 0 
        AND SUM(s.ATT) >= 50
    ORDER BY
        ps.Name ASC, ps.Anio ASC;
''')

df = get_data(query)
if df.empty:
    print("No se puede mostrar la información")
else:
    print(df)

print("----------------------------------------------------------------------------------------")

query = ('''SELECT SUM(s.Yards) as Total_Yards
    FROM Statistics s
    WHERE s.Type_ID = 2  -- 2 representa rushing (carreras)''')
df = get_data(query)
if df.empty:
    print("La tabla 'Player_season' está vacía.")
else:
    print(df)
print("----------------------------------------------------------------------------------------")

