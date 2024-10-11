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
# Lista de datos que deseas insertar uno por uno
datos_a_insertar = [
    (30,'Jameis Winston','QB',2019),
    (9,'Dak Prescott','QB',2019),
    (19,'Jared Goff','QB',2019),
    (18,'Philip Rivers','QB',2019),
    (2,'Matt Ryan','QB',2019),
    (29,'Russell Wilson','QB',2019),
    (22,'Tom Brady','QB',2019),
    (17,'Derek Carr','QB',2019),
    (26,'Carson Wentz','QB',2019),
    (16,'Patrick Mahomes','QB',2019),
    (12,'Aaron Rodgers','QB',2019),
    (28,'Jimmy Garoppolo','QB',2019),
    (13,'Deshaun Watson','QB',2019),
    (8,'Baker Mayfield','QB',2019),
    (1,'Kyler Murray','QB',2019),
    (21,'Kirk Cousins','QB',2019),
    (20,'Ryan Fitzpatrick','QB',2019),
    (7,'Andy Dalton','QB',2019),
    (5,'Kyle Allen','QB',2019),
    (15,'Gardner Minshew','QB',2019),
    (6,'Mitchell Trubisky','QB',2019),
    (3,'Lamar Jackson','QB',2019),
    (4,'Josh Allen','QB',2019),
    (24,'Daniel Jones','QB',2019),
    (25,'Sam Darnold','QB',2019),
    (23,'Drew Brees','QB',2019),
    (14,'Jacoby Brissett','QB',2019),
    (31,'Ryan Tannehill','QB',2019),
    (11,'Matthew Stafford','QB',2019),
    (10,'Joe Flacco','QB',2019),
    (27,'Mason Rudolph','QB',2019),
    (32,'Case Keenum','QB',2019),
    (23,'Teddy Bridgewater','QB',2019),
    (32,'Dwayne Haskins','QB',2019),
    (31,'Marcus Mariota','QB',2019),
    (27,'Devlin Hodges','QB',2019),
    (24,'Eli Manning','QB',2019),
    (10,'Drew Lock','QB',2019),
    (11,'David Blough','QB',2019),
    (15,'Nick Foles','QB',2019),
    (11,'Jeff Driskel','QB',2019),
    (16,'Matt Moore','QB',2019),
    (2,'Matt Schaub','QB',2019),
    (5,'Cam Newton','QB',2019),
    (20,'Josh Rosen','QB',2019),
    (10,'Brandon Allen','QB',2019),
    (7,'Ryan Finley','QB',2019),
    (6,'Chase Daniel','QB',2019),
    (25,'Luke Falk','QB',2019),
    (14,'Brian Hoyer','QB',2019),
    (4,'Matt Barkley','QB',2019),
    (27,'Ben Roethlisberger','QB',2019),
    (5,'Will Grier','QB',2019),
    (3,'Robert Griffin III','QB',2019),
    (13,'AJ McCarron','QB',2019),
    (21,'Sean Mannion','QB',2019),
    (32,'Colt McCoy','QB',2019),
    (17,'Mike Glennon','QB',2019),
    (23,'Taysom Hill','QB',2019),
    (1,'Brett Hundley','QB',2019),
    (22,'Julian Edelman','WR',2019),
    (10,'Courtland Sutt','WR',2019),
    (10,'Emmanuel Sanders','WR',2019),
    (22,'James White','RB',2019),
    (27,'Jaylen Samuels','RB',2019),
    (18,'Tyrod Taylor','QB',2019),
    (19,'Johnny Hekker','P',2019),
    (4,'John Brown','WR',2019),
    (1,'Andy Lee','P',2019),
    (7,'Alex Erickson','WR',2019),
    (26,'Josh McCown','QB',2019),
    (8,'Odell Beckham Jr.','WR',2019),
    (20,'Albert Wilson','WR',2019),
    (11,'Danny Amendola','WR',2019),
    (30,'Ryan Griffin','QB',2019),
    (15,'Logan Cooke','P',2019),
    (28,'Dante Pettis','WR',2019),
    (12,'Tim Boyle','QB',2019),
    (22,'Jarrett Stidham','QB',2019),
    (23,'Alvin Kamara','RB',2019),
    (5,'Michael Palardy','P',2019),
    (31,'Brett Kern','P',2019),
    (32,'Kelvin Harmon','WR',2019),
    (13,'DeAndre Hopkins','WR',2019),
    (10,'Andrew Beck','FB',2019),
    (2,'Kenjon Barner','RB',2019),
    (19,'Blake Bortles','QB',2019),
    (25,'Trevor Siemian','QB',2019),
    (24,'Alex Tanney','QB',2019),
    (20,'Matt Haack','P',2019),
    (16,'Dustin Colquitt','P',2019),
    (9,'Randall Cobb','WR',2019),
    (25,'Bilal Powell','RB',2019),
    (22,'Josh Gordon','WR',2019),
    (8,'Garrett Gilbert','QB',2019),
    (25,'David Fales','QB',2019),
    (21,'Stefon Diggs','WR',2019),
    (19,'Cooper Kupp','WR',2019),
    (14,'Zach Pascal','WR',2019),
    (10,'Colby Wadman','P',2019),
    (26,'Jake Elliott','PK',2019),
    (8,'Kareem Hunt','RB',2019),
    (5,'Christian McCaffrey','RB',2019),
    (20,'Preston Williams','WR',2019),
    (32,'Steven Sims','WR',2019),
    (3,'Sam Koch','P',2019),
    (23,'Michael Thomas','WR',2019),
    (2,'Julio Jones','WR',2019),
    (30,'Chris Godwin','WR',2019),
    (16,'Travis Kelce','TE',2019),
    (20,'DeVante Parker','WR',2019),
    (18,'Keenan Allen','WR',2019),
    (11,'Kenny Golladay','WR',2019),
    (9,'Amari Cooper','WR',2019),
    (5,'DJ Moore','WR',2019),
    (8,'Jarvis Landry','WR',2019),
    (13,'DeAndre Hopkins','WR',2019),
    (19,'Cooper Kupp','WR',2019),
    (30,'Mike Evans','WR',2019),
    (6,'Allen Robinson II','WR',2019),
    (17,'Darren Waller','TE',2019),
    (19,'Robert Woods','WR',2019),
    (21,'Stefon Diggs','WR',2019),
    (22,'Julian Edelman','WR',2019),
    (10,'Courtland Sutton','WR',2019),
    (9,'Michael Gallup','WR',2019),
    (4,'John Brown','WR',2019),
    (29,'Tyler Lockett','WR',2019),
    (28,'George Kittle','TE',2019),
    (31,'A.J. Brown','WR',2019),
    (7,'Tyler Boyd','WR',2019),
    (15,'DJ Chark Jr.','WR',2019),
    (5,'Christian McCaffrey','RB',2019),
    (18,'Mike Williams','WR',2019),
    (12,'Davante Adams','WR',2019),
    (18,'Austin Ekeler','RB',2019),
    (32,'Terry McLaurin','WR',2019),
    (26,'Zach Ertz','TE',2019),
    (29,'DK Metcalf','WR',2019),
    (10,'Emmanuel Sanders','WR',2019),
    (2,'Calvin Ridley','WR',2019),
    (16,'Tyreek Hill','WR',2019),
    (3,'Mark Andrews','TE',2019),
    (25,'Jamison Crowder','WR',2019),
    (9,'Randall Cobb','WR',2019),
    (1,'Larry Fitzgerald','WR',2019),
    (28,'Deebo Samuel Sr.','WR',2019),
    (2,'Austin Hooper','TE',2019),
    (11,'Marvin Jones Jr.','WR',2019),
    (25,'Robbie Chosen','WR',2019),
    (4,'Cole Beasley','WR',2019),
    (15,'Chris Conley','WR',2019),
    (24,'Darius Slayton','WR',2019),
    (27,'James Washington','WR',2019),
    (19,'Tyler Higbee','TE',2019),
    (1,'Christian Kirk','WR',2019),
    (23,'Jared Cook','TE',2019),
    (27,'Diontae Johnson','WR',2019),
    (11,'Danny Amendola','WR',2019),
    (24,'Golden Tate','WR',2019),
    (16,'Sammy Watkins','WR',2019),
    (13,'William Fuller V','WR',2019),
    (15,'Dede Westbrook','WR',2019),
    (6,'Anthony Miller','WR',2019),
    (18,'Hunter Henry','TE',2019),
    (17,'Tyrell Williams','WR',2019),
    (22,'James White','RB',2019),
    (30,'Breshad Perriman','WR',2019),
    (5,'Curtis Samuel','WR',2019),
    (14,'Zach Pascal','WR',2019),
    (26,'Dallas Goedert','TE',2019),
    (17,'Hunter Renfrow','WR',2019),
    (31,'Corey Davis','WR',2019),
    (5,'Greg Olsen','TE',2019),
    (3,'Marquise Brown','WR',2019),
    (19,'Brandin Cooks','WR',2019),
    (24,'Sterling Shepard','WR',2019),
    (7,'Auden Tate','WR',2019),
    (20,'Mike Gesicki','TE',2019),
    (10,'Noah Fant','TE',2019),
    (13,'Kenny Stills','WR',2019),
    (27,'JuJu Smith-Schuster','WR',2019),
    (16,'Mecole Hardman','WR',2019),
    (23,'Alvin Kamara','RB',2019),
    (9,'Jason Witten','TE',2019),
    (7,'Alex Erickson','WR',2019),
    (15,'Leonard Fournette','RB',2019),
    (22,'Mohamed Sanu','WR',2019),
    (21,'Dalvin Cook','RB',2019),
    (26,'Miles Sanders','RB',2019),
    (7,'John Ross','WR',2019),
    (14,'T.Y. Hilton','WR',2019),
    (26,'Alshon Jeffery','WR',2019),
    (12,'Allen Lazard','WR',2019),
    (12,'Aaron Jones','RB',2019),
    (24,'Evan Engram','TE',2019),
    (25,'Le Veon Bell','RB',2019),
    (30,'O.J. Howard','TE',2019),
    (6,'Tarik Cohen','RB',2019),
    (12,'Marquez Valdes-Scantling','WR',2019),
    (16,'Demarcus Robinson','WR',2019),
    (14,'Jack Doyle','TE',2019),
    (12,'Jimmy Graham','TE',2019),
    (2,'Russell Gage','WR',2019),
    (31,'Jonnu Smith','TE',2019),
    (24,'Saquon Barkley','RB',2019),
    (7,'Tyler Eifert','TE',2019),
    (25,'Demaryius Thomas','WR',2019),
    (20,'Preston Williams','WR',2019),
    (22,'Josh Gordon','WR',2019),
    (23,'Ted Ginn Jr.','WR',2019),
    (9,'Ezekiel Elliott','RB',2019),
    (21,'Adam Thielen','WR',2019),
    (13,'Jordan Akins','TE',2019),
    (20,'Allen Hurns','WR',2019),
    (2,'Devonta Freeman','RB',2019),
    (13,'Duke Johnson','RB',2019),
    (19,'Gerald Everett','TE',2019),
    (22,'Phillip Dorsett','WR',2019),
    (4,'Dawson Knox','TE',2019),
    (32,'Chris Thompson','RB',2019),
    (14,'Eric Ebron','TE',2019),
    (31,'Adam Humphries','WR',2019),
    (1,'David Johnson','RB',2019),
    (21,'Kyle Rudolph','TE',2019),
    (11,'T.J. Hockenson','TE',2019),
    (9,'Blake Jarwin','TE',2019),
    (32,'Kelvin Harmon','WR',2019),
    (26,'Nelson Agholor','WR',2019),
    (15,'Keelan Cole Sr.','WR',2019),
    (1,'Damiere Byrd','WR',2019),
    (22,'Jakobi Meyers','WR',2019),
    (28,'Kendrick Bourne','WR',2019),
    (6,'Taylor Gabriel','WR',2019),
    (20,'Albert Wilson','WR',2019),
    (29,'Jacob Hollister','TE',2019),
    (3,'Hayden Hurst','TE',2019),
    (20,'Kenyan Drake','RB',2019),
    (13,'Darren Fells','TE',2019),
    (3,'Willie Snead IV','WR',2019),
    (31,'Tajae Sharpe','WR',2019),
    (19,'Josh Reynolds','WR',2019),
    (17,'Jalen Richard','RB',2019),
    (3,'Nick Boyle','TE',2019),
    (25,'Ryan Griffin','TE',2019),
    (14,'Nyheim Hines','RB',2019),
    (30,'Cameron Brate','TE',2019),
    (21,'Irv Smith Jr.','TE',2019),
    (32,'Steven Sims','WR',2019),
    (30,'Ronald Jones','RB',2019),
    (27,'Jaylen Samuels','RB',2019),
    (29,'David Moore','WR',2019),
    (24,'Cody Latimer','WR',2019),
    (10,'DaeSean Hamilton','WR',2019),
    (5,'Jarius Wright','WR',2019),
    (18,'Melvin Gordon III','RB',2019),
    (21,'Bisi Johnson','WR',2019),
    (17,'DeAndre Washington','RB',2019),
    (12,'Geronimo Allison','WR',2019),
    (7,'Joe Mixon','RB',2019),
    (30,'Dare Ogunbowale','RB',2019),
    (8,'Kareem Hunt','RB',2019),
    (22,'Rex Burkhead','RB',2019),
    (8,'Nick Chubb','RB',2019),
    (14,'Marcus Johnson','WR',2019),
    (27,'Vance McDonald','TE',2019),
    (3,'Seth Roberts','WR',2019),
    (24,'Kaden Smith','TE',2019),
    (29,'Chris Carson','RB',2019),
    (29,'Will Dissly','TE',2019),
    (11,'Marvin Hall','WR',2019),
    (10,'Royce Freeman','RB',2019),
    (26,'Greg Ward','WR',2019),
    (4,'Isaiah McKenzie','WR',2019),
    (13,'Keke Coutee','WR',2019),
    (12,'Jamaal Williams','RB',2019),
    (27,'James Conner','RB',2019),
    (3,'Mark Ingram II','RB',2019),
    (32,'Paul Richardson Jr.','WR',2019),
    (29,'Malik Turner','WR',2019),
    (20,'Isaiah Ford','WR',2019),
    (7,'Pharoh Cooper','WR',2019),
    (7,'C.J. Uzomah','TE',2019),
    (32,'Jeremy Sprinkle','TE',2019),
    (28,'Kyle Juszczyk','FB',2019),
    (1,'Charles Clay','TE',2019),
    (23,'Latavius Murray','RB',2019),
    (7,'Giovani Bernard','RB',2019),
    (23,'Taysom Hill','QB',2019),
    (23,'Tre Quan Smith','WR',2019),
    (11,'J.D. McKissic','RB',2019),
    (8,'Ricky Seals-Jones','TE',2019),
    (23,'Josh Hill','TE',2019),
    (25,'Vyncint Smith','WR',2019),
    (29,'Jaron Brown','WR',2019),
    (12,'Jake Kumerow','WR',2019),
    (10,'Tim Patrick','WR',2019),
    (17,'Zay Jones','WR',2019),
    (31,'Delanie Walker','TE',2019),
    (16,'Damien Williams','RB',2019),
    (19,'Todd Gurley II','RB',2019),
    (31,'Derrick Henry','RB',2019),
    (31,'Anthony Firkser','TE',2019),
    (26,'Boston Scott','RB',2019),
    (20,'Patrick Laird','RB',2019),
    (1,'Maxx Williams','TE',2019),
    (8,'Damion Ratley','WR',2019),
    (30,'Scotty Miller','WR',2019),
    (32,'Trey Quinn','WR',2019),
    (3,'Miles Boykin','WR',2019),
    (10,'Phillip Lindsay','RB',2019),
    (2,'Justin Hardy','WR',2019),
    (4,'Devin Singletary','RB',2019),
    (24,'Bennie Fowler','WR',2019),
    (1,'Andy Isabella','WR',2019),
    (1,'KeeSean Johnson','WR',2019),
    (28,'Marquise Goodwin','WR',2019),
    (6,'Javon Wims','WR',2019),
    (6,'David Montgomery','RB',2019),
    (21,'Laquon Treadwell','WR',2019),
    (16,'LeSean McCoy','RB',2019),
    (18,'Dontrelle Inman','WR',2019),
    (28,'Raheem Mostert','RB',2019),
    (28,'Tevin Coleman','RB',2019),
    (14,'Chester Rogers','WR',2019),
    (9,'Tavon Austin','WR',2019),
    (17,'Foster Moreau','TE',2019),
    (22,'Ben Watson','TE',2019),
    (11,'Logan Thomas','TE',2019),
    (31,'Kalif Raymond','WR',2019),
    (16,'Byron Pringle','WR',2019),
    (26,'J.J. Arcega-Whiteside','WR',2019),
    (24,'Rhett Ellison','TE',2019),
    (16,'Darrel Williams','RB',2019),
    (29,'Nick Vannett','TE',2019),
    (4,'Duke Williams','WR',2019),
    (17,'Josh Jacobs','RB',2019),
    (28,'Richie James','WR',2019),
    (31,'Dion Lewis','RB',2019),
    (20,'Jakeem Grant Sr.','WR',2019),
    (13,'DeAndre Carter','WR',2019),
    (26,'DeSean Jackson','WR',2019),
    (30,'Justin Watson','WR',2019),
    (12,'Marcedes Lewis','TE',2019),
    (15,'James Shaughnessy','TE',2019),
    (8,'Demetrius Harris','TE',2019),
    (2,'Jaeden Graham','TE',2019),
    (21,'C.J. Ham','FB',2019),
    (15,'Ryquell Armstead','RB',2019),
    (32,'Adrian Peterson','RB',2019),
    (11,'Jesse James','TE',2019),
    (15,'Seth DeValve','TE',2019),
    (5,'Ian Thomas','TE',2019),
    (17,'Keelan Doss','WR',2019),
    (22,'Matt LaCosse','TE',2019),
    (14,'Parris Campbell','WR',2019),
    (11,'Kerryon Johnson','RB',2019),
    (23,'Dan Arnold','TE',2019),
    (26,'Mack Hollins','WR',2019),
    (4,'T.J. Yeldon','RB',2019),
    (27,'Deon Cain','WR',2019),
    (32,'Vernon Davis','TE',2019),
    (28,'Matt Breida','RB',2019),
    (17,'Marcell Ateman','WR',2019),
    (30,'Peyton Barber','RB',2019),
    (25,'Braxton Berrios','WR',2019),
    (2,'Olamide Zaccheaus','WR',2019),
    (10,'Jeff Heuerman','TE',2019),
    (4,'Tommy Sweeney','TE',2019),
    (22,'Ryan Izzo','TE',2019),
    (9,'Devin Smith','WR',2019),
    (22,'Brandon Bolden','RB',2019),
    (12,'Trevor Davis','WR',2019),
    (15,'Nick Leary','TE',2019),
    (28,'Dante Pettis','WR',2019),
    (11,'Ty Johnson','RB',2019),
    (17,'Derek Carrier','TE',2019),
    (9,'Tony Pollard','RB',2019),
    (5,'Brandon Zylstra','WR',2019),
    (1,'Chase Edmonds','RB',2019),
    (22,'Keal Harry','WR',2019),
    (32,'Hale Hentges','TE',2019),
    (24,'Wayne Gallman','RB',2019),
    (4,'Frank Gore','RB',2019),
    (12,'Robert Tonyan','TE',2019),
    (12,'Danny Vitale','FB',2019),
    (22,'Sony Michel','RB',2019),
    (14,'Mo Alie-Cox','TE',2019),
    (8,'Dontrell Hilliard','RB',2019),
    (32,'J.P. Holtz','TE',2019),
    (28,'Ross Dwelley','TE',2019),
    (2,'Christian Blake','WR',2019),
    (31,'MyCole Pruitt','TE',2019),
    (25,'Ty Montgomery II','WR',2019),
    (10,'Andrew Beck','FB',2019),
    (8,'Antonio Callaway','WR',2019),
    (20,'Mark Walton','RB',2019),
    (21,'Ameer Abdullah','RB',2019),
    (26,'Joshua Perkins','TE',2019),
    (2,'Ito Smith','RB',2019),
    (6,'Jesper Horsted','TE',2019),
    (6,'Trey Burton','TE',2019),
    (6,'Cordarrelle Patterson','RB',2019),
    (29,'Rashaad Penny','RB',2019),
    (14,'Marlon Mack','RB',2019),
    (21,'Alexander Mattison','RB',2019),
    (7,'Damion Willis','WR',2019),
    (1,'Trent Sherfield Sr.','WR',2019),
    (29,'Luke Willson','TE',2019),
    (32,'Derrius Guice','RB',2019),
    (18,'Virgil Green','TE',2019),
    (29,'C.J. Prosise','RB',2019),
    (8,'KhaDarel Hodge','WR',2019),
    (6,'Adam Shaheen','TE',2019),
    (25,'Daniel Brown','TE',2019),
    (4,'Tyler Kroft','TE',2019),
    (8,'Ernest Johnson','RB',2019),
    (21,'Chad Beebe','WR',2019),
    (3,'Justice Hill','RB',2019),
    (26,'Jordan Howard','RB',2019),
    (2,'Brian Hill','RB',2019),
    (6,'Riley Ridley','WR',2019),
    (5,'Chris Hogan','WR',2019),
    (16,'Blake Bell','TE',2019),
    (17,'Rico Gafford','CB',2019),
    (15,'Geoff Swaim','TE',2019),
    (20,'Durham Smythe','TE',2019),
    (32,'Wendell Smallwood','RB',2019),
    (4,'Robert Foster','WR',2019),
    (20,'Kalen Ballage','RB',2019),
    (27,'Tevin Jones','WR',2019),
    (11,'Chris Lacy','WR',2019),
    (6,'Ben Braunecker','TE',2019),
    (14,'Jonathan Williams','RB',2019),
    (21,'Tyler Conklin','TE',2019),
    (20,'Clive Walford','TE',2019),
    (5,'Reggie Bonnafon','RB',2019),
    (10,'Devontae Booker','RB',2019),
    (22,'Antonio Brown','WR',2019),
    (18,'Andre Patton','WR',2019),
    (29,'Travis Homer','RB',2019),
    (8,'Rashard Higgins','WR',2019),
    (31,'Khari Blasingame','FB',2019),
    (2,'Luke Stocker','TE',2019),
    (5,'DeAndrew White','WR',2019),
    (20,'Myles Gaskin','RB',2019),
    (14,'Ross Travis','TE',2019),
    (8,'Stephen Carlson','TE',2019),
    (18,'Lance Kendricks','TE',2019),
    (16,'Deon Yelder','TE',2019),
    (27,'Trey Edmunds','RB',2019),
    (26,'Deontay Burnett','WR',2019),
    (3,'Patrick Ricard','FB',2019),
    (25,'Trevon Wesco','TE',2019),
    (9,'Cedrick Wilson Jr.','WR',2019),
    (21,'Alexander Hollins','WR',2019),
    (3,'Gus Edwards','RB',2019),
    (17,'Alec Ingold','FB',2019),
    (14,'Jordan Wilkins','RB',2019),
    (18,'Jason Moore','WR',2019),
    (16,'Darwin Thompson','RB',2019),
    (13,'Carlos Hyde','RB',2019),
    (10,'Andy Janovich','FB',2019),
    (4,'Patrick DiMarco','FB',2019),
    (8,'David Njoku','TE',2019),
    (24,'TJ Jones','WR',2019),
    (18,'Geremy Davis','WR',2019),
    (22,'Elandon Roberts','LB',2019),
    (10,'Troy Fumagalli','TE',2019),
    (13,'Steven Mitchell Jr.','WR',2019),
    (19,'Darrell Henderson Jr.','RB',2019),
    (23,'Zach Line','FB',2019),
    (17,'J.J. Nelson','WR',2019),
    (2,'Ty Sambrailo','OT',2019),
    (30,'Bobo Wilson','WR',2019),
    (30,'Ishmael Hyman','WR',2019),
    (28,'Jeff Wilson Jr.','RB',2019),
    (22,'Gunner Olszewski','WR',2019),
    (25,'Bilal Powell','RB',2019),
    (26,'Jordan Matthews','TE',2019),
    (18,'Derek Watt','FB',2019),
    (14,'Devin Funchess','TE',2019),
    (4,'Lee Smith','TE',2019),
    (10,'Diontae Spencer','WR',2019),
    (15,'C.J. Board','WR',2019),
    (18,'Travis Benjamin','WR',2019),
    (7,'Drew Sample','TE',2019),
    (30,'Codey McElroy','TE',2019),
    (24,'Cody Core','WR',2019),
    (8,'Pharaoh Brown','TE',2019),
    (27,'Ryan Switzer','WR',2019),
    (32,'Cam Sims','WR',2019),
    (30,'Tanner Hudson','TE',2019),
    (19,'Johnny Mundt','TE',2019),
    (24,'Russell Shepard','WR',2019),
    (26,'Darren Sproles','RB',2019),
    (23,'Deonte Harty','WR',2019),
    (29,'Nick Bellore','LB',2019),
    (19,'Nick Scott','S',2019),
    (15,'Devine Ozigbo','RB',2019),
    (27,'Benny Snell Jr.','RB',2019),
    (1,'Michael Crabtree','WR',2019),
    (16,'Anthony Sherman','FB',2019),
    (2,'Kenjon Barner','RB',2019),
    (16,'Spencer Ware','RB',2019),
    (5,'Mike Davis','RB',2019),
    (24,'Da Mari Scott','WR',2019),
    (18,'Justin Jackson','RB',2019),
    (3,'Chris Moore','WR',2019),
    (10,'Fred Brown','WR',2019),
    (6,'Eric Saubert','TE',2019),
    (27,'Johnny Holton','WR',2019),
    (4,'Andre Roberts','WR',2019),
    (25,'Josh Bellamy','WR',2019),
    (23,'Zach Zenner','RB',2019),
    (11,'David Blough','QB',2019),
    (15,'Marqise Lee','WR',2019),
    (5,'Donte Moncrief','WR',2019),
    (12,'Tra Carson','RB',2019),
    (7,'Stanley Morgan Jr.','WR',2019),
    (31,'Darius Jennings','WR',2019),
    (26,'Robert Davis','WR',2019),
    (11,'Nick Bawden','FB',2019),
    (21,'Mike Boone','RB',2019),
    (14,'Ashton Dulin','WR',2019),
    (19,'Malcolm Brown','RB',2019),
    (31,'Rashard Davis','WR',2019),
    (9,'Ventell Bryant','WR',2019),
    (15,'Michael Walker','WR',2019),
    (15,'Josh Oliver','TE',2019),
    (17,'Ryan Grant','WR',2019),
    (18,'Troymaine Pope','RB',2019),
    (19,'Mike Thomas','WR',2019),
    (2,'Keith Smith','FB',2019),
    (30,'T.J. Logan','RB',2019),
    (7,'Cethan Carter','TE',2019),
    (31,'Cody Hollister','WR',2019),
    (11,'Isaac Nauta','TE',2019),
    (18,'Sean Culkin','TE',2019),
    (25,'Jeff Smith','WR',2019),
    (24,'Scott Simonson','TE',2019),
    (5,'Chris Manhertz','TE',2019),
    (15,'Tyler Ervin','RB',2019),
    (31,'Kevin Byard III','S',2019),
    (29,'John Ursua','WR',2019),
    (30,'Antony Auclair','TE',2019),
    (28,'Levine Toilolo','TE',2019),
    (13,'Taiwan Jones','RB',2019),
    (24,'Elijhaa Penny','RB',2019),
    (24,'Javorius Allen','RB',2019),
    (15,'Ben Koyack','TE',2019),
    (11,'Paul Perkins','RB',2019),
    (23,'Austin Carr','WR',2019),
    (27,'Kerrith Whyte','RB',2019),
    (23,'Ricky Ortiz','FB',2019),
    (13,'Jordan Thomas','TE',2019),
    (17,'Dwayne Harris','WR',2019),
    (15,'Cody Davis','S',2019),
    (25,'Chris Herndon','TE',2019),
    (2,'Qadree Ollison','RB',2019),
    (16,'De Anthony Thomas','WR',2019),
    (11,'Jeff Driskel','QB',2019),
    (23,'Dwayne Washington','RB',2019),
    (9,'Dalton Schultz','TE',2019),
    (13,'Deshaun Watson','QB',2019),
    (3,'Jaleel Scott','WR',2019),
    (5,'Alex Armah','RB',2019),
    (29,'Tyrone Swoopes','TE',2019),
    (22,'Jakob Johnson','FB',2019),
    (15,'Charles Jones','TE',2019),
    (11,'Bo Scarbrough','RB',2019),
    (27,'Roosevelt Nix','FB',2019),
    (1,'Darrell Daniels','TE',2019),
    (27,'Zach Gentry','TE',2019),
    (23,'Krishawn Hogan','WR',2019),
    (27,'Xavier Grimble','TE',2019),
    (30,'Cyril Grayson Jr.','WR',2019),
    (14,'Jacoby Brissett','QB',2019),
    (31,'Dennis Kelly','OT',2019),
    (31,'David Quessenberry','OT',2019),
    (4,'Senorise Perry','RB',2019),
    (24,'Eric Tomlinson','TE',2019),
    (4,'Dion Dawkins','OT',2019),
    (11,'Wes Hills','RB',2019),
    (12,'Darrius Shepherd','WR',2019),
    (24,'Jonathan Hilliman','RB',2019),
    (20,'Jason Sanders','PK',2019),
    (30,'Vita Vea','DT',2019),
    (20,'Christian Wilkins','DT',2019),
    (18,'Tyrod Taylor','QB',2019),
    (21,'Kirk Cousins','QB',2019),
    (9,'Jamize Olawale','FB',2019),
    (20,'Deon Lacey','LB',2019),
    (32,'Michael Burton','FB',2019),
    (26,'Jay Ajayi','RB',2019),
    (29,'George Fant','OT',2019),
    (23,'Justin Hardee Sr.','CB',2019),
    (31,'Dalyn Dawkins','RB',2019),
    (8,'Taywan Taylor','WR',2019),
    (14,'Chad Williams','WR',2019),
    (20,'Michael Deiter','G',2019),
    (11,'Travis Fulgham','WR',2019),
    (12,'Jace Sternberger','TE',2019),
    (31,'Dane Cruikshank','S',2019),
    (18,'Jalen Guyton','WR',2019),
    (23,'Lil Jordan Humphrey','WR',2019),
    (19,'David Long Jr.','CB',2019),
    (11,'Jamal Agnew','WR',2019),
    (2,'Kaleb McGary','OT',2019),
    (7,'Andy Dalton','QB',2019),
    (25,'Quincy Enunwa','WR',2019),
    (21,'Garrett Bradbury','C',2019),
    (8,'Wyatt Teller','G',2019),
    (31,'Derrick Henry','RB',2019),
    (8,'Nick Chubb','RB',2019),
    (9,'Ezekiel Elliott','RB',2019),
    (29,'Chris Carson','RB',2019),
    (15,'Leonard Fournette','RB',2019),
    (17,'Josh Jacobs','RB',2019),
    (7,'Joe Mixon','RB',2019),
    (21,'Dalvin Cook','RB',2019),
    (14,'Marlon Mack','RB',2019),
    (12,'Aaron Jones','RB',2019),
    (13,'Carlos Hyde','RB',2019),
    (10,'Phillip Lindsay','RB',2019),
    (24,'Saquon Barkley','RB',2019),
    (22,'Sony Michel','RB',2019),
    (32,'Adrian Peterson','RB',2019),
    (6,'David Montgomery','RB',2019),
    (26,'Miles Sanders','RB',2019),
    (20,'Kenyan Drake','RB',2019),
    (25,'Le Veon Bell','RB',2019),
    (4,'Devin Singletary','RB',2019),
    (28,'Raheem Mostert','RB',2019),
    (30,'Ronald Jones','RB',2019),
    (3,'Gus Edwards','RB',2019),
    (2,'Devonta Freeman','RB',2019),
    (23,'Latavius Murray','RB',2019),
    (28,'Matt Breida','RB',2019),
    (4,'Frank Gore','RB',2019),
    (18,'Austin Ekeler','RB',2019),
    (28,'Tevin Coleman','RB',2019),
    (26,'Jordan Howard','RB',2019),
    (16,'Damien Williams','RB',2019),
    (10,'Royce Freeman','RB',2019),
    (30,'Peyton Barber','RB',2019),
    (16,'LeSean McCoy','RB',2019),
    (27,'James Conner','RB',2019),
    (21,'Alexander Mattison','RB',2019),
    (12,'Jamaal Williams','RB',2019),
    (9,'Tony Pollard','RB',2019),
    (13,'Duke Johnson','RB',2019),
    (11,'Kerryon Johnson','RB',2019),
    (17,'DeAndre Washington','RB',2019),
    (11,'Bo Scarbrough','RB',2019),
    (29,'Rashaad Penny','RB',2019),
    (1,'David Johnson','RB',2019),
    (2,'Brian Hill','RB',2019),
    (14,'Jordan Wilkins','RB',2019),
    (1,'Chase Edmonds','RB',2019),
    (22,'Rex Burkhead','RB',2019),
    (21,'Mike Boone','RB',2019),
    (11,'Ty Johnson','RB',2019),
    (19,'Malcolm Brown','RB',2019),
    (26,'Boston Scott','RB',2019),
    (32,'Derrius Guice','RB',2019),
    (14,'Jonathan Williams','RB',2019),
    (3,'Justice Hill','RB',2019),
    (6,'Tarik Cohen','RB',2019),
    (31,'Dion Lewis','RB',2019),
    (11,'J.D. McKissic','RB',2019),
    (20,'Mark Walton','RB',2019),
    (18,'Justin Jackson','RB',2019),
    (14,'Nyheim Hines','RB',2019),
    (7,'Giovani Bernard','RB',2019),
    (20,'Patrick Laird','RB',2019),
    (17,'Jalen Richard','RB',2019),
    (16,'Darrel Williams','RB',2019),
    (32,'Chris Thompson','RB',2019),
    (20,'Kalen Ballage','RB',2019),
    (20,'Myles Gaskin','RB',2019),
    (5,'Curtis Samuel','WR',2019),
    (16,'Darwin Thompson','RB',2019),
    (27,'Kerrith Whyte','RB',2019),
    (5,'Reggie Bonnafon','RB',2019),
    (19,'Robert Woods','WR',2019),
    (21,'Ameer Abdullah','RB',2019),
    (29,'Travis Homer','RB',2019),
    (24,'Wayne Gallman','RB',2019),
    (15,'Ryquell Armstead','RB',2019),
    (2,'Ito Smith','RB',2019),
    (6,'Cordarrelle Patterson','RB',2019),
    (1,'Christian Kirk','WR',2019),
    (27,'Trey Edmunds','RB',2019),
    (24,'Jonathan Hilliman','RB',2019),
    (32,'Wendell Smallwood','RB',2019),
    (31,'Jonnu Smith','TE',2019),
    (12,'Trevor Davis','WR',2019),
    (24,'Sterling Shepard','WR',2019),
    (29,'C.J. Prosise','RB',2019),
    (22,'Brandon Bolden','RB',2019),
    (26,'Darren Sproles','RB',2019),
    (4,'T.J. Yeldon','RB',2019),
    (3,'Anthony Levine Sr.','S',2019),
    (23,'Dwayne Washington','RB',2019),
    (31,'A.J. Brown','WR',2019),
    (19,'Brandin Cooks','WR',2019),
    (25,'Vyncint Smith','WR',2019),
    (16,'Spencer Ware','RB',2019),
    (2,'Qadree Ollison','RB',2019),
    (8,'Dontrell Hilliard','RB',2019),
    (4,'Isaiah McKenzie','WR',2019),
    (22,'Keal Harry','WR',2019),
    (12,'Tra Carson','RB',2019),
    (9,'Tavon Austin','WR',2019),
    (11,'C.J. Anderson','RB',2019),
    (27,'Diontae Johnson','WR',2019),
    (13,'Taiwan Jones','RB',2019),
    (5,'DJ Moore','WR',2019),
    (24,'Elijhaa Penny','RB',2019),
    (24,'Javorius Allen','RB',2019),
    (29,'Marshawn Lynch','RB',2019),
    (14,'Parris Campbell','WR',2019),
    (2,'Calvin Ridley','WR',2019),
    (23,'Deonte Harty','WR',2019),
    (26,'Jay Ajayi','RB',2019),
    (11,'Paul Perkins','RB',2019),
    (4,'Robert Foster','WR',2019),
    (17,'Derek Carrier','TE',2019),
    (5,'Mike Davis','RB',2019),
    (15,'Devine Ozigbo','RB',2019),
    (15,'Dede Westbrook','WR',2019),
    (31,'Dalyn Dawkins','RB',2019),
    (29,'David Moore','WR',2019),
    (7,'Tyler Boyd','WR',2019),
    (19,'Josh Reynolds','WR',2019),
    (16,'Tyreek Hill','WR',2019),
    (28,'George Kittle','TE',2019),
    (22,'Phillip Dorsett','WR',2019),
    (11,'Wes Hills','RB',2019),
    (12,'Allen Lazard','WR',2019),
    (8,'Ernest Johnson','RB',2019),
    (23,'Zach Line','FB',2019),
    (24,'Bennie Fowler','WR',2019),
    (6,'Taylor Gabriel','WR',2019),
    (18,'Troymaine Pope','RB',2019),
    (14,'Chester Rogers','WR',2019),
    (30,'Dare Ogunbowale','RB',2019),
    (10,'Courtland Sutton','WR',2019),
    (17,'Alec Ingold','FB',2019),
    (21,'C.J. Ham','FB',2019),
    (16,'Mecole Hardman','WR',2019),
    (24,'Golden Tate','WR',2019),
    (18,'Keenan Allen','WR',2019),
    (30,'Breshad Perriman','WR',2019),
    (20,'Samaje Perine','RB',2019),
    (30,'Scotty Miller','WR',2019),
    (28,'Marquise Goodwin','WR',2019),
    (1,'Andy Isabella','WR',2019),
    (13,'Keke Coutee','WR',2019),
    (16,'Sammy Watkins','WR',2019),
    (2,'Russell Gage','WR',2019),
    (22,'Damien Harris','RB',2019),
    (25,'Josh Adams','RB',2019),
    (22,'Mohamed Sanu','WR',2019),
    (20,'Isaiah Ford','WR',2019),
    (12,'Dexter Williams','RB',2019),
    (30,'John Franklin','WR',2019),
    (29,'DK Metcalf','WR',2019),
    (5,'Alex Armah','RB',2019),
    (8,'Jarvis Landry','WR',2019),
    (15,'Tyler Ervin','RB',2019),
    (18,'Derek Watt','FB',2019),
    (30,'T.J. Logan','RB',2019),
    (13,'Buddy Howell','RB',2019),
    (16,'Anthony Sherman','FB',2019),
    (32,'Josh Ferguson','RB',2019),
    (12,'Marquez Valdes-Scantling','WR',2019),
    (27,'Johnny Holton','WR',2019),
    (11,'Jamal Agnew','WR',2019),
    (10,'Devontae Booker','RB',2019),
    (5,'Jordan Scarlett','RB',2019),
    (19,'John Kelly Jr.','RB',2019),
    (4,'Dawson Knox','TE',2019),
    (2,'Keith Smith','FB',2019),
    (30,'Chris Godwin','WR',2019),
    (6,'Ryan Nall','FB',2019),
    (4,'Andre Roberts','WR',2019),
    (4,'Patrick DiMarco','FB',2019),
    (28,'Kyle Juszczyk','FB',2019),
    (11,'Marvin Hall','WR',2019),
    (26,'Nelson Agholor','WR',2019),
    (24,'Evan Engram','TE',2019),
    (12,'Geronimo Allison','WR',2019),
    (29,'Will Dissly','TE',2019),
    (27,'Tony Brooks-James','RB',2019),
    (21,'Adam Thielen','WR',2019),
    (10,'Diontae Spencer','WR',2019),
    (9,'Amari Cooper','WR',2019),
    (19,'Nick Scott','S',2019),
    (21,'Bisi Johnson','WR',2019),
    (20,'De Lance Turner','RB',2019),
    (22,'Antonio Brown','WR',2019),
    (5,'Colin Jones','S',2019),
    (16,'De Anthony Thomas','WR',2019),
    (17,'Darren Waller','TE',2019),
    (26,'Greg Ward','WR',2019),
    (24,'Da Mari Scott','WR',2019),
    (1,'Alfred Morris','RB',2019),
    (16,'Travis Kelce','TE',2019),
    (20,'Clive Walford','TE',2019),
    (25,'Robbie Chosen','WR',2019),
    (25,'Jamison Crowder','WR',2019),
    (7,'John Ross','WR',2019),
    (17,'Erik Harris','S',2019),
    (22,'James Develin','FB',2019),
    (4,'Senorise Perry','RB',2019),
    (12,'Danny Vitale','FB',2019),
    (17,'Zay Jones','WR',2019),
    (1,'KeeSean Johnson','WR',2019),
    (26,'Alshon Jeffery','WR',2019),
    (27,'Vance McDonald','TE',2019),
    (18,'Mike Williams','WR',2019),
    (7,'Pharoh Cooper','WR',2019),
    (25,'Trevon Wesco','TE',2019),
    (15,'Marqise Lee','WR',2019),
    (31,'Adam Humphries','WR',2019),
    (10,'Andy Janovich','FB',2019),
    (3,'Trace McSorley','QB',2019),
    (3,'Chris Moore','WR',2019),
    (14,'Quenton Nelson','G',2019),
    (19,'Gerald Everett','TE',2019),
    (6,'Anthony Miller','WR',2019),
    (28,'Richie James','WR',2019),
    (23,'Zach Zenner','RB',2019),
    (2,'Julio Jones','WR',2019),
    (28,'Nick Mullens','QB',2019),
    (13,'Bryan Anger','P',2019),
    (29,'Tyler Lockett','WR',2019),
    (31,'Kalif Raymond','WR',2019),
    (5,'Jarius Wright','WR',2019),
    (27,'Jordan Berry','P',2019),
    (23,'Michael Thomas','WR',2019),
    (10,'Noah Fant','TE',2019),
    (13,'Deshaun Watson','QB',2020),
    (16,'Patrick Mahomes','QB',2020),
    (30,'Tom Brady','QB',2020),
    (2,'Matt Ryan','QB',2020),
    (4,'Josh Allen','QB',2020),
    (18,'Justin Herbert','QB',2020),
    (12,'Aaron Rodgers','QB',2020),
    (21,'Kirk Cousins','QB',2020),
    (29,'Russell Wilson','QB',2020),
    (14,'Philip Rivers','QB',2020),
    (17,'Derek Carr','QB',2020),
    (11,'Matthew Stafford','QB',2020),
    (1,'Kyler Murray','QB',2020),
    (19,'Jared Goff','QB',2020),
    (31,'Ryan Tannehill','QB',2020),
    (27,'Ben Roethlisberger','QB',2020),
    (5,'Teddy Bridgewater','QB',2020),
    (8,'Baker Mayfield','QB',2020),
    (24,'Daniel Jones','QB',2020),
    (23,'Drew Brees','QB',2020),
    (10,'Drew Lock','QB',2020),
    (3,'Lamar Jackson','QB',2020),
    (7,'Joe Burrow','QB',2020),
    (22,'Cam Newton','QB',2020),
    (26,'Carson Wentz','QB',2020),
    (28,'Nick Mullens','QB',2020),
    (15,'Gardner Minshew','QB',2020),
    (25,'Sam Darnold','QB',2020),
    (9,'Andy Dalton','QB',2020),
    (20,'Ryan Fitzpatrick','QB',2020),
    (6,'Mitchell Trubisky','QB',2020),
    (9,'Dak Prescott','QB',2020),
    (6,'Nick Foles','QB',2020),
    (20,'Tua Tagovailoa','QB',2020),
    (32,'Alex Smith','QB',2020),
    (32,'Dwayne Haskins','QB',2020),
    (28,'Jimmy Garoppolo','QB',2020),
    (15,'Mike Glennon','QB',2020),
    (26,'Jalen Hurts','QB',2020),
    (23,'Taysom Hill','QB',2020),
    (7,'Brandon Allen','QB',2020),
    (25,'Joe Flacco','QB',2020),
    (28,'C.J. Beathard','QB',2020),
    (15,'Jake Luton','QB',2020),
    (32,'Kyle Allen','QB',2020),
    (10,'Jeff Driskel','QB',2020),
    (24,'Colt McCoy','QB',2020),
    (5,'PJ Walker','QB',2020),
    (27,'Mason Rudolph','QB',2020),
    (10,'Brett Rypien','QB',2020),
    (11,'Chase Daniel','QB',2020),
    (22,'Jarrett Stidham','QB',2020),
    (16,'Chad Henne','QB',2020),
    (9,'Garrett Gilbert','QB',2020),
    (19,'John Wolford','QB',2020),
    (17,'Marcus Mariota','QB',2020),
    (9,'Ben DiNucci','QB',2020),
    (18,'Tyrod Taylor','QB',2020),
    (4,'Matt Barkley','QB',2020),
    (7,'Ryan Finley','QB',2020),
    (30,'Blaine Gabbert','QB',2020),
    (32,'Taylor Heinicke','QB',2020),
    (22,'Brian Hoyer','QB',2020),
    (1,'Chris Streveler','QB',2020),
    (3,'Trace McSorley','QB',2020),
    (23,'Jameis Winston','QB',2020),
    (8,'Jarvis Landry','WR',2020),
    (11,'David Blough','QB',2020),
    (8,'Case Keenum','QB',2020),
    (25,'Jamison Crowder','WR',2020),
    (22,'Jakobi Meyers','WR',2020),
    (3,'Robert Griffin III','QB',2020),
    (2,'Russell Gage','WR',2020),
    (22,'Julian Edelman','WR',2020),
    (29,'Geno Smith','QB',2020),
    (26,'Nate Sudfeld','QB',2020),
    (20,'Lynn Bowden Jr.','WR',2020),
    (17,'Zay Jones','WR',2020),
    (32,'Logan Thomas','TE',2020),
    (5,'Joseph Charlton','P',2020),
    (1,'Andy Lee','P',2020),
    (17,'Nathan Peterman','QB',2020),
    (9,'Cedrick Wilson Jr.','WR',2020),
    (4,'Cole Beasley','WR',2020),
    (13,'AJ McCarron','QB',2020),
    (24,'Golden Tate','WR',2020),
    (6,'Tyler Bray','QB',2020),
    (8,'Odell Beckham Jr.','WR',2020),
    (14,'Jacoby Brissett','QB',2020),
    (7,'Tyler Boyd','WR',2020),
    (3,'Sam Koch','P',2020),
    (26,'Greg Ward','WR',2020),
    (3,'Tyler Huntley','QB',2020),
    (4,'Jaquan Johnson','S',2020),
    (10,'Kendall Hinton','WR',2020),
    (16,'Tommy Townsend','P',2020),
    (4,'Isaiah McKenzie','WR',2020),
    (31,'Logan Woodside','QB',2020),
    (16,'Travis Kelce','TE',2020),
    (18,'Easton Stick','QB',2020),
    (27,'Joshua Dobbs','QB',2020),
    (31,'Brett Kern','P',2020),
    (13,'Randall Cobb','WR',2020),
    (9,'Chris Jones','P',2020),
    (18,'Keenan Allen','WR',2020),
    (16,'Sammy Watkins','WR',2020),
    (31,'Adam Humphries','WR',2020),
    (24,'Riley Dixon','P',2020),
    (7,'Alex Erickson','WR',2020),
    (14,'Zach Pascal','WR',2020),
    (12,'Tim Boyle','QB',2020),
    (11,'Jamal Agnew','WR',2020),
    (5,'DJ Moore','WR',2020),
    (25,'Jeff Smith','WR',2020),
    (32,'Isaiah Wright','WR',2020),
    (15,'James Robinson','RB',2020),
    (9,'CeeDee Lamb','WR',2020),
    (4,'Stefon Diggs','WR',2020),
    (1,'DeAndre Hopkins','WR',2020),
    (21,'Justin Jefferson','WR',2020),
    (12,'Davante Adams','WR',2020),
    (2,'Calvin Ridley','WR',2020),
    (29,'DK Metcalf','WR',2020),
    (16,'Tyreek Hill','WR',2020),
    (6,'Allen Robinson II','WR',2020),
    (17,'Darren Waller','TE',2020),
    (13,'Brandin Cooks','WR',2020),
    (32,'Terry McLaurin','WR',2020),
    (9,'Amari Cooper','WR',2020),
    (5,'Robbie Chosen','WR',2020),
    (31,'A.J. Brown','WR',2020),
    (29,'Tyler Lockett','WR',2020),
    (30,'Mike Evans','WR',2020),
    (31,'Corey Davis','WR',2020),
    (11,'Marvin Jones Jr.','WR',2020),
    (19,'Cooper Kupp','WR',2020),
    (19,'Robert Woods','WR',2020),
    (21,'Adam Thielen','WR',2020),
    (27,'Diontae Johnson','WR',2020),
    (7,'Tee Higgins','WR',2020),
    (17,'Nelson Agholor','WR',2020),
    (13,'William Fuller V','WR',2020),
    (27,'Chase Claypool','WR',2020),
    (10,'Jerry Jeudy','WR',2020),
    (5,'Curtis Samuel','WR',2020),
    (9,'Michael Gallup','WR',2020),
    (30,'Chris Godwin','WR',2020),
    (27,'JuJu Smith-Schuster','WR',2020),
    (20,'DeVante Parker','WR',2020),
    (2,'Julio Jones','WR',2020),
    (3,'Marquise Brown','WR',2020),
    (14,'T.Y. Hilton','WR',2020),
    (18,'Mike Williams','WR',2020),
    (23,'Alvin Kamara','RB',2020),
    (24,'Darius Slayton','WR',2020),
    (28,'Brandon Aiyuk','WR',2020),
    (10,'Tim Patrick','WR',2020),
    (23,'Emmanuel Sanders','WR',2020),
    (11,'T.J. Hockenson','TE',2020),
    (15,'DJ Chark Jr.','WR',2020),
    (20,'Mike Gesicki','TE',2020),
    (3,'Mark Andrews','TE',2020),
    (12,'Marquez Valdes-Scantling','WR',2020),
    (10,'Noah Fant','TE',2020),
    (28,'Kendrick Bourne','WR',2020),
    (24,'Sterling Shepard','WR',2020),
    (17,'Hunter Renfrow','WR',2020),
    (24,'Evan Engram','TE',2020),
    (15,'Keelan Cole Sr.','WR',2020),
    (28,'George Kittle','TE',2020),
    (6,'Darnell Mooney','WR',2020),
    (30,'Rob Gronkowski','TE',2020),
    (1,'Christian Kirk','WR',2020),
    (19,'Josh Reynolds','WR',2020),
    (9,'Dalton Schultz','TE',2020),
    (18,'Hunter Henry','TE',2020),
    (22,'Damiere Byrd','WR',2020),
    (11,'Danny Amendola','WR',2020),
    (15,'Laviska Shenault Jr.','WR',2020),
    (8,'Rashard Higgins','WR',2020),
    (4,'Gabe Davis','WR',2020),
    (32,'J.D. McKissic','RB',2020),
    (12,'Robert Tonyan','TE',2020),
    (2,'Hayden Hurst','TE',2020),
    (16,'Mecole Hardman','WR',2020),
    (27,'Eric Ebron','TE',2020),
    (26,'Travis Fulgham','WR',2020),
    (26,'Dallas Goedert','TE',2020),
    (7,'A.J. Green','WR',2020),
    (19,'Tyler Higbee','TE',2020),
    (18,'Jalen Guyton','WR',2020),
    (25,'Breshad Perriman','WR',2020),
    (23,'Jared Cook','TE',2020),
    (14,'Michael Pittman Jr.','WR',2020),
    (30,'Scotty Miller','WR',2020),
    (6,'Anthony Miller','WR',2020),
    (30,'Antonio Brown','WR',2020),
    (14,'Nyheim Hines','RB',2020),
    (32,'Cam Sims','WR',2020),
    (15,'Chris Conley','WR',2020),
    (16,'Demarcus Robinson','WR',2020),
    (4,'John Brown','WR',2020),
    (6,'Jimmy Graham','TE',2020),
    (17,'Henry Ruggs III','WR',2020),
    (12,'Allen Lazard','WR',2020),
    (31,'Jonnu Smith','TE',2020),
    (23,'Tre Quan Smith','WR',2020),
    (23,'Michael Thomas','WR',2020),
    (6,'David Montgomery','RB',2020),
    (1,'Dan Arnold','TE',2020),
    (8,'Austin Hooper','TE',2020),
    (3,'Willie Snead IV','WR',2020),
    (19,'Gerald Everett','TE',2020),
    (29,'David Moore','WR',2020),
    (1,'Larry Fitzgerald','WR',2020),
    (18,'Austin Ekeler','RB',2020),
    (13,'Jordan Akins','TE',2020),
    (1,'Chase Edmonds','RB',2020),
    (13,'Keke Coutee','WR',2020),
    (18,'Tyron Billy-Johnson','WR',2020),
    (26,'Jalen Reagor','WR',2020),
    (14,'Mo Alie-Cox','TE',2020),
    (28,'Richie James','WR',2020),
    (25,'Braxton Berrios','WR',2020),
    (27,'James Washington','WR',2020),
    (28,'Deebo Samuel Sr.','WR',2020),
    (20,'Myles Gaskin','RB',2020),
    (31,'Anthony Firkser','TE',2020),
    (10,'KJ Hamler','WR',2020),
    (22,'James White','RB',2020),
    (20,'Jakeem Grant Sr.','WR',2020),
    (5,'Mike Davis','RB',2020),
    (21,'Irv Smith Jr.','TE',2020),
    (21,'Dalvin Cook','RB',2020),
    (25,'Denzel Mims','WR',2020),
    (11,'Andre Swift','RB',2020),
    (7,'Giovani Bernard','RB',2020),
    (12,'Aaron Jones','RB',2020),
    (15,'Tyler Eifert','TE',2020),
    (7,'Drew Sample','TE',2020),
    (11,'Quintez Cephus','WR',2020),
    (26,'Richard Rodgers','TE',2020),
    (11,'Kenny Golladay','WR',2020),
    (9,'Ezekiel Elliott','RB',2020),
    (26,'Zach Ertz','TE',2020),
    (21,'Kyle Rudolph','TE',2020),
    (13,'David Johnson','RB',2020),
    (13,'Darren Fells','TE',2020),
    (22,'Keal Harry','WR',2020),
    (8,'Kareem Hunt','RB',2020),
    (8,'Donovan Peoples-Jones','WR',2020),
    (11,'Marvin Hall','WR',2020),
    (14,'Jonathan Taylor','RB',2020),
    (16,'Clyde Edwards-Helaire','RB',2020),
    (10,'DaeSean Hamilton','WR',2020),
    (20,'Preston Williams','WR',2020),
    (4,'Dawson Knox','TE',2020),
    (25,'Chris Herndon','TE',2020),
    (29,'Chris Carson','RB',2020),
    (30,'Cameron Brate','TE',2020),
    (20,'Isaiah Ford','WR',2020),
    (2,'Olamide Zaccheaus','WR',2020),
    (15,'Collin Johnson','WR',2020),
    (4,'Devin Singletary','RB',2020),
    (3,'Miles Boykin','WR',2020),
    (32,'Steven Sims','WR',2020),
    (15,'James Shaughnessy','TE',2020),
    (14,'Marcus Johnson','WR',2020),
    (28,'Jerick McKinnon','RB',2020),
    (14,'Jack Doyle','TE',2020),
    (29,'Will Dissly','TE',2020),
    (14,'Trey Burton','TE',2020),
    (13,'Duke Johnson','RB',2020),
    (32,'Antonio Gibson','RB',2020),
    (28,'Ross Dwelley','TE',2020),
    (6,'Cole Kmet','TE',2020),
    (29,'Greg Olsen','TE',2020),
    (8,'Harrison Bryant','TE',2020),
    (17,'Josh Jacobs','RB',2020),
    (26,'DeSean Jackson','WR',2020),
    (12,'Jamaal Williams','RB',2020),
    (13,'Chad Hansen','WR',2020),
    (30,'Leonard Fournette','RB',2020),
    (28,'Jordan Reed','TE',2020),
    (1,'Andy Isabella','WR',2020),
    (19,'Van Jefferson','WR',2020),
    (27,'James Conner','RB',2020),
    (8,'David Njoku','TE',2020),
    (23,'Marquez Callaway','WR',2020),
    (26,'Boston Scott','RB',2020),
    (29,'Jacob Hollister','TE',2020),
    (20,'Durham Smythe','TE',2020),
    (28,'Kyle Juszczyk','FB',2020),
    (21,'Chad Beebe','WR',2020),
    (3,'Devin Duvernay','WR',2020),
    (22,'Ryan Izzo','TE',2020),
    (2,'Brian Hill','RB',2020),
    (26,'Miles Sanders','RB',2020),
    (21,'Tyler Conklin','TE',2020),
    (17,'Bryan Edwards','WR',2020),
    (22,'Rex Burkhead','RB',2020),
    (9,'Tony Pollard','RB',2020),
    (21,'Bisi Johnson','WR',2020),
    (11,'Mohamed Sanu','WR',2020),
    (31,'Kalif Raymond','WR',2020),
    (11,'Kerryon Johnson','RB',2020),
    (23,'Deonte Harty','WR',2020),
    (8,'KhaDarel Hodge','WR',2020),
    (23,'Latavius Murray','RB',2020),
    (20,'Mack Hollins','WR',2020),
    (18,'Justin Jackson','RB',2020),
    (1,'KeeSean Johnson','WR',2020),
    (23,'Adam Trautman','TE',2020),
    (30,'Tyler Johnson','WR',2020),
    (26,'John Hightower','WR',2020),
    (25,'Kalen Ballage','RB',2020),
    (30,'Ronald Jones','RB',2020),
    (2,'Todd Gurley II','RB',2020),
    (32,'Dontrelle Inman','WR',2020),
    (13,'Pharaoh Brown','TE',2020),
    (19,'Malcolm Brown','RB',2020),
    (16,'Byron Pringle','WR',2020),
    (18,'Donald Parham Jr.','TE',2020),
    (29,'Freddie Swain','WR',2020),
    (19,'Darrell Henderson Jr.','RB',2020),
    (10,'Melvin Gordon III','RB',2020),
    (28,'Raheem Mostert','RB',2020),
    (9,'Noah Brown','WR',2020),
    (8,'Nick Chubb','RB',2020),
    (7,'Auden Tate','WR',2020),
    (20,'Adam Shaheen','TE',2020),
    (5,'Christian McCaffrey','RB',2020),
    (18,'Joshua Kelley','RB',2020),
    (15,'Chris Thompson','RB',2020),
    (30,'O.J. Howard','TE',2020),
    (5,'Ian Thomas','TE',2020),
    (13,'Kenny Stills','WR',2020),
    (2,'Christian Blake','WR',2020),
    (17,'Foster Moreau','TE',2020),
    (25,'Le Veon Bell','RB',2020),
    (17,'Jalen Richard','RB',2020),
    (7,'Joe Mixon','RB',2020),
    (1,'Kenyan Drake','RB',2020),
    (28,'Jeff Wilson Jr.','RB',2020),
    (6,'Cordarrelle Patterson','RB',2020),
    (7,'Mike Thomas','WR',2020),
    (11,'Jesse James','TE',2020),
    (3,'Gus Edwards','RB',2020),
    (24,'Dion Lewis','RB',2020),
    (21,'Alexander Mattison','RB',2020),
    (19,'Cam Akers','RB',2020),
    (10,'Albert Okwuegbunam Jr.','TE',2020),
    (3,'J.K. Dobbins','RB',2020),
    (4,'Tyler Kroft','TE',2020),
    (25,'Chris Hogan','WR',2020),
    (12,'Equanimeous St. Brown','WR',2020),
    (16,'Darrel Williams','RB',2020),
    (26,'Alshon Jeffery','WR',2020),
    (31,'Derrick Henry','RB',2020),
    (24,'Wayne Gallman','RB',2020),
    (22,'Sony Michel','RB',2020),
    (12,'Jace Sternberger','TE',2020),
    (3,'Nick Boyle','TE',2020),
    (24,'Kaden Smith','TE',2020),
    (29,'DeeJay Dallas','RB',2020),
    (9,'Blake Bell','TE',2020),
    (17,'Alec Ingold','FB',2020),
    (12,'Marcedes Lewis','TE',2020),
    (18,'Stephen Anderson','TE',2020),
    (26,'Quez Watkins','WR',2020),
    (14,'Jordan Wilkins','RB',2020),
    (1,'Maxx Williams','TE',2020),
    (11,'Adrian Peterson','RB',2020),
    (30,'LeSean McCoy','RB',2020),
    (24,'C.J. Board','WR',2020),
    (31,'Cameron Batson','WR',2020),
    (27,'Vance McDonald','TE',2020),
    (25,'Ty Johnson','RB',2020),
    (21,'C.J. Ham','FB',2020),
    (20,'Matt Breida','RB',2020),
    (10,'Nick Vannett','TE',2020),
    (4,'Zack Moss','RB',2020),
    (30,'Justin Watson','WR',2020),
    (29,'Carlos Hyde','RB',2020),
    (1,'Darrell Daniels','TE',2020),
    (20,'Malcolm Perry','RB',2020),
    (24,'Austin Mack','WR',2020),
    (29,'Travis Homer','RB',2020),
    (25,'Frank Gore','RB',2020),
    (7,'C.J. Uzomah','TE',2020),
    (25,'Ryan Griffin','TE',2020),
    (28,'Trent Taylor','WR',2020),
    (26,'J.J. Arcega-Whiteside','WR',2020),
    (12,'Tyler Ervin','RB',2020),
    (17,'Devontae Booker','RB',2020),
    (31,'Geoff Swaim','TE',2020),
    (10,'Royce Freeman','RB',2020),
    (10,'Troy Fumagalli','TE',2020),
    (14,'DeMichael Harris','WR',2020),
    (27,'Ray-Ray McCloud III','WR',2020),
    (24,'Dante Pettis','WR',2020),
    (2,'Ito Smith','RB',2020),
    (5,'Pharoh Cooper','WR',2020),
    (18,'KJ Hill Jr.','WR',2020),
    (14,'Parris Campbell','WR',2020),
    (17,'Jason Witten','TE',2020),
    (2,'Brandon Powell','WR',2020),
    (20,'Patrick Laird','RB',2020),
    (6,'Ryan Nall','FB',2020),
    (7,'Samaje Perine','RB',2020),
    (10,'Courtland Sutton','WR',2020),
    (12,'Malik Taylor','WR',2020),
    (16,'Darwin Thompson','RB',2020),
    (2,'Luke Stocker','TE',2020),
    (24,'Damion Ratley','WR',2020),
    (25,'La Mical Perine','RB',2020),
    (10,'Tyrie Cleveland','WR',2020),
    (16,'Nick Keizer','TE',2020),
    (22,'Gunner Olszewski','WR',2020),
    (27,'Benny Snell Jr.','RB',2020),
    (20,'Salvon Ahmed','RB',2020),
    (13,'Steven Mitchell Jr.','WR',2020),
    (8,'Ja Marcus Bradley','WR',2020),
    (24,'Saquon Barkley','RB',2020),
    (2,'Keith Smith','FB',2020),
    (5,'Rodney Smith','RB',2020),
    (24,'Devonta Freeman','RB',2020),
    (21,'Ameer Abdullah','RB',2020),
    (30,'Jaydon Mickens','WR',2020),
    (31,'Jeremy McNichols','RB',2020),
    (15,'Dare Ogunbowale','RB',2020),
    (27,'Anthony McFarland Jr.','RB',2020),
    (7,'Cethan Carter','TE',2020),
    (19,'Johnny Mundt','TE',2020),
    (14,'Ashton Dulin','WR',2020),
    (5,'Chris Manhertz','TE',2020),
    (22,'Damien Harris','RB',2020),
    (3,'Mark Ingram II','RB',2020),
    (18,'Virgil Green','TE',2020),
    (1,'Trent Sherfield Sr.','WR',2020),
    (31,'MyCole Pruitt','TE',2020),
    (2,'Laquon Treadwell','WR',2020),
    (6,'Javon Wims','WR',2020),
    (3,'Dez Bryant','WR',2020),
    (24,'Levine Toilolo','TE',2020),
    (23,'Josh Hill','TE',2020),
    (27,'Jaylen Samuels','RB',2020),
    (12,'Darrius Shepherd','WR',2020),
    (23,'Lil Jordan Humphrey','WR',2020),
    (6,'Demetrius Harris','TE',2020),
    (3,'Patrick Ricard','FB',2020),
    (11,'Hunter Bryant','TE',2020),
    (17,'Theo Riddick','RB',2020),
    (18,'Troymaine Pope','RB',2020),
    (15,'Devine Ozigbo','RB',2020),
    (30,'Tanner Hudson','TE',2020),
    (28,'River Cracraft','WR',2020),
    (6,'Tarik Cohen','RB',2020),
    (6,'Ted Ginn Jr.','WR',2020),
    (31,'Khari Blasingame','FB',2020),
    (23,'Juwan Johnson','TE',2020),
    (6,'Riley Ridley','WR',2020),
    (22,'Devin Asiasi','TE',2020),
    (32,'Robert Foster','WR',2020),
    (16,'Deon Yelder','TE',2020),
    (28,'Charlie Woerner','TE',2020),
    (4,'Lee Smith','TE',2020),
    (22,'Jakob Johnson','FB',2020),
    (25,'Lawrence Cager','TE',2020),
    (13,'Kahale Warring','TE',2020),
    (5,'Brandon Zylstra','WR',2020),
    (4,'Andre Roberts','WR',2020),
    (28,'Tevin Coleman','RB',2020),
    (30,'Ke Shawn Vaughn','RB',2020),
    (28,'JaMycal Hasty','RB',2020),
    (31,'Nick Westbrook-Ikhine','WR',2020),
    (15,'Terry Godwin','WR',2020),
    (5,'Seth Roberts','WR',2020),
    (25,'Daniel Brown','TE',2020),
    (20,'DeAndre Washington','RB',2020),
    (14,'Marlon Mack','RB',2020),
    (7,'Trayveon Williams','RB',2020),
    (22,'Isaiah Zuber','WR',2020),
    (25,'Josh Adams','RB',2020),
    (23,'Michael Burton','FB',2020),
    (10,'Phillip Lindsay','RB',2020),
    (23,'Ty Montgomery II','WR',2020),
    (23,'Austin Carr','WR',2020),
    (28,'Austin Walter','RB',2020),
    (31,'Darrynton Evans','RB',2020),
    (10,'Diontae Spencer','WR',2020),
    (1,'Ezekiel Turner','LB',2020),
    (12,'Dominique Dafney','TE',2020),
    (26,'Corey Clement','RB',2020),
    (2,'Jaeden Graham','TE',2020),
    (18,'Gabe Nabers','FB',2020),
    (14,'Daurice Fountain','WR',2020),
    (4,'T.J. Yeldon','RB',2020),
    (4,'Jake Kumerow','WR',2020),
    (11,'Jonathan Williams','RB',2020),
    (12,'AJ Dillon','RB',2020),
    (12,'Tavon Austin','WR',2020),
    (24,'Elijhaa Penny','RB',2020),
    (20,'Antonio Callaway','WR',2020),
    (3,'Justice Hill','RB',2020),
    (4,'Antonio Williams','RB',2020),
    (24,'Alfred Morris','RB',2020),
    (26,'Deontay Burnett','WR',2020),
    (13,'C.J. Prosise','RB',2020),
    (5,'Reggie Bonnafon','RB',2020),
    (5,'Alex Armah','RB',2020),
    (7,'John Ross','WR',2020),
    (15,'Eric Saubert','TE',2020),
    (25,'Josh Malone','WR',2020),
    (4,'Reggie Gilliam','FB',2020),
    (25,'Jaleel Scott','WR',2020),
    (22,'Dalton Keene','TE',2020),
    (29,'Colby Parkinson','TE',2020),
    (5,'Trenton Cannon','RB',2020),
    (22,'Donte Moncrief','WR',2020),
    (17,'Derek Carrier','TE',2020),
    (8,'Ernest Johnson','RB',2020),
    (3,'James Proche II','WR',2020),
    (8,'Andy Janovich','FB',2020),
    (5,'Keith Kirkwood','WR',2020),
    (4,'Siran Neal','CB',2020),
    (25,'Vyncint Smith','WR',2020),
    (29,'Luke Willson','TE',2020),
    (9,'Blake Jarwin','TE',2020),
    (32,'Peyton Barber','RB',2020),
    (31,'Cody Hollister','WR',2020),
    (12,'Josiah Deguara','TE',2020),
    (23,'Bennie Fowler','WR',2020),
    (16,'Marcus Kemp','WR',2020),
    (8,'Stephen Carlson','TE',2020),
    (1,'Jonathan Ward','RB',2020),
    (32,'Temarrick Hemingway','TE',2020),
    (16,'Gehrig Dieter','WR',2020),
    (21,'Mike Boone','RB',2020),
    (15,'Ben Ellefson','TE',2020),
    (29,'Nick Bellore','LB',2020),
    (20,'Chandler Cox','FB',2020),
    (6,'DeAndre Carter','WR',2020),
    (11,'Jason Cabinda','FB',2020),
    (13,'Charlie Heck','OT',2020),
    (1,'D.J. Foster','RB',2020),
    (5,'Colin Thompson','TE',2020),
    (13,'Max Scharping','G',2020),
    (13,'Scottie Phillips','RB',2020),
    (6,'Lamar Miller','RB',2020),
    (32,'Jeremy Sprinkle','TE',2020),
    (13,'Cullen Gillaspia','LB',2020),
    (21,'Brandon Dillon','TE',2020),
    (16,'Anthony Sherman','FB',2020),
    (23,'Tommylee Lewis','WR',2020),
    (10,'Jake Butt','TE',2020),
    (31,'Onta Foreman','RB',2020),
    (10,'LeVante Bellamy','RB',2020),
    (7,'Trenton Irwin','WR',2020),
    (25,'Trevon Wesco','TE',2020),
    (6,'Bobby Massie','OT',2020),
    (29,'Alex Collins','RB',2020),
    (15,'Dede Westbrook','WR',2020),
    (22,'J.J. Taylor','RB',2020),
    (26,'Jason Croom','TE',2020),
    (13,'Buddy Howell','RB',2020),
    (29,'Penny Hart','WR',2020),
    (32,'Antonio Gandy-Golden','TE',2020),
    (11,'Isaac Nauta','TE',2020),
    (22,'Jordan Thomas','TE',2020),
    (15,'Craig Reynolds','RB',2020),
    (15,'Bruce Miller','FB',2020),
    (16,'Eric Fisher','OT',2020),
    (32,'Marcus Baugh','TE',2020),
    (8,'Dontrell Hilliard','RB',2020),
    (26,'Adrian Killins','RB',2020),
    (8,'Kendall Lamm','OT',2020),
    (4,'Taiwan Jones','RB',2020),
    (30,'Kenjon Barner','RB',2020),
    (9,'C.J. Goodwin','CB',2020),
    (24,'Eric Tomlinson','TE',2020),
    (1,'Seth DeValve','TE',2020),
    (6,'J.P. Holtz','TE',2020),
    (7,'Mason Schreck','TE',2020),
    (27,'Jerald Hawkins','OT',2020),
    (21,'Tajae Sharpe','WR',2020),
    (27,'Kevin Rader','TE',2020),
    (16,'Ricky Seals-Jones','TE',2020),
    (32,'Jeff Badet','WR',2020),
    (8,'Taywan Taylor','WR',2020),
    (24,'Nick Gates','C',2020),
    (15,'Tyler Davis','TE',2020),
    (26,'Hakeem Butler','WR',2020),
    (14,'Noah Togiai','TE',2020),
    (18,'Joe Reed','WR',2020),
    (31,'Aaron Brewer','G',2020),
    (26,'Jason Huntley','RB',2020),
    (17,'Rico Gafford','CB',2020),
    (30,'Antony Auclair','TE',2020),
    (30,'Cyril Grayson Jr.','WR',2020),
    (26,'Jordan Howard','RB',2020),
    (7,'Shawn Williams','S',2020),
    (29,'Rashaad Penny','RB',2020),
    (6,'Artavis Pierce','RB',2020),
    (29,'Bo Scarbrough','RB',2020),
    (5,'Jeremy Chinn','S',2020),
    (5,'Tommy Stevens','TE',2020),
    (9,'Rico Dowdle','RB',2020),
    (20,'Clayton Fejedelem','S',2020),
    (23,'Dwayne Washington','RB',2020),
    (23,'Tony Jones Jr.','RB',2020),
    (6,'Barkevious Mingo','LB',2020),
    (31,'Senorise Perry','RB',2020),
    (12,'Dexter Williams','RB',2020),
    (12,'John Lovett','FB',2020),
    (2,'Tony Brooks-James','RB',2020),
    (31,'Amani Hooker','S',2020),
    (9,'Darian Thompson','S',2020),
    (8,'JoJo Natson','WR',2020),
    (2,'Qadree Ollison','RB',2020),
    (11,'C.J. Moore','S',2020),
    (2,'Sharrod Neasman','S',2020),
    (5,'Myles Hartsfield','S',2020),
    (17,'Jeff Heath','S',2020),
    (10,'Sam Martin','P',2020),
    (3,'Matt Skura','C',2020),
    (17,'AJ Cole','P',2020),
    (8,'Jamie Gillan','P',2020),
    (2,'Matt Schaub','QB',2020),
    (18,'Ty Long','P',2020),
    (30,'Tom Brady','QB',2021),
    (18,'Justin Herbert','QB',2021),
    (19,'Matthew Stafford','QB',2021),
    (16,'Patrick Mahomes','QB',2021),
    (17,'Derek Carr','QB',2021),
    (7,'Joe Burrow','QB',2021),
    (9,'Dak Prescott','QB',2021),
    (4,'Josh Allen','QB',2021),
    (21,'Kirk Cousins','QB',2021),
    (12,'Aaron Rodgers','QB',2021),
    (2,'Matt Ryan','QB',2021),
    (28,'Jimmy Garoppolo','QB',2021),
    (22,'Mac Jones','QB',2021),
    (1,'Kyler Murray','QB',2021),
    (27,'Ben Roethlisberger','QB',2021),
    (31,'Ryan Tannehill','QB',2021),
    (15,'Trevor Lawrence','QB',2021),
    (14,'Carson Wentz','QB',2021),
    (32,'Taylor Heinicke','QB',2021),
    (11,'Jared Goff','QB',2021),
    (26,'Jalen Hurts','QB',2021),
    (29,'Russell Wilson','QB',2021),
    (3,'Lamar Jackson','QB',2021),
    (13,'Davis Mills','QB',2021),
    (20,'Tua Tagovailoa','QB',2021),
    (5,'Sam Darnold','QB',2021),
    (25,'Zach Wilson','QB',2021),
    (6,'Andy Dalton','QB',2021),
    (20,'Jacoby Brissett','QB',2021),
    (23,'Trevor Siemian','QB',2021),
    (3,'Tyler Huntley','QB',2021),
    (23,'Taysom Hill','QB',2021),
    (13,'Tyrod Taylor','QB',2021),
    (25,'Mike White','QB',2021),
    (24,'Mike Glennon','QB',2021),
    (10,'Drew Lock','QB',2021),
    (1,'Colt McCoy','QB',2021),
    (29,'Geno Smith','QB',2021),
    (5,'Cam Newton','QB',2021),
    (25,'Josh Johnson','QB',2021),
    (28,'Trey Lance','QB',2021),
    (11,'Tim Boyle','QB',2021),
    (8,'Case Keenum','QB',2021),
    (26,'Gardner Minshew','QB',2021),
    (9,'Cooper Rush','QB',2021),
    (12,'Jordan Love','QB',2021),
    (5,'PJ Walker','QB',2021),
    (25,'Joe Flacco','QB',2021),
    (27,'Mason Rudolph','QB',2021),
    (6,'Nick Foles','QB',2021),
    (22,'Brian Hoyer','QB',2021),
    (24,'Jake Fromm','QB',2021),
    (32,'Garrett Gilbert','QB',2021),
    (21,'Sean Mannion','QB',2021),
    (7,'Brandon Allen','QB',2021),
    (8,'Nick Mullens','QB',2021),
    (23,'Ian Book','QB',2021),
    (32,'Kyle Allen','QB',2021),
    (9,'Cedrick Wilson Jr.','WR',2021),
    (16,'Chad Henne','QB',2021),
    (11,'Tom Kennedy','WR',2021),
    (30,'Blaine Gabbert','QB',2021),
    (7,'Tyler Boyd','WR',2021),
    (22,'Jakobi Meyers','WR',2021),
    (4,'Mitchell Trubisky','QB',2021),
    (11,'Jack Fox','P',2021),
    (21,'Justin Jefferson','WR',2021),
    (1,'Christian Kirk','WR',2021),
    (22,'Kendrick Bourne','WR',2021),
    (14,'Jacob Eason','QB',2021),
    (28,'Deebo Samuel','WR',2021),
    (1,'Chris Banjo','S',2021),
    (2,'Josh Rosen','QB',2021),
    (24,'Kadarius Toney','WR',2021),
    (10,'Courtland Sutton','WR',2021),
    (16,'Tommy Townsend','P',2021),
    (31,'Matthias Farley','S',2021),
    (31,'Derrick Henry','RB',2021),
    (19,'John Wolford','QB',2021),
    (21,'Kellen Mond','QB',2021),
    (17,'Marcus Mariota','QB',2021),
    (9,'Ezekiel Elliott','RB',2021),
    (19,'Johnny Hekker','P',2021),
    (26,'Greg Ward','WR',2021),
    (10,'Kendall Hinton','WR',2021),
    (3,'Sam Koch','P',2021),
    (13,'Danny Amendola','WR',2021),
    (4,'Cole Beasley','WR',2021),
    (2,'Cordarrelle Patterson','RB',2021),
    (18,'Keenan Allen','WR',2021),
    (13,'Rex Burkhead','RB',2021),
    (8,'Jarvis Landry','WR',2021),
    (20,'Albert Wilson','WR',2021),
    (27,'Chris Boswell','PK',2021),
    (25,'Jamison Crowder','WR',2021),
    (24,'Riley Dixon','P',2021),
    (18,'Ty Long','P',2021),
    (4,'Stefon Diggs','WR',2021),
    (19,'Cooper Kupp','WR',2021),
    (25,'Keelan Cole Sr.','WR',2021),
    (20,'Mike Gesicki','TE',2021),
    (11,'David Blough','QB',2021),
    (10,'Brett Rypien','QB',2021),
    (2,'Feleipe Franks','TE',2021),
    (6,'David Montgomery','RB',2021),
    (23,'Blake Gillikin','P',2021),
    (31,'A.J. Brown','WR',2021),
    (11,'Andre Swift','RB',2021),
    (5,'Brandon Zylstra','WR',2021),
    (12,'Davante Adams','WR',2021),
    (7,'Ja Marr Chase','WR',2021),
    (28,'Deebo Samuel Sr.','WR',2021),
    (3,'Mark Andrews','TE',2021),
    (16,'Tyreek Hill','WR',2021),
    (29,'Tyler Lockett','WR',2021),
    (27,'Diontae Johnson','WR',2021),
    (5,'DJ Moore','WR',2021),
    (18,'Mike Williams','WR',2021),
    (16,'Travis Kelce','TE',2021),
    (9,'CeeDee Lamb','WR',2021),
    (7,'Tee Higgins','WR',2021),
    (14,'Michael Pittman Jr.','WR',2021),
    (6,'Darnell Mooney','WR',2021),
    (32,'Terry McLaurin','WR',2021),
    (17,'Hunter Renfrow','WR',2021),
    (13,'Brandin Cooks','WR',2021),
    (30,'Mike Evans','WR',2021),
    (2,'Kyle Pitts','TE',2021),
    (20,'Jaylen Waddle','WR',2021),
    (3,'Marquise Brown','WR',2021),
    (29,'DK Metcalf','WR',2021),
    (26,'DeVonta Smith','WR',2021),
    (11,'Amon-Ra St. Brown','WR',2021),
    (28,'George Kittle','TE',2021),
    (9,'Amari Cooper','WR',2021),
    (27,'Chase Claypool','WR',2021),
    (1,'A.J. Green','WR',2021),
    (15,'Marvin Jones Jr.','WR',2021),
    (26,'Dallas Goedert','TE',2021),
    (28,'Brandon Aiyuk','WR',2021),
    (9,'Dalton Schultz','TE',2021),
    (30,'Rob Gronkowski','TE',2021),
    (19,'Van Jefferson','WR',2021),
    (2,'Russell Gage','WR',2021),
    (26,'Zach Ertz','TE',2021),
    (10,'Tim Patrick','WR',2021),
    (23,'Marquez Callaway','WR',2021),
    (16,'Mecole Hardman','WR',2021),
    (10,'Noah Fant','TE',2021),
    (17,'Darren Waller','TE',2021),
    (21,'K.J. Osborn','WR',2021),
    (18,'Austin Ekeler','RB',2021),
    (26,'Quez Watkins','WR',2021),
    (4,'Emmanuel Sanders','WR',2021),
    (15,'Laviska Shenault Jr.','WR',2021),
    (6,'Cole Kmet','TE',2021),
    (22,'Hunter Henry','TE',2021),
    (8,'Donovan Peoples-Jones','WR',2021),
    (21,'Tyler Conklin','TE',2021),
    (4,'Dawson Knox','TE',2021),
    (11,'Kalif Raymond','WR',2021),
    (17,'Bryan Edwards','WR',2021),
    (23,'Deonte Harty','WR',2021),
    (16,'Byron Pringle','WR',2021),
    (18,'Jared Cook','TE',2021),
    (19,'Tyler Higbee','TE',2021),
    (4,'Gabe Davis','WR',2021),
    (17,'Zay Jones','WR',2021),
    (8,'Odell Beckham Jr.','WR',2021),
    (24,'Kenny Golladay','WR',2021),
    (5,'Robbie Chosen','WR',2021),
    (20,'DeVante Parker','WR',2021),
    (3,'Rashod Bateman','WR',2021),
    (12,'Allen Lazard','WR',2021),
    (27,'Pat Freiermuth','TE',2021),
    (7,'C.J. Uzomah','TE',2021),
    (29,'Gerald Everett','TE',2021),
    (31,'Nick Westbrook-Ikhine','WR',2021),
    (8,'David Njoku','TE',2021),
    (22,'Nelson Agholor','WR',2021),
    (27,'Najee Harris','RB',2021),
    (10,'Jerry Jeudy','WR',2021),
    (19,'DeSean Jackson','WR',2021),
    (16,'Darrel Williams','RB',2021),
    (18,'Jalen Guyton','WR',2021),
    (13,'Nico Collins','WR',2021),
    (23,'Alvin Kamara','RB',2021),
    (1,'Rondale Moore','WR',2021),
    (31,'Julio Jones','WR',2021),
    (15,'Laquon Treadwell','WR',2021),
    (12,'Marquez Valdes-Scantling','WR',2021),
    (6,'Allen Robinson II','WR',2021),
    (24,'Evan Engram','TE',2021),
    (2,'Olamide Zaccheaus','WR',2021),
    (22,'Brandon Bolden','RB',2021),
    (31,'Josh Reynolds','WR',2021),
    (3,'Sammy Watkins','WR',2021),
    (12,'Aaron Jones','RB',2021),
    (14,'Zach Pascal','WR',2021),
    (32,'Adam Humphries','WR',2021),
    (23,'Tre Quan Smith','WR',2021),
    (1,'James Conner','RB',2021),
    (17,'Foster Moreau','TE',2021),
    (25,'Ty Johnson','RB',2021),
    (30,'Tyler Johnson','WR',2021),
    (14,'Jonathan Taylor','RB',2021),
    (20,'Durham Smythe','TE',2021),
    (18,'Joshua Palmer','WR',2021),
    (17,'Josh Jacobs','RB',2021),
    (8,'Austin Hooper','TE',2021),
    (29,'Freddie Swain','WR',2021),
    (24,'Darius Slayton','WR',2021),
    (9,'Tony Pollard','RB',2021),
    (14,'T.Y. Hilton','WR',2021),
    (10,'Albert Okwuegbunam Jr.','TE',2021),
    (6,'Damiere Byrd','WR',2021),
    (25,'Michael Carter','RB',2021),
    (13,'Chris Conley','WR',2021),
    (14,'Mo Alie-Cox','TE',2021),
    (10,'Javonte Williams','RB',2021),
    (7,'Joe Mixon','RB',2021),
    (6,'Marquise Goodwin','WR',2021),
    (12,'AJ Dillon','RB',2021),
    (1,'Chase Edmonds','RB',2021),
    (14,'Nyheim Hines','RB',2021),
    (14,'Jack Doyle','TE',2021),
    (31,'Chester Rogers','WR',2021),
    (26,'Jalen Reagor','WR',2021),
    (28,'Kyle Juszczyk','FB',2021),
    (32,'DeAndre Carter','WR',2021),
    (22,'Jonnu Smith','TE',2021),
    (32,'Antonio Gibson','RB',2021),
    (31,'Anthony Firkser','TE',2021),
    (5,'Ameer Abdullah','RB',2021),
    (28,'Jauan Jennings','WR',2021),
    (27,'Ray-Ray McCloud III','WR',2021),
    (8,'Rashard Higgins','WR',2021),
    (3,'Devin Duvernay','WR',2021),
    (24,'Devontae Booker','RB',2021),
    (16,'Demarcus Robinson','WR',2021),
    (23,'Adam Trautman','TE',2021),
    (24,'Saquon Barkley','RB',2021),
    (2,'Mike Davis','RB',2021),
    (24,'Kyle Rudolph','TE',2021),
    (26,'Kenneth Gainwell','RB',2021),
    (23,'Lil Jordan Humphrey','WR',2021),
    (32,'John Bates','TE',2021),
    (30,'Cameron Brate','TE',2021),
    (12,'Josiah Deguara','TE',2021),
    (15,'James Shaughnessy','TE',2021),
    (20,'Myles Gaskin','RB',2021),
    (8,'Harrison Bryant','TE',2021),
    (29,'Will Dissly','TE',2021),
    (2,'Tajae Sharpe','WR',2021),
    (4,'Devin Singletary','RB',2021),
    (21,'Alexander Mattison','RB',2021),
    (13,'Chris Moore','WR',2021),
    (13,'David Johnson','RB',2021),
    (24,'John Ross','WR',2021),
    (21,'Dalvin Cook','RB',2021),
    (20,'Mack Hollins','WR',2021),
    (2,'Hayden Hurst','TE',2021),
    (12,'Marcedes Lewis','TE',2021),
    (13,'Jordan Akins','TE',2021),
    (15,'Tavon Austin','WR',2021),
    (10,'Melvin Gordon III','RB',2021),
    (30,'Cyril Grayson Jr.','WR',2021),
    (32,'Cam Sims','WR',2021),
    (31,'Geoff Swaim','TE',2021),
    (1,'Antoine Wesley','WR',2021),
    (3,'James Proche II','WR',2021),
    (4,'Zack Moss','RB',2021),
    (7,'Samaje Perine','RB',2021),
    (3,'Devonta Freeman','RB',2021),
    (5,'Ian Thomas','TE',2021),
    (9,'Noah Brown','WR',2021),
    (22,'Keal Harry','WR',2021),
    (8,'Demetric Felton','RB',2021),
    (5,'Tommy Tremble','TE',2021),
    (18,'Justin Jackson','RB',2021),
    (4,'Isaiah McKenzie','WR',2021),
    (13,'Brevin Jordan','TE',2021),
    (8,'Kareem Hunt','RB',2021),
    (8,'Nick Chubb','RB',2021),
    (5,'Chuba Hubbard','RB',2021),
    (25,'Tyler Kroft','TE',2021),
    (14,'Ashton Dulin','WR',2021),
    (13,'Pharaoh Brown','TE',2021),
    (6,'Jimmy Graham','TE',2021),
    (30,'Breshad Perriman','WR',2021),
    (27,'Zach Gentry','TE',2021),
    (18,'Stephen Anderson','TE',2021),
    (32,'Dyami Brown','WR',2021),
    (23,'Mark Ingram II','RB',2021),
    (14,'Parris Campbell','WR',2021),
    (20,'Isaiah Ford','WR',2021),
    (29,'Travis Homer','RB',2021),
    (23,'Juwan Johnson','TE',2021),
    (26,'Miles Sanders','RB',2021),
    (11,'Jamaal Williams','RB',2021),
    (11,'KhaDarel Hodge','WR',2021),
    (28,'JaMycal Hasty','RB',2021),
    (7,'Chris Evans','RB',2021),
    (9,'Malik Turner','WR',2021),
    (8,'Ernest Johnson','RB',2021),
    (28,'Elijah Mitchell','RB',2021),
    (30,'O.J. Howard','TE',2021),
    (8,'Anthony Schwartz','WR',2021),
    (23,'Nick Vannett','TE',2021),
    (25,'Denzel Mims','WR',2021),
    (19,'Ben Skowronek','WR',2021),
    (29,'DeeJay Dallas','RB',2021),
    (22,'Damien Harris','RB',2021),
    (16,'Clyde Edwards-Helaire','RB',2021),
    (19,'Sony Michel','RB',2021),
    (21,'C.J. Ham','FB',2021),
    (31,'Onta Foreman','RB',2021),
    (22,'Rhamondre Stevenson','RB',2021),
    (11,'Brock Wright','TE',2021),
    (20,'Salvon Ahmed','RB',2021),
    (21,'Ihmir Smith-Marsette','WR',2021),
    (15,'Dare Ogunbowale','RB',2021),
    (25,'Jeff Smith','WR',2021),
    (20,'Adam Shaheen','TE',2021),
    (16,'Jerick McKinnon','RB',2021),
    (14,'Kylen Granson','TE',2021),
    (16,'Derrick Gore','RB',2021),
    (24,'Collin Johnson','WR',2021),
    (6,'Damien Williams','RB',2021),
    (11,'Trinity Benson','WR',2021),
    (12,'Equanimeous St. Brown','WR',2021),
    (9,'Blake Jarwin','TE',2021),
    (6,'Khalil Herbert','RB',2021),
    (23,'Ty Montgomery II','WR',2021),
    (16,'Blake Bell','TE',2021),
    (28,'Trent Sherfield Sr.','WR',2021),
    (31,'Dontrell Hilliard','RB',2021),
    (3,'Ty Son Williams','RB',2021),
    (26,'Boston Scott','RB',2021),
    (32,'Dax Milne','WR',2021),
    (7,'Drew Sample','TE',2021),
    (5,'Royce Freeman','RB',2021),
    (3,'Latavius Murray','RB',2021),
    (32,'Jaret Patterson','RB',2021),
    (17,'Jalen Richard','RB',2021),
    (4,'Matt Breida','RB',2021),
    (15,'Chris Manhertz','TE',2021),
    (20,'Preston Williams','WR',2021),
    (23,'Kenny Stills','WR',2021),
    (21,'Dede Westbrook','WR',2021),
    (17,'Peyton Barber','RB',2021),
    (3,'Josh Oliver','TE',2021),
    (2,'Lee Smith','TE',2021),
    (30,'Ronald Jones','RB',2021),
    (8,'Ja Marcus Bradley','WR',2021),
    (29,'Dee Eskridge','WR',2021),
    (6,'Jesse James','TE',2021),
    (11,'Godwin Igwebuike','RB',2021),
    (29,'Penny Hart','WR',2021),
    (12,'Juwann Winfree','WR',2021),
    (2,'Keith Smith','FB',2021),
    (15,'Luke Farrell','TE',2021),
    (18,'Jason Moore','WR',2021),
    (5,'Alex Erickson','WR',2021),
    (15,'Jacob Hollister','TE',2021),
    (7,'Mike Thomas','WR',2021),
    (28,'Charlie Woerner','TE',2021),
    (11,'Craig Reynolds','RB',2021),
    (28,'Ross Dwelley','TE',2021),
    (25,'Tevin Coleman','RB',2021),
    (31,'Dez Fitzpatrick','WR',2021),
    (29,'Rashaad Penny','RB',2021),
    (10,'Eric Saubert','TE',2021),
    (13,'Antony Auclair','TE',2021),
    (20,'Phillip Lindsay','RB',2021),
    (12,'Amari Rodgers','WR',2021),
    (18,'Tre McKitty','TE',2021),
    (4,'Tommy Sweeney','TE',2021),
    (22,'Jakob Johnson','FB',2021),
    (2,'Parker Hesse','TE',2021),
    (30,'Jaelon Darden','WR',2021),
    (1,'Eno Benjamin','RB',2021),
    (20,'Duke Johnson','RB',2021),
    (21,'Chris Herndon','TE',2021),
    (7,'Auden Tate','WR',2021),
    (23,'Kevin White','WR',2021),
    (18,'Joshua Kelley','RB',2021),
    (30,'Scotty Miller','WR',2021),
    (19,'Kendall Blanton','TE',2021),
    (25,'Kenny Yeboah','TE',2021),
    (16,'Noah Gray','TE',2021),
    (25,'D.J. Montgomery','WR',2021),
    (18,'Andre Roberts','WR',2021),
    (12,'Tyler Davis','TE',2021),
    (7,'Trenton Irwin','WR',2021),
    (12,'Dominique Dafney','TE',2021),
    (1,'Jonathan Ward','RB',2021),
    (10,'Seth Williams','WR',2021),
    (11,'Shane Zylstra','TE',2021),
    (31,'Cody Hollister','WR',2021),
    (27,'Cody White','WR',2021),
    (29,'Colby Parkinson','TE',2021),
    (16,'Josh Gordon','WR',2021),
    (16,'Michael Burton','FB',2021),
    (9,'Jeremy Sprinkle','TE',2021),
    (28,'Jeff Wilson Jr.','RB',2021),
    (22,'Gunner Olszewski','WR',2021),
    (30,'Le Veon Bell','RB',2021),
    (24,'Elijhaa Penny','RB',2021),
    (9,'Corey Clement','RB',2021),
    (23,'Tony Jones Jr.','RB',2021),
    (32,'Jonathan Williams','RB',2021),
    (4,'Jake Kumerow','WR',2021),
    (32,'Curtis Samuel','WR',2021),
    (9,'Sean McKeon','TE',2021),
    (30,'Ke Shawn Vaughn','RB',2021),
    (28,'Trey Sermon','RB',2021),
    (14,'Mike Strachan','WR',2021),
    (2,'Christian Blake','WR',2021),
    (16,'Marcus Kemp','WR',2021),
    (4,'Reggie Gilliam','FB',2021),
    (6,'Dazz Newsome','WR',2021),
    (3,'Tylan Wallace','WR',2021),
    (11,'Jermar Jefferson','RB',2021),
    (10,'Mike Boone','RB',2021),
    (26,'Jack Stoll','TE',2021),
    (21,'Wayne Gallman','RB',2021),
    (21,'Garrett Bradbury','C',2021),
    (14,'Dezmon Patmon','WR',2021),
    (25,'Nick Bawden','FB',2021),
    (26,'Jordan Howard','RB',2021),
    (24,'David Sills V','WR',2021),
    (11,'Bobby Price','CB',2021),
    (18,'Gabe Nabers','FB',2021),
    (20,'Cethan Carter','TE',2021),
    (11,'Jason Cabinda','FB',2021),
    (15,'Tyron Billy-Johnson','WR',2021),
    (7,'Mitchell Wilcox','TE',2021),
    (15,'Ryquell Armstead','RB',2021),
    (23,'Adam Prentice','FB',2021),
    (27,'Derek Watt','FB',2021),
    (1,'Greg Dortch','WR',2021),
    (2,'Frank Darby','WR',2021),
    (17,'Derek Carrier','TE',2021),
    (1,'Andy Isabella','WR',2021),
    (27,'Benny Snell Jr.','RB',2021),
    (21,'Luke Stocker','TE',2021),
    (23,'Dwayne Washington','RB',2021),
    (5,'Reggie Bonnafon','RB',2021),
    (2,'Qadree Ollison','RB',2021),
    (7,'Stanley Morgan Jr.','WR',2021),
    (5,'C.J. Saunders','WR',2021),
    (27,'Anthony McFarland Jr.','RB',2021),
    (1,'Demetrius Harris','TE',2021),
    (15,'Jaydon Mickens','WR',2021),
    (19,'Cam Akers','RB',2021),
    (25,'Tarik Black','WR',2021),
    (8,'Andy Janovich','FB',2021),
    (25,'Austin Walter','RB',2021),
    (19,'Brycen Hopkins','TE',2021),
    (21,'Kene Nwangwu','RB',2021),
    (27,'Kevin Rader','TE',2021),
    (23,'Ethan Wolf','TE',2021),
    (27,'Kalen Ballage','RB',2021),
    (14,'Marlon Mack','RB',2021),
    (22,'J.J. Taylor','RB',2021),
    (20,'Hunter Long','TE',2021),
    (31,'Racey McMath','WR',2021),
    (3,'Eric Tomlinson','TE',2021),
    (8,'Johnny Stanton IV','FB',2021),
    (3,'Miles Boykin','WR',2021),
    (31,'Amani Hooker','S',2021),
    (26,'Lane Johnson','OT',2021),
    (14,'Keke Coutee','WR',2021),
    (23,'Easop Winston Jr.','WR',2021),
    (29,'Nick Bellore','LB',2021),
    (11,'Taylor Decker','OT',2021),
    (31,'Khari Blasingame','FB',2021),
    (6,'Ryan Nall','FB',2021),
    (7,'Trayveon Williams','RB',2021),
    (12,'Patrick Taylor Jr.','RB',2021),
    (14,'Danny Pinter','C',2021),
    (24,'Andrew Thomas','OT',2021),
    (25,'Conor McDermott','OT',2021),
    (20,'Christian Wilkins','DT',2021),
    (9,'Terence Steele','OT',2021),
    (23,'Alex Armah','RB',2021),
    (28,'Trent Williams','OT',2021),
    (28,'Travis Benjamin','WR',2021),
    (5,'Colin Thompson','TE',2021),
    (4,'Dion Dawkins','OT',2021),
    (1,'Darrell Daniels','TE',2021),
    (24,'Keion Crossen','CB',2021),
    (11,'Matt Nelson','OT',2021),
    (5,'Giovanni Ricci','FB',2021),
    (21,'Ben Ellefson','TE',2021),
    (10,'Tyrie Cleveland','WR',2021),
    (5,'Stephen Sullivan','TE',2021),
    (26,'Jason Huntley','RB',2021),
    (31,'Tory Carter','FB',2021),
    (6,'Isaiah Coulter','WR',2021),
    (31,'Mekhi Sargent','RB',2021),
    (18,'Tevaughn Campbell','CB',2021),
    (18,'Larry Rountree III','RB',2021),
    (16,'Mike Remmers','OT',2021),
    (10,'Diontae Spencer','WR',2021),
    (25,'La Mical Perine','RB',2021),
    (14,'Deon Jackson','RB',2021),
    (11,'C.J. Moore','S',2021),
    (5,'Sean Chandler','S',2021),
    (19,'Buddy Howell','RB',2021),
    (14,'Sam Ehlinger','QB',2021),
    (13,'Tremon Smith','CB',2021),
    (17,'Dallin Leavitt','S',2021),
    (19,'Jake Funk','RB',2021),
    (15,'Andrew Wingard','S',2021),
    (25,'Braden Mann','P',2021),
    (15,'Nathan Cottrell','RB',2021),
    (18,'Maurice Ffrench','WR',2021),
    (20,'Michael Palardy','P',2021),
    (1,'Andy Lee','P',2021),
    (20,'Clayton Fejedelem','S',2021),
    (18,'Chase Daniel','QB',2021),
    (24,'Alex Bachman','WR',2021),
    (31,'Logan Woodside','QB',2021),
    (16,'Patrick Mahomes','QB',2022),
    (18,'Justin Herbert','QB',2022),
    (30,'Tom Brady','QB',2022),
    (21,'Kirk Cousins','QB',2022),
    (7,'Joe Burrow','QB',2022),
    (11,'Jared Goff','QB',2022),
    (4,'Josh Allen','QB',2022),
    (29,'Geno Smith','QB',2022),
    (15,'Trevor Lawrence','QB',2022),
    (26,'Jalen Hurts','QB',2022),
    (12,'Aaron Rodgers','QB',2022),
    (20,'Tua Tagovailoa','QB',2022),
    (10,'Russell Wilson','QB',2022),
    (17,'Derek Carr','QB',2022),
    (24,'Daniel Jones','QB',2022),
    (13,'Davis Mills','QB',2022),
    (14,'Matt Ryan','QB',2022),
    (22,'Mac Jones','QB',2022),
    (23,'Andy Dalton','QB',2022),
    (9,'Dak Prescott','QB',2022),
    (8,'Jacoby Brissett','QB',2022),
    (31,'Ryan Tannehill','QB',2022),
    (28,'Jimmy Garoppolo','QB',2022),
    (27,'Kenny Pickett','QB',2022),
    (1,'Kyler Murray','QB',2022),
    (3,'Lamar Jackson','QB',2022),
    (6,'Justin Fields','QB',2022),
    (2,'Marcus Mariota','QB',2022),
    (5,'Baker Mayfield','QB',2022),
    (19,'Matthew Stafford','QB',2022),
    (32,'Taylor Heinicke','QB',2022),
    (32,'Carson Wentz','QB',2022),
    (25,'Zach Wilson','QB',2022),
    (28,'Brock Purdy','QB',2022),
    (27,'Mitchell Trubisky','QB',2022),
    (25,'Mike White','QB',2022),
    (5,'Sam Darnold','QB',2022),
    (8,'Deshaun Watson','QB',2022),
    (25,'Joe Flacco','QB',2022),
    (9,'Cooper Rush','QB',2022),
    (23,'Jameis Winston','QB',2022),
    (22,'Bailey Zappe','QB',2022),
    (1,'Colt McCoy','QB',2022),
    (5,'PJ Walker','QB',2022),
    (2,'Desmond Ridder','QB',2022),
    (20,'Teddy Bridgewater','QB',2022),
    (26,'Gardner Minshew','QB',2022),
    (3,'Tyler Huntley','QB',2022),
    (17,'Jarrett Stidham','QB',2022),
    (14,'Sam Ehlinger','QB',2022),
    (20,'Skylar Thompson','QB',2022),
    (10,'Brett Rypien','QB',2022),
    (13,'Kyle Allen','QB',2022),
    (1,'Trace McSorley','QB',2022),
    (31,'Joshua Dobbs','QB',2022),
    (1,'David Blough','QB',2022),
    (19,'John Wolford','QB',2022),
    (3,'Anthony Brown Jr.','QB',2022),
    (31,'Malik Willis','QB',2022),
    (23,'Taysom Hill','QB',2022),
    (14,'Nick Foles','QB',2022),
    (21,'Nick Mullens','QB',2022),
    (12,'Jordan Love','QB',2022),
    (28,'Trey Lance','QB',2022),
    (6,'Trevor Siemian','QB',2022),
    (32,'Sam Howell','QB',2022),
    (24,'Davis Webb','QB',2022),
    (19,'Bryce Perkins','QB',2022),
    (6,'Nathan Peterman','QB',2022),
    (13,'Jeff Driskel','QB',2022),
    (25,'Chris Streveler','QB',2022),
    (5,'Jacob Eason','QB',2022),
    (24,'Tyrod Taylor','QB',2022),
    (18,'Chase Daniel','QB',2022),
    (22,'Brian Hoyer','QB',2022),
    (15,'C.J. Beathard','QB',2022),
    (5,'Christian McCaffrey','RB',2022),
    (21,'Justin Jefferson','WR',2022),
    (6,'Tim Boyle','QB',2022),
    (30,'Blaine Gabbert','QB',2022),
    (7,'Tyler Boyd','WR',2022),
    (30,'Kyle Trask','QB',2022),
    (7,'Brandon Allen','QB',2022),
    (19,'Riley Dixon','P',2022),
    (25,'Braden Mann','P',2022),
    (21,'Ryan Wright','P',2022),
    (28,'Josh Johnson','QB',2022),
    (4,'Case Keenum','QB',2022),
    (11,'Jack Fox','P',2022),
    (1,'Andy Lee','P',2022),
    (17,'Mack Hollins','WR',2022),
    (31,'Derrick Henry','RB',2022),
    (27,'Najee Harris','RB',2022),
    (25,'Braxton Berrios','WR',2022),
    (6,'Chase Claypool','WR',2022),
    (16,'Chad Henne','QB',2022),
    (13,'Rex Burkhead','RB',2022),
    (17,'Davante Adams','WR',2022),
    (13,'Phillip Dorsett','WR',2022),
    (8,'Amari Cooper','WR',2022),
    (19,'Cooper Kupp','WR',2022),
    (11,'Nate Sudfeld','QB',2022),
    (30,'Leonard Fournette','RB',2022),
    (21,'Dalvin Cook','RB',2022),
    (15,'Christian Kirk','WR',2022),
    (16,'Tommy Townsend','P',2022),
    (3,'James Proche II','WR',2022),
    (25,'Lawrence Cager','TE',2022),
    (24,'Jamie Gillan','P',2022),
    (20,'Cedrick Wilson Jr.','WR',2022),
    (29,'DeeJay Dallas','RB',2022),
    (7,'Ja Marr Chase','WR',2022),
    (25,'Garrett Wilson','WR',2022),
    (20,'Tyreek Hill','WR',2022),
    (26,'A.J. Brown','WR',2022),
    (4,'Stefon Diggs','WR',2022),
    (9,'CeeDee Lamb','WR',2022),
    (20,'Jaylen Waddle','WR',2022),
    (16,'Travis Kelce','TE',2022),
    (26,'DeVonta Smith','WR',2022),
    (32,'Terry McLaurin','WR',2022),
    (11,'Amon-Ra St. Brown','WR',2022),
    (30,'Mike Evans','WR',2022),
    (29,'DK Metcalf','WR',2022),
    (23,'Chris Olave','WR',2022),
    (29,'Tyler Lockett','WR',2022),
    (7,'Tee Higgins','WR',2022),
    (30,'Chris Godwin','WR',2022),
    (28,'Brandon Aiyuk','WR',2022),
    (10,'Jerry Jeudy','WR',2022),
    (16,'JuJu Smith-Schuster','WR',2022),
    (14,'Michael Pittman Jr.','WR',2022),
    (11,'T.J. Hockenson','TE',2022),
    (18,'Mike Williams','WR',2022),
    (5,'DJ Moore','WR',2022),
    (27,'Diontae Johnson','WR',2022),
    (2,'Drake London','WR',2022),
    (3,'Mark Andrews','TE',2022),
    (8,'Donovan Peoples-Jones','WR',2022),
    (4,'Gabe Davis','WR',2022),
    (10,'Courtland Sutton','WR',2022),
    (15,'Zay Jones','WR',2022),
    (22,'Jakobi Meyers','WR',2022),
    (27,'George Pickens','WR',2022),
    (12,'Allen Lazard','WR',2022),
    (18,'Joshua Palmer','WR',2022),
    (15,'Evan Engram','TE',2022),
    (28,'George Kittle','TE',2022),
    (18,'Keenan Allen','WR',2022),
    (27,'Pat Freiermuth','TE',2022),
    (24,'Darius Slayton','WR',2022),
    (18,'Austin Ekeler','RB',2022),
    (1,'DeAndre Hopkins','WR',2022),
    (21,'Adam Thielen','WR',2022),
    (1,'Marquise Brown','WR',2022),
    (26,'Dallas Goedert','TE',2022),
    (13,'Brandin Cooks','WR',2022),
    (16,'Marquez Valdes-Scantling','WR',2022),
    (32,'Curtis Samuel','WR',2022),
    (21,'K.J. Osborn','WR',2022),
    (28,'Deebo Samuel','WR',2022),
    (8,'David Njoku','TE',2022),
    (14,'Parris Campbell','WR',2022),
    (19,'Tyler Higbee','TE',2022),
    (11,'Kalif Raymond','WR',2022),
    (12,'Christian Watson','WR',2022),
    (14,'Alec Pierce','WR',2022),
    (9,'Dalton Schultz','TE',2022),
    (24,'Richie James','WR',2022),
    (9,'Noah Brown','WR',2022),
    (18,'Gerald Everett','TE',2022),
    (25,'Tyler Conklin','TE',2022),
    (13,'Chris Moore','WR',2022),
    (6,'Cole Kmet','TE',2022),
    (22,'DeVante Parker','WR',2022),
    (18,'DeAndre Carter','WR',2022),
    (25,'Corey Davis','WR',2022),
    (2,'Olamide Zaccheaus','WR',2022),
    (15,'Marvin Jones Jr.','WR',2022),
    (31,'Robert Woods','WR',2022),
    (32,'Jahan Dotson','WR',2022),
    (4,'Dawson Knox','TE',2022),
    (16,'Jerick McKinnon','RB',2022),
    (22,'Hunter Henry','TE',2022),
    (23,'Juwan Johnson','TE',2022),
    (11,'DJ Chark Jr.','WR',2022),
    (13,'Jordan Akins','TE',2022),
    (6,'Darnell Mooney','WR',2022),
    (23,'Alvin Kamara','RB',2022),
    (5,'Terrace Marshall Jr.','WR',2022),
    (23,'Rashid Shaheed','WR',2022),
    (29,'Noah Fant','TE',2022),
    (13,'Nico Collins','WR',2022),
    (11,'Josh Reynolds','WR',2022),
    (12,'Robert Tonyan','TE',2022),
    (1,'Greg Dortch','WR',2022),
    (3,'Demarcus Robinson','WR',2022),
    (31,'Chigoziem Okonkwo','TE',2022),
    (25,'Elijah Moore','WR',2022),
    (31,'Austin Hooper','TE',2022),
    (31,'Treylon Burks','WR',2022),
    (7,'Joe Mixon','RB',2022),
    (22,'Kendrick Bourne','WR',2022),
    (30,'Russell Gage','WR',2022),
    (12,'Romeo Doubs','WR',2022),
    (9,'Michael Gallup','WR',2022),
    (4,'Isaiah McKenzie','WR',2022),
    (22,'Rhamondre Stevenson','RB',2022),
    (17,'Foster Moreau','TE',2022),
    (12,'Randall Cobb','WR',2022),
    (20,'Trent Sherfield Sr.','WR',2022),
    (28,'Jauan Jennings','WR',2022),
    (7,'Hayden Hurst','TE',2022),
    (1,'Rondale Moore','WR',2022),
    (10,'Greg Dulcich','TE',2022),
    (3,'Devin Duvernay','WR',2022),
    (1,'Zach Ertz','TE',2022),
    (17,'Josh Jacobs','RB',2022),
    (31,'Nick Westbrook-Ikhine','WR',2022),
    (12,'Aaron Jones','RB',2022),
    (24,'Isaiah Hodgins','WR',2022),
    (30,'Cade Otton','TE',2022),
    (11,'Andre Swift','RB',2022),
    (17,'Darren Waller','TE',2022),
    (29,'Marquise Goodwin','WR',2022),
    (19,'Ben Skowronek','WR',2022),
    (3,'Isaiah Likely','TE',2022),
    (9,'Tony Pollard','RB',2022),
    (19,'Van Jefferson','WR',2022),
    (22,'Nelson Agholor','WR',2022),
    (20,'Mike Gesicki','TE',2022),
    (2,'Kyle Pitts','TE',2022),
    (26,'Quez Watkins','WR',2022),
    (32,'Antonio Gibson','RB',2022),
    (29,'Will Dissly','TE',2022),
    (19,'Allen Robinson II','WR',2022),
    (24,'Saquon Barkley','RB',2022),
    (17,'Hunter Renfrow','WR',2022),
    (12,'Sammy Watkins','WR',2022),
    (32,'Logan Thomas','TE',2022),
    (6,'Equanimeous St. Brown','WR',2022),
    (29,'Colby Parkinson','TE',2022),
    (6,'David Montgomery','RB',2022),
    (15,'Travis Etienne Jr.','RB',2022),
    (16,'Justin Watson','WR',2022),
    (14,'Jelani Woods','TE',2022),
    (10,'Kendall Hinton','WR',2022),
    (14,'Kylen Granson','TE',2022),
    (1,'James Conner','RB',2022),
    (30,'Julio Jones','WR',2022),
    (16,'Noah Gray','TE',2022),
    (19,'Tutu Atwell','WR',2022),
    (16,'Mecole Hardman','WR',2022),
    (5,'Shi Smith','WR',2022),
    (30,'Rachaad White','RB',2022),
    (25,'Michael Carter','RB',2022),
    (7,'Samaje Perine','RB',2022),
    (3,'Rashod Bateman','WR',2022),
    (5,'Robbie Chosen','WR',2022),
    (4,'Devin Singletary','RB',2022),
    (23,'Tre Quan Smith','WR',2022),
    (23,'Jarvis Landry','WR',2022),
    (5,'Laviska Shenault Jr.','WR',2022),
    (2,'Damiere Byrd','WR',2022),
    (24,'Daniel Bellinger','TE',2022),
    (1,'Trey McBride','TE',2022),
    (16,'Skyy Moore','WR',2022),
    (22,'Tyquan Thornton','WR',2022),
    (22,'Jonnu Smith','TE',2022),
    (6,'Dante Pettis','WR',2022),
    (28,'Ray-Ray McCloud III','WR',2022),
    (4,'Nyheim Hines','RB',2022),
    (8,'Nick Chubb','RB',2022),
    (8,'Harrison Bryant','TE',2022),
    (1,'A.J. Green','WR',2022),
    (25,'C.J. Uzomah','TE',2022),
    (7,'Trenton Irwin','WR',2022),
    (24,'Wan Dale Robinson','WR',2022),
    (10,'Melvin Gordon III','RB',2022),
    (25,'Breece Hall','RB',2022),
    (11,'Brock Wright','TE',2022),
    (27,'Jaylen Warren','RB',2022),
    (8,'David Bell','WR',2022),
    (17,'Ameer Abdullah','RB',2022),
    (8,'Kareem Hunt','RB',2022),
    (14,'Deon Jackson','RB',2022),
    (23,'Adam Trautman','TE',2022),
    (14,'Ashton Dulin','WR',2022),
    (12,'AJ Dillon','RB',2022),
    (12,'Amari Rodgers','WR',2022),
    (20,'Raheem Mostert','RB',2022),
    (2,'KhaDarel Hodge','WR',2022),
    (28,'Kyle Juszczyk','FB',2022),
    (5,'Ian Thomas','TE',2022),
    (23,'Eno Benjamin','RB',2022),
    (14,'Mo Alie-Cox','TE',2022),
    (15,'Jamal Agnew','WR',2022),
    (25,'Denzel Mims','WR',2022),
    (20,'Jeff Wilson Jr.','RB',2022),
    (30,'Scotty Miller','WR',2022),
    (21,'Irv Smith Jr.','TE',2022),
    (4,'James Cook','RB',2022),
    (21,'Jalen Nailor','WR',2022),
    (31,'Dontrell Hilliard','RB',2022),
    (30,'Cameron Brate','TE',2022),
    (9,'Jake Ferguson','TE',2022),
    (5,'Tommy Tremble','TE',2022),
    (32,'J.D. McKissic','RB',2022),
    (23,'Michael Thomas','WR',2022),
    (24,'Kadarius Toney','WR',2022),
    (5,'Chuba Hubbard','RB',2022),
    (26,'Kenneth Gainwell','RB',2022),
    (10,'KJ Hamler','WR',2022),
    (13,'Dameon Pierce','RB',2022),
    (29,'Kenneth Walker III','RB',2022),
    (4,'Khalil Shakir','WR',2022),
    (23,'Marquez Callaway','WR',2022),
    (10,'Chase Edmonds','RB',2022),
    (29,'Travis Homer','RB',2022),
    (19,'Brandon Powell','WR',2022),
    (24,'Sterling Shepard','WR',2022),
    (3,'DeSean Jackson','WR',2022),
    (27,'Connor Heyward','TE',2022),
    (16,'Clyde Edwards-Helaire','RB',2022),
    (2,'MyCole Pruitt','TE',2022),
    (26,'Zach Pascal','WR',2022),
    (3,'Josh Oliver','TE',2022),
    (10,'Eric Saubert','TE',2022),
    (13,'O.J. Howard','TE',2022),
    (14,'Jonathan Taylor','RB',2022),
    (32,'Dyami Brown','WR',2022),
    (17,'Keelan Cole Sr.','WR',2022),
    (11,'Tom Kennedy','WR',2022),
    (21,'Johnny Mundt','TE',2022),
    (7,'Mitchell Wilcox','TE',2022),
    (2,'Tyler Allgeier','RB',2022),
    (20,'Cedrick Wilson Jr.','WR',2022),
    (6,'Byron Pringle','WR',2022),
    (15,'Dan Arnold','TE',2022),
    (25,'Jeff Smith','WR',2022),
    (10,'Latavius Murray','RB',2022),
    (24,'Tanner Hudson','TE',2022),
    (27,'Zach Gentry','TE',2022),
    (18,'Donald Parham Jr.','TE',2022),
    (16,'Isiah Pacheco','RB',2022),
    (20,'Durham Smythe','TE',2022),
    (13,'Brevin Jordan','TE',2022),
    (15,'JaMycal Hasty','RB',2022),
    (26,'Jack Stoll','TE',2022),
    (2,'Cordarrelle Patterson','RB',2022),
    (9,'T.Y. Hilton','WR',2022),
    (24,'Matt Breida','RB',2022),
    (8,'Pharaoh Brown','TE',2022),
    (19,'Cam Akers','RB',2022),
    (6,'Keal Harry','WR',2022),
    (11,'Craig Reynolds','RB',2022),
    (12,'Josiah Deguara','TE',2022),
    (11,'James Mitchell','TE',2022),
    (13,'Teagan Quitoriano','TE',2022),
    (30,'Breshad Perriman','WR',2022),
    (19,'Brycen Hopkins','TE',2022),
    (32,'John Bates','TE',2022),
    (16,'Jody Fortson Jr.','TE',2022),
    (6,'Velus Jones Jr.','WR',2022),
    (24,'David Sills V','WR',2022),
    (28,'Ross Dwelley','TE',2022),
    (20,'Alec Ingold','FB',2022),
    (13,'Dare Ogunbowale','RB',2022),
    (27,'Steven Sims','WR',2022),
    (21,'Jalen Reagor','WR',2022),
    (9,'Peyton Hendershot','TE',2022),
    (20,'River Cracraft','WR',2022),
    (19,'Darrell Henderson Jr.','RB',2022),
    (11,'Justin Jackson','RB',2022),
    (18,'Joshua Kelley','RB',2022),
    (2,'Anthony Firkser','TE',2022),
    (5,'Giovanni Ricci','FB',2022),
    (25,'Zonovan Knight','RB',2022),
    (24,'Marcus Johnson','WR',2022),
    (10,'Marlon Mack','RB',2022),
    (22,'Damien Harris','RB',2022),
    (10,'Mike Boone','RB',2022),
    (10,'Albert Okwuegbunam Jr.','TE',2022),
    (5,'Raheem Blackshear','RB',2022),
    (9,'Ezekiel Elliott','RB',2022),
    (21,'Alexander Mattison','RB',2022),
    (3,'Kenyan Drake','RB',2022),
    (32,'Cam Sims','WR',2022),
    (2,'Parker Hesse','TE',2022),
    (18,'Michael Bandy','WR',2022),
    (25,'Ty Johnson','RB',2022),
    (21,'C.J. Ham','FB',2022),
    (4,'Quintin Morris','TE',2022),
    (12,'Samori Toure','WR',2022),
    (24,'Kenny Golladay','WR',2022),
    (26,'Grant Calcaterra','TE',2022),
    (30,'Ko Kieft','TE',2022),
    (10,'Eric Tomlinson','TE',2022),
    (26,'Miles Sanders','RB',2022),
    (22,'Marcus Jones','CB',2022),
    (31,'Kyle Philips','WR',2022),
    (10,'Javonte Williams','RB',2022),
    (19,'Kyren Williams','RB',2022),
    (10,'Jalen Virgil','WR',2022),
    (3,'Patrick Ricard','FB',2022),
    (23,'Kevin White','WR',2022),
    (10,'Freddie Swain','WR',2022),
    (11,'Jamaal Williams','RB',2022),
    (18,'Tre McKitty','TE',2022),
    (10,'Andrew Beck','FB',2022),
    (4,'Reggie Gilliam','FB',2022),
    (23,'Mark Ingram II','RB',2022),
    (12,'Marcedes Lewis','TE',2022),
    (24,'Chris Myarick','TE',2022),
    (4,'Jake Kumerow','WR',2022),
    (18,'Jalen Guyton','WR',2022),
    (32,'Armani Rogers','TE',2022),
    (9,'Malik Davis','RB',2022),
    (7,'Trent Taylor','WR',2022),
    (3,'James Proche II','WR',2022),
    (2,'Avery Williams','RB',2022),
    (4,'Jamison Crowder','WR',2022),
    (32,'Brian Robinson Jr.','RB',2022),
    (11,'Shane Zylstra','TE',2022),
    (14,'Mike Strachan','WR',2022),
    (31,'Geoff Swaim','TE',2022),
    (3,'Justice Hill','RB',2022),
    (29,'Dee Eskridge','WR',2022),
    (17,'Brandon Bolden','RB',2022),
    (28,'Tyler Kroft','TE',2022),
    (6,'Khalil Herbert','RB',2022),
    (31,'Hassan Haskins','RB',2022),
    (24,'Nick Vannett','TE',2022),
    (1,'Corey Clement','RB',2022),
    (31,'Cody Hollister','WR',2022),
    (18,'Sony Michel','RB',2022),
    (27,'Gunner Olszewski','WR',2022),
    (25,'James Robinson','RB',2022),
    (8,'Anthony Schwartz','WR',2022),
    (3,'Charlie Kolar','TE',2022),
    (23,'David Johnson','RB',2022),
    (31,'Chris Conley','WR',2022),
    (5,'Stephen Sullivan','TE',2022),
    (1,'Andre Baccellia','WR',2022),
    (8,'Michael Woods II','WR',2022),
    (28,'Tevin Coleman','RB',2022),
    (4,'John Brown','WR',2022),
    (15,'Chris Manhertz','TE',2022),
    (29,'Laquon Treadwell','WR',2022),
    (10,'Brandon Johnson','WR',2022),
    (3,'J.K. Dobbins','RB',2022),
    (22,'Pierre Strong Jr.','RB',2022),
    (31,'Julius Chestnut','RB',2022),
    (11,'Jameson Williams','WR',2022),
    (32,'Jonathan Williams','RB',2022),
    (15,'Luke Farrell','TE',2022),
    (31,'Racey McMath','WR',2022),
    (4,'Zack Moss','RB',2022),
    (24,'Gary Brightwell','RB',2022),
    (7,'Mike Thomas','WR',2022),
    (7,'Chris Evans','RB',2022),
    (19,'Malcolm Brown','RB',2022),
    (32,'Dax Milne','WR',2022),
    (30,'Cole Beasley','WR',2022),
    (19,'Kendall Blanton','TE',2022),
    (13,'Royce Freeman','RB',2022),
    (6,'Darrynton Evans','RB',2022),
    (3,'Tylan Wallace','WR',2022),
    (30,'Deven Thompkins','WR',2022),
    (7,'Trayveon Williams','RB',2022),
    (23,'Tony Jones Jr.','RB',2022),
    (15,'Tim Jones','WR',2022),
    (14,'Jordan Wilkins','RB',2022),
    (19,'Ronnie Rivers','RB',2022),
    (30,'Kyle Rudolph','TE',2022),
    (20,'Myles Gaskin','RB',2022),
    (10,'Tyrie Cleveland','WR',2022),
    (6,'Ryan Griffin','TE',2022),
    (5,'Onta Foreman','RB',2022),
    (12,'Tyler Davis','TE',2022),
    (21,'Ben Ellefson','TE',2022),
    (6,'Trevon Wesco','TE',2022),
    (8,'Jaelon Darden','WR',2022),
    (8,'Daylen Baldwin','WR',2022),
    (14,'Dezmon Patmon','WR',2022),
    (9,'Simi Fehoko','WR',2022),
    (10,'Tyler Badie','RB',2022),
    (29,'Dareke Young','WR',2022),
    (32,'Cole Turner','TE',2022),
    (16,'Ronald Jones','RB',2022),
    (3,'Andy Isabella','WR',2022),
    (29,'Cade Johnson','WR',2022),
    (21,'Kene Nwangwu','RB',2022),
    (1,'Keaontay Ingram','RB',2022),
    (16,'Blake Bell','TE',2022),
    (14,'Keke Coutee','WR',2022),
    (29,'Penny Hart','WR',2022),
    (22,'Lil Jordan Humphrey','WR',2022),
    (14,'Phillip Lindsay','RB',2022),
    (30,'Ke Shawn Vaughn','RB',2022),
    (17,'Jesper Horsted','TE',2022),
    (13,'Troy Hairston','FB',2022),
    (1,'Maxx Williams','TE',2022),
    (23,'Keith Kirkwood','WR',2022),
    (12,'Juwann Winfree','WR',2022),
    (27,'Benny Snell Jr.','RB',2022),
    (12,'Patrick Taylor Jr.','RB',2022),
    (18,'Stone Smartt','TE',2022),
    (20,'Braylon Sanders','WR',2022),
    (29,'Rashaad Penny','RB',2022),
    (9,'Dennis Houston','WR',2022),
    (22,'Ty Montgomery II','WR',2022),
    (26,'Boston Scott','RB',2022),
    (11,'Quintez Cephus','WR',2022),
    (2,'Bryan Edwards','WR',2022),
    (2,'Frank Darby','WR',2022),
    (6,'Ihmir Smith-Marsette','WR',2022),
    (6,'Nsimba Webster','WR',2022),
    (18,'Larry Rountree III','RB',2022),
    (19,'Austin Trammell','WR',2022),
    (23,'Deonte Harty','WR',2022),
    (18,'Isaiah Spiller','RB',2022),
    (19,'Jake Gervase','S',2022),
    (9,'Jalen Tolbert','WR',2022),
    (16,'Michael Burton','FB',2022),
    (27,'Derek Watt','FB',2022),
    (27,'Miles Boykin','WR',2022),
    (9,'Sean McKeon','TE',2022),
    (27,'Anthony McFarland Jr.','RB',2022),
    (17,'Jakob Johnson','FB',2022),
    (5,'Spencer Brown','RB',2022),
    (28,'Danny Gray','WR',2022),
    (1,'Stephen Anderson','TE',2022),
    (1,'Darrel Williams','RB',2022),
    (9,'KaVontae Turpin','WR',2022),
    (23,'Adam Prentice','FB',2022),
    (11,'Penei Sewell','OT',2022),
    (2,'Keith Smith','FB',2022),
    (17,'Tyron Billy-Johnson','WR',2022),
    (8,'Demetric Felton','RB',2022),
    (22,'J.J. Taylor','RB',2022),
    (20,'Salvon Ahmed','RB',2022),
    (6,'Trestan Ebner','RB',2022),
    (18,'Zander Horvath','FB',2022),
    (25,'Jeremy Ruckert','TE',2022),
    (23,'Dwayne Washington','RB',2022),
    (4,'Tommy Sweeney','TE',2022),
    (8,'Ernest Johnson','RB',2022),
    (11,'Maurice Alexander','WR',2022),
    (29,'Tyler Mabry','TE',2022),
    (13,'Jalen Camp','WR',2022),
    (31,'Jonathan Ward','RB',2022),
    (28,'Elijah Mitchell','RB',2022),
    (13,'Mason Schreck','TE',2022),
    (31,'C.J. Board','WR',2022),
    (1,'Pharoh Cooper','WR',2022),
    (19,'Jacob Harris','WR',2022),
    (11,'Jason Cabinda','FB',2022),
    (1,'Ty Son Williams','RB',2022),
    (7,'Devin Asiasi','TE',2022),
    (18,'Jason Moore','WR',2022),
    (18,'Richard Rodgers','TE',2022),
    (3,'Mike Davis','RB',2022),
    (13,'Kamu Grugier-Hill','LB',2022),
    (29,'Godwin Igwebuike','RB',2022),
    (10,'Devine Ozigbo','RB',2022),
    (31,'Mason Kinsey','WR',2022),
    (2,'Caleb Huntley','RB',2022),
    (20,'Erik Ezukanma','WR',2022),
    (27,'Cody White','WR',2022),
    (10,'Montrell Washington','WR',2022),
    (31,'Josh Gordon','WR',2022),
    (12,'David Bakhtiari','OT',2022),
    (8,'Jack Conklin','OT',2022),
    (4,'Tanner Gentry','WR',2022),
    (3,'Gus Edwards','RB',2022),
    (6,'Khari Blasingame','FB',2022),
    (9,'James Washington','WR',2022),
    (7,'Stanley Morgan Jr.','WR',2022),
    (26,'Noah Togiai','TE',2022),
    (2,'Feleipe Franks','TE',2022),
    (28,'Charlie Woerner','TE',2022),
    (17,'DJ Turner','WR',2022),
    (8,'Miller Forristall','TE',2022),
    (20,'Tanner Conner','TE',2022),
    (19,'Lance McCutcheon','WR',2022),
    (6,'Jake Tonges','TE',2022),
    (2,'Josh Ali','WR',2022),
    (32,'Jaret Patterson','RB',2022),
    (28,'Tyrion Davis-Price','RB',2022),
    (30,'Giovani Bernard','RB',2022),
    (7,'Drew Sample','TE',2022),
    (28,'Jordan Mason','RB',2022),
    (28,'Deebo Samuel Sr.','WR',2022),
    (17,'Zamir White','RB',2022),
    (11,'C.J. Moore','S',2022),
    (22,'Kevin Harris','RB',2022),
    (15,'Snoop Conner','RB',2022),
    (21,'Ty Chandler','RB',2022),
    (26,'Trey Sermon','RB',2022),
    (8,'Jerome Ford','RB',2022),
    (32,'Reggie Bonnafon','RB',2022),
    (12,'Kylin Hill','RB',2022),
    (4,'Duke Johnson','RB',2022),
    (27,'Marcus Allen','LB',2022),
    (29,'Nick Bellore','LB',2022),
    (13,'M.J. Stewart','S',2022),
    (2,'Damien Williams','RB',2022),
    (5,'Sean Chandler','S',2022),
    (25,'Ashtyn Davis','S',2022),
    (23,'Jordan Howard','RB',2022),
    (9,'Bryan Anger','P',2022),
    (20,'Clayton Fejedelem','S',2022),
    (12,'Dallin Leavitt','S',2022),
    (17,'Matthias Farley','S',2022),
    (3,'Anthony Brown Jr.','QB',2022),
    (29,'Michael Dickson','P',2022),
    (20,'Tua Tagovailoa','QB',2023),
    (11,'Jared Goff','QB',2023),
    (9,'Dak Prescott','QB',2023),
    (4,'Josh Allen','QB',2023),
    (28,'Brock Purdy','QB',2023),
    (16,'Patrick Mahomes','QB',2023),
    (12,'Jordan Love','QB',2023),
    (13,'C.J. Stroud','QB',2023),
    (30,'Baker Mayfield','QB',2023),
    (15,'Trevor Lawrence','QB',2023),
    (19,'Matthew Stafford','QB',2023),
    (32,'Sam Howell','QB',2023),
    (23,'Derek Carr','QB',2023),
    (26,'Jalen Hurts','QB',2023),
    (3,'Lamar Jackson','QB',2023),
    (29,'Geno Smith','QB',2023),
    (14,'Gardner Minshew','QB',2023),
    (18,'Justin Herbert','QB',2023),
    (10,'Russell Wilson','QB',2023),
    (5,'Bryce Young','QB',2023),
    (2,'Desmond Ridder','QB',2023),
    (6,'Justin Fields','QB',2023),
    (21,'Joshua Dobbs','QB',2023),
    (21,'Kirk Cousins','QB',2023),
    (7,'Joe Burrow','QB',2023),
    (25,'Zach Wilson','QB',2023),
    (17,'Aidan Connell','QB',2023),
    (22,'Mac Jones','QB',2023),
    (27,'Kenny Pickett','QB',2023),
    (7,'Jake Browning','QB',2023),
    (31,'Will Levis','QB',2023),
    (1,'Kyler Murray','QB',2023),
    (8,'Joe Flacco','QB',2023),
    (31,'Ryan Tannehill','QB',2023),
    (24,'Tyrod Taylor','QB',2023),
    (21,'Nick Mullens','QB',2023),
    (22,'Bailey Zappe','QB',2023),
    (17,'Jimmy Garoppolo','QB',2023),
    (18,'Easton Stick','QB',2023),
    (8,'Deshaun Watson','QB',2023),
    (24,'Tommy DeVito','QB',2023),
    (24,'Daniel Jones','QB',2023),
    (2,'Taylor Heinicke','QB',2023),
    (6,'Tyson Bagent','QB',2023),
    (25,'Trevor Siemian','QB',2023),
    (27,'Mason Rudolph','QB',2023),
    (8,'PJ Walker','QB',2023),
    (27,'Mitchell Trubisky','QB',2023),
    (14,'Anthony Richardson','QB',2023),
    (29,'Drew Lock','QB',2023),
    (10,'Jarrett Stidham','QB',2023),
    (8,'Dorian Thompson-Robinson','QB',2023),
    (5,'Andy Dalton','QB',2023),
    (25,'Tim Boyle','QB',2023),
    (15,'C.J. Beathard','QB',2023),
    (28,'Sam Darnold','QB',2023),
    (13,'Case Keenum','QB',2023),
    (23,'Jameis Winston','QB',2023),
    (17,'Brian Hoyer','QB',2023),
    (32,'Jacoby Brissett','QB',2023),
    (3,'Tyler Huntley','QB',2023),
    (16,'Blaine Gabbert','QB',2023),
    (13,'Davis Mills','QB',2023),
    (19,'Brett Rypien','QB',2023),
    (21,'Jaren Hall','QB',2023),
    (8,'Jeff Driskel','QB',2023),
    (26,'Marcus Mariota','QB',2023),
    (19,'Carson Wentz','QB',2023),
    (9,'Cooper Rush','QB',2023),
    (23,'Taysom Hill','QB',2023),
    (20,'Mike White','QB',2023),
    (31,'Malik Willis','QB',2023),
    (1,'Clayton Tune','QB',2023),
    (18,'Keenan Allen','WR',2023),
    (12,'Sean Clifford','QB',2023),
    (11,'Jalen Reeves-Maybin','LB',2023),
    (26,'Braden Mann','P',2023),
    (2,'Logan Woodside','QB',2023),
    (2,'Drake London','WR',2023),
    (7,'AJ McCarron','QB',2023),
    (25,'Thomas Morstead','P',2023),
    (26,'Kenneth Gainwell','RB',2023),
    (31,'Derrick Henry','RB',2023),
    (12,'Dontayvion Wicks','WR',2023),
    (15,'Logan Cooke','P',2023),
    (17,'Jakobi Meyers','WR',2023),
    (16,'Tommy Townsend','P',2023),
    (5,'Johnny Hekker','P',2023),
    (13,'Devin Singletary','RB',2023),
    (16,'Jerick McKinnon','RB',2023),
    (32,'Dyami Brown','WR',2023),
    (25,'Aaron Rodgers','QB',2023),
    (31,'DeAndre Hopkins','WR',2023),
    (6,'Nathan Peterman','QB',2023),
    (7,'Tyler Boyd','WR',2023),
    (7,'Tanner Hudson','TE',2023),
    (2,'Jonnu Smith','TE',2023),
    (30,'Chris Godwin','WR',2023),
    (24,'Parris Campbell','WR',2023),
    (28,'Deebo Samuel','WR',2023),
    (30,'Kyle Trask','QB',2023),
    (20,'Cedrick Wilson','WR',2023),
    (17,'Josh Jacobs','RB',2023),
    (21,'Cam Akers','RB',2023),
    (22,'Malik Cunningham','WR',2023),
    (16,'Kadarius Toney','WR',2023),
    (29,'DeeJay Dallas','RB',2023),
    (27,'Connor Heyward','TE',2023),
    (21,'Justin Jefferson','WR',2023),
    (13,'Tank Dell','WR',2023),
    (11,'Amon-Ra St. Brown','WR',2023),
    (20,'De Von Achane','RB',2023),
    (25,'Garrett Wilson','WR',2023),
    (15,'Christian Kirk','WR',2023),
    (7,'Ja Marr Chase','WR',2023),
    (20,'Tyreek Hill','WR',2023),
    (9,'CeeDee Lamb','WR',2023),
    (19,'Puka Nacua','WR',2023),
    (26,'A.J. Brown','WR',2023),
    (6,'DJ Moore','WR',2023),
    (28,'Brandon Aiyuk','WR',2023),
    (13,'Nico Collins','WR',2023),
    (30,'Mike Evans','WR',2023),
    (8,'Amari Cooper','WR',2023),
    (18,'Keenan Allen','WR',2023),
    (7,'Ja Marr Chase','WR',2023),
    (4,'Stefon Diggs','WR',2023),
    (14,'Michael Pittman Jr.','WR',2023),
    (17,'Davante Adams','WR',2023),
    (27,'George Pickens','WR',2023),
    (23,'Chris Olave','WR',2023),
    (29,'DK Metcalf','WR',2023),
    (21,'Justin Jefferson','WR',2023),
    (26,'DeVonta Smith','WR',2023),
    (31,'DeAndre Hopkins','WR',2023),
    (25,'Garrett Wilson','WR',2023),
    (30,'Chris Godwin','WR',2023),
    (28,'George Kittle','TE',2023),
    (15,'Calvin Ridley','WR',2023),
    (5,'Adam Thielen','WR',2023),
    (20,'Jaylen Waddle','WR',2023),
    (32,'Terry McLaurin','WR',2023),
    (16,'Travis Kelce','TE',2023),
    (15,'Evan Engram','TE',2023),
    (21,'T.J. Hockenson','TE',2023),
    (16,'Rashee Rice','WR',2023),
    (21,'Jordan Addison','WR',2023),
    (2,'Drake London','WR',2023),
    (29,'Tyler Lockett','WR',2023),
    (28,'Deebo Samuel','WR',2023),
    (11,'Sam LaPorta','TE',2023),
    (8,'David Njoku','TE',2023),
    (3,'Zay Flowers','WR',2023),
    (1,'Trey McBride','TE',2023),
    (17,'Jakobi Meyers','WR',2023),
    (12,'Jayden Reed','WR',2023),
    (15,'Christian Kirk','WR',2023),
    (10,'Courtland Sutton','WR',2023),
    (14,'Josh Downs','WR',2023),
    (24,'Darius Slayton','WR',2023),
    (9,'Jake Ferguson','TE',2023),
    (10,'Jerry Jeudy','WR',2023),
    (4,'Gabe Davis','WR',2023),
    (19,'Cooper Kupp','WR',2023),
    (23,'Rashid Shaheed','WR',2023),
    (6,'Cole Kmet','TE',2023),
    (27,'Diontae Johnson','WR',2023),
    (13,'Tank Dell','WR',2023),
    (12,'Romeo Doubs','WR',2023),
    (4,'Dalton Kincaid','TE',2023),
    (7,'Tyler Boyd','WR',2023),
    (2,'Kyle Pitts','TE',2023),
    (9,'Brandin Cooks','WR',2023),
    (7,'Tee Higgins','WR',2023),
    (8,'Elijah Moore','WR',2023),
    (13,'Dalton Schultz','TE',2023),
    (29,'Jaxon Smith-Njigba','WR',2023),
    (25,'Tyler Conklin','TE',2023),
    (32,'Curtis Samuel','WR',2023),
    (4,'Khalil Shakir','WR',2023),
    (11,'Josh Reynolds','WR',2023),
    (26,'Dallas Goedert','TE',2023),
    (25,'Breece Hall','RB',2023),
    (2,'Jonnu Smith','TE',2023),
    (18,'Joshua Palmer','WR',2023),
    (12,'Dontayvion Wicks','WR',2023),
    (1,'Marquise Brown','WR',2023),
    (13,'Noah Brown','WR',2023),
    (3,'Odell Beckham Jr.','WR',2023),
    (1,'Michael Wilson','WR',2023),
    (28,'Christian McCaffrey','RB',2023),
    (22,'DeMario Douglas','WR',2023),
    (24,'Darren Waller','TE',2023),
    (30,'Rachaad White','RB',2023),
    (3,'Mark Andrews','TE',2023),
    (21,'K.J. Osborn','WR',2023),
    (31,'Chigoziem Okonkwo','TE',2023),
    (5,'DJ Chark Jr.','WR',2023),
    (24,'Wan Dale Robinson','WR',2023),
    (32,'Jahan Dotson','WR',2023),
    (14,'Alec Pierce','WR',2023),
    (32,'Logan Thomas','TE',2023),
    (19,'Tyler Higbee','TE',2023),
    (11,'Kalif Raymond','WR',2023),
    (2,'Bijan Robinson','RB',2023),
    (19,'Tutu Atwell','WR',2023),
    (15,'Travis Etienne Jr.','RB',2023),
    (23,'Alvin Kamara','RB',2023),
    (16,'Justin Watson','WR',2023),
    (10,'Samaje Perine','RB',2023),
    (30,'Cade Otton','TE',2023),
    (23,'Michael Thomas','WR',2023),
    (4,'James Cook','RB',2023),
    (18,'Austin Ekeler','RB',2023),
    (18,'Quentin Johnston','WR',2023),
    (13,'Robert Woods','WR',2023),
    (31,'Chris Moore','WR',2023),
    (12,'Christian Watson','WR',2023),
    (22,'Hunter Henry','TE',2023),
    (9,'Michael Gallup','WR',2023),
    (5,'Jonathan Mingo','WR',2023),
    (29,'Noah Fant','TE',2023),
    (6,'Darnell Mooney','WR',2023),
    (18,'Gerald Everett','TE',2023),
    (3,'Isaiah Likely','TE',2023),
    (22,'Kendrick Bourne','WR',2023),
    (22,'DeVante Parker','WR',2023),
    (32,'Antonio Gibson','RB',2023),
    (30,'Trey Palmer','WR',2023),
    (31,'Tyjae Spears','RB',2023),
    (3,'Nelson Agholor','WR',2023),
    (10,'Marvin Mims Jr.','WR',2023),
    (7,'Joe Mixon','RB',2023),
    (24,'Jalin Hyatt','WR',2023),
    (19,'Demarcus Robinson','WR',2023),
    (31,'Nick Westbrook-Ikhine','WR',2023),
    (27,'Jaylen Warren','RB',2023),
    (23,'Juwan Johnson','TE',2023),
    (14,'Kylen Granson','TE',2023),
    (32,'Brian Robinson Jr.','RB',2023),
    (3,'Rashod Bateman','WR',2023),
    (20,'Durham Smythe','TE',2023),
    (12,'Tucker Kraft','TE',2023),
    (11,'Jameson Williams','WR',2023),
    (7,'Tanner Hudson','TE',2023),
    (1,'Rondale Moore','WR',2023),
    (12,'Luke Musgrave','TE',2023),
    (17,'Tre Tucker','WR',2023),
    (21,'Brandon Powell','WR',2023),
    (15,'Zay Jones','WR',2023),
    (8,'Jerome Ford','RB',2023),
    (7,'Trenton Irwin','WR',2023),
    (11,'Jahmyr Gibbs','RB',2023),
    (16,'Marquez Valdes-Scantling','WR',2023),
    (22,'Ezekiel Elliott','RB',2023),
    (25,'Allen Lazard','WR',2023),
    (9,'Tony Pollard','RB',2023),
    (27,'Pat Freiermuth','TE',2023),
    (16,'Noah Gray','TE',2023),
    (17,'Michael Mayer','TE',2023),
    (20,'Cedrick Wilson Jr.','WR',2023),
    (17,'Josh Jacobs','RB',2023),
    (23,'Taysom Hill','QB',2023),
    (18,'Donald Parham Jr.','TE',2023),
    (10,'Brandon Johnson','WR',2023),
    (27,'Allen Robinson II','WR',2023),
    (24,'Saquon Barkley','RB',2023),
    (1,'Greg Dortch','WR',2023),
    (9,'Jalen Tolbert','WR',2023),
    (28,'Jauan Jennings','WR',2023),
    (22,'JuJu Smith-Schuster','WR',2023),
    (29,'Kenneth Walker III','RB',2023),
    (17,'Hunter Renfrow','WR',2023),
    (24,'Daniel Bellinger','TE',2023),
    (2,'Mack Hollins','WR',2023),
    (18,'Mike Williams','WR',2023),
    (29,'Colby Parkinson','TE',2023),
    (23,'A.T. Perry','WR',2023),
    (22,'Mike Gesicki','TE',2023),
    (16,'Isiah Pacheco','RB',2023),
    (16,'Skyy Moore','WR',2023),
    (20,'Braxton Berrios','WR',2023),
    (22,'Rhamondre Stevenson','RB',2023),
    (17,'Austin Hooper','TE',2023),
    (12,'Aaron Jones','RB',2023),
    (5,'Chuba Hubbard','RB',2023),
    (18,'Alex Erickson','WR',2023),
    (2,'KhaDarel Hodge','WR',2023),
    (24,'Isaiah Hodgins','WR',2023),
    (25,'Xavier Gipson','WR',2023),
    (10,'Javonte Williams','RB',2023),
    (15,'Jamal Agnew','WR',2023),
    (8,'Cedric Tillman','WR',2023),
    (12,'AJ Dillon','RB',2023),
    (31,'Treylon Burks','WR',2023),
    (13,'Brevin Jordan','TE',2023),
    (12,'Bo Melton','WR',2023),
    (31,'Derrick Henry','RB',2023),
    (26,'Andre Swift','RB',2023),
    (21,'Josh Oliver','TE',2023),
    (19,'Van Jefferson','WR',2023),
    (29,'Zach Charbonnet','RB',2023),
    (6,'Roschon Johnson','RB',2023),
    (22,'Pharaoh Brown','TE',2023),
    (14,'Will Mallory','TE',2023),
    (3,'Justice Hill','RB',2023),
    (19,'Kyren Williams','RB',2023),
    (10,'Adam Trautman','TE',2023),
    (20,'De Von Achane','RB',2023),
    (29,'Jake Bobo','WR',2023),
    (5,'Tommy Tremble','TE',2023),
    (23,'Foster Moreau','TE',2023),
    (13,'Devin Singletary','RB',2023),
    (2,'Tyler Allgeier','RB',2023),
    (16,'Jerick McKinnon','RB',2023),
    (14,'Zack Moss','RB',2023),
    (21,'Alexander Mattison','RB',2023),
    (16,'Clyde Edwards-Helaire','RB',2023),
    (1,'Zach Ertz','TE',2023),
    (4,'Dawson Knox','TE',2023),
    (5,'Hayden Hurst','TE',2023),
    (26,'Kenneth Gainwell','RB',2023),
    (31,'Kyle Philips','WR',2023),
    (3,'Gus Edwards','RB',2023),
    (27,'Calvin Austin III','WR',2023),
    (20,'Raheem Mostert','RB',2023),
    (21,'Johnny Mundt','TE',2023),
    (29,'Will Dissly','TE',2023),
    (27,'Najee Harris','RB',2023),
    (16,'Kadarius Toney','WR',2023),
    (32,'Dyami Brown','WR',2023),
    (6,'Tyler Scott','WR',2023),
    (27,'Connor Heyward','TE',2023),
    (8,'David Bell','WR',2023),
    (1,'James Conner','RB',2023),
    (26,'Olamide Zaccheaus','WR',2023),
    (7,'Drew Sample','TE',2023),
    (1,'Elijah Higgins','TE',2023),
    (10,'Lil Jordan Humphrey','WR',2023),
    (14,'Mo Alie-Cox','TE',2023),
    (2,'Scotty Miller','WR',2023),
    (32,'Byron Pringle','WR',2023),
    (10,'Jaleel McLaughlin','RB',2023),
    (32,'Jamison Crowder','WR',2023),
    (21,'Ty Chandler','RB',2023),
    (13,'John Metchie III','WR',2023),
    (7,'Chase Brown','RB',2023),
    (15,'Luke Farrell','TE',2023),
    (18,'Stone Smartt','TE',2023),
    (11,'Donovan Peoples-Jones','WR',2023),
    (5,'Miles Sanders','RB',2023),
    (14,'Jonathan Taylor','RB',2023),
    (32,'John Bates','TE',2023),
    (25,'Jeremy Ruckert','TE',2023),
    (4,'Deonte Harty','WR',2023),
    (14,'Drew Ogletree','TE',2023),
    (9,'Rico Dowdle','RB',2023),
    (26,'Quez Watkins','WR',2023),
    (15,'Ernest Johnson','RB',2023),
    (5,'Terrace Marshall Jr.','WR',2023),
    (22,'Jalen Reagor','WR',2023),
    (28,'Ray-Ray McCloud III','WR',2023),
    (6,'Khalil Herbert','RB',2023),
    (8,'Jordan Akins','TE',2023),
    (15,'Parker Washington','WR',2023),
    (17,'Ameer Abdullah','RB',2023),
    (9,'KaVontae Turpin','WR',2023),
    (20,'Robbie Chosen','WR',2023),
    (5,'Stephen Sullivan','TE',2023),
    (12,'Malik Heath','WR',2023),
    (25,'Mecole Hardman','WR',2023),
    (20,'River Cracraft','WR',2023),
    (32,'Cole Turner','TE',2023),
    (4,'Latavius Murray','RB',2023),
    (28,'Kyle Juszczyk','FB',2023),
    (20,'Alec Ingold','FB',2023),
    (1,'Emari Demercado','RB',2023),
    (11,'David Montgomery','RB',2023),
    (23,'Kendre Miller','RB',2023),
    (7,'Andrei Iosivas','WR',2023),
    (7,'Irv Smith Jr.','TE',2023),
    (16,'Richie James','WR',2023),
    (6,'Robert Tonyan','TE',2023),
    (2,'MyCole Pruitt','TE',2023),
    (24,'Parris Campbell','WR',2023),
    (19,'Darrell Henderson Jr.','RB',2023),
    (25,'Michael Carter','RB',2023),
    (13,'Dameon Pierce','RB',2023),
    (17,'Zamir White','RB',2023),
    (10,'Lucas Krull','TE',2023),
    (19,'Davis Allen','TE',2023),
    (1,'Geoff Swaim','TE',2023),
    (30,'David Moore','WR',2023),
    (31,'Josh Whyle','TE',2023),
    (3,'Keaton Mitchell','RB',2023),
    (11,'Brock Wright','TE',2023),
    (22,'Tyquan Thornton','WR',2023),
    (13,'Xavier Hutchinson','WR',2023),
    (18,'Jalen Guyton','WR',2023),
    (24,'Matt Breida','RB',2023),
    (20,'Salvon Ahmed','RB',2023),
    (3,'Charlie Kolar','TE',2023),
    (4,'Trent Sherfield Sr.','WR',2023),
    (20,'Jeff Wilson Jr.','RB',2023),
    (8,'Kareem Hunt','RB',2023),
    (15,'Tim Jones','WR',2023),
    (23,'Lynn Bowden Jr.','WR',2023),
    (30,'Deven Thompkins','WR',2023),
    (14,'Isaiah McKenzie','WR',2023),
    (30,'Chase Edmonds','RB',2023),
    (8,'Harrison Bryant','TE',2023),
    (25,'Dalvin Cook','RB',2023),
    (19,'Brycen Hopkins','TE',2023),
    (12,'Samori Toure','WR',2023),
    (6,'Onta Foreman','RB',2023),
    (20,'Chase Claypool','WR',2023),
    (26,'Julio Jones','WR',2023),
    (21,'Cam Akers','RB',2023),
    (28,'Chris Conley','WR',2023),
    (28,'Ronnie Bell','WR',2023),
    (8,'Marquise Goodwin','WR',2023),
    (19,'Ben Skowronek','WR',2023),
    (18,'Derius Davis','WR',2023),
    (12,'Josiah Deguara','TE',2023),
    (9,'Luke Schoonmaker','TE',2023),
    (7,'Charlie Jones','WR',2023),
    (9,'Jalen Brooks','WR',2023),
    (23,'Jamaal Williams','RB',2023),
    (4,'Ty Johnson','RB',2023),
    (6,'Equanimeous St. Brown','WR',2023),
    (27,'Darnell Washington','TE',2023),
    (5,'Laviska Shenault Jr.','WR',2023),
    (30,'Rakim Jarrett','WR',2023),
    (25,'C.J. Uzomah','TE',2023),
    (30,'Payne Durham','TE',2023),
    (22,'Kevin Harris','RB',2023),
    (24,'Sterling Shepard','WR',2023),
    (7,'Mitchell Wilcox','TE',2023),
    (5,'Ian Thomas','TE',2023),
    (14,'D.J. Montgomery','WR',2023),
    (25,'Jason Brownlee','WR',2023),
    (13,'Andrew Beck','FB',2023),
    (16,'Justyn Ross','WR',2023),
    (3,'Patrick Ricard','FB',2023),
    (26,'Boston Scott','RB',2023),
    (5,'Ihmir Smith-Marsette','WR',2023),
    (20,'Darrynton Evans','RB',2023),
    (12,'Patrick Taylor Jr.','RB',2023),
    (20,'Julian Hill','TE',2023),
    (24,'Gary Brightwell','RB',2023),
    (8,'Pierre Strong Jr.','RB',2023),
    (11,'Craig Reynolds','RB',2023),
    (3,'Melvin Gordon III','RB',2023),
    (5,'Raheem Blackshear','RB',2023),
    (5,'Mike Strachan','WR',2023),
    (25,'Israel Abanikanda','RB',2023),
    (26,'Britain Covey','WR',2023),
    (22,'Ty Montgomery II','WR',2023),
    (13,'Mike Boone','RB',2023),
    (9,'Deuce Vaughn','RB',2023),
    (23,'Jimmy Graham','TE',2023),
    (25,'Randall Cobb','WR',2023),
    (17,'DeAndre Carter','WR',2023),
    (26,'Grant Calcaterra','TE',2023),
    (2,'Cordarrelle Patterson','RB',2023),
    (26,'Jack Stoll','TE',2023),
    (15,'Elijah Cooks','WR',2023),
    (9,'Peyton Hendershot','TE',2023),
    (23,'Keith Kirkwood','WR',2023),
    (23,'Tony Jones Jr.','RB',2023),
    (24,'Lawrence Cager','TE',2023),
    (11,'Marvin Jones Jr.','WR',2023),
    (15,'Brenton Strange','TE',2023),
    (18,'Isaiah Spiller','RB',2023),
    (14,'Tyler Goodson','RB',2023),
    (2,'Keith Smith','FB',2023),
    (18,'Keelan Doss','WR',2023),
    (16,'La Mical Perine','RB',2023),
    (13,'Teagan Quitoriano','TE',2023),
    (18,'Joshua Kelley','RB',2023),
    (28,'Charlie Woerner','TE',2023),
    (12,'Kenyan Drake','RB',2023),
    (11,'Khalil Dorsey','CB',2023),
    (28,'Jordan Mason','RB',2023),
    (6,'Marcedes Lewis','TE',2023),
    (19,'Austin Trammell','WR',2023),
    (21,'Jalen Nailor','WR',2023),
    (25,'Kenny Yeboah','TE',2023),
    (11,'James Mitchell','TE',2023),
    (16,'Blake Bell','TE',2023),
    (29,'DeeJay Dallas','RB',2023),
    (4,'Quintin Morris','TE',2023),
    (1,'Keaontay Ingram','RB',2023),
    (13,'Steven Sims','WR',2023),
    (21,'C.J. Ham','FB',2023),
    (10,'Greg Dulcich','TE',2023),
    (12,'Emanuel Wilson','RB',2023),
    (19,'Ronnie Rivers','RB',2023),
    (21,'Nick Muse','TE',2023),
    (10,'Nate Adkins','TE',2023),
    (24,'Eric Gray','RB',2023),
    (25,'Nick Bawden','FB',2023),
    (8,'Nick Chubb','RB',2023),
    (31,'Trevon Wesco','TE',2023),
    (12,'Ben Sims','TE',2023),
    (6,'Velus Jones Jr.','WR',2023),
    (1,'Zach Pascal','WR',2023),
    (22,'Kayshon Boutte','WR',2023),
    (13,'Dare Ogunbowale','RB',2023),
    (3,'Devin Duvernay','WR',2023),
    (9,'Hunter Luepke','RB',2023),
    (25,'Brandin Echols','CB',2023),
    (27,'Miles Boykin','WR',2023),
    (10,'Chris Manhertz','TE',2023),
    (3,'Laquon Treadwell','WR',2023),
    (4,'Damien Harris','RB',2023),
    (3,'J.K. Dobbins','RB',2023),
    (28,'Willie Snead IV','WR',2023),
    (24,'Deon Jackson','RB',2023),
    (28,'Elijah Mitchell','RB',2023),
    (19,'Royce Freeman','RB',2023),
    (32,'Alex Armah','RB',2023),
    (14,'Trey Sermon','RB',2023),
    (18,'Elijah Dotson','RB',2023),
    (25,'Malik Taylor','WR',2023),
    (1,'Damien Williams','RB',2023),
    (9,'Eric Saubert','TE',2023),
    (17,'Jakob Johnson','FB',2023),
    (28,'Ross Dwelley','TE',2023),
    (23,'Adam Prentice','FB',2023),
    (14,'Jake Funk','RB',2023),
    (32,'Chris Rodriguez Jr.','RB',2023),
    (24,'Jashaun Corbin','RB',2023),
    (2,'John FitzPatrick','TE',2023),
    (6,'Collin Johnson','WR',2023),
    (3,'Tylan Wallace','WR',2023),
    (27,'Anthony McFarland Jr.','RB',2023),
    (29,'Cody Thompson','WR',2023),
    (7,'Trayveon Williams','RB',2023),
    (18,'Justin Herbert','QB',2023),
    (21,'Trishton Jackson','WR',2023),
    (2,'Tucker Fisk','TE',2023),
    (18,'Simi Fehoko','WR',2023),
    (30,'Sean Tucker','RB',2023),
    (19,'Tyler Johnson','WR',2023),
    (10,'Michael Burton','FB',2023),
    (11,'Devine Ozigbo','RB',2023),
    (11,'Zonovan Knight','RB',2023),
    (31,'Kevin Rader','TE',2023),
    (31,'Mason Kinsey','WR',2023),
    (11,'Malcolm Rodriguez','LB',2023),
    (17,'Cole Fotheringham','TE',2023),
    (15,'Tank Bigsby','RB',2023),
    (14,'Evan Hull','RB',2023),
    (17,'Greg Van Roten','G',2023),
    (26,'Rashaad Penny','RB',2023),
    (11,'Dan Skipper','OT',2023),
    (17,'Jesper Horsted','TE',2023),
    (32,'Sam Howell','QB',2023),
    (18,'Nick Vannett','TE',2023),
    (4,'Reggie Gilliam','FB',2023),
    (22,'Cole Strange','G',2023),
    (31,'Colton Dowell','WR',2023),
    (6,'Khari Blasingame','FB',2023),
    (5,'Giovanni Ricci','FB',2023),
    (30,'Ke Shawn Vaughn','RB',2023),
    (30,'Ko Kieft','TE',2023),
    (31,'Jeffery Simmons','DT',2023),
    (7,'Kwamie Lassiter II','WR',2023),
    (11,'Antoine Green','WR',2023),
    (31,'Ryan Tannehill','QB',2023),
    (2,'Damiere Byrd','WR',2023),
    (10,'Phillip Dorsett','WR',2023),
    (16,'Donovan Smith','OT',2023),
    (32,'Jonathan Williams','RB',2023),
    (6,'Trent Taylor','WR',2023),
    (14,'Juwann Winfree','WR',2023),
    (8,'James Proche II','WR',2023),
    (15,'JaMycal Hasty','RB',2023),
    (25,'Irvin Charles','WR',2023),
    (26,'Albert Okwuegbunam Jr.','TE',2023),
    (9,'Sean McKeon','TE',2023),
    (6,'Travis Homer','RB',2023),
    (29,'Dee Eskridge','WR',2023),
    (24,'Ben Bredeson','G',2023),
    (14,'Amari Rodgers','WR',2023),
    (23,'Jordan Mims','RB',2023),
    (27,'Rodney Williams','TE',2023),
    (7,'Shedrick Jackson','WR',2023),
    (20,'Erik Ezukanma','WR',2023),
    (24,'Gunner Olszewski','WR',2023),
    (13,'C.J. Stroud','QB',2023),
    (7,'Chris Evans','RB',2023),
    (29,'Geno Smith','QB',2023),
    (12,'James Robinson','RB',2023),
    (30,'Robert Hainsey','C',2023),
    (2,'Desmond Ridder','QB',2023),
    (7,'Jake Browning','QB',2023),
    (30,'David Wells','TE',2023),
    (28,'Christian McCaffrey','RB',2023),
    (19,'Kyren Williams','RB',2023),
    (4,'James Cook','RB',2023),
    (26,'Andre Swift','RB',2023),
    (1,'James Conner','RB',2023),
    (27,'Najee Harris','RB',2023),
    (7,'Joe Mixon','RB',2023),
    (11,'David Montgomery','RB',2023),
    (20,'Raheem Mostert','RB',2023),
    (15,'Travis Etienne Jr','RB',2023),
    (9,'Tony Pollard','RB',2023),
    (25,'Breece Hall','RB',2023),
    (30,'Rachaad White','RB',2023),
    (2,'Bijan Robinson','RB',2023),
    (24,'Saquon Barkley','RB',2023),
    (11,'Jahmyr Gibbs','RB',2023),
    (16,'Isiah Pacheco','RB',2023),
    (3,'Lamar Jackson','QB',2023),
    (6,'Justin Fields','QB',2023),
    (26,'Jalen Hurts','QB',2023),
    (4,'Josh Allen','QB',2023),
    (21,'Joshua Dobbs','QB',2023),
    (16,'Patrick Mahomes','QB',2023),
    (10,'Russell Wilson','QB',2023),
    (15,'Trevor Lawrence','QB',2023),
    (5,'Bryce Young','QB',2023),
    (12,'Jordan Love','QB',2023),
    (1,'Kyler Murray','QB',2023),
    (9,'Dak Prescott','QB',2023),
    (25,'Zach Wilson','QB',2023),
    (24,'Daniel Jones','QB',2023),
    (24,'Tyrod Taylor','QB',2023),
    (24,'Tommy DeVito','QB',2023),
    (20,'Jeff Wilson','RB',2023),
    (30,'Baker Mayfield','QB',2023),
    (18,'Easton Stick','QB',2023),
    (28,'Brock Purdy','QB',2023),
    (8,'Deshaun Watson','QB',2023),
    (12,'Patrick Taylor','RB',2023),
    (14,'Anthony Richardson','QB',2023),
    (2,'Taylor Heinicke','QB',2023),
    (19,'Darrell Henderson','RB',2023),
    (6,'Tyson Bagent','QB',2023),
    (20,'Chris Brooks','RB',2023),
    (14,'Gardner Minshew','QB',2023),
    (22,'Mac Jones','QB',2023),
    (23,'Tony Jones','RB',2023),
    (7,'Joe Burrow','QB',2023),
    (22,'Bailey Zappe','QB',2023),
    (20,'Tua Tagovailoa','QB',2023),
    (19,'Matthew Stafford','QB',2023),
    (8,'Dorian Thompson-Robinson','QB',2023),
    (31,'Will Levis','QB',2023),
    (19,'Carson Wentz','QB',2023),
    (3,'Tyler Huntley','QB',2023),
    (27,'Mitchell Trubisky','QB',2023),
    (27,'Kenny Pickett','QB',2023),
    (26,'Marcus Mariota','QB',2023),
    (16,'Blaine Gabbert','QB',2023),
    (23,'Derek Carr','QB',2023),
    (25,'Trevor Siemian','QB',2023),
    (4,'Leonard Fournette','RB',2023),
    (17,'Jimmy Garoppolo','QB',2023),
    (15,'C.J. Beathard','QB',2023),
    (8,'Jeff Driskel','QB',2023),
    (17,'Brandon Bolden','RB',2023),
    (8,'PJ Walker','QB',2023),
    (1,'Clayton Tune','QB',2023),
    (32,'Derrick Gore','RB',2023),
    (21,'Kirk Cousins','QB',2023),
    (21,'Nick Mullens','QB',2023),
    (31,'Malik Willis','QB',2023),
    (28,'Tyrion Davis-Price','RB',2023),
    (32,'Jacoby Brissett','QB',2023),
    (19,'Brett Rypien','QB',2023),
    (19,'Zach Evans','RB',2023),
    (28,'Sam Darnold','QB',2023),
    (29,'Drew Lock','QB',2023),
    (21,'Jaren Hall','QB',2023),
    (21,'Kene Nwangwu','RB',2023),
    (5,'Andy Dalton','QB',2023),
    (31,'Jonathan Ward','RB',2023),
    (12,'Keisean Nixon','CB',2023),
    (17,'Aidan Connell','QB',2023),
    (1,'Blake Gillikin','P',2023),
    (13,'Davis Mills','QB',2023),
    (27,'Mason Rudolph','QB',2023),
    (10,'Jarrett Stidham','QB',2023),
    (2,'Logan Woodside','QB',2023),
    (25,'Tim Boyle','QB',2023),
    (11,'Jalen Reeves-Maybin','LB',2023),
    (25,'Ashtyn Davis','S',2023),
    (8,'Joe Flacco','QB',2023),
    (1,'Ezekiel Turner','LB',2023),
    (31,'Amani Hooker','S',2023),
    (13,'Case Keenum','QB',2023),
    (32,'Tress Way','P',2023),
    (11,'Jason Cabinda','FB',2023),
    (18,'Nick Niemann','LB',2023),
    (31,'Ty Zentner','P',2023),
    (30,'Kyle Trask','QB',2023),
    (11,'Teddy Bridgewater','QB',2023),
    (12,'Sean Clifford','QB',2023),
    (17,'Brian Hoyer','QB',2023),
    (15,'Matt Barkley','QB',2023),
    (6,'Nathan Peterman','QB',2023),
    (9,'Cooper Rush','QB',2023),
    (23,'Jameis Winston','QB',2023),
    (20,'Mike White','QB',2023),
    (5,'Johnny Hekker','P',2023),
    (31,'Ryan Stonehouse','P',2023),
    (4,'Kyle Allen','QB',2023),
    (13,'Cameron Johnston','P',2023),
]

# Insertar los datos uno por uno
for data in datos_a_insertar:
    cursor.execute('''
    INSERT INTO Player_season (Team_ID, Name, Posicion, Anio)
    VALUES (?, ?, ?, ?)
    ''', data)
"""

# Incertar las estadísticas de los jugadores
datos_a_insertar = [
(' Jameis Winston',30,QB,16,626,5109,71,33,(SELECT Player_ID FROM Player_season WHERE Name = 'Jameis Winston' AND Anio = 2019),1),
(' Dak Prescott',9,QB,16,596,4902,62,30,(SELECT Player_ID FROM Player_season WHERE Name = 'Dak Prescott' AND Anio = 2019),1),
(' Jared Goff',19,QB,16,626,4638,66,22,(SELECT Player_ID FROM Player_season WHERE Name = 'Jared Goff' AND Anio = 2019),1),
(' Philip Rivers',18,QB,16,591,4615,84,23,(SELECT Player_ID FROM Player_season WHERE Name = 'Philip Rivers' AND Anio = 2019),1),
(' Matt Ryan',2,QB,15,616,4466,93,26,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Ryan' AND Anio = 2019),1),
(' Russell Wilson',29,QB,16,516,4110,60,31,(SELECT Player_ID FROM Player_season WHERE Name = 'Russell Wilson' AND Anio = 2019),"1),"
(' Tom Brady',22,QB,16,613,4057,59,24,(SELECT Player_ID FROM Player_season WHERE Name = 'Tom Brady' AND Anio = 2019),"1),"
(' Derek Carr',17,QB,16,513,4054,75,21,(SELECT Player_ID FROM Player_season WHERE Name = 'Derek Carr' AND Anio = 2019),"1),"
(' Carson Wentz',26,QB,16,607,4039,53,27,(SELECT Player_ID FROM Player_season WHERE Name = 'Carson Wentz' AND Anio = 2019),"1),"
(' Patrick Mahomes',16,QB,14,484,4031,83,26,(SELECT Player_ID FROM Player_season WHERE Name = 'Patrick Mahomes' AND Anio = 2019),"1),"
(' Aaron Rodgers',12,QB,16,569,4002,74,26,(SELECT Player_ID FROM Player_season WHERE Name = 'Aaron Rodgers' AND Anio = 2019),"1),"
(' Jimmy Garoppolo',28,QB,16,476,3978,75,27,(SELECT Player_ID FROM Player_season WHERE Name = 'Jimmy Garoppolo' AND Anio = 2019),"1),"
(' Deshaun Watson',13,QB,15,495,3852,54,26,(SELECT Player_ID FROM Player_season WHERE Name = 'Deshaun Watson' AND Anio = 2019),"1),"
(' Baker Mayfield',8,QB,16,534,3827,89,22,(SELECT Player_ID FROM Player_season WHERE Name = 'Baker Mayfield' AND Anio = 2019),"1),"
(' Kyler Murray',1,QB,16,542,3722,88,20,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyler Murray' AND Anio = 2019),"1),"
(' Kirk Cousins',21,QB,15,444,3603,66,26,(SELECT Player_ID FROM Player_season WHERE Name = 'Kirk Cousins' AND Anio = 2019),"1),"
(' Ryan Fitzpatrick',20,QB,15,502,3529,51,20,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Fitzpatrick' AND Anio = 2019),"1),"
(' Andy Dalton',7,QB,13,528,3494,66,16,(SELECT Player_ID FROM Player_season WHERE Name = 'Andy Dalton' AND Anio = 2019),"1),"
(' Kyle Allen',5,QB,13,489,3322,52,17,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Allen' AND Anio = 2019),"1),"
(' Gardner Minshew',15,QB,14,470,3271,70,21,(SELECT Player_ID FROM Player_season WHERE Name = 'Gardner Minshew' AND Anio = 2019),"1),"
(' Mitchell Trubisky',6,QB,15,516,3138,53,17,(SELECT Player_ID FROM Player_season WHERE Name = 'Mitchell Trubisky' AND Anio = 2019),"1),"
(' Lamar Jackson',3,QB,15,401,3127,83,36,(SELECT Player_ID FROM Player_season WHERE Name = 'Lamar Jackson' AND Anio = 2019),"1),"
(' Josh Allen',4,QB,16,461,3089,53,20,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Allen' AND Anio = 2019),"1),"
(' Daniel Jones',24,QB,13,459,3027,75,24,(SELECT Player_ID FROM Player_season WHERE Name = 'Daniel Jones' AND Anio = 2019),"1),"
(' Sam Darnold',25,QB,13,441,3024,92,19,(SELECT Player_ID FROM Player_season WHERE Name = 'Sam Darnold' AND Anio = 2019),"1),"
(' Drew Brees',23,QB,11,378,2979,61,27,(SELECT Player_ID FROM Player_season WHERE Name = 'Drew Brees' AND Anio = 2019),"1),"
(' Jacoby Brissett',14,QB,15,447,2942,50,18,(SELECT Player_ID FROM Player_season WHERE Name = 'Jacoby Brissett' AND Anio = 2019),"1),"
(' Ryan Tannehill',31,QB,12,286,2742,91,22,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Tannehill' AND Anio = 2019),"1),"
(' Matthew Stafford',11,QB,8,291,2499,66,19,(SELECT Player_ID FROM Player_season WHERE Name = 'Matthew Stafford' AND Anio = 2019),"1),"
(' Joe Flacco',10,QB,8,262,1822,70,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Joe Flacco' AND Anio = 2019),"1),"
(' Mason Rudolph',27,QB,10,283,1765,76,13,(SELECT Player_ID FROM Player_season WHERE Name = 'Mason Rudolph' AND Anio = 2019),"1),"
(' Case Keenum',32,QB,10,247,1707,69,11,(SELECT Player_ID FROM Player_season WHERE Name = 'Case Keenum' AND Anio = 2019),"1),"
(' Teddy Bridgewater',23,QB,9,196,1384,45,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Teddy Bridgewater' AND Anio = 2019),"1),"
(' Dwayne Haskins',32,QB,9,203,1365,75,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Dwayne Haskins' AND Anio = 2019),"1),"
(' Marcus Mariota',31,QB,7,160,1203,75,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Marcus Mariota' AND Anio = 2019),"1),"
(' Devlin Hodges',27,QB,8,160,1063,79,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Devlin Hodges' AND Anio = 2019),"1),"
(' Eli Manning',24,QB,4,147,1042,55,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Eli Manning' AND Anio = 2019),"1),"
(' Drew Lock',10,QB,5,156,1020,48,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Drew Lock' AND Anio = 2019),"1),"
(' David Blough',11,QB,5,174,984,75,4,(SELECT Player_ID FROM Player_season WHERE Name = 'David Blough' AND Anio = 2019),"1),"
(' Nick Foles',15,QB,4,117,736,39,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Foles' AND Anio = 2019),"1),"
(' Jeff Driskel',11,QB,3,105,685,47,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeff Driskel' AND Anio = 2019),"1),"
(' Matt Moore',16,QB,6,91,659,57,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Moore' AND Anio = 2019),"1),"
(' Matt Schaub',2,QB,6,67,580,35,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Schaub' AND Anio = 2019),"1),"
(' Cam Newton',5,QB,2,89,572,44,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cam Newton' AND Anio = 2019),"1),"
(' Josh Rosen',20,QB,6,109,567,40,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Rosen' AND Anio = 2019),"1),"
(' Brandon Allen',10,QB,3,84,515,75,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Allen' AND Anio = 2019),"1),"
(' Ryan Finley',7,QB,3,87,474,47,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Finley' AND Anio = 2019),"1),"
(' Chase Daniel',6,QB,3,64,435,37,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Chase Daniel' AND Anio = 2019),"1),"
(' Luke Falk',25,QB,3,73,416,36,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Luke Falk' AND Anio = 2019),"1),"
(' Brian Hoyer',14,QB,4,65,372,23,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Brian Hoyer' AND Anio = 2019),"1),"
(' Matt Barkley',4,QB,2,51,359,41,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Barkley' AND Anio = 2019),"1),"
(' Ben Roethlisberger',27,QB,2,62,351,45,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ben Roethlisberger' AND Anio = 2019),"1),"
(' Will Grier',5,QB,2,52,228,28,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Will Grier' AND Anio = 2019),"1),"
(' Robert Griffin III',3,QB,7,38,225,39,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Robert Griffin III' AND Anio = 2019),"1),"
(' AJ McCarron',13,QB,2,37,225,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'AJ McCarron' AND Anio = 2019),"1),"
(' Sean Mannion',21,QB,3,21,126,35,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Sean Mannion' AND Anio = 2019),"1),"
(' Colt McCoy',32,QB,1,27,122,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Colt McCoy' AND Anio = 2019),"1),"
(' Mike Glennon',17,QB,2,10,56,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Glennon' AND Anio = 2019),"1),"
(' Taysom Hill',23,QB,16,6,55,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Taysom Hill' AND Anio = 2019),"1),"
(' Brett Hundley',1,QB,3,11,49,28,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brett Hundley' AND Anio = 2019),"1),"
(' Julian Edelman',22,WR,16,2,47,32,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Julian Edelman' AND Anio = 2019),"1),"
(' Courtland Sutt',10,WR,16,1,38,38,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Courtland Sutt' AND Anio = 2019),"1),"
(' Emmanuel Sanders',10,WR,17,1,35,35,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Emmanuel Sanders' AND Anio = 2019),"1),"
(' James White',22,RB,15,1,35,35,0,(SELECT Player_ID FROM Player_season WHERE Name = 'James White' AND Anio = 2019),"1),"
(' Jaylen Samuels',27,RB,14,5,35,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaylen Samuels' AND Anio = 2019),"1),"
(' Tyrod Taylor',18,QB,8,6,33,14,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyrod Taylor' AND Anio = 2019),"1),"
(' Johnny Hekker',19,P,16,3,28,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Johnny Hekker' AND Anio = 2019),"1),"
(' John Brown',4,WR,15,1,28,28,1,(SELECT Player_ID FROM Player_season WHERE Name = 'John Brown' AND Anio = 2019),"1),"
(' Andy Lee',1,P,15,1,26,26,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andy Lee' AND Anio = 2019),"1),"
(' Alex Erickson',7,WR,16,1,26,26,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Alex Erickson' AND Anio = 2019),"1),"
(' Josh McCown',26,QB,3,5,24,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh McCown' AND Anio = 2019),"1),"
(' Odell Beckham Jr.',8,WR,16,2,20,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Odell Beckham Jr.' AND Anio = 2019),"1),"
(' Albert Wilson',20,WR,13,2,20,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Albert Wilson' AND Anio = 2019),"1),"
(' Danny Amendola',11,WR,15,1,19,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Danny Amendola' AND Anio = 2019),"1),"
(' Ryan Griffin',30,QB,2,4,18,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Griffin' AND Anio = 2019),"1),"
(' Logan Cooke',15,P,16,2,16,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Logan Cooke' AND Anio = 2019),"1),"
(' Dante Pettis',28,WR,11,1,16,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dante Pettis' AND Anio = 2019),"1),"
(' Tim Boyle',12,QB,3,4,15,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tim Boyle' AND Anio = 2019),"1),"
(' Jarrett Stidham',22,QB,3,4,14,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jarrett Stidham' AND Anio = 2019),"1),"
(' Alvin Kamara',23,RB,14,1,13,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Alvin Kamara' AND Anio = 2019),"1),"
(' Michael Palardy',5,P,16,1,12,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Palardy' AND Anio = 2019),"1),"
(' Brett Kern',31,P,16,2,11,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brett Kern' AND Anio = 2019),"1),"
(' Kelvin Harmon',32,WR,16,1,11,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kelvin Harmon' AND Anio = 2019),"1),"
(' DeAndre Hopkins',13,WR,15,2,6,6,1,(SELECT Player_ID FROM Player_season WHERE Name = 'DeAndre Hopkins' AND Anio = 2019),"1),"
(' Andrew Beck',10,FB,16,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andrew Beck' AND Anio = 2019),"1),"
(' Kenjon Barner',2,RB,14,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenjon Barner' AND Anio = 2019),"1),"
(' Blake Bortles',19,QB,3,2,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Blake Bortles' AND Anio = 2019),"1),"
(' Trevor Siemian',25,QB,1,6,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trevor Siemian' AND Anio = 2019),"1),"
(' Alex Tanney',24,QB,1,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Alex Tanney' AND Anio = 2019),"1),"
(' Matt Haack',20,P,16,2,1,1,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Haack' AND Anio = 2019),"1),"
(' Dustin Colquitt',16,P,16,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dustin Colquitt' AND Anio = 2019),"1),"
(' Randall Cobb',9,WR,15,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Randall Cobb' AND Anio = 2019),"1),"
(' Bilal Powell',25,RB,13,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Bilal Powell' AND Anio = 2019),"1),"
(' Josh Gordon',22,WR,11,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Gordon' AND Anio = 2019),"1),"
(' Garrett Gilbert',8,QB,5,3,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Garrett Gilbert' AND Anio = 2019),"1),"
(' David Fales',25,QB,2,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'David Fales' AND Anio = 2019),"1),"
(' Stefon Diggs',21,WR,15,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Stefon Diggs' AND Anio = 2019),"1),"
(' Cooper Kupp',19,WR,16,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cooper Kupp' AND Anio = 2019),"1),"
(' Zach Pascal',14,WR,16,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Pascal' AND Anio = 2019),"1),"
(' Colby Wadman',10,P,16,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Colby Wadman' AND Anio = 2019),"1),"
(' Jake Elliott',26,PK,16,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jake Elliott' AND Anio = 2019),"1),"
(' Kareem Hunt',8,RB,8,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kareem Hunt' AND Anio = 2019),"1),"
(' Christian McCaffrey',5,RB,16,2,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian McCaffrey' AND Anio = 2019),"1),"
(' Preston Williams',20,WR,8,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Preston Williams' AND Anio = 2019),"1),"
(' Steven Sims',32,WR,16,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Steven Sims' AND Anio = 2019),"1),"
(' Sam Koch',3,P,16,1,-2,-2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Sam Koch' AND Anio = 2019),"1),"
(' Michael Thomas ',23,WR,16,149,1725,49,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Thomas ' AND Anio = 2019),"3),"
(' Julio Jones ',2,WR,15,99,1394,54,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Julio Jones ' AND Anio = 2019),"3),"
(' Chris Godwin ',30,WR,14,86,1333,71,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Godwin ' AND Anio = 2019),"3),"
(' Travis Kelce ',16,TE,16,97,1229,47,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Travis Kelce ' AND Anio = 2019),"3),"
(' DeVante Parker ',20,WR,16,72,1202,51,9,(SELECT Player_ID FROM Player_season WHERE Name = 'DeVante Parker ' AND Anio = 2019),"3),"
(' Keenan Allen ',18,WR,16,104,1199,45,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Keenan Allen ' AND Anio = 2019),"3),"
(' Kenny Golladay ',11,WR,16,65,1190,75,11,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenny Golladay ' AND Anio = 2019),"3),"
(' Amari Cooper ',9,WR,16,79,1189,53,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Amari Cooper ' AND Anio = 2019),"3),"
(' DJ Moore ',5,WR,15,87,1175,52,4,(SELECT Player_ID FROM Player_season WHERE Name = 'DJ Moore ' AND Anio = 2019),"3),"
(' Jarvis Landry ',8,WR,16,83,1174,65,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Jarvis Landry ' AND Anio = 2019),"3),"
(' DeAndre Hopkins ',13,WR,15,104,1165,43,7,(SELECT Player_ID FROM Player_season WHERE Name = 'DeAndre Hopkins ' AND Anio = 2019),"3),"
(' Cooper Kupp ',19,WR,16,94,1161,66,10,(SELECT Player_ID FROM Player_season WHERE Name = 'Cooper Kupp ' AND Anio = 2019),"3),"
(' Mike Evans ',30,WR,13,67,1157,67,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Evans ' AND Anio = 2019),"3),"
(' Allen Robinson II',6,WR,16,98,1147,49,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Allen Robinson II' AND Anio = 2019),"3),"
(' Darren Waller ',17,TE,16,90,1145,75,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Darren Waller ' AND Anio = 2019),"3),"
(' Robert Woods ',19,WR,15,90,1134,48,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Robert Woods ' AND Anio = 2019),"3),"
(' Stefon Diggs ',21,WR,15,63,1130,66,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Stefon Diggs ' AND Anio = 2019),"3),"
(' Julian Edelman ',22,WR,16,100,1117,44,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Julian Edelman ' AND Anio = 2019),"3),"
(' Courtland Sutton ',10,WR,16,72,1112,70,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Courtland Sutton ' AND Anio = 2019),"3),"
(' Michael Gallup ',9,WR,14,66,1107,62,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Gallup ' AND Anio = 2019),"3),"
(' John Brown ',4,WR,15,72,1060,53,6,(SELECT Player_ID FROM Player_season WHERE Name = 'John Brown ' AND Anio = 2019),"3),"
(' Tyler Lockett ',29,WR,16,82,1057,44,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Lockett ' AND Anio = 2019),"3),"
(' George Kittle ',28,TE,14,85,1053,61,5,(SELECT Player_ID FROM Player_season WHERE Name = 'George Kittle ' AND Anio = 2019),"3),"
(' A.J. Brown ',31,WR,16,52,1051,91,8,(SELECT Player_ID FROM Player_season WHERE Name = 'A.J. Brown ' AND Anio = 2019),"3),"
(' Tyler Boyd ',7,WR,16,90,1046,47,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Boyd ' AND Anio = 2019),"3),"
(' Odell Beckham Jr.',8,WR,16,74,1035,89,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Odell Beckham Jr.' AND Anio = 2019),"3),"
(' DJ Chark Jr.',15,WR,15,73,1008,69,8,(SELECT Player_ID FROM Player_season WHERE Name = 'DJ Chark Jr.' AND Anio = 2019),"3),"
(' Christian McCaffrey ',5,RB,16,116,1005,28,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian McCaffrey ' AND Anio = 2019),"3),"
(' Mike Williams ',18,WR,15,49,1001,56,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Williams ' AND Anio = 2019),"3),"
(' Davante Adams ',12,WR,12,83,997,58,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Davante Adams ' AND Anio = 2019),"3),"
(' Austin Ekeler ',18,RB,16,92,993,84,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Austin Ekeler ' AND Anio = 2019),"3),"
(' Terry McLaurin ',32,WR,14,58,919,75,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Terry McLaurin ' AND Anio = 2019),"3),"
(' Zach Ertz ',26,TE,15,88,916,30,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Ertz ' AND Anio = 2019),"3),"
(' DK Metcalf ',29,WR,16,58,900,54,7,(SELECT Player_ID FROM Player_season WHERE Name = 'DK Metcalf ' AND Anio = 2019),"3),"
(' Emmanuel Sanders ',10,WR,17,66,869,75,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Emmanuel Sanders ' AND Anio = 2019),"3),"
(' Calvin Ridley ',2,WR,13,63,866,36,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Calvin Ridley ' AND Anio = 2019),"3),"
(' Tyreek Hill ',16,WR,12,58,860,57,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyreek Hill ' AND Anio = 2019),"3),"
(' Mark Andrews ',3,TE,15,64,852,51,10,(SELECT Player_ID FROM Player_season WHERE Name = 'Mark Andrews ' AND Anio = 2019),"3),"
(' Jamison Crowder ',25,WR,16,78,833,41,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamison Crowder ' AND Anio = 2019),"3),"
(' Randall Cobb ',9,WR,15,55,828,59,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Randall Cobb ' AND Anio = 2019),"3),"
(' Larry Fitzgerald ',1,WR,16,75,804,54,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Larry Fitzgerald ' AND Anio = 2019),"3),"
(' Deebo Samuel Sr.',28,WR,15,57,802,42,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Deebo Samuel Sr.' AND Anio = 2019),"3),"
(' Austin Hooper ',2,TE,13,75,787,35,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Austin Hooper ' AND Anio = 2019),"3),"
(' Marvin Jones Jr.',11,WR,13,62,779,47,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Marvin Jones Jr.' AND Anio = 2019),"3),"
(' Robbie Chosen ',25,WR,16,52,779,92,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Robbie Chosen ' AND Anio = 2019),"3),"
(' Cole Beasley ',4,WR,15,67,778,51,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Cole Beasley ' AND Anio = 2019),"3),"
(' Chris Conley ',15,WR,16,47,775,70,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Conley ' AND Anio = 2019),"3),"
(' Darius Slayton ',24,WR,14,48,740,55,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Darius Slayton ' AND Anio = 2019),"3),"
(' James Washington ',27,WR,15,44,735,79,3,(SELECT Player_ID FROM Player_season WHERE Name = 'James Washington ' AND Anio = 2019),"3),"
(' Tyler Higbee ',19,TE,15,69,734,33,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Higbee ' AND Anio = 2019),"3),"
(' Christian Kirk ',1,WR,13,68,709,69,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian Kirk ' AND Anio = 2019),"3),"
(' Jared Cook ',23,TE,14,43,705,61,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Jared Cook ' AND Anio = 2019),"3),"
(' Diontae Johnson ',27,WR,16,59,680,45,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Diontae Johnson ' AND Anio = 2019),"3),"
(' Danny Amendola ',11,WR,15,62,678,47,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Danny Amendola ' AND Anio = 2019),"3),"
(' Golden Tate ',24,WR,11,49,676,64,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Golden Tate ' AND Anio = 2019),"3),"
(' Sammy Watkins ',16,WR,14,52,673,68,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Sammy Watkins ' AND Anio = 2019),"3),"
(' William Fuller V',13,WR,11,49,670,54,3,(SELECT Player_ID FROM Player_season WHERE Name = 'William Fuller V' AND Anio = 2019),"3),"
(' Dede Westbrook ',15,WR,15,66,660,39,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Dede Westbrook ' AND Anio = 2019),"3),"
(' Anthony Miller ',6,WR,16,52,656,35,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Anthony Miller ' AND Anio = 2019),"3),"
(' Hunter Henry ',18,TE,12,55,652,30,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Hunter Henry ' AND Anio = 2019),"3),"
(' Tyrell Williams ',17,WR,14,42,651,46,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyrell Williams ' AND Anio = 2019),"3),"
(' James White ',22,RB,15,72,645,59,5,(SELECT Player_ID FROM Player_season WHERE Name = 'James White ' AND Anio = 2019),"3),"
(' Breshad Perriman ',30,WR,14,36,645,44,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Breshad Perriman ' AND Anio = 2019),"3),"
(' Curtis Samuel ',5,WR,16,54,627,44,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Curtis Samuel ' AND Anio = 2019),"3),"
(' Zach Pascal ',14,WR,16,41,607,37,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Pascal ' AND Anio = 2019),"3),"
(' Dallas Goedert ',26,TE,15,58,607,28,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Dallas Goedert ' AND Anio = 2019),"3),"
(' Hunter Renfrow ',17,WR,13,49,605,65,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Hunter Renfrow ' AND Anio = 2019),"3),"
(' Corey Davis ',31,WR,15,43,601,38,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Corey Davis ' AND Anio = 2019),"3),"
(' Greg Olsen ',5,TE,14,52,597,41,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Greg Olsen ' AND Anio = 2019),"3),"
(' Marquise Brown ',3,WR,14,46,584,83,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Marquise Brown ' AND Anio = 2019),"3),"
(' Brandin Cooks ',19,WR,14,42,583,57,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandin Cooks ' AND Anio = 2019),"3),"
(' Sterling Shepard ',24,WR,10,57,576,36,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Sterling Shepard ' AND Anio = 2019),"3),"
(' Auden Tate ',7,WR,12,40,575,33,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Auden Tate ' AND Anio = 2019),"3),"
(' Mike Gesicki ',20,TE,16,51,570,34,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Gesicki ' AND Anio = 2019),"3),"
(' Noah Fant ',10,TE,16,40,562,75,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Noah Fant ' AND Anio = 2019),"3),"
(' Kenny Stills ',13,WR,13,40,561,45,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenny Stills ' AND Anio = 2019),"3),"
(' JuJu Smith-Schuster ',27,WR,12,42,552,76,3,(SELECT Player_ID FROM Player_season WHERE Name = 'JuJu Smith-Schuster ' AND Anio = 2019),"3),"
(' Mecole Hardman ',16,WR,16,26,538,83,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Mecole Hardman ' AND Anio = 2019),"3),"
(' Alvin Kamara ',23,RB,14,81,533,41,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Alvin Kamara ' AND Anio = 2019),"3),"
(' Jason Witten ',9,TE,16,63,529,33,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Jason Witten ' AND Anio = 2019),"3),"
(' Alex Erickson ',7,WR,16,43,529,52,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Alex Erickson ' AND Anio = 2019),"3),"
(' Leonard Fournette ',15,RB,15,76,522,27,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Leonard Fournette ' AND Anio = 2019),"3),"
(' Mohamed Sanu ',22,WR,15,59,520,28,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Mohamed Sanu ' AND Anio = 2019),"3),"
(' Dalvin Cook ',21,RB,14,53,519,31,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dalvin Cook ' AND Anio = 2019),"3),"
(' Miles Sanders ',26,RB,16,50,509,45,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Miles Sanders ' AND Anio = 2019),"3),"
(' John Ross ',7,WR,8,28,506,66,3,(SELECT Player_ID FROM Player_season WHERE Name = 'John Ross ' AND Anio = 2019),"3),"
(' T.Y. Hilton ',14,WR,10,45,501,35,5,(SELECT Player_ID FROM Player_season WHERE Name = 'T.Y. Hilton ' AND Anio = 2019),"3),"
(' Alshon Jeffery ',26,WR,10,43,490,38,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Alshon Jeffery ' AND Anio = 2019),"3),"
(' Allen Lazard ',12,WR,16,35,477,43,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Allen Lazard ' AND Anio = 2019),"3),"
(' Aaron Jones ',12,RB,16,49,474,67,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Aaron Jones ' AND Anio = 2019),"3),"
(' Evan Engram ',24,TE,8,44,467,75,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Evan Engram ' AND Anio = 2019),"3),"
(' Le'Veon Bell ',25,RB,15,66,461,23,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Le'Veon Bell ' AND Anio = 2019),"3),"
(' O.J. Howard ',30,TE,14,34,459,33,1,(SELECT Player_ID FROM Player_season WHERE Name = 'O.J. Howard ' AND Anio = 2019),"3),"
(' Tarik Cohen ',6,RB,16,79,456,31,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Tarik Cohen ' AND Anio = 2019),"3),"
(' Marquez Valdes-Scantling ',12,WR,16,26,452,74,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Marquez Valdes-Scantling ' AND Anio = 2019),"3),"
(' Demarcus Robinson ',16,WR,16,32,449,44,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Demarcus Robinson ' AND Anio = 2019),"3),"
(' Jack Doyle ',14,TE,16,43,448,23,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Jack Doyle ' AND Anio = 2019),"3),"
(' Jimmy Graham ',12,TE,16,38,447,48,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Jimmy Graham ' AND Anio = 2019),"3),"
(' Russell Gage ',2,WR,16,49,446,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Russell Gage ' AND Anio = 2019),"3),"
(' Jonnu Smith ',31,TE,16,35,439,57,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonnu Smith ' AND Anio = 2019),"3),"
(' Saquon Barkley ',24,RB,13,52,438,65,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Saquon Barkley ' AND Anio = 2019),"3),"
(' Tyler Eifert ',7,TE,16,43,436,27,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Eifert ' AND Anio = 2019),"3),"
(' Demaryius Thomas ',25,WR,11,36,433,47,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Demaryius Thomas ' AND Anio = 2019),"3),"
(' Preston Williams ',20,WR,8,32,428,35,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Preston Williams ' AND Anio = 2019),"3),"
(' Josh Gordon ',22,WR,11,27,426,58,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Gordon ' AND Anio = 2019),"3),"
(' Ted Ginn Jr.',23,WR,16,30,421,45,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Ted Ginn Jr.' AND Anio = 2019),"3),"
(' Ezekiel Elliott ',9,RB,16,54,420,27,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Ezekiel Elliott ' AND Anio = 2019),"3),"
(' Adam Thielen ',21,WR,10,30,418,44,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Adam Thielen ' AND Anio = 2019),"3),"
(' Jordan Akins ',13,TE,16,36,418,53,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Akins ' AND Anio = 2019),"3),"
(' Allen Hurns ',20,WR,14,32,416,27,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Allen Hurns ' AND Anio = 2019),"3),"
(' Devonta Freeman ',2,RB,14,59,410,28,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Devonta Freeman ' AND Anio = 2019),"3),"
(' Duke Johnson ',13,RB,16,44,410,21,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Duke Johnson ' AND Anio = 2019),"3),"
(' Gerald Everett ',19,TE,13,37,408,33,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Gerald Everett ' AND Anio = 2019),"3),"
(' Phillip Dorsett ',22,WR,14,29,397,58,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Phillip Dorsett ' AND Anio = 2019),"3),"
(' Dawson Knox ',4,TE,15,28,388,49,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Dawson Knox ' AND Anio = 2019),"3),"
(' Chris Thompson ',32,RB,11,42,378,39,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Thompson ' AND Anio = 2019),"3),"
(' Eric Ebron ',14,TE,11,31,375,48,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Eric Ebron ' AND Anio = 2019),"3),"
(' Adam Humphries ',31,WR,12,37,374,30,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Adam Humphries ' AND Anio = 2019),"3),"
(' David Johnson ',1,RB,13,36,370,31,4,(SELECT Player_ID FROM Player_season WHERE Name = 'David Johnson ' AND Anio = 2019),"3),"
(' Kyle Rudolph ',21,TE,16,39,367,32,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Rudolph ' AND Anio = 2019),"3),"
(' T.J. Hockenson ',11,TE,12,32,367,39,2,(SELECT Player_ID FROM Player_season WHERE Name = 'T.J. Hockenson ' AND Anio = 2019),"3),"
(' Blake Jarwin ',9,TE,16,31,365,42,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Blake Jarwin ' AND Anio = 2019),"3),"
(' Kelvin Harmon ',32,WR,16,30,365,30,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kelvin Harmon ' AND Anio = 2019),"3),"
(' Nelson Agholor ',26,WR,11,39,363,43,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Nelson Agholor ' AND Anio = 2019),"3),"
(' Keelan Cole Sr.',15,WR,16,24,361,55,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Keelan Cole Sr.' AND Anio = 2019),"3),"
(' Damiere Byrd ',1,WR,11,32,359,58,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Damiere Byrd ' AND Anio = 2019),"3),"
(' Jakobi Meyers ',22,WR,15,26,359,35,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jakobi Meyers ' AND Anio = 2019),"3),"
(' Kendrick Bourne ',28,WR,16,30,358,30,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Kendrick Bourne ' AND Anio = 2019),"3),"
(' Taylor Gabriel ',6,WR,9,29,353,53,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Taylor Gabriel ' AND Anio = 2019),"3),"
(' Albert Wilson ',20,WR,13,43,351,35,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Albert Wilson ' AND Anio = 2019),"3),"
(' Jacob Hollister ',29,TE,11,41,349,22,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Jacob Hollister ' AND Anio = 2019),"3),"
(' Hayden Hurst ',3,TE,16,30,349,61,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Hayden Hurst ' AND Anio = 2019),"3),"
(' Kenyan Drake ',20,RB,14,50,345,26,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenyan Drake ' AND Anio = 2019),"3),"
(' Darren Fells ',13,TE,16,34,341,24,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Darren Fells ' AND Anio = 2019),"3),"
(' Willie Snead IV',3,WR,16,31,339,50,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Willie Snead IV' AND Anio = 2019),"3),"
(' Tajae Sharpe ',31,WR,15,25,329,47,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Tajae Sharpe ' AND Anio = 2019),"3),"
(' Josh Reynolds ',19,WR,16,21,326,31,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Reynolds ' AND Anio = 2019),"3),"
(' Jalen Richard ',17,RB,16,36,323,33,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Richard ' AND Anio = 2019),"3),"
(' Nick Boyle ',3,TE,16,31,321,35,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Boyle ' AND Anio = 2019),"3),"
(' Ryan Griffin ',25,TE,13,34,320,45,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Griffin ' AND Anio = 2019),"3),"
(' Nyheim Hines ',14,RB,16,44,320,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nyheim Hines ' AND Anio = 2019),"3),"
(' Cameron Brate ',30,TE,16,36,311,37,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Cameron Brate ' AND Anio = 2019),"3),"
(' Irv Smith Jr.',21,TE,16,36,311,29,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Irv Smith Jr.' AND Anio = 2019),"3),"
(' Steven Sims ',32,WR,16,34,310,65,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Steven Sims ' AND Anio = 2019),"3),"
(' Ronald Jones ',30,RB,16,31,309,41,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ronald Jones ' AND Anio = 2019),"3),"
(' Jaylen Samuels ',27,RB,14,47,305,27,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaylen Samuels ' AND Anio = 2019),"3),"
(' David Moore ',29,WR,14,17,301,60,2,(SELECT Player_ID FROM Player_season WHERE Name = 'David Moore ' AND Anio = 2019),"3),"
(' Cody Latimer ',24,WR,15,24,300,43,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Cody Latimer ' AND Anio = 2019),"3),"
(' DaeSean Hamilton ',10,WR,16,28,297,28,1,(SELECT Player_ID FROM Player_season WHERE Name = 'DaeSean Hamilton ' AND Anio = 2019),"3),"
(' Jarius Wright ',5,WR,16,28,296,33,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jarius Wright ' AND Anio = 2019),"3),"
(' Melvin Gordon III',18,RB,12,42,296,25,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Melvin Gordon III' AND Anio = 2019),"3),"
(' Bisi Johnson ',21,WR,16,31,294,23,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Bisi Johnson ' AND Anio = 2019),"3),"
(' DeAndre Washington ',17,RB,16,36,292,28,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DeAndre Washington ' AND Anio = 2019),"3),"
(' Geronimo Allison ',12,WR,16,34,287,31,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Geronimo Allison ' AND Anio = 2019),"3),"
(' Joe Mixon ',7,RB,16,35,287,33,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Joe Mixon ' AND Anio = 2019),"3),"
(' Dare Ogunbowale ',30,RB,16,35,286,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dare Ogunbowale ' AND Anio = 2019),"3),"
(' Kareem Hunt ',8,RB,8,37,285,29,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kareem Hunt ' AND Anio = 2019),"3),"
(' Rex Burkhead ',22,RB,13,27,279,32,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Rex Burkhead ' AND Anio = 2019),"3),"
(' Nick Chubb ',8,RB,16,36,278,32,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Chubb ' AND Anio = 2019),"3),"
(' Marcus Johnson ',14,WR,8,17,277,50,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Marcus Johnson ' AND Anio = 2019),"3),"
(' Vance McDonald ',27,TE,14,38,273,22,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Vance McDonald ' AND Anio = 2019),"3),"
(' Seth Roberts ',3,WR,16,21,271,33,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Seth Roberts ' AND Anio = 2019),"3),"
(' Kaden Smith ',24,TE,9,31,268,32,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Kaden Smith ' AND Anio = 2019),"3),"
(' Chris Carson ',29,RB,15,37,266,21,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Carson ' AND Anio = 2019),"3),"
(' Will Dissly ',29,TE,6,23,262,38,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Will Dissly ' AND Anio = 2019),"3),"
(' Marvin Hall ',11,WR,9,7,261,58,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Marvin Hall ' AND Anio = 2019),"3),"
(' Royce Freeman ',10,RB,16,43,256,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Royce Freeman ' AND Anio = 2019),"3),"
(' Greg Ward ',26,WR,7,28,254,38,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Greg Ward ' AND Anio = 2019),"3),"
(' Isaiah McKenzie ',4,WR,15,27,254,46,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Isaiah McKenzie ' AND Anio = 2019),"3),"
(' Keke Coutee ',13,WR,9,22,254,51,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Keke Coutee ' AND Anio = 2019),"3),"
(' Jamaal Williams ',12,RB,14,39,253,17,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamaal Williams ' AND Anio = 2019),"3),"
(' James Conner ',27,RB,10,34,251,26,3,(SELECT Player_ID FROM Player_season WHERE Name = 'James Conner ' AND Anio = 2019),"3),"
(' Mark Ingram II',3,RB,15,26,247,25,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Mark Ingram II' AND Anio = 2019),"3),"
(' Paul Richardson Jr.',32,WR,10,28,245,22,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Paul Richardson Jr.' AND Anio = 2019),"3),"
(' Malik Turner ',29,WR,15,15,245,33,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Malik Turner ' AND Anio = 2019),"3),"
(' Isaiah Ford ',20,WR,8,23,244,28,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Isaiah Ford ' AND Anio = 2019),"3),"
(' Pharoh Cooper ',7,WR,12,25,243,28,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Pharoh Cooper ' AND Anio = 2019),"3),"
(' C.J. Uzomah ',7,TE,16,27,242,36,2,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Uzomah ' AND Anio = 2019),"3),"
(' Jeremy Sprinkle ',32,TE,16,26,241,23,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeremy Sprinkle ' AND Anio = 2019),"3),"
(' Kyle Juszczyk ',28,FB,12,20,239,49,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Juszczyk ' AND Anio = 2019),"3),"
(' Charles Clay ',1,TE,15,18,237,47,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Charles Clay ' AND Anio = 2019),"3),"
(' Latavius Murray ',23,RB,16,34,235,30,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Latavius Murray ' AND Anio = 2019),"3),"
(' Giovani Bernard ',7,RB,16,30,234,35,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Giovani Bernard ' AND Anio = 2019),"3),"
(' Taysom Hill ',23,QB,16,19,234,45,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Taysom Hill ' AND Anio = 2019),"3),"
(' Tre'Quan Smith ',23,WR,11,18,234,32,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Tre'Quan Smith ' AND Anio = 2019),"3),"
(' J.D. McKissic ',11,RB,16,34,233,26,1,(SELECT Player_ID FROM Player_season WHERE Name = 'J.D. McKissic ' AND Anio = 2019),"3),"
(' Ricky Seals-Jones ',8,TE,14,14,229,59,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Ricky Seals-Jones ' AND Anio = 2019),"3),"
(' Josh Hill ',23,TE,16,25,226,29,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Hill ' AND Anio = 2019),"3),"
(' Vyncint Smith ',25,WR,13,17,225,37,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Vyncint Smith ' AND Anio = 2019),"3),"
(' Jaron Brown ',29,WR,14,16,220,48,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaron Brown ' AND Anio = 2019),"3),"
(' Jake Kumerow ',12,WR,14,12,219,49,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jake Kumerow ' AND Anio = 2019),"3),"
(' Tim Patrick ',10,WR,8,16,218,38,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tim Patrick ' AND Anio = 2019),"3),"
(' Zay Jones ',17,WR,15,27,216,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Zay Jones ' AND Anio = 2019),"3),"
(' Delanie Walker ',31,TE,7,21,215,29,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Delanie Walker ' AND Anio = 2019),"3),"
(' Damien Williams ',16,RB,11,30,213,32,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Damien Williams ' AND Anio = 2019),"3),"
(' Todd Gurley II',19,RB,15,31,207,23,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Todd Gurley II' AND Anio = 2019),"3),"
(' Derrick Henry ',31,RB,15,18,206,75,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Derrick Henry ' AND Anio = 2019),"3),"
(' Anthony Firkser ',31,TE,15,14,204,39,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Anthony Firkser ' AND Anio = 2019),"3),"
(' Boston Scott ',26,RB,11,24,204,39,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Boston Scott ' AND Anio = 2019),"3),"
(' Patrick Laird ',20,RB,15,23,204,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Patrick Laird ' AND Anio = 2019),"3),"
(' Maxx Williams ',1,TE,16,15,202,28,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Maxx Williams ' AND Anio = 2019),"3),"
(' Damion Ratley ',8,WR,13,12,200,46,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Damion Ratley ' AND Anio = 2019),"3),"
(' Scotty Miller ',30,WR,10,13,200,48,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Scotty Miller ' AND Anio = 2019),"3),"
(' Trey Quinn ',32,WR,12,26,198,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Trey Quinn ' AND Anio = 2019),"3),"
(' Miles Boykin ',3,WR,16,13,198,50,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Miles Boykin ' AND Anio = 2019),"3),"
(' Phillip Lindsay ',10,RB,16,35,196,36,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Phillip Lindsay ' AND Anio = 2019),"3),"
(' Justin Hardy ',2,WR,16,19,195,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Hardy ' AND Anio = 2019),"3),"
(' Devin Singletary ',4,RB,12,29,194,49,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Devin Singletary ' AND Anio = 2019),"3),"
(' Bennie Fowler ',24,WR,8,23,193,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Bennie Fowler ' AND Anio = 2019),"3),"
(' Andy Isabella ',1,WR,15,9,189,88,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Andy Isabella ' AND Anio = 2019),"3),"
(' KeeSean Johnson ',1,WR,10,21,187,31,1,(SELECT Player_ID FROM Player_season WHERE Name = 'KeeSean Johnson ' AND Anio = 2019),"3),"
(' Marquise Goodwin ',28,WR,9,12,186,38,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Marquise Goodwin ' AND Anio = 2019),"3),"
(' Javon Wims ',6,WR,16,18,186,37,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Javon Wims ' AND Anio = 2019),"3),"
(' David Montgomery ',6,RB,16,25,185,30,1,(SELECT Player_ID FROM Player_season WHERE Name = 'David Montgomery ' AND Anio = 2019),"3),"
(' Laquon Treadwell ',21,WR,13,9,184,58,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Laquon Treadwell ' AND Anio = 2019),"3),"
(' LeSean McCoy ',16,RB,13,28,181,23,1,(SELECT Player_ID FROM Player_season WHERE Name = 'LeSean McCoy ' AND Anio = 2019),"3),"
(' Dontrelle Inman ',18,WR,7,12,181,28,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dontrelle Inman ' AND Anio = 2019),"3),"
(' Raheem Mostert ',28,RB,16,14,180,39,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Raheem Mostert ' AND Anio = 2019),"3),"
(' Tevin Coleman ',28,RB,14,21,180,37,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tevin Coleman ' AND Anio = 2019),"3),"
(' Chester Rogers ',14,WR,12,16,179,27,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Chester Rogers ' AND Anio = 2019),"3),"
(' Tavon Austin ',9,WR,14,13,177,59,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tavon Austin ' AND Anio = 2019),"3),"
(' Foster Moreau ',17,TE,13,21,174,23,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Foster Moreau ' AND Anio = 2019),"3),"
(' Ben Watson ',22,TE,10,17,173,26,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ben Watson ' AND Anio = 2019),"3),"
(' Logan Thomas ',11,TE,16,16,173,17,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Logan Thomas ' AND Anio = 2019),"3),"
(' Kalif Raymond ',31,WR,8,9,170,52,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kalif Raymond ' AND Anio = 2019),"3),"
(' Byron Pringle ',16,WR,16,12,170,28,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Byron Pringle ' AND Anio = 2019),"3),"
(' J.J. Arcega-Whiteside ',26,WR,16,10,169,30,1,(SELECT Player_ID FROM Player_season WHERE Name = 'J.J. Arcega-Whiteside ' AND Anio = 2019),"3),"
(' Rhett Ellison ',24,TE,10,18,167,31,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Rhett Ellison ' AND Anio = 2019),"3),"
(' Darrel Williams ',16,RB,12,15,167,52,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Darrel Williams ' AND Anio = 2019),"3),"
(' Nick Vannett ',29,TE,16,17,166,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Vannett ' AND Anio = 2019),"3),"
(' Duke Williams ',4,WR,4,12,166,41,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Duke Williams ' AND Anio = 2019),"3),"
(' Josh Jacobs ',17,RB,13,20,166,28,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Jacobs ' AND Anio = 2019),"3),"
(' Richie James ',28,WR,16,6,165,57,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Richie James ' AND Anio = 2019),"3),"
(' Dion Lewis ',31,RB,16,25,164,24,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Dion Lewis ' AND Anio = 2019),"3),"
(' Jakeem Grant Sr.',20,WR,10,19,164,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jakeem Grant Sr.' AND Anio = 2019),"3),"
(' DeAndre Carter ',13,WR,16,11,162,46,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DeAndre Carter ' AND Anio = 2019),"3),"
(' DeSean Jackson ',26,WR,3,9,159,53,2,(SELECT Player_ID FROM Player_season WHERE Name = 'DeSean Jackson ' AND Anio = 2019),"3),"
(' Justin Watson ',30,WR,16,15,159,17,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Watson ' AND Anio = 2019),"3),"
(' Marcedes Lewis ',12,TE,16,15,156,25,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Marcedes Lewis ' AND Anio = 2019),"3),"
(' James O'Shaughnessy ',15,TE,5,14,153,35,2,(SELECT Player_ID FROM Player_season WHERE Name = 'James O'Shaughnessy ' AND Anio = 2019),"3),"
(' Demetrius Harris ',8,TE,15,15,149,23,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Demetrius Harris ' AND Anio = 2019),"3),"
(' Jaeden Graham ',2,TE,16,9,149,53,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaeden Graham ' AND Anio = 2019),"3),"
(' C.J. Ham ',21,FB,16,17,149,36,1,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Ham ' AND Anio = 2019),"3),"
(' Ryquell Armstead ',15,RB,16,14,144,31,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryquell Armstead ' AND Anio = 2019),"3),"
(' Adrian Peterson ',32,RB,15,17,142,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Adrian Peterson ' AND Anio = 2019),"3),"
(' Jesse James ',11,TE,16,16,142,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jesse James ' AND Anio = 2019),"3),"
(' Seth DeValve ',15,TE,12,12,140,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Seth DeValve ' AND Anio = 2019),"3),"
(' Ian Thomas ',5,TE,16,16,136,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ian Thomas ' AND Anio = 2019),"3),"
(' Keelan Doss ',17,WR,8,11,133,31,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Keelan Doss ' AND Anio = 2019),"3),"
(' Matt LaCosse ',22,TE,11,13,131,24,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt LaCosse ' AND Anio = 2019),"3),"
(' Parris Campbell ',14,WR,7,18,127,27,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Parris Campbell ' AND Anio = 2019),"3),"
(' Kerryon Johnson ',11,RB,8,10,127,36,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kerryon Johnson ' AND Anio = 2019),"3),"
(' Dan Arnold ',23,TE,5,8,127,37,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Dan Arnold ' AND Anio = 2019),"3),"
(' Mack Hollins ',26,WR,16,10,125,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mack Hollins ' AND Anio = 2019),"3),"
(' T.J. Yeldon ',4,RB,6,13,124,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'T.J. Yeldon ' AND Anio = 2019),"3),"
(' Deon Cain ',27,WR,13,9,124,35,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Deon Cain ' AND Anio = 2019),"3),"
(' Vernon Davis ',32,TE,4,10,123,48,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Vernon Davis ' AND Anio = 2019),"3),"
(' Matt Breida ',28,RB,13,19,120,17,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Breida ' AND Anio = 2019),"3),"
(' Marcell Ateman ',17,WR,11,5,116,36,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marcell Ateman ' AND Anio = 2019),"3),"
(' Peyton Barber ',30,RB,16,16,115,16,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Peyton Barber ' AND Anio = 2019),"3),"
(' Braxton Berrios ',25,WR,16,6,115,69,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Braxton Berrios ' AND Anio = 2019),"3),"
(' Olamide Zaccheaus ',2,WR,10,3,115,93,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Olamide Zaccheaus ' AND Anio = 2019),"3),"
(' Jeff Heuerman ',10,TE,14,14,114,26,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeff Heuerman ' AND Anio = 2019),"3),"
(' Tommy Sweeney ',4,TE,6,8,114,29,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tommy Sweeney ' AND Anio = 2019),"3),"
(' Ryan Izzo ',22,TE,6,6,114,41,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Izzo ' AND Anio = 2019),"3),"
(' Devin Smith ',9,WR,4,5,113,51,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Devin Smith ' AND Anio = 2019),"3),"
(' Brandon Bolden ',22,RB,15,9,111,29,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Bolden ' AND Anio = 2019),"3),"
(' Trevor Davis ',12,WR,14,8,111,28,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trevor Davis ' AND Anio = 2019),"3),"
(' Nick O'Leary ',15,TE,12,13,109,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick O'Leary ' AND Anio = 2019),"3),"
(' Dante Pettis ',28,WR,11,11,109,21,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Dante Pettis ' AND Anio = 2019),"3),"
(' Ty Johnson ',11,RB,16,24,109,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ty Johnson ' AND Anio = 2019),"3),"
(' Derek Carrier ',17,TE,16,13,108,25,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Derek Carrier ' AND Anio = 2019),"3),"
(' Tony Pollard ',9,RB,15,15,107,21,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tony Pollard ' AND Anio = 2019),"3),"
(' Brandon Zylstra ',5,WR,8,8,106,40,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Zylstra ' AND Anio = 2019),"3),"
(' Chase Edmonds ',1,RB,13,12,105,31,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Chase Edmonds ' AND Anio = 2019),"3),"
(' N'Keal Harry ',22,WR,7,12,105,18,2,(SELECT Player_ID FROM Player_season WHERE Name = 'N'Keal Harry ' AND Anio = 2019),"3),"
(' Hale Hentges ',32,TE,11,8,103,24,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Hale Hentges ' AND Anio = 2019),"3),"
(' Wayne Gallman ',24,RB,10,11,102,21,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Wayne Gallman ' AND Anio = 2019),"3),"
(' Frank Gore ',4,RB,16,13,100,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Frank Gore ' AND Anio = 2019),"3),"
(' Robert Tonyan ',12,TE,11,10,100,28,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Robert Tonyan ' AND Anio = 2019),"3),"
(' Danny Vitale ',12,FB,15,7,97,27,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Danny Vitale ' AND Anio = 2019),"3),"
(' Sony Michel ',22,RB,16,12,94,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Sony Michel ' AND Anio = 2019),"3),"
(' Mo Alie-Cox ',14,TE,16,8,93,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mo Alie-Cox ' AND Anio = 2019),"3),"
(' Dontrell Hilliard ',8,RB,14,12,92,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dontrell Hilliard ' AND Anio = 2019),"3),"
(' J.P. Holtz ',32,TE,14,7,91,30,0,(SELECT Player_ID FROM Player_season WHERE Name = 'J.P. Holtz ' AND Anio = 2019),"3),"
(' Ross Dwelley ',28,TE,16,15,91,25,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Ross Dwelley ' AND Anio = 2019),"3),"
(' Christian Blake ',2,WR,9,11,91,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian Blake ' AND Anio = 2019),"3),"
(' MyCole Pruitt ',31,TE,16,6,90,42,1,(SELECT Player_ID FROM Player_season WHERE Name = 'MyCole Pruitt ' AND Anio = 2019),"3),"
(' Ty Montgomery II',25,WR,16,13,90,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ty Montgomery II' AND Anio = 2019),"3),"
(' Andrew Beck ',10,FB,16,9,90,29,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Andrew Beck ' AND Anio = 2019),"3),"
(' Antonio Callaway ',8,WR,4,8,89,41,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Antonio Callaway ' AND Anio = 2019),"3),"
(' Mark Walton ',20,RB,7,15,89,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mark Walton ' AND Anio = 2019),"3),"
(' Ameer Abdullah ',21,RB,16,15,88,16,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ameer Abdullah ' AND Anio = 2019),"3),"
(' Joshua Perkins ',26,TE,5,9,87,24,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Joshua Perkins ' AND Anio = 2019),"3),"
(' Ito Smith ',2,RB,7,11,87,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ito Smith ' AND Anio = 2019),"3),"
(' Jesper Horsted ',6,TE,6,8,87,20,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jesper Horsted ' AND Anio = 2019),"3),"
(' Trey Burton ',6,TE,8,14,84,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trey Burton ' AND Anio = 2019),"3),"
(' Cordarrelle Patterson ',6,RB,16,11,83,33,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cordarrelle Patterson ' AND Anio = 2019),"3),"
(' Rashaad Penny ',29,RB,10,8,83,30,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Rashaad Penny ' AND Anio = 2019),"3),"
(' Marlon Mack ',14,RB,14,14,82,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marlon Mack ' AND Anio = 2019),"3),"
(' Alexander Mattison ',21,RB,13,10,82,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Alexander Mattison ' AND Anio = 2019),"3),"
(' Damion Willis ',7,WR,10,9,82,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Damion Willis ' AND Anio = 2019),"3),"
(' Trent Sherfield Sr.',1,WR,16,4,80,38,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trent Sherfield Sr.' AND Anio = 2019),"3),"
(' Luke Willson ',29,TE,8,8,79,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Luke Willson ' AND Anio = 2019),"3),"
(' Derrius Guice ',32,RB,5,7,79,45,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Derrius Guice ' AND Anio = 2019),"3),"
(' Virgil Green ',18,TE,15,9,78,15,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Virgil Green ' AND Anio = 2019),"3),"
(' C.J. Prosise ',29,RB,9,10,76,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Prosise ' AND Anio = 2019),"3),"
(' KhaDarel Hodge ',8,WR,16,4,76,41,0,(SELECT Player_ID FROM Player_season WHERE Name = 'KhaDarel Hodge ' AND Anio = 2019),"3),"
(' Adam Shaheen ',6,TE,8,9,74,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Adam Shaheen ' AND Anio = 2019),"3),"
(' Daniel Brown ',25,TE,16,7,72,24,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Daniel Brown ' AND Anio = 2019),"3),"
(' Tyler Kroft ',4,TE,11,6,71,20,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Kroft ' AND Anio = 2019),"3),"
(' D'Ernest Johnson ',8,RB,16,6,71,27,0,(SELECT Player_ID FROM Player_season WHERE Name = 'D'Ernest Johnson ' AND Anio = 2019),"3),"
(' Chad Beebe ',21,WR,3,2,70,61,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chad Beebe ' AND Anio = 2019),"3),"
(' Justice Hill ',3,RB,16,8,70,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Justice Hill ' AND Anio = 2019),"3),"
(' Jordan Howard ',26,RB,10,10,69,20,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Howard ' AND Anio = 2019),"3),"
(' Brian Hill ',2,RB,12,10,69,12,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Brian Hill ' AND Anio = 2019),"3),"
(' Riley Ridley ',6,WR,5,6,69,32,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Riley Ridley ' AND Anio = 2019),"3),"
(' Chris Hogan ',5,WR,7,8,67,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Hogan ' AND Anio = 2019),"3),"
(' Blake Bell ',16,TE,15,8,67,30,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Blake Bell ' AND Anio = 2019),"3),"
(' Rico Gafford ',17,CB,4,2,66,49,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Rico Gafford ' AND Anio = 2019),"3),"
(' Geoff Swaim ',15,TE,6,13,65,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Geoff Swaim ' AND Anio = 2019),"3),"
(' Durham Smythe ',20,TE,16,7,65,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Durham Smythe ' AND Anio = 2019),"3),"
(' Wendell Smallwood ',32,RB,15,9,64,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Wendell Smallwood ' AND Anio = 2019),"3),"
(' Robert Foster ',4,WR,13,3,64,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Robert Foster ' AND Anio = 2019),"3),"
(' Kalen Ballage ',20,RB,12,14,63,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kalen Ballage ' AND Anio = 2019),"3),"
(' Tevin Jones ',27,WR,5,4,61,28,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tevin Jones ' AND Anio = 2019),"3),"
(' Chris Lacy ',11,WR,7,3,60,48,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Lacy ' AND Anio = 2019),"3),"
(' Ben Braunecker ',6,TE,11,6,59,18,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ben Braunecker ' AND Anio = 2019),"3),"
(' Jonathan Williams ',14,RB,9,5,59,31,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonathan Williams ' AND Anio = 2019),"3),"
(' Tyler Conklin ',21,TE,15,8,58,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Conklin ' AND Anio = 2019),"3),"
(' Clive Walford ',20,TE,7,4,57,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Clive Walford ' AND Anio = 2019),"3),"
(' Reggie Bonnafon ',5,RB,16,6,57,32,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Reggie Bonnafon ' AND Anio = 2019),"3),"
(' Devontae Booker ',10,RB,16,6,57,25,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Devontae Booker ' AND Anio = 2019),"3),"
(' Antonio Brown ',22,WR,1,4,56,20,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Antonio Brown ' AND Anio = 2019),"3),"
(' Andre Patton ',18,WR,13,6,56,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andre Patton ' AND Anio = 2019),"3),"
(' Travis Homer ',29,RB,16,11,56,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Travis Homer ' AND Anio = 2019),"3),"
(' Rashard Higgins ',8,WR,10,4,55,35,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Rashard Higgins ' AND Anio = 2019),"3),"
(' Khari Blasingame ',31,FB,6,4,54,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Khari Blasingame ' AND Anio = 2019),"3),"
(' Luke Stocker ',2,TE,15,8,53,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Luke Stocker ' AND Anio = 2019),"3),"
(' DeAndrew White ',5,WR,10,4,51,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DeAndrew White ' AND Anio = 2019),"3),"
(' Myles Gaskin ',20,RB,7,7,51,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Myles Gaskin ' AND Anio = 2019),"3),"
(' Ross Travis ',14,TE,3,4,51,25,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ross Travis ' AND Anio = 2019),"3),"
(' Stephen Carlson ',8,TE,9,5,51,21,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Stephen Carlson ' AND Anio = 2019),"3),"
(' Lance Kendricks ',18,TE,12,3,50,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Lance Kendricks ' AND Anio = 2019),"3),"
(' Deon Yelder ',16,TE,9,3,50,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Deon Yelder ' AND Anio = 2019),"3),"
(' Trey Edmunds ',27,RB,11,6,48,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trey Edmunds ' AND Anio = 2019),"3),"
(' Deontay Burnett ',26,WR,1,2,48,41,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Deontay Burnett ' AND Anio = 2019),"3),"
(' Patrick Ricard ',3,FB,16,8,47,10,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Patrick Ricard ' AND Anio = 2019),"3),"
(' Trevon Wesco ',25,TE,16,2,47,32,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trevon Wesco ' AND Anio = 2019),"3),"
(' Cedrick Wilson Jr.',9,WR,6,5,46,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cedrick Wilson Jr.' AND Anio = 2019),"3),"
(' Alexander Hollins ',21,WR,5,2,46,35,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Alexander Hollins ' AND Anio = 2019),"3),"
(' Gus Edwards ',3,RB,16,7,45,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Gus Edwards ' AND Anio = 2019),"3),"
(' Alec Ingold ',17,FB,16,6,44,14,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Alec Ingold ' AND Anio = 2019),"3),"
(' Jordan Wilkins ',14,RB,14,7,43,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Wilkins ' AND Anio = 2019),"3),"
(' Jason Moore ',18,WR,10,2,43,32,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jason Moore ' AND Anio = 2019),"3),"
(' Darwin Thompson ',16,RB,12,9,43,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Darwin Thompson ' AND Anio = 2019),"3),"
(' Carlos Hyde ',13,RB,16,10,42,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Carlos Hyde ' AND Anio = 2019),"3),"
(' Andy Janovich ',10,FB,7,5,42,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andy Janovich ' AND Anio = 2019),"3),"
(' Patrick DiMarco ',4,FB,16,5,41,27,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Patrick DiMarco ' AND Anio = 2019),"3),"
(' David Njoku ',8,TE,4,5,41,18,1,(SELECT Player_ID FROM Player_season WHERE Name = 'David Njoku ' AND Anio = 2019),"3),"
(' TJ Jones ',24,WR,3,3,38,28,1,(SELECT Player_ID FROM Player_season WHERE Name = 'TJ Jones ' AND Anio = 2019),"3),"
(' Geremy Davis ',18,WR,7,3,38,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Geremy Davis ' AND Anio = 2019),"3),"
(' Elandon Roberts ',22,LB,16,1,38,38,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Elandon Roberts ' AND Anio = 2019),"3),"
(' Troy Fumagalli ',10,TE,11,6,38,9,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Troy Fumagalli ' AND Anio = 2019),"3),"
(' Steven Mitchell Jr.',13,WR,3,2,37,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Steven Mitchell Jr.' AND Anio = 2019),"3),"
(' Darrell Henderson Jr.',19,RB,13,4,37,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Darrell Henderson Jr.' AND Anio = 2019),"3),"
(' Zach Line ',23,FB,12,6,36,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Line ' AND Anio = 2019),"3),"
(' J.J. Nelson ',17,WR,2,4,36,29,1,(SELECT Player_ID FROM Player_season WHERE Name = 'J.J. Nelson ' AND Anio = 2019),"3),"
(' Ty Sambrailo ',2,OT,13,1,35,35,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ty Sambrailo ' AND Anio = 2019),"3),"
(' Bobo Wilson ',30,WR,6,3,35,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Bobo Wilson ' AND Anio = 2019),"3),"
(' Ishmael Hyman ',30,WR,2,2,34,31,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ishmael Hyman ' AND Anio = 2019),"3),"
(' Jeff Wilson Jr.',28,RB,10,3,34,25,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeff Wilson Jr.' AND Anio = 2019),"3),"
(' Gunner Olszewski ',22,WR,8,2,34,29,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Gunner Olszewski ' AND Anio = 2019),"3),"
(' Bilal Powell ',25,RB,13,7,33,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Bilal Powell ' AND Anio = 2019),"3),"
(' Jordan Matthews ',26,TE,2,4,33,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Matthews ' AND Anio = 2019),"3),"
(' Derek Watt ',18,FB,16,3,32,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Derek Watt ' AND Anio = 2019),"3),"
(' Devin Funchess ',14,TE,1,3,32,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Devin Funchess ' AND Anio = 2019),"3),"
(' Lee Smith ',4,TE,16,4,31,9,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Lee Smith ' AND Anio = 2019),"3),"
(' Diontae Spencer ',10,WR,16,6,31,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Diontae Spencer ' AND Anio = 2019),"3),"
(' C.J. Board ',15,WR,4,2,31,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Board ' AND Anio = 2019),"3),"
(' Travis Benjamin ',18,WR,5,6,30,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Travis Benjamin ' AND Anio = 2019),"3),"
(' Drew Sample ',7,TE,9,5,30,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Drew Sample ' AND Anio = 2019),"3),"
(' Codey McElroy ',30,TE,1,1,30,30,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Codey McElroy ' AND Anio = 2019),"3),"
(' Cody Core ',24,WR,16,3,28,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cody Core ' AND Anio = 2019),"3),"
(' Pharaoh Brown ',8,TE,9,2,27,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Pharaoh Brown ' AND Anio = 2019),"3),"
(' Ryan Switzer ',27,WR,9,8,27,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Switzer ' AND Anio = 2019),"3),"
(' Cam Sims ',32,WR,7,2,27,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cam Sims ' AND Anio = 2019),"3),"
(' Tanner Hudson ',30,TE,9,2,26,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tanner Hudson ' AND Anio = 2019),"3),"
(' Johnny Mundt ',19,TE,13,4,26,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Johnny Mundt ' AND Anio = 2019),"3),"
(' Russell Shepard ',24,WR,3,3,25,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Russell Shepard ' AND Anio = 2019),"3),"
(' Darren Sproles ',26,RB,6,6,24,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Darren Sproles ' AND Anio = 2019),"3),"
(' Deonte Harty ',23,WR,14,6,24,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Deonte Harty ' AND Anio = 2019),"3),"
(' Nick Bellore ',29,LB,14,2,23,20,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Bellore ' AND Anio = 2019),"3),"
(' Nick Scott ',19,S,16,1,23,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Scott ' AND Anio = 2019),"3),"
(' Devine Ozigbo ',15,RB,10,3,23,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Devine Ozigbo ' AND Anio = 2019),"3),"
(' Benny Snell Jr.',27,RB,13,3,23,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Benny Snell Jr.' AND Anio = 2019),"3),"
(' Michael Crabtree ',1,WR,2,4,22,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Crabtree ' AND Anio = 2019),"3),"
(' Anthony Sherman ',16,FB,16,2,22,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Anthony Sherman ' AND Anio = 2019),"3),"
(' Kenjon Barner ',2,RB,14,6,22,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenjon Barner ' AND Anio = 2019),"3),"
(' Spencer Ware ',16,RB,3,5,22,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Spencer Ware ' AND Anio = 2019),"3),"
(' Mike Davis ',5,RB,12,7,22,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Davis ' AND Anio = 2019),"3),"
(' Da'Mari Scott ',24,WR,5,2,22,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Da'Mari Scott ' AND Anio = 2019),"3),"
(' Justin Jackson ',18,RB,7,9,22,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Jackson ' AND Anio = 2019),"3),"
(' Chris Moore ',3,WR,14,3,21,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Moore ' AND Anio = 2019),"3),"
(' Fred Brown ',10,WR,13,2,21,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Fred Brown ' AND Anio = 2019),"3),"
(' Eric Saubert ',6,TE,2,2,21,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Eric Saubert ' AND Anio = 2019),"3),"
(' Johnny Holton ',27,WR,16,3,21,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Johnny Holton ' AND Anio = 2019),"3),"
(' Andre Roberts ',4,WR,13,3,20,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andre Roberts ' AND Anio = 2019),"3),"
(' Josh Bellamy ',25,WR,7,2,20,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Bellamy ' AND Anio = 2019),"3),"
(' Zach Zenner ',23,RB,4,2,19,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Zenner ' AND Anio = 2019),"3),"
(' David Blough ',11,QB,5,1,19,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'David Blough ' AND Anio = 2019),"3),"
(' Marqise Lee ',15,WR,6,3,18,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marqise Lee ' AND Anio = 2019),"3),"
(' Donte Moncrief ',5,WR,5,4,18,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Donte Moncrief ' AND Anio = 2019),"3),"
(' Tra Carson ',12,RB,3,4,18,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tra Carson ' AND Anio = 2019),"3),"
(' Stanley Morgan Jr.',7,WR,11,3,18,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Stanley Morgan Jr.' AND Anio = 2019),"3),"
(' Darius Jennings ',31,WR,8,2,17,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Darius Jennings ' AND Anio = 2019),"3),"
(' Robert Davis ',26,WR,6,2,17,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Robert Davis ' AND Anio = 2019),"3),"
(' Nick Bawden ',11,FB,10,4,17,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Bawden ' AND Anio = 2019),"3),"
(' Mike Boone ',21,RB,16,3,17,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Boone ' AND Anio = 2019),"3),"
(' Ashton Dulin ',14,WR,13,2,17,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ashton Dulin ' AND Anio = 2019),"3),"
(' Malcolm Brown ',19,RB,14,2,16,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Malcolm Brown ' AND Anio = 2019),"3),"
(' Rashard Davis ',31,WR,1,1,16,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Rashard Davis ' AND Anio = 2019),"3),"
(' Ventell Bryant ',9,WR,12,1,15,15,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ventell Bryant ' AND Anio = 2019),"3),"
(' Michael Walker ',15,WR,7,2,15,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Walker ' AND Anio = 2019),"3),"
(' Josh Oliver ',15,TE,4,3,15,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Oliver ' AND Anio = 2019),"3),"
(' Ryan Grant ',17,WR,2,4,14,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Grant ' AND Anio = 2019),"3),"
(' Troymaine Pope ',18,RB,14,2,14,13,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Troymaine Pope ' AND Anio = 2019),"3),"
(' Mike Thomas ',19,WR,16,2,14,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Thomas ' AND Anio = 2019),"3),"
(' Keith Smith ',2,FB,16,1,13,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Keith Smith ' AND Anio = 2019),"3),"
(' T.J. Logan ',30,RB,12,2,13,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'T.J. Logan ' AND Anio = 2019),"3),"
(' Cethan Carter ',7,TE,15,2,13,8,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Cethan Carter ' AND Anio = 2019),"3),"
(' Cody Hollister ',31,WR,5,2,13,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cody Hollister ' AND Anio = 2019),"3),"
(' Isaac Nauta ',11,TE,6,2,13,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Isaac Nauta ' AND Anio = 2019),"3),"
(' Sean Culkin ',18,TE,4,1,12,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Sean Culkin ' AND Anio = 2019),"3),"
(' Jeff Smith ',25,WR,1,1,12,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeff Smith ' AND Anio = 2019),"3),"
(' Scott Simonson ',24,TE,5,2,11,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Scott Simonson ' AND Anio = 2019),"3),"
(' Chris Manhertz ',5,TE,15,1,11,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Manhertz ' AND Anio = 2019),"3),"
(' Tyler Ervin ',15,RB,10,2,11,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Ervin ' AND Anio = 2019),"3),"
(' Kevin Byard III',31,S,16,1,11,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kevin Byard III' AND Anio = 2019),"3),"
(' John Ursua ',29,WR,3,1,11,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'John Ursua ' AND Anio = 2019),"3),"
(' Antony Auclair ',30,TE,8,1,11,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Antony Auclair ' AND Anio = 2019),"3),"
(' Levine Toilolo ',28,TE,13,2,10,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Levine Toilolo ' AND Anio = 2019),"3),"
(' Taiwan Jones ',13,RB,11,1,9,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Taiwan Jones ' AND Anio = 2019),"3),"
(' Elijhaa Penny ',24,RB,16,2,9,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Elijhaa Penny ' AND Anio = 2019),"3),"
(' Javorius Allen ',24,RB,10,1,9,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Javorius Allen ' AND Anio = 2019),"3),"
(' Ben Koyack ',15,TE,11,1,9,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ben Koyack ' AND Anio = 2019),"3),"
(' Paul Perkins ',11,RB,4,1,9,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Paul Perkins ' AND Anio = 2019),"3),"
(' Austin Carr ',23,WR,6,1,9,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Austin Carr ' AND Anio = 2019),"3),"
(' Kerrith Whyte ',27,RB,6,1,9,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kerrith Whyte ' AND Anio = 2019),"3),"
(' Ricky Ortiz ',23,FB,1,1,8,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ricky Ortiz ' AND Anio = 2019),"3),"
(' Jordan Thomas ',13,TE,5,1,8,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Thomas ' AND Anio = 2019),"3),"
(' Dwayne Harris ',17,WR,3,1,7,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dwayne Harris ' AND Anio = 2019),"3),"
(' Cody Davis ',15,S,16,1,7,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cody Davis ' AND Anio = 2019),"3),"
(' Chris Herndon ',25,TE,1,1,7,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Herndon ' AND Anio = 2019),"3),"
(' Qadree Ollison ',2,RB,8,1,7,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Qadree Ollison ' AND Anio = 2019),"3),"
(' De'Anthony Thomas ',16,WR,14,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'De'Anthony Thomas ' AND Anio = 2019),"3),"
(' Jeff Driskel ',11,QB,3,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeff Driskel ' AND Anio = 2019),"3),"
(' Dwayne Washington ',23,RB,16,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dwayne Washington ' AND Anio = 2019),"3),"
(' Dalton Schultz ',9,TE,16,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dalton Schultz ' AND Anio = 2019),"3),"
(' Deshaun Watson ',13,QB,15,1,6,6,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Deshaun Watson ' AND Anio = 2019),"3),"
(' Jaleel Scott ',3,WR,3,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaleel Scott ' AND Anio = 2019),"3),"
(' Alex Armah ',5,RB,16,2,6,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Alex Armah ' AND Anio = 2019),"3),"
(' Tyrone Swoopes ',29,TE,5,1,5,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyrone Swoopes ' AND Anio = 2019),"3),"
(' Jakob Johnson ',22,FB,4,1,5,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jakob Johnson ' AND Anio = 2019),"3),"
(' Charles Jones ',15,TE,4,1,5,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Charles Jones ' AND Anio = 2019),"3),"
(' Bo Scarbrough ',11,RB,6,1,5,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Bo Scarbrough ' AND Anio = 2019),"3),"
(' Roosevelt Nix ',27,FB,3,2,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Roosevelt Nix ' AND Anio = 2019),"3),"
(' Darrell Daniels ',1,TE,11,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Darrell Daniels ' AND Anio = 2019),"3),"
(' Zach Gentry ',27,TE,4,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Gentry ' AND Anio = 2019),"3),"
(' Krishawn Hogan ',23,WR,8,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Krishawn Hogan ' AND Anio = 2019),"3),"
(' Xavier Grimble ',27,TE,3,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Xavier Grimble ' AND Anio = 2019),"3),"
(' Cyril Grayson Jr.',30,WR,2,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cyril Grayson Jr.' AND Anio = 2019),"3),"
(' Jacoby Brissett ',14,QB,15,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jacoby Brissett ' AND Anio = 2019),"3),"
(' Dennis Kelly ',31,OT,15,1,1,1,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Dennis Kelly ' AND Anio = 2019),"3),"
(' David Quessenberry ',31,OT,4,1,1,1,1,(SELECT Player_ID FROM Player_season WHERE Name = 'David Quessenberry ' AND Anio = 2019),"3),"
(' Senorise Perry ',4,RB,11,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Senorise Perry ' AND Anio = 2019),"3),"
(' Eric Tomlinson ',24,TE,2,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Eric Tomlinson ' AND Anio = 2019),"3),"
(' Dion Dawkins ',4,OT,16,1,1,1,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Dion Dawkins ' AND Anio = 2019),"3),"
(' Wes Hills ',11,RB,1,2,1,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Wes Hills ' AND Anio = 2019),"3),"
(' Darrius Shepherd ',12,WR,6,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Darrius Shepherd ' AND Anio = 2019),"3),"
(' Jonathan Hilliman ',24,RB,3,3,1,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonathan Hilliman ' AND Anio = 2019),"3),"
(' Jason Sanders ',20,PK,16,1,1,1,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jason Sanders ' AND Anio = 2019),"3),"
(' Vita Vea ',30,DT,16,1,1,1,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Vita Vea ' AND Anio = 2019),"3),"
(' Christian Wilkins ',20,DT,16,1,1,1,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian Wilkins ' AND Anio = 2019),"3),"
(' Tyrod Taylor ',18,QB,8,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyrod Taylor ' AND Anio = 2019),"3),"
(' Kirk Cousins ',21,QB,15,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kirk Cousins ' AND Anio = 2019),"3),"
(' Jamize Olawale ',9,FB,16,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamize Olawale ' AND Anio = 2019),"3),"
(' Deon Lacey ',20,LB,16,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Deon Lacey ' AND Anio = 2019),"3),"
(' Michael Burton ',32,FB,10,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Burton ' AND Anio = 2019),"3),"
(' Jay Ajayi ',26,RB,3,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jay Ajayi ' AND Anio = 2019),"3),"
(' George Fant ',29,OT,16,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'George Fant ' AND Anio = 2019),"3),"
(' Justin Hardee Sr.',23,CB,16,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Hardee Sr.' AND Anio = 2019),"3),"
(' Dalyn Dawkins ',31,RB,2,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dalyn Dawkins ' AND Anio = 2019),"3),"
(' Taywan Taylor ',8,WR,3,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Taywan Taylor ' AND Anio = 2019),"3),"
(' Chad Williams ',14,WR,1,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chad Williams ' AND Anio = 2019),"3),"
(' Michael Deiter ',20,G,16,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Deiter ' AND Anio = 2019),"3),"
(' Travis Fulgham ',11,WR,3,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Travis Fulgham ' AND Anio = 2019),"3),"
(' Jace Sternberger ',12,TE,6,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jace Sternberger ' AND Anio = 2019),"3),"
(' Dane Cruikshank ',31,S,16,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dane Cruikshank ' AND Anio = 2019),"3),"
(' Jalen Guyton ',18,WR,3,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Guyton ' AND Anio = 2019),"3),"
(' Lil'Jordan Humphrey ',23,WR,5,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Lil'Jordan Humphrey ' AND Anio = 2019),"3),"
(' David Long Jr.',19,CB,8,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'David Long Jr.' AND Anio = 2019),"3),"
(' Jamal Agnew ',11,WR,13,1,-2,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamal Agnew ' AND Anio = 2019),"3),"
(' Kaleb McGary ',2,OT,16,1,-3,-3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kaleb McGary ' AND Anio = 2019),"3),"
(' Andy Dalton ',7,QB,13,1,-4,-4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andy Dalton ' AND Anio = 2019),"3),"
(' Quincy Enunwa ',25,WR,1,1,-4,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Quincy Enunwa ' AND Anio = 2019),"3),"
(' Garrett Bradbury ',21,C,16,1,-4,-4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Garrett Bradbury ' AND Anio = 2019),"3),"
(' Wyatt Teller ',8,G,15,1,-5,-5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Wyatt Teller ' AND Anio = 2019),"3),"
(' Derrick Henry',31,RB,15,303,1540,74,16,(SELECT Player_ID FROM Player_season WHERE Name = 'Derrick Henry' AND Anio = 2019),"2),"
(' Nick Chubb',8,RB,16,298,1494,88,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Chubb' AND Anio = 2019),"2),"
(' Christian McCaffrey',5,RB,16,287,1387,84,15,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian McCaffrey' AND Anio = 2019),"2),"
(' Ezekiel Elliott',9,RB,16,301,1357,33,12,(SELECT Player_ID FROM Player_season WHERE Name = 'Ezekiel Elliott' AND Anio = 2019),"2),"
(' Chris Carson',29,RB,15,278,1230,59,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Carson' AND Anio = 2019),"2),"
(' Lamar Jackson',3,QB,15,176,1206,47,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Lamar Jackson' AND Anio = 2019),"2),"
(' Leonard Fournette',15,RB,15,265,1152,81,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Leonard Fournette' AND Anio = 2019),"2),"
(' Josh Jacobs',17,RB,13,242,1150,51,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Jacobs' AND Anio = 2019),"2),"
(' Joe Mixon',7,RB,16,278,1137,41,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Joe Mixon' AND Anio = 2019),"2),"
(' Dalvin Cook',21,RB,14,250,1135,75,13,(SELECT Player_ID FROM Player_season WHERE Name = 'Dalvin Cook' AND Anio = 2019),"2),"
(' Marlon Mack',14,RB,14,247,1091,63,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Marlon Mack' AND Anio = 2019),"2),"
(' Aaron Jones',12,RB,16,236,1084,56,16,(SELECT Player_ID FROM Player_season WHERE Name = 'Aaron Jones' AND Anio = 2019),"2),"
(' Carlos Hyde',13,RB,16,245,1070,58,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Carlos Hyde' AND Anio = 2019),"2),"
(' Mark Ingram II',3,RB,15,202,1018,53,10,(SELECT Player_ID FROM Player_season WHERE Name = 'Mark Ingram II' AND Anio = 2019),"2),"
(' Phillip Lindsay',10,RB,16,224,1011,40,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Phillip Lindsay' AND Anio = 2019),"2),"
(' Saquon Barkley',24,RB,13,217,1003,68,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Saquon Barkley' AND Anio = 2019),"2),"
(' Sony Michel',22,RB,16,247,912,26,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Sony Michel' AND Anio = 2019),"2),"
(' Adrian Peterson',32,RB,15,211,898,32,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Adrian Peterson' AND Anio = 2019),"2),"
(' David Montgomery',6,RB,16,242,889,55,6,(SELECT Player_ID FROM Player_season WHERE Name = 'David Montgomery' AND Anio = 2019),"2),"
(' Todd Gurley II',19,RB,15,223,857,25,12,(SELECT Player_ID FROM Player_season WHERE Name = 'Todd Gurley II' AND Anio = 2019),"2),"
(' Miles Sanders',26,RB,16,179,818,65,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Miles Sanders' AND Anio = 2019),"2),"
(' Kenyan Drake',20,RB,14,170,817,80,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenyan Drake' AND Anio = 2019),"2),"
(' Alvin Kamara',23,RB,14,171,797,40,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Alvin Kamara' AND Anio = 2019),"2),"
(' Le'Veon Bell',25,RB,15,245,789,19,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Le'Veon Bell' AND Anio = 2019),"2),"
(' Devin Singletary',4,RB,12,151,775,38,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Devin Singletary' AND Anio = 2019),"2),"
(' Raheem Mostert',28,RB,16,137,772,41,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Raheem Mostert' AND Anio = 2019),"2),"
(' Ronald Jones',30,RB,16,172,724,49,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Ronald Jones' AND Anio = 2019),"2),"
(' Gus Edwards',3,RB,16,133,711,63,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Gus Edwards' AND Anio = 2019),"2),"
(' Devonta Freeman',2,RB,14,184,656,28,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Devonta Freeman' AND Anio = 2019),"2),"
(' Latavius Murray',23,RB,16,146,637,30,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Latavius Murray' AND Anio = 2019),"2),"
(' Matt Breida',28,RB,13,123,623,83,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Breida' AND Anio = 2019),"2),"
(' Melvin Gordon III',18,RB,12,162,612,24,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Melvin Gordon III' AND Anio = 2019),"2),"
(' Frank Gore',4,RB,16,166,599,41,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Frank Gore' AND Anio = 2019),"2),"
(' Austin Ekeler',18,RB,16,132,557,35,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Austin Ekeler' AND Anio = 2019),"2),"
(' Tevin Coleman',28,RB,14,137,544,48,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Tevin Coleman' AND Anio = 2019),"2),"
(' Kyler Murray',1,QB,16,93,544,35,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyler Murray' AND Anio = 2019),"2),"
(' Jordan Howard',26,RB,10,119,525,20,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Howard' AND Anio = 2019),"2),"
(' Josh Allen',4,QB,16,109,510,36,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Allen' AND Anio = 2019),"2),"
(' Damien Williams',16,RB,11,111,498,91,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Damien Williams' AND Anio = 2019),"2),"
(' Royce Freeman',10,RB,16,132,496,26,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Royce Freeman' AND Anio = 2019),"2),"
(' Peyton Barber',30,RB,16,154,470,17,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Peyton Barber' AND Anio = 2019),"2),"
(' LeSean McCoy',16,RB,13,101,465,39,4,(SELECT Player_ID FROM Player_season WHERE Name = 'LeSean McCoy' AND Anio = 2019),"2),"
(' James Conner',27,RB,10,116,464,25,4,(SELECT Player_ID FROM Player_season WHERE Name = 'James Conner' AND Anio = 2019),"2),"
(' Alexander Mattison',21,RB,13,100,462,35,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Alexander Mattison' AND Anio = 2019),"2),"
(' Jamaal Williams',12,RB,14,107,460,45,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamaal Williams' AND Anio = 2019),"2),"
(' Tony Pollard',9,RB,15,86,455,44,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Tony Pollard' AND Anio = 2019),"2),"
(' Benny Snell Jr.',27,RB,13,108,426,23,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Benny Snell Jr.' AND Anio = 2019),"2),"
(' Deshaun Watson',13,QB,15,82,413,30,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Deshaun Watson' AND Anio = 2019),"2),"
(' Duke Johnson',13,RB,16,83,410,40,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Duke Johnson' AND Anio = 2019),"2),"
(' Kerryon Johnson',11,RB,8,113,403,20,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Kerryon Johnson' AND Anio = 2019),"2),"
(' DeAndre Washington',17,RB,16,108,387,36,3,(SELECT Player_ID FROM Player_season WHERE Name = 'DeAndre Washington' AND Anio = 2019),"2),"
(' Bo Scarbrough',11,RB,6,89,377,30,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Bo Scarbrough' AND Anio = 2019),"2),"
(' Rashaad Penny',29,RB,10,65,370,58,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Rashaad Penny' AND Anio = 2019),"2),"
(' David Johnson',1,RB,13,94,345,18,2,(SELECT Player_ID FROM Player_season WHERE Name = 'David Johnson' AND Anio = 2019),"2),"
(' Gardner Minshew',15,QB,14,67,344,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Gardner Minshew' AND Anio = 2019),"2),"
(' Russell Wilson',29,QB,16,75,342,21,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Russell Wilson' AND Anio = 2019),"2),"
(' Brian Hill',2,RB,12,78,323,27,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Brian Hill' AND Anio = 2019),"2),"
(' Jordan Wilkins',14,RB,14,51,307,55,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Wilkins' AND Anio = 2019),"2),"
(' Chase Edmonds',1,RB,13,60,303,37,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Chase Edmonds' AND Anio = 2019),"2),"
(' Rex Burkhead',22,RB,13,65,302,33,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Rex Burkhead' AND Anio = 2019),"2),"
(' Daniel Jones',24,QB,13,45,279,26,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Daniel Jones' AND Anio = 2019),"2),"
(' Dak Prescott',9,QB,16,52,277,42,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Dak Prescott' AND Anio = 2019),"2),"
(' Mike Boone',21,RB,16,49,273,59,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Boone' AND Anio = 2019),"2),"
(' Ty Johnson',11,RB,16,63,273,40,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ty Johnson' AND Anio = 2019),"2),"
(' James White',22,RB,15,67,263,32,1,(SELECT Player_ID FROM Player_season WHERE Name = 'James White' AND Anio = 2019),"2),"
(' Malcolm Brown',19,RB,14,69,255,17,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Malcolm Brown' AND Anio = 2019),"2),"
(' Jameis Winston',30,QB,16,59,250,26,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jameis Winston' AND Anio = 2019),"2),"
(' Boston Scott',26,RB,11,61,245,25,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Boston Scott' AND Anio = 2019),"2),"
(' Derrius Guice',32,RB,5,42,245,60,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Derrius Guice' AND Anio = 2019),"2),"
(' Ryan Fitzpatrick',20,QB,15,54,243,20,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Fitzpatrick' AND Anio = 2019),"2),"
(' Carson Wentz',26,QB,16,62,243,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Carson Wentz' AND Anio = 2019),"2),"
(' Jonathan Williams',14,RB,9,49,235,48,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonathan Williams' AND Anio = 2019),"2),"
(' Bilal Powell',25,RB,13,59,229,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Bilal Powell' AND Anio = 2019),"2),"
(' Jacoby Brissett',14,QB,15,56,228,24,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Jacoby Brissett' AND Anio = 2019),"2),"
(' Justice Hill',3,RB,16,58,225,18,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Justice Hill' AND Anio = 2019),"2),"
(' Patrick Mahomes',16,QB,14,43,218,25,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Patrick Mahomes' AND Anio = 2019),"2),"
(' Tarik Cohen',6,RB,16,64,213,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tarik Cohen' AND Anio = 2019),"2),"
(' Dion Lewis',31,RB,16,54,209,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dion Lewis' AND Anio = 2019),"2),"
(' J.D. McKissic',11,RB,16,38,205,44,0,(SELECT Player_ID FROM Player_season WHERE Name = 'J.D. McKissic' AND Anio = 2019),"2),"
(' Mark Walton',20,RB,7,53,201,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mark Walton' AND Anio = 2019),"2),"
(' Justin Jackson',18,RB,7,29,200,40,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Jackson' AND Anio = 2019),"2),"
(' Nyheim Hines',14,RB,16,52,199,18,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Nyheim Hines' AND Anio = 2019),"2),"
(' Mitchell Trubisky',6,QB,15,48,193,23,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Mitchell Trubisky' AND Anio = 2019),"2),"
(' Ryan Tannehill',31,QB,12,43,185,25,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Tannehill' AND Anio = 2019),"2),"
(' Aaron Rodgers',12,QB,16,46,183,17,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Aaron Rodgers' AND Anio = 2019),"2),"
(' Kareem Hunt',8,RB,8,43,179,16,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Kareem Hunt' AND Anio = 2019),"2),"
(' Jaylen Samuels',27,RB,14,66,175,13,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaylen Samuels' AND Anio = 2019),"2),"
(' Giovani Bernard',7,RB,16,53,170,25,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Giovani Bernard' AND Anio = 2019),"2),"
(' Patrick Laird',20,RB,15,62,168,18,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Patrick Laird' AND Anio = 2019),"2),"
(' Deebo Samuel Sr.',28,WR,15,14,159,31,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Deebo Samuel Sr.' AND Anio = 2019),"2),"
(' Taysom Hill',23,QB,16,27,156,30,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Taysom Hill' AND Anio = 2019),"2),"
(' Jeff Driskel',11,QB,3,22,151,23,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeff Driskel' AND Anio = 2019),"2),"
(' Matt Ryan',2,QB,15,34,147,12,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Ryan' AND Anio = 2019),"2),"
(' Darrell Henderson Jr.',19,RB,13,39,147,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Darrell Henderson Jr.' AND Anio = 2019),"2),"
(' Jalen Richard',17,RB,16,39,145,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Richard' AND Anio = 2019),"2),"
(' Baker Mayfield',8,QB,16,28,141,18,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Baker Mayfield' AND Anio = 2019),"2),"
(' Darrel Williams',16,RB,12,41,141,41,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Darrel Williams' AND Anio = 2019),"2),"
(' Chris Thompson',32,RB,11,37,138,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Thompson' AND Anio = 2019),"2),"
(' Kalen Ballage',20,RB,12,74,135,8,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Kalen Ballage' AND Anio = 2019),"2),"
(' Myles Gaskin',20,RB,7,36,133,27,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Myles Gaskin' AND Anio = 2019),"2),"
(' Curtis Samuel',5,WR,16,19,130,16,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Curtis Samuel' AND Anio = 2019),"2),"
(' Marcus Mariota',31,QB,7,24,129,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marcus Mariota' AND Anio = 2019),"2),"
(' Darwin Thompson',16,RB,12,37,128,12,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Darwin Thompson' AND Anio = 2019),"2),"
(' Kerrith Whyte',27,RB,6,24,122,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kerrith Whyte' AND Anio = 2019),"2),"
(' Reggie Bonnafon',5,RB,16,16,116,59,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Reggie Bonnafon' AND Anio = 2019),"2),"
(' Robert Woods',19,WR,15,17,115,20,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Robert Woods' AND Anio = 2019),"2),"
(' Ameer Abdullah',21,RB,16,23,115,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ameer Abdullah' AND Anio = 2019),"2),"
(' Travis Homer',29,RB,16,18,114,29,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Travis Homer' AND Anio = 2019),"2),"
(' Wayne Gallman',24,RB,10,29,110,22,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Wayne Gallman' AND Anio = 2019),"2),"
(' Ryquell Armstead',15,RB,16,35,108,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryquell Armstead' AND Anio = 2019),"2),"
(' Kyle Allen',5,QB,13,32,106,17,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Allen' AND Anio = 2019),"2),"
(' Ito Smith',2,RB,7,22,106,28,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ito Smith' AND Anio = 2019),"2),"
(' Jeff Wilson Jr.',28,RB,10,27,105,25,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeff Wilson Jr.' AND Anio = 2019),"2),"
(' Cordarrelle Patterson',6,RB,16,17,103,46,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cordarrelle Patterson' AND Anio = 2019),"2),"
(' Ty Montgomery II',25,WR,16,32,103,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ty Montgomery II' AND Anio = 2019),"2),"
(' Dwayne Haskins',32,QB,9,20,101,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dwayne Haskins' AND Anio = 2019),"2),"
(' Christian Kirk',1,WR,13,10,93,28,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian Kirk' AND Anio = 2019),"2),"
(' Trey Edmunds',27,RB,11,22,92,45,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trey Edmunds' AND Anio = 2019),"2),"
(' Jonathan Hilliman',24,RB,3,30,91,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonathan Hilliman' AND Anio = 2019),"2),"
(' Steven Sims',32,WR,16,9,85,65,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Steven Sims' AND Anio = 2019),"2),"
(' Derek Carr',17,QB,16,27,82,15,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Derek Carr' AND Anio = 2019),"2),"
(' Wendell Smallwood',32,RB,15,22,81,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Wendell Smallwood' AND Anio = 2019),"2),"
(' Jonnu Smith',31,TE,16,4,78,57,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonnu Smith' AND Anio = 2019),"2),"
(' Ryan Finley',7,QB,3,10,77,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Finley' AND Anio = 2019),"2),"
(' Andy Dalton',7,QB,13,32,73,17,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Andy Dalton' AND Anio = 2019),"2),"
(' Trevor Davis',12,WR,14,4,73,60,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Trevor Davis' AND Anio = 2019),"2),"
(' Sterling Shepard',24,WR,10,6,72,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Sterling Shepard' AND Anio = 2019),"2),"
(' C.J. Prosise',29,RB,9,23,72,17,1,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Prosise' AND Anio = 2019),"2),"
(' Drew Lock',10,QB,5,18,72,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Drew Lock' AND Anio = 2019),"2),"
(' Robert Griffin III',3,QB,7,20,70,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Robert Griffin III' AND Anio = 2019),"2),"
(' Brandon Bolden',22,RB,15,15,68,21,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Bolden' AND Anio = 2019),"2),"
(' Devlin Hodges',27,QB,8,21,68,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Devlin Hodges' AND Anio = 2019),"2),"
(' Darren Sproles',26,RB,6,17,66,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Darren Sproles' AND Anio = 2019),"2),"
(' Matthew Stafford',11,QB,8,20,66,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Matthew Stafford' AND Anio = 2019),"2),"
(' Kirk Cousins',21,QB,15,31,63,14,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kirk Cousins' AND Anio = 2019),"2),"
(' T.J. Yeldon',4,RB,6,17,63,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'T.J. Yeldon' AND Anio = 2019),"2),"
(' Anthony Levine Sr.',3,S,16,2,62,60,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Anthony Levine Sr.' AND Anio = 2019),"2),"
(' Jimmy Garoppolo',28,QB,16,46,62,11,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jimmy Garoppolo' AND Anio = 2019),"2),"
(' Sam Darnold',25,QB,13,33,62,24,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Sam Darnold' AND Anio = 2019),"2),"
(' Stefon Diggs',21,WR,15,5,61,27,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Stefon Diggs' AND Anio = 2019),"2),"
(' Dwayne Washington',23,RB,16,8,60,31,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dwayne Washington' AND Anio = 2019),"2),"
(' A.J. Brown',31,WR,16,3,60,49,1,(SELECT Player_ID FROM Player_season WHERE Name = 'A.J. Brown' AND Anio = 2019),"2),"
(' Brandin Cooks',19,WR,14,6,52,27,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandin Cooks' AND Anio = 2019),"2),"
(' Vyncint Smith',25,WR,13,3,52,20,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Vyncint Smith' AND Anio = 2019),"2),"
(' Spencer Ware',16,RB,3,17,51,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Spencer Ware' AND Anio = 2019),"2),"
(' Qadree Ollison',2,RB,8,22,50,6,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Qadree Ollison' AND Anio = 2019),"2),"
(' Dontrell Hilliard',8,RB,14,13,49,11,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Dontrell Hilliard' AND Anio = 2019),"2),"
(' Isaiah McKenzie',4,WR,15,8,49,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Isaiah McKenzie' AND Anio = 2019),"2),"
(' N'Keal Harry',22,WR,7,5,49,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'N'Keal Harry' AND Anio = 2019),"2),"
(' Tra Carson',12,RB,3,18,48,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tra Carson' AND Anio = 2019),"2),"
(' Tavon Austin',9,WR,14,6,47,20,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tavon Austin' AND Anio = 2019),"2),"
(' Albert Wilson',20,WR,13,5,45,28,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Albert Wilson' AND Anio = 2019),"2),"
(' C.J. Anderson',11,RB,2,16,43,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Anderson' AND Anio = 2019),"2),"
(' Mason Rudolph',27,QB,10,21,42,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mason Rudolph' AND Anio = 2019),"2),"
(' Brett Hundley',1,QB,3,7,41,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brett Hundley' AND Anio = 2019),"2),"
(' Diontae Johnson',27,WR,16,4,41,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Diontae Johnson' AND Anio = 2019),"2),"
(' Taiwan Jones',13,RB,11,9,40,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Taiwan Jones' AND Anio = 2019),"2),"
(' Jared Goff',19,QB,16,33,40,8,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jared Goff' AND Anio = 2019),"2),"
(' DJ Moore',5,WR,15,6,40,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DJ Moore' AND Anio = 2019),"2),"
(' AJ McCarron',13,QB,2,5,39,18,1,(SELECT Player_ID FROM Player_season WHERE Name = 'AJ McCarron' AND Anio = 2019),"2),"
(' Brandon Allen',10,QB,3,10,39,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Allen' AND Anio = 2019),"2),"
(' Elijhaa Penny',24,RB,16,15,39,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Elijhaa Penny' AND Anio = 2019),"2),"
(' Javorius Allen',24,RB,10,10,36,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Javorius Allen' AND Anio = 2019),"2),"
(' Tom Brady',22,QB,16,26,34,17,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Tom Brady' AND Anio = 2019),"2),"
(' Marshawn Lynch',29,RB,1,12,34,15,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Marshawn Lynch' AND Anio = 2019),"2),"
(' Parris Campbell',14,WR,7,4,34,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Parris Campbell' AND Anio = 2019),"2),"
(' Calvin Ridley',2,WR,13,2,34,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Calvin Ridley' AND Anio = 2019),"2),"
(' Alex Erickson',7,WR,16,5,33,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Alex Erickson' AND Anio = 2019),"2),"
(' Teddy Bridgewater',23,QB,9,28,31,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Teddy Bridgewater' AND Anio = 2019),"2),"
(' David Blough',11,QB,5,8,31,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'David Blough' AND Anio = 2019),"2),"
(' Deonte Harty',23,WR,14,4,31,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Deonte Harty' AND Anio = 2019),"2),"
(' Jay Ajayi',26,RB,3,10,30,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jay Ajayi' AND Anio = 2019),"2),"
(' Philip Rivers',18,QB,16,12,29,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Philip Rivers' AND Anio = 2019),"2),"
(' Paul Perkins',11,RB,4,12,29,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Paul Perkins' AND Anio = 2019),"2),"
(' Robert Foster',4,WR,13,2,29,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Robert Foster' AND Anio = 2019),"2),"
(' Kenjon Barner',2,RB,14,4,28,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenjon Barner' AND Anio = 2019),"2),"
(' Julian Edelman',22,WR,16,8,27,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Julian Edelman' AND Anio = 2019),"2),"
(' Derek Carrier',17,TE,16,1,27,27,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Derek Carrier' AND Anio = 2019),"2),"
(' Mike Davis',5,RB,12,13,27,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Davis' AND Anio = 2019),"2),"
(' Devine Ozigbo',15,RB,10,9,27,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Devine Ozigbo' AND Anio = 2019),"2),"
(' Dede Westbrook',15,WR,15,5,27,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dede Westbrook' AND Anio = 2019),"2),"
(' Dalyn Dawkins',31,RB,2,11,26,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dalyn Dawkins' AND Anio = 2019),"2),"
(' David Moore',29,WR,14,3,25,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'David Moore' AND Anio = 2019),"2),"
(' Nick Foles',15,QB,4,4,23,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Foles' AND Anio = 2019),"2),"
(' Tyler Boyd',7,WR,16,4,23,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Boyd' AND Anio = 2019),"2),"
(' Josh Reynolds',19,WR,16,5,23,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Reynolds' AND Anio = 2019),"2),"
(' Tyreek Hill',16,WR,12,8,23,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyreek Hill' AND Anio = 2019),"2),"
(' George Kittle',28,TE,14,5,22,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'George Kittle' AND Anio = 2019),"2),"
(' Will Grier',5,QB,2,7,22,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Will Grier' AND Anio = 2019),"2),"
(' Phillip Dorsett',22,WR,14,3,21,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Phillip Dorsett' AND Anio = 2019),"2),"
(' Wes Hills',11,RB,1,10,21,15,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Wes Hills' AND Anio = 2019),"2),"
(' Allen Lazard',12,WR,16,1,21,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Allen Lazard' AND Anio = 2019),"2),"
(' D'Ernest Johnson',8,RB,16,4,21,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'D'Ernest Johnson' AND Anio = 2019),"2),"
(' Joe Flacco',10,QB,8,12,20,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Joe Flacco' AND Anio = 2019),"2),"
(' Zach Line',23,FB,12,7,20,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Line' AND Anio = 2019),"2),"
(' Bennie Fowler',24,WR,8,1,20,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Bennie Fowler' AND Anio = 2019),"2),"
(' Taylor Gabriel',6,WR,9,3,20,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Taylor Gabriel' AND Anio = 2019),"2),"
(' Troymaine Pope',18,RB,14,10,20,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Troymaine Pope' AND Anio = 2019),"2),"
(' DJ Chark Jr.',15,WR,15,2,20,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DJ Chark Jr.' AND Anio = 2019),"2),"
(' Ted Ginn Jr.',23,WR,16,3,18,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ted Ginn Jr.' AND Anio = 2019),"2),"
(' DeAndre Hopkins',13,WR,15,2,18,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DeAndre Hopkins' AND Anio = 2019),"2),"
(' Chester Rogers',14,WR,12,1,18,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chester Rogers' AND Anio = 2019),"2),"
(' Dare Ogunbowale',30,RB,16,11,17,12,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Dare Ogunbowale' AND Anio = 2019),"2),"
(' Courtland Sutton',10,WR,16,3,17,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Courtland Sutton' AND Anio = 2019),"2),"
(' Alec Ingold',17,FB,16,10,17,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Alec Ingold' AND Anio = 2019),"2),"
(' C.J. Ham',21,FB,16,7,17,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Ham' AND Anio = 2019),"2),"
(' Mecole Hardman',16,WR,16,4,17,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mecole Hardman' AND Anio = 2019),"2),"
(' Golden Tate',24,WR,11,1,16,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Golden Tate' AND Anio = 2019),"2),"
(' Keenan Allen',18,WR,16,3,16,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Keenan Allen' AND Anio = 2019),"2),"
(' Breshad Perriman',30,WR,14,2,16,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Breshad Perriman' AND Anio = 2019),"2),"
(' Zach Pascal',14,WR,16,2,16,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Pascal' AND Anio = 2019),"2),"
(' Samaje Perine',20,RB,1,5,16,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Samaje Perine' AND Anio = 2019),"2),"
(' Scotty Miller',30,WR,10,2,16,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Scotty Miller' AND Anio = 2019),"2),"
(' Marquise Goodwin',28,WR,9,1,15,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marquise Goodwin' AND Anio = 2019),"2),"
(' Andy Isabella',1,WR,15,4,15,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andy Isabella' AND Anio = 2019),"2),"
(' Colt McCoy',32,QB,1,2,14,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Colt McCoy' AND Anio = 2019),"2),"
(' Keke Coutee',13,WR,9,2,14,10,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Keke Coutee' AND Anio = 2019),"2),"
(' Josh Rosen',20,QB,6,3,13,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Rosen' AND Anio = 2019),"2),"
(' Case Keenum',32,QB,10,9,12,9,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Case Keenum' AND Anio = 2019),"2),"
(' Sammy Watkins',16,WR,14,2,12,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Sammy Watkins' AND Anio = 2019),"2),"
(' Russell Gage',2,WR,16,4,12,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Russell Gage' AND Anio = 2019),"2),"
(' Damien Harris',22,RB,2,4,12,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Damien Harris' AND Anio = 2019),"2),"
(' Josh Adams',25,RB,3,8,12,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Adams' AND Anio = 2019),"2),"
(' Randall Cobb',9,WR,15,3,11,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Randall Cobb' AND Anio = 2019),"2),"
(' Mohamed Sanu',22,WR,15,3,11,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mohamed Sanu' AND Anio = 2019),"2),"
(' Isaiah Ford',20,WR,8,1,11,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Isaiah Ford' AND Anio = 2019),"2),"
(' Dexter Williams',12,RB,4,5,11,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dexter Williams' AND Anio = 2019),"2),"
(' John Franklin',30,WR,1,1,11,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'John Franklin' AND Anio = 2019),"2),"
(' DK Metcalf',29,WR,16,2,11,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DK Metcalf' AND Anio = 2019),"2),"
(' Alex Armah',5,RB,16,6,11,4,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Alex Armah' AND Anio = 2019),"2),"
(' Odell Beckham Jr.',8,WR,16,3,10,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Odell Beckham Jr.' AND Anio = 2019),"2),"
(' Jarvis Landry',8,WR,16,1,10,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jarvis Landry' AND Anio = 2019),"2),"
(' Tyler Ervin',15,RB,10,1,10,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Ervin' AND Anio = 2019),"2),"
(' Derek Watt',18,FB,16,7,10,3,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Derek Watt' AND Anio = 2019),"2),"
(' T.J. Logan',30,RB,12,3,10,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'T.J. Logan' AND Anio = 2019),"2),"
(' Buddy Howell',13,RB,16,5,10,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Buddy Howell' AND Anio = 2019),"2),"
(' Anthony Sherman',16,FB,16,4,9,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Anthony Sherman' AND Anio = 2019),"2),"
(' Josh Ferguson',32,RB,2,3,9,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Ferguson' AND Anio = 2019),"2),"
(' Marquez Valdes-Scantling',12,WR,16,2,9,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marquez Valdes-Scantling' AND Anio = 2019),"2),"
(' Johnny Holton',27,WR,16,1,9,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Johnny Holton' AND Anio = 2019),"2),"
(' Jamal Agnew',11,WR,13,1,9,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamal Agnew' AND Anio = 2019),"2),"
(' Devontae Booker',10,RB,16,2,9,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Devontae Booker' AND Anio = 2019),"2),"
(' Jordan Scarlett',5,RB,9,4,9,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Scarlett' AND Anio = 2019),"2),"
(' John Kelly Jr.',19,RB,4,3,9,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'John Kelly Jr.' AND Anio = 2019),"2),"
(' Dawson Knox',4,TE,15,1,9,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dawson Knox' AND Anio = 2019),"2),"
(' Keith Smith',2,FB,16,5,8,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Keith Smith' AND Anio = 2019),"2),"
(' Chris Godwin',30,WR,14,1,8,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Godwin' AND Anio = 2019),"2),"
(' Ryan Nall',6,FB,8,2,8,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Nall' AND Anio = 2019),"2),"
(' Eli Manning',24,QB,4,4,7,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Eli Manning' AND Anio = 2019),"2),"
(' Ben Roethlisberger',27,QB,2,1,7,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ben Roethlisberger' AND Anio = 2019),"2),"
(' Andre Roberts',4,WR,13,1,7,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andre Roberts' AND Anio = 2019),"2),"
(' Tyrod Taylor',18,QB,8,10,7,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyrod Taylor' AND Anio = 2019),"2),"
(' Patrick DiMarco',4,FB,16,3,7,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Patrick DiMarco' AND Anio = 2019),"2),"
(' Kyle Juszczyk',28,FB,12,3,7,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Juszczyk' AND Anio = 2019),"2),"
(' John Brown',4,WR,15,2,7,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'John Brown' AND Anio = 2019),"2),"
(' Marvin Hall',11,WR,9,1,7,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marvin Hall' AND Anio = 2019),"2),"
(' Nelson Agholor',26,WR,11,2,7,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nelson Agholor' AND Anio = 2019),"2),"
(' Evan Engram',24,TE,8,3,7,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Evan Engram' AND Anio = 2019),"2),"
(' Geronimo Allison',12,WR,16,1,7,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Geronimo Allison' AND Anio = 2019),"2),"
(' Will Dissly',29,TE,6,1,7,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Will Dissly' AND Anio = 2019),"2),"
(' Tony Brooks-James',27,RB,3,8,7,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tony Brooks-James' AND Anio = 2019),"2),"
(' Chase Daniel',6,QB,3,6,6,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chase Daniel' AND Anio = 2019),"2),"
(' Adam Thielen',21,WR,10,4,6,3,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Adam Thielen' AND Anio = 2019),"2),"
(' Diontae Spencer',10,WR,16,3,6,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Diontae Spencer' AND Anio = 2019),"2),"
(' Amari Cooper',9,WR,16,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Amari Cooper' AND Anio = 2019),"2),"
(' Keelan Cole Sr.',15,WR,16,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Keelan Cole Sr.' AND Anio = 2019),"2),"
(' Nick Scott',19,S,16,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Scott' AND Anio = 2019),"2),"
(' Bisi Johnson',21,WR,16,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Bisi Johnson' AND Anio = 2019),"2),"
(' De'Lance Turner',20,RB,8,4,6,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'De'Lance Turner' AND Anio = 2019),"2),"
(' Antonio Brown',22,WR,1,1,5,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Antonio Brown' AND Anio = 2019),"2),"
(' Colin Jones',5,S,16,1,5,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Colin Jones' AND Anio = 2019),"2),"
(' De'Anthony Thomas',16,WR,14,2,5,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'De'Anthony Thomas' AND Anio = 2019),"2),"
(' Darren Waller',17,TE,16,2,5,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Darren Waller' AND Anio = 2019),"2),"
(' Jakeem Grant Sr.',20,WR,10,4,5,7,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jakeem Grant Sr.' AND Anio = 2019),"2),"
(' Greg Ward',26,WR,7,1,5,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Greg Ward' AND Anio = 2019),"2),"
(' Da'Mari Scott',24,WR,5,1,5,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Da'Mari Scott' AND Anio = 2019),"2),"
(' Alfred Morris',1,RB,1,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Alfred Morris' AND Anio = 2019),"2),"
(' Travis Kelce',16,TE,16,1,4,4,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Travis Kelce' AND Anio = 2019),"2),"
(' Clive Walford',20,TE,7,0,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Clive Walford' AND Anio = 2019),"2),"
(' Robbie Chosen',25,WR,16,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Robbie Chosen' AND Anio = 2019),"2),"
(' Jamison Crowder',25,WR,16,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamison Crowder' AND Anio = 2019),"2),"
(' Cooper Kupp',19,WR,16,2,4,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cooper Kupp' AND Anio = 2019),"2),"
(' John Ross',7,WR,8,3,4,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'John Ross' AND Anio = 2019),"2),"
(' Erik Harris',17,S,16,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Erik Harris' AND Anio = 2019),"2),"
(' James Develin',22,FB,2,2,3,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'James Develin' AND Anio = 2019),"2),"
(' Senorise Perry',4,RB,11,3,3,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Senorise Perry' AND Anio = 2019),"2),"
(' Danny Vitale',12,FB,15,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Danny Vitale' AND Anio = 2019),"2),"
(' Zay Jones',17,WR,15,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Zay Jones' AND Anio = 2019),"2),"
(' KeeSean Johnson',1,WR,10,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'KeeSean Johnson' AND Anio = 2019),"2),"
(' Andrew Beck',10,FB,16,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andrew Beck' AND Anio = 2019),"2),"
(' Brian Hoyer',14,QB,4,8,2,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brian Hoyer' AND Anio = 2019),"2),"
(' Alshon Jeffery',26,WR,10,1,2,2,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Alshon Jeffery' AND Anio = 2019),"2),"
(' Vance McDonald',27,TE,14,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Vance McDonald' AND Anio = 2019),"2),"
(' Allen Robinson II',6,WR,16,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Allen Robinson II' AND Anio = 2019),"2),"
(' Willie Snead IV',3,WR,16,2,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Willie Snead IV' AND Anio = 2019),"2),"
(' Matt Haack',20,P,16,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Haack' AND Anio = 2019),"2),"
(' Mike Williams',18,WR,15,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Williams' AND Anio = 2019),"2),"
(' Pharoh Cooper',7,WR,12,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Pharoh Cooper' AND Anio = 2019),"2),"
(' Trevon Wesco',25,TE,16,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trevon Wesco' AND Anio = 2019),"2),"
(' Josh Gordon',22,WR,11,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Gordon' AND Anio = 2019),"2),"
(' Marqise Lee',15,WR,6,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marqise Lee' AND Anio = 2019),"2),"
(' Adam Humphries',31,WR,12,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Adam Humphries' AND Anio = 2019),"2),"
(' Andy Janovich',10,FB,7,1,1,1,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Andy Janovich' AND Anio = 2019),"2),"
(' Trace McSorley',3,QB,1,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trace McSorley' AND Anio = 2019),"2),"
(' Brett Kern',31,P,16,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brett Kern' AND Anio = 2019),"2),"
(' Marvin Jones Jr.',11,WR,13,2,0,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marvin Jones Jr.' AND Anio = 2019),"2),"
(' Mike Glennon',17,QB,2,2,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Glennon' AND Anio = 2019),"2),"
(' Paul Richardson Jr.',32,WR,10,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Paul Richardson Jr.' AND Anio = 2019),"2),"
(' Chris Moore',3,WR,14,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Moore' AND Anio = 2019),"2),"
(' Quenton Nelson',14,G,16,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Quenton Nelson' AND Anio = 2019),"2),"
(' Gerald Everett',19,TE,13,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Gerald Everett' AND Anio = 2019),"2),"
(' Matt Moore',16,QB,6,5,-1,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Moore' AND Anio = 2019),"2),"
(' Ryan Griffin',30,QB,2,4,-1,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Griffin' AND Anio = 2019),"2),"
(' Anthony Miller',6,WR,16,1,-1,-1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Anthony Miller' AND Anio = 2019),"2),"
(' Richie James',28,WR,16,2,-1,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Richie James' AND Anio = 2019),"2),"
(' Josh McCown',26,QB,3,2,-2,-1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh McCown' AND Anio = 2019),"2),"
(' Cam Newton',5,QB,2,5,-2,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cam Newton' AND Anio = 2019),"2),"
(' Zach Zenner',23,RB,4,3,-2,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Zenner' AND Anio = 2019),"2),"
(' Jarrett Stidham',22,QB,3,2,-2,-1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jarrett Stidham' AND Anio = 2019),"2),"
(' Matt Schaub',2,QB,6,3,-3,-1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Schaub' AND Anio = 2019),"2),"
(' Julio Jones',2,WR,15,2,-3,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Julio Jones' AND Anio = 2019),"2),"
(' Garrett Gilbert',8,QB,5,3,-3,-1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Garrett Gilbert' AND Anio = 2019),"2),"
(' Nick Mullens',28,QB,1,3,-3,-1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Mullens' AND Anio = 2019),"2),"
(' Drew Brees',23,QB,11,9,-4,2,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Drew Brees' AND Anio = 2019),"2),"
(' Matt Barkley',4,QB,2,2,-4,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Barkley' AND Anio = 2019),"2),"
(' Bryan Anger',13,P,14,1,-5,-5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Bryan Anger' AND Anio = 2019),"2),"
(' Sean Mannion',21,QB,3,6,-5,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Sean Mannion' AND Anio = 2019),"2),"
(' Tyler Lockett',29,WR,16,4,-5,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Lockett' AND Anio = 2019),"2),"
(' Kalif Raymond',31,WR,8,1,-5,-5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kalif Raymond' AND Anio = 2019),"2),"
(' Jarius Wright',5,WR,16,1,-7,-7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jarius Wright' AND Anio = 2019),"2),"
(' Tim Boyle',12,QB,3,5,-7,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tim Boyle' AND Anio = 2019),"2),"
(' Jordan Berry',27,P,16,2,-8,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Berry' AND Anio = 2019),"2),"
(' Blake Bortles',19,QB,3,2,-9,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Blake Bortles' AND Anio = 2019),"2),"
(' Michael Thomas',23,WR,16,1,-9,-9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Thomas' AND Anio = 2019),"2),"
(' Noah Fant',10,TE,16,3,-12,-2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Noah Fant' AND Anio = 2019),"2),"
(' Deshaun Watson',13,QB,16,544,4823,77,33,(SELECT Player_ID FROM Player_season WHERE Name = 'Deshaun Watson' AND Anio = 2020),"1),"
(' Patrick Mahomes',16,QB,15,588,4740,75,38,(SELECT Player_ID FROM Player_season WHERE Name = 'Patrick Mahomes' AND Anio = 2020),"1),"
(' Tom Brady',30,QB,16,610,4633,50,40,(SELECT Player_ID FROM Player_season WHERE Name = 'Tom Brady' AND Anio = 2020),"1),"
(' Matt Ryan',2,QB,16,626,4581,63,26,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Ryan' AND Anio = 2020),"1),"
(' Josh Allen',4,QB,16,572,4544,55,37,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Allen' AND Anio = 2020),"1),"
(' Justin Herbert',18,QB,15,595,4336,72,31,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Herbert' AND Anio = 2020),"1),"
(' Aaron Rodgers',12,QB,16,526,4299,78,48,(SELECT Player_ID FROM Player_season WHERE Name = 'Aaron Rodgers' AND Anio = 2020),"1),"
(' Kirk Cousins',21,QB,16,516,4265,71,35,(SELECT Player_ID FROM Player_season WHERE Name = 'Kirk Cousins' AND Anio = 2020),"1),"
(' Russell Wilson',29,QB,16,558,4212,62,40,(SELECT Player_ID FROM Player_season WHERE Name = 'Russell Wilson' AND Anio = 2020),"1),"
(' Philip Rivers',14,QB,16,543,4169,55,24,(SELECT Player_ID FROM Player_season WHERE Name = 'Philip Rivers' AND Anio = 2020),"1),"
(' Derek Carr',17,QB,16,517,4103,85,27,(SELECT Player_ID FROM Player_season WHERE Name = 'Derek Carr' AND Anio = 2020),"1),"
(' Matthew Stafford',11,QB,16,528,4084,73,26,(SELECT Player_ID FROM Player_season WHERE Name = 'Matthew Stafford' AND Anio = 2020),"1),"
(' Kyler Murray',1,QB,16,558,3971,80,26,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyler Murray' AND Anio = 2020),"1),"
(' Jared Goff',19,QB,15,552,3952,56,20,(SELECT Player_ID FROM Player_season WHERE Name = 'Jared Goff' AND Anio = 2020),"1),"
(' Ryan Tannehill',31,QB,16,481,3819,75,33,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Tannehill' AND Anio = 2020),"1),"
(' Ben Roethlisberger',27,QB,15,608,3803,84,33,(SELECT Player_ID FROM Player_season WHERE Name = 'Ben Roethlisberger' AND Anio = 2020),"1),"
(' Teddy Bridgewater',5,QB,15,492,3733,75,15,(SELECT Player_ID FROM Player_season WHERE Name = 'Teddy Bridgewater' AND Anio = 2020),"1),"
(' Baker Mayfield',8,QB,16,486,3563,75,26,(SELECT Player_ID FROM Player_season WHERE Name = 'Baker Mayfield' AND Anio = 2020),"1),"
(' Daniel Jones',24,QB,14,448,2943,53,11,(SELECT Player_ID FROM Player_season WHERE Name = 'Daniel Jones' AND Anio = 2020),"1),"
(' Drew Brees',23,QB,12,390,2942,52,24,(SELECT Player_ID FROM Player_season WHERE Name = 'Drew Brees' AND Anio = 2020),"1),"
(' Drew Lock',10,QB,13,443,2933,92,16,(SELECT Player_ID FROM Player_season WHERE Name = 'Drew Lock' AND Anio = 2020),"1),"
(' Lamar Jackson',3,QB,15,376,2757,47,26,(SELECT Player_ID FROM Player_season WHERE Name = 'Lamar Jackson' AND Anio = 2020),"1),"
(' Joe Burrow',7,QB,10,404,2688,67,13,(SELECT Player_ID FROM Player_season WHERE Name = 'Joe Burrow' AND Anio = 2020),"1),"
(' Cam Newton',22,QB,15,368,2657,50,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Cam Newton' AND Anio = 2020),"1),"
(' Carson Wentz',26,QB,12,437,2620,59,16,(SELECT Player_ID FROM Player_season WHERE Name = 'Carson Wentz' AND Anio = 2020),"1),"
(' Nick Mullens',28,QB,10,326,2437,49,12,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Mullens' AND Anio = 2020),"1),"
(' Gardner Minshew',15,QB,9,327,2259,51,16,(SELECT Player_ID FROM Player_season WHERE Name = 'Gardner Minshew' AND Anio = 2020),"1),"
(' Sam Darnold',25,QB,12,364,2208,69,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Sam Darnold' AND Anio = 2020),"1),"
(' Andy Dalton',9,QB,11,333,2169,69,14,(SELECT Player_ID FROM Player_season WHERE Name = 'Andy Dalton' AND Anio = 2020),"1),"
(' Ryan Fitzpatrick',20,QB,9,267,2091,70,13,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Fitzpatrick' AND Anio = 2020),"1),"
(' Mitchell Trubisky',6,QB,10,297,2055,53,16,(SELECT Player_ID FROM Player_season WHERE Name = 'Mitchell Trubisky' AND Anio = 2020),"1),"
(' Dak Prescott',9,QB,5,222,1856,58,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Dak Prescott' AND Anio = 2020),"1),"
(' Nick Foles',6,QB,9,312,1852,50,10,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Foles' AND Anio = 2020),"1),"
(' Tua Tagovailoa',20,QB,10,290,1814,35,11,(SELECT Player_ID FROM Player_season WHERE Name = 'Tua Tagovailoa' AND Anio = 2020),"1),"
(' Alex Smith',32,QB,8,252,1582,68,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Alex Smith' AND Anio = 2020),"1),"
(' Dwayne Haskins',32,QB,7,241,1439,50,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Dwayne Haskins' AND Anio = 2020),"1),"
(' Jimmy Garoppolo',28,QB,6,140,1096,76,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Jimmy Garoppolo' AND Anio = 2020),"1),"
(' Mike Glennon',15,QB,5,179,1072,46,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Glennon' AND Anio = 2020),"1),"
(' Jalen Hurts',26,QB,15,148,1061,81,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Hurts' AND Anio = 2020),"1),"
(' Taysom Hill',23,QB,16,121,928,44,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Taysom Hill' AND Anio = 2020),"1),"
(' Brandon Allen',7,QB,5,142,925,72,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Allen' AND Anio = 2020),"1),"
(' Joe Flacco',25,QB,5,134,864,52,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Joe Flacco' AND Anio = 2020),"1),"
(' C.J. Beathard',28,QB,6,104,787,49,6,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Beathard' AND Anio = 2020),"1),"
(' Jake Luton',15,QB,3,110,624,73,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jake Luton' AND Anio = 2020),"1),"
(' Kyle Allen',32,QB,4,87,610,52,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Allen' AND Anio = 2020),"1),"
(' Jeff Driskel',10,QB,3,64,432,45,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeff Driskel' AND Anio = 2020),"1),"
(' Colt McCoy',24,QB,4,66,375,35,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Colt McCoy' AND Anio = 2020),"1),"
(' PJ Walker',5,QB,4,56,368,52,1,(SELECT Player_ID FROM Player_season WHERE Name = 'PJ Walker' AND Anio = 2020),"1),"
(' Mason Rudolph',27,QB,5,43,324,47,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Mason Rudolph' AND Anio = 2020),"1),"
(' Brett Rypien',10,QB,3,40,295,48,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Brett Rypien' AND Anio = 2020),"1),"
(' Chase Daniel',11,QB,4,43,264,28,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Chase Daniel' AND Anio = 2020),"1),"
(' Jarrett Stidham',22,QB,5,44,256,38,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jarrett Stidham' AND Anio = 2020),"1),"
(' Chad Henne',16,QB,3,38,248,37,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Chad Henne' AND Anio = 2020),"1),"
(' Garrett Gilbert',9,QB,1,38,243,32,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Garrett Gilbert' AND Anio = 2020),"1),"
(' John Wolford',19,QB,1,38,231,38,0,(SELECT Player_ID FROM Player_season WHERE Name = 'John Wolford' AND Anio = 2020),"1),"
(' Marcus Mariota',17,QB,1,28,226,35,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Marcus Mariota' AND Anio = 2020),"1),"
(' Ben DiNucci',9,QB,3,43,219,32,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ben DiNucci' AND Anio = 2020),"1),"
(' Tyrod Taylor',18,QB,2,30,208,37,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyrod Taylor' AND Anio = 2020),"1),"
(' Matt Barkley',4,QB,5,21,197,56,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Barkley' AND Anio = 2020),"1),"
(' Ryan Finley',7,QB,5,32,164,30,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Finley' AND Anio = 2020),"1),"
(' Blaine Gabbert',30,QB,4,16,143,35,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Blaine Gabbert' AND Anio = 2020),"1),"
(' Taylor Heinicke',32,QB,1,19,137,29,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Taylor Heinicke' AND Anio = 2020),"1),"
(' Brian Hoyer',22,QB,1,24,130,25,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brian Hoyer' AND Anio = 2020),"1),"
(' Chris Streveler',1,QB,5,16,105,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Streveler' AND Anio = 2020),"1),"
(' Trace McSorley',3,QB,2,10,90,70,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Trace McSorley' AND Anio = 2020),"1),"
(' Jameis Winston',23,QB,4,11,75,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jameis Winston' AND Anio = 2020),"1),"
(' Jarvis Landry',8,WR,15,4,74,37,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jarvis Landry' AND Anio = 2020),"1),"
(' David Blough',11,QB,1,10,49,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'David Blough' AND Anio = 2020),"1),"
(' Case Keenum',8,QB,2,10,46,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Case Keenum' AND Anio = 2020),"1),"
(' Jamison Crowder',25,WR,12,1,43,43,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamison Crowder' AND Anio = 2020),"1),"
(' Jakobi Meyers',22,WR,14,2,43,24,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jakobi Meyers' AND Anio = 2020),"1),"
(' Robert Griffin III',3,QB,4,14,42,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Robert Griffin III' AND Anio = 2020),"1),"
(' Russell Gage',2,WR,16,2,39,39,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Russell Gage' AND Anio = 2020),"1),"
(' Julian Edelman',22,WR,6,2,38,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Julian Edelman' AND Anio = 2020),"1),"
(' Geno Smith',29,QB,1,5,33,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Geno Smith' AND Anio = 2020),"1),"
(' Nate Sudfeld',26,QB,1,12,32,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nate Sudfeld' AND Anio = 2020),"1),"
(' Lynn Bowden Jr.',20,WR,10,2,32,32,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Lynn Bowden Jr.' AND Anio = 2020),"1),"
(' Zay Jones',17,WR,16,1,29,29,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Zay Jones' AND Anio = 2020),"1),"
(' Logan Thomas',32,TE,16,1,28,28,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Logan Thomas' AND Anio = 2020),"1),"
(' Joseph Charlton',5,P,16,1,28,28,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Joseph Charlton' AND Anio = 2020),"1),"
(' Andy Lee',1,P,16,1,26,26,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andy Lee' AND Anio = 2020),"1),"
(' Nathan Peterman',17,QB,1,5,25,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nathan Peterman' AND Anio = 2020),"1),"
(' Cedrick Wilson Jr.',9,WR,16,2,23,12,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Cedrick Wilson Jr.' AND Anio = 2020),"1),"
(' Cole Beasley',4,WR,15,1,20,20,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Cole Beasley' AND Anio = 2020),"1),"
(' AJ McCarron',13,QB,2,1,20,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'AJ McCarron' AND Anio = 2020),"1),"
(' Golden Tate',24,WR,12,2,18,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Golden Tate' AND Anio = 2020),"1),"
(' Tyler Bray',6,QB,1,5,18,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Bray' AND Anio = 2020),"1),"
(' Odell Beckham Jr.',8,WR,7,1,18,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Odell Beckham Jr.' AND Anio = 2020),"1),"
(' Jacoby Brissett',14,QB,11,8,17,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jacoby Brissett' AND Anio = 2020),"1),"
(' Tyler Boyd',7,WR,15,2,16,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Boyd' AND Anio = 2020),"1),"
(' Sam Koch',3,P,15,1,15,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Sam Koch' AND Anio = 2020),"1),"
(' Greg Ward',26,WR,16,1,15,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Greg Ward' AND Anio = 2020),"1),"
(' Tyler Huntley',3,QB,2,5,15,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Huntley' AND Anio = 2020),"1),"
(' Jaquan Johnson',4,S,14,1,13,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaquan Johnson' AND Anio = 2020),"1),"
(' Kendall Hinton',10,WR,1,9,13,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kendall Hinton' AND Anio = 2020),"1),"
(' Tommy Townsend',16,P,16,1,13,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tommy Townsend' AND Anio = 2020),"1),"
(' Isaiah McKenzie',4,WR,16,1,12,12,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Isaiah McKenzie' AND Anio = 2020),"1),"
(' Logan Woodside',31,QB,6,3,7,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Logan Woodside' AND Anio = 2020),"1),"
(' Travis Kelce',16,TE,15,2,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Travis Kelce' AND Anio = 2020),"1),"
(' Easton Stick',18,QB,1,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Easton Stick' AND Anio = 2020),"1),"
(' Joshua Dobbs',27,QB,1,5,2,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Joshua Dobbs' AND Anio = 2020),"1),"
(' Brett Kern',31,P,13,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brett Kern' AND Anio = 2020),"1),"
(' Randall Cobb',13,WR,10,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Randall Cobb' AND Anio = 2020),"1),"
(' Chris Jones',9,P,8,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Jones' AND Anio = 2020),"1),"
(' Keenan Allen',18,WR,14,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Keenan Allen' AND Anio = 2020),"1),"
(' Sammy Watkins',16,WR,10,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Sammy Watkins' AND Anio = 2020),"1),"
(' Adam Humphries',31,WR,7,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Adam Humphries' AND Anio = 2020),"1),"
(' Riley Dixon',24,P,16,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Riley Dixon' AND Anio = 2020),"1),"
(' Alex Erickson',7,WR,16,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Alex Erickson' AND Anio = 2020),"1),"
(' Zach Pascal',14,WR,16,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Pascal' AND Anio = 2020),"1),"
(' Tim Boyle',12,QB,8,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tim Boyle' AND Anio = 2020),"1),"
(' Jamal Agnew',11,WR,14,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamal Agnew' AND Anio = 2020),"1),"
(' DJ Moore',5,WR,15,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DJ Moore' AND Anio = 2020),"1),"
(' Jeff Smith',25,WR,12,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeff Smith' AND Anio = 2020),"1),"
(' Isaiah Wright',32,WR,14,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Isaiah Wright' AND Anio = 2020),"1),"
(' James Robinson',15,RB,14,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'James Robinson' AND Anio = 2020),"1),"
(' CeeDee Lamb',9,WR,16,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'CeeDee Lamb' AND Anio = 2020),"1),"
(' Stefon Diggs',4,WR,16,127,1535,55,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Stefon Diggs' AND Anio = 2020),"3),"
(' Travis Kelce',16,TE,15,105,1416,45,11,(SELECT Player_ID FROM Player_season WHERE Name = 'Travis Kelce' AND Anio = 2020),"3),"
(' DeAndre Hopkins',1,WR,16,115,1407,60,6,(SELECT Player_ID FROM Player_season WHERE Name = 'DeAndre Hopkins' AND Anio = 2020),"3),"
(' Justin Jefferson',21,WR,16,88,1400,71,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Jefferson' AND Anio = 2020),"3),"
(' Davante Adams',12,WR,14,115,1374,56,18,(SELECT Player_ID FROM Player_season WHERE Name = 'Davante Adams' AND Anio = 2020),"3),"
(' Calvin Ridley',2,WR,15,90,1374,63,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Calvin Ridley' AND Anio = 2020),"3),"
(' DK Metcalf',29,WR,16,83,1303,62,10,(SELECT Player_ID FROM Player_season WHERE Name = 'DK Metcalf' AND Anio = 2020),"3),"
(' Tyreek Hill',16,WR,15,87,1276,75,15,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyreek Hill' AND Anio = 2020),"3),"
(' Allen Robinson II',6,WR,16,102,1250,42,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Allen Robinson II' AND Anio = 2020),"3),"
(' Darren Waller',17,TE,16,107,1196,38,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Darren Waller' AND Anio = 2020),"3),"
(' DJ Moore',5,WR,15,66,1193,74,4,(SELECT Player_ID FROM Player_season WHERE Name = 'DJ Moore' AND Anio = 2020),"3),"
(' Brandin Cooks',13,WR,15,81,1150,57,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandin Cooks' AND Anio = 2020),"3),"
(' Terry McLaurin',32,WR,15,87,1118,68,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Terry McLaurin' AND Anio = 2020),"3),"
(' Amari Cooper',9,WR,16,92,1114,69,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Amari Cooper' AND Anio = 2020),"3),"
(' Robbie Chosen',5,WR,16,95,1096,75,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Robbie Chosen' AND Anio = 2020),"3),"
(' A.J. Brown',31,WR,14,70,1075,73,11,(SELECT Player_ID FROM Player_season WHERE Name = 'A.J. Brown' AND Anio = 2020),"3),"
(' Tyler Lockett',29,WR,16,100,1054,47,10,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Lockett' AND Anio = 2020),"3),"
(' Mike Evans',30,WR,16,70,1006,50,13,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Evans' AND Anio = 2020),"3),"
(' Keenan Allen',18,WR,14,100,992,28,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Keenan Allen' AND Anio = 2020),"3),"
(' Corey Davis',31,WR,14,65,984,75,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Corey Davis' AND Anio = 2020),"3),"
(' Marvin Jones Jr.',11,WR,16,76,978,43,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Marvin Jones Jr.' AND Anio = 2020),"3),"
(' Cooper Kupp',19,WR,15,92,974,55,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Cooper Kupp' AND Anio = 2020),"3),"
(' Cole Beasley',4,WR,15,82,967,35,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Cole Beasley' AND Anio = 2020),"3),"
(' Robert Woods',19,WR,16,90,936,56,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Robert Woods' AND Anio = 2020),"3),"
(' CeeDee Lamb',9,WR,16,74,935,52,5,(SELECT Player_ID FROM Player_season WHERE Name = 'CeeDee Lamb' AND Anio = 2020),"3),"
(' Adam Thielen',21,WR,15,74,925,51,14,(SELECT Player_ID FROM Player_season WHERE Name = 'Adam Thielen' AND Anio = 2020),"3),"
(' Diontae Johnson',27,WR,15,88,923,47,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Diontae Johnson' AND Anio = 2020),"3),"
(' Tee Higgins',7,WR,16,67,908,67,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Tee Higgins' AND Anio = 2020),"3),"
(' Nelson Agholor',17,WR,16,48,896,85,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Nelson Agholor' AND Anio = 2020),"3),"
(' William Fuller V',13,WR,11,53,879,77,8,(SELECT Player_ID FROM Player_season WHERE Name = 'William Fuller V' AND Anio = 2020),"3),"
(' Chase Claypool',27,WR,16,62,873,84,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Chase Claypool' AND Anio = 2020),"3),"
(' Jerry Jeudy',10,WR,16,52,856,92,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Jerry Jeudy' AND Anio = 2020),"3),"
(' Curtis Samuel',5,WR,15,77,851,44,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Curtis Samuel' AND Anio = 2020),"3),"
(' Michael Gallup',9,WR,16,59,843,55,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Gallup' AND Anio = 2020),"3),"
(' Tyler Boyd',7,WR,15,79,841,72,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Boyd' AND Anio = 2020),"3),"
(' Jarvis Landry',8,WR,15,72,840,32,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Jarvis Landry' AND Anio = 2020),"3),"
(' Chris Godwin',30,WR,12,65,840,47,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Godwin' AND Anio = 2020),"3),"
(' JuJu Smith-Schuster',27,WR,16,97,831,31,9,(SELECT Player_ID FROM Player_season WHERE Name = 'JuJu Smith-Schuster' AND Anio = 2020),"3),"
(' DeVante Parker',20,WR,14,63,793,31,4,(SELECT Player_ID FROM Player_season WHERE Name = 'DeVante Parker' AND Anio = 2020),"3),"
(' Russell Gage',2,WR,16,72,786,35,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Russell Gage' AND Anio = 2020),"3),"
(' Julio Jones',2,WR,9,51,771,44,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Julio Jones' AND Anio = 2020),"3),"
(' Marquise Brown',3,WR,16,58,769,70,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Marquise Brown' AND Anio = 2020),"3),"
(' T.Y. Hilton',14,WR,15,56,762,50,5,(SELECT Player_ID FROM Player_season WHERE Name = 'T.Y. Hilton' AND Anio = 2020),"3),"
(' Mike Williams',18,WR,15,48,756,64,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Williams' AND Anio = 2020),"3),"
(' Alvin Kamara',23,RB,15,83,756,52,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Alvin Kamara' AND Anio = 2020),"3),"
(' Darius Slayton',24,WR,16,50,751,41,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Darius Slayton' AND Anio = 2020),"3),"
(' Brandon Aiyuk',28,WR,12,60,748,49,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Aiyuk' AND Anio = 2020),"3),"
(' Tim Patrick',10,WR,15,51,742,61,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Tim Patrick' AND Anio = 2020),"3),"
(' Jakobi Meyers',22,WR,14,59,729,35,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jakobi Meyers' AND Anio = 2020),"3),"
(' Emmanuel Sanders',23,WR,14,61,726,51,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Emmanuel Sanders' AND Anio = 2020),"3),"
(' T.J. Hockenson',11,TE,16,67,723,51,6,(SELECT Player_ID FROM Player_season WHERE Name = 'T.J. Hockenson' AND Anio = 2020),"3),"
(' DJ Chark Jr.',15,WR,13,53,706,73,5,(SELECT Player_ID FROM Player_season WHERE Name = 'DJ Chark Jr.' AND Anio = 2020),"3),"
(' Mike Gesicki',20,TE,15,53,703,70,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Gesicki' AND Anio = 2020),"3),"
(' Mark Andrews',3,TE,14,58,701,39,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Mark Andrews' AND Anio = 2020),"3),"
(' Jamison Crowder',25,WR,12,59,699,69,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamison Crowder' AND Anio = 2020),"3),"
(' Marquez Valdes-Scantling',12,WR,16,33,690,78,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Marquez Valdes-Scantling' AND Anio = 2020),"3),"
(' Noah Fant',10,TE,15,62,673,37,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Noah Fant' AND Anio = 2020),"3),"
(' Logan Thomas',32,TE,16,72,670,30,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Logan Thomas' AND Anio = 2020),"3),"
(' Kendrick Bourne',28,WR,15,49,667,49,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Kendrick Bourne' AND Anio = 2020),"3),"
(' Sterling Shepard',24,WR,12,66,656,29,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Sterling Shepard' AND Anio = 2020),"3),"
(' Hunter Renfrow',17,WR,16,56,656,53,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Hunter Renfrow' AND Anio = 2020),"3),"
(' Evan Engram',24,TE,16,63,654,53,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Evan Engram' AND Anio = 2020),"3),"
(' Keelan Cole Sr.',15,WR,16,55,642,51,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Keelan Cole Sr.' AND Anio = 2020),"3),"
(' George Kittle',28,TE,8,48,634,44,2,(SELECT Player_ID FROM Player_season WHERE Name = 'George Kittle' AND Anio = 2020),"3),"
(' Darnell Mooney',6,WR,16,61,631,53,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Darnell Mooney' AND Anio = 2020),"3),"
(' Zach Pascal',14,WR,16,44,629,42,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Pascal' AND Anio = 2020),"3),"
(' Rob Gronkowski',30,TE,16,45,623,48,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Rob Gronkowski' AND Anio = 2020),"3),"
(' Christian Kirk',1,WR,14,48,621,80,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian Kirk' AND Anio = 2020),"3),"
(' Josh Reynolds',19,WR,16,52,618,40,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Reynolds' AND Anio = 2020),"3),"
(' Dalton Schultz',9,TE,16,63,615,28,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Dalton Schultz' AND Anio = 2020),"3),"
(' Hunter Henry',18,TE,14,60,613,33,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Hunter Henry' AND Anio = 2020),"3),"
(' Damiere Byrd',22,WR,16,47,604,42,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Damiere Byrd' AND Anio = 2020),"3),"
(' Danny Amendola',11,WR,14,46,602,50,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Danny Amendola' AND Anio = 2020),"3),"
(' Laviska Shenault Jr.',15,WR,14,58,600,36,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Laviska Shenault Jr.' AND Anio = 2020),"3),"
(' Rashard Higgins',8,WR,13,37,599,43,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Rashard Higgins' AND Anio = 2020),"3),"
(' Gabe Davis',4,WR,16,35,599,56,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Gabe Davis' AND Anio = 2020),"3),"
(' J.D. McKissic',32,RB,16,80,589,29,2,(SELECT Player_ID FROM Player_season WHERE Name = 'J.D. McKissic' AND Anio = 2020),"3),"
(' Robert Tonyan',12,TE,16,52,586,45,11,(SELECT Player_ID FROM Player_season WHERE Name = 'Robert Tonyan' AND Anio = 2020),"3),"
(' Hayden Hurst',2,TE,16,56,571,42,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Hayden Hurst' AND Anio = 2020),"3),"
(' Mecole Hardman',16,WR,16,41,560,49,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Mecole Hardman' AND Anio = 2020),"3),"
(' Eric Ebron',27,TE,15,56,558,27,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Eric Ebron' AND Anio = 2020),"3),"
(' Travis Fulgham',26,WR,13,38,539,42,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Travis Fulgham' AND Anio = 2020),"3),"
(' Dallas Goedert',26,TE,11,46,524,41,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Dallas Goedert' AND Anio = 2020),"3),"
(' A.J. Green',7,WR,16,47,523,33,2,(SELECT Player_ID FROM Player_season WHERE Name = 'A.J. Green' AND Anio = 2020),"3),"
(' Tyler Higbee',19,TE,15,44,521,44,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Higbee' AND Anio = 2020),"3),"
(' Jalen Guyton',18,WR,16,28,511,72,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Guyton' AND Anio = 2020),"3),"
(' Breshad Perriman',25,WR,12,30,505,53,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Breshad Perriman' AND Anio = 2020),"3),"
(' Jared Cook',23,TE,15,37,504,46,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Jared Cook' AND Anio = 2020),"3),"
(' Michael Pittman Jr.',14,WR,13,40,503,45,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Pittman Jr.' AND Anio = 2020),"3),"
(' Scotty Miller',30,WR,16,33,501,48,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Scotty Miller' AND Anio = 2020),"3),"
(' Anthony Miller',6,WR,16,49,485,34,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Anthony Miller' AND Anio = 2020),"3),"
(' Antonio Brown',30,WR,8,45,483,46,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Antonio Brown' AND Anio = 2020),"3),"
(' Nyheim Hines',14,RB,16,63,482,29,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Nyheim Hines' AND Anio = 2020),"3),"
(' Cam Sims',32,WR,16,32,477,50,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Cam Sims' AND Anio = 2020),"3),"
(' Chris Conley',15,WR,15,40,471,51,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Conley' AND Anio = 2020),"3),"
(' Demarcus Robinson',16,WR,16,45,466,28,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Demarcus Robinson' AND Anio = 2020),"3),"
(' John Brown',4,WR,9,33,458,46,3,(SELECT Player_ID FROM Player_season WHERE Name = 'John Brown' AND Anio = 2020),"3),"
(' Jimmy Graham',6,TE,16,50,456,30,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Jimmy Graham' AND Anio = 2020),"3),"
(' Henry Ruggs III',17,WR,13,26,452,72,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Henry Ruggs III' AND Anio = 2020),"3),"
(' Allen Lazard',12,WR,10,33,451,72,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Allen Lazard' AND Anio = 2020),"3),"
(' Jonnu Smith',31,TE,15,41,448,63,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonnu Smith' AND Anio = 2020),"3),"
(' Tre'Quan Smith',23,WR,14,34,448,31,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Tre'Quan Smith' AND Anio = 2020),"3),"
(' Randall Cobb',13,WR,10,38,441,34,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Randall Cobb' AND Anio = 2020),"3),"
(' Michael Thomas',23,WR,7,40,438,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Thomas' AND Anio = 2020),"3),"
(' David Montgomery',6,RB,15,54,438,28,2,(SELECT Player_ID FROM Player_season WHERE Name = 'David Montgomery' AND Anio = 2020),"3),"
(' Dan Arnold',1,TE,16,31,438,59,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Dan Arnold' AND Anio = 2020),"3),"
(' Austin Hooper',8,TE,13,46,435,36,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Austin Hooper' AND Anio = 2020),"3),"
(' Willie Snead IV',3,WR,13,33,432,34,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Willie Snead IV' AND Anio = 2020),"3),"
(' Sammy Watkins',16,WR,10,37,421,37,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Sammy Watkins' AND Anio = 2020),"3),"
(' Greg Ward',26,WR,16,53,419,32,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Greg Ward' AND Anio = 2020),"3),"
(' Gerald Everett',19,TE,16,41,417,40,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Gerald Everett' AND Anio = 2020),"3),"
(' David Moore',29,WR,16,35,417,57,6,(SELECT Player_ID FROM Player_season WHERE Name = 'David Moore' AND Anio = 2020),"3),"
(' Larry Fitzgerald',1,WR,13,54,409,18,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Larry Fitzgerald' AND Anio = 2020),"3),"
(' Austin Ekeler',18,RB,10,54,403,28,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Austin Ekeler' AND Anio = 2020),"3),"
(' Jordan Akins',13,TE,13,37,403,26,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Akins' AND Anio = 2020),"3),"
(' Chase Edmonds',1,RB,16,53,402,30,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Chase Edmonds' AND Anio = 2020),"3),"
(' Keke Coutee',13,WR,8,33,400,64,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Keke Coutee' AND Anio = 2020),"3),"
(' Tyron Billy-Johnson',18,WR,12,20,398,55,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyron Billy-Johnson' AND Anio = 2020),"3),"
(' Jalen Reagor',26,WR,11,31,396,55,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Reagor' AND Anio = 2020),"3),"
(' Mo Alie-Cox',14,TE,15,31,394,45,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Mo Alie-Cox' AND Anio = 2020),"3),"
(' Richie James',28,WR,11,23,394,47,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Richie James' AND Anio = 2020),"3),"
(' Braxton Berrios',25,WR,16,37,394,43,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Braxton Berrios' AND Anio = 2020),"3),"
(' James Washington',27,WR,16,30,392,50,5,(SELECT Player_ID FROM Player_season WHERE Name = 'James Washington' AND Anio = 2020),"3),"
(' Deebo Samuel Sr.',28,WR,7,33,391,35,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Deebo Samuel Sr.' AND Anio = 2020),"3),"
(' Golden Tate',24,WR,12,35,388,39,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Golden Tate' AND Anio = 2020),"3),"
(' Myles Gaskin',20,RB,10,41,388,59,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Myles Gaskin' AND Anio = 2020),"3),"
(' Anthony Firkser',31,TE,16,39,387,45,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Anthony Firkser' AND Anio = 2020),"3),"
(' KJ Hamler',10,WR,13,30,381,49,3,(SELECT Player_ID FROM Player_season WHERE Name = 'KJ Hamler' AND Anio = 2020),"3),"
(' James White',22,RB,14,49,375,34,1,(SELECT Player_ID FROM Player_season WHERE Name = 'James White' AND Anio = 2020),"3),"
(' Jakeem Grant Sr.',20,WR,14,36,373,30,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jakeem Grant Sr.' AND Anio = 2020),"3),"
(' Mike Davis',5,RB,15,59,373,23,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Davis' AND Anio = 2020),"3),"
(' Irv Smith Jr.',21,TE,13,30,365,36,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Irv Smith Jr.' AND Anio = 2020),"3),"
(' Dalvin Cook',21,RB,14,44,361,50,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Dalvin Cook' AND Anio = 2020),"3),"
(' Denzel Mims',25,WR,9,23,357,30,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Denzel Mims' AND Anio = 2020),"3),"
(' D'Andre Swift',11,RB,13,46,357,26,2,(SELECT Player_ID FROM Player_season WHERE Name = 'D'Andre Swift' AND Anio = 2020),"3),"
(' Giovani Bernard',7,RB,16,47,355,42,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Giovani Bernard' AND Anio = 2020),"3),"
(' Aaron Jones',12,RB,14,47,355,30,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Aaron Jones' AND Anio = 2020),"3),"
(' Tyler Eifert',15,TE,15,36,349,28,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Eifert' AND Anio = 2020),"3),"
(' Drew Sample',7,TE,16,40,349,23,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Drew Sample' AND Anio = 2020),"3),"
(' Quintez Cephus',11,WR,13,20,349,49,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Quintez Cephus' AND Anio = 2020),"3),"
(' Richard Rodgers',26,TE,14,24,345,33,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Richard Rodgers' AND Anio = 2020),"3),"
(' James Robinson',15,RB,14,49,344,28,3,(SELECT Player_ID FROM Player_season WHERE Name = 'James Robinson' AND Anio = 2020),"3),"
(' Kenny Golladay',11,WR,5,20,338,48,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenny Golladay' AND Anio = 2020),"3),"
(' Ezekiel Elliott',9,RB,15,52,338,19,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Ezekiel Elliott' AND Anio = 2020),"3),"
(' Zach Ertz',26,TE,11,36,335,42,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Ertz' AND Anio = 2020),"3),"
(' Kyle Rudolph',21,TE,12,28,334,25,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Rudolph' AND Anio = 2020),"3),"
(' Odell Beckham Jr.',8,WR,7,23,319,43,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Odell Beckham Jr.' AND Anio = 2020),"3),"
(' Julian Edelman',22,WR,6,21,315,49,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Julian Edelman' AND Anio = 2020),"3),"
(' David Johnson',13,RB,12,33,314,32,2,(SELECT Player_ID FROM Player_season WHERE Name = 'David Johnson' AND Anio = 2020),"3),"
(' Darren Fells',13,TE,16,21,312,44,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Darren Fells' AND Anio = 2020),"3),"
(' N'Keal Harry',22,WR,14,33,309,30,2,(SELECT Player_ID FROM Player_season WHERE Name = 'N'Keal Harry' AND Anio = 2020),"3),"
(' Kareem Hunt',8,RB,16,38,304,26,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Kareem Hunt' AND Anio = 2020),"3),"
(' Donovan Peoples-Jones',8,WR,12,14,304,75,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Donovan Peoples-Jones' AND Anio = 2020),"3),"
(' Marvin Hall',11,WR,12,18,302,73,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Marvin Hall' AND Anio = 2020),"3),"
(' Jonathan Taylor',14,RB,15,36,299,39,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonathan Taylor' AND Anio = 2020),"3),"
(' Clyde Edwards-Helaire',16,RB,13,36,297,26,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Clyde Edwards-Helaire' AND Anio = 2020),"3),"
(' DaeSean Hamilton',10,WR,16,23,293,40,2,(SELECT Player_ID FROM Player_season WHERE Name = 'DaeSean Hamilton' AND Anio = 2020),"3),"
(' Preston Williams',20,WR,8,18,288,47,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Preston Williams' AND Anio = 2020),"3),"
(' Dawson Knox',4,TE,12,24,288,36,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Dawson Knox' AND Anio = 2020),"3),"
(' Chris Herndon',25,TE,16,31,287,26,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Herndon' AND Anio = 2020),"3),"
(' Chris Carson',29,RB,12,37,287,29,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Carson' AND Anio = 2020),"3),"
(' Cameron Brate',30,TE,16,28,282,25,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Cameron Brate' AND Anio = 2020),"3),"
(' Isaiah McKenzie',4,WR,16,30,282,46,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Isaiah McKenzie' AND Anio = 2020),"3),"
(' Isaiah Ford',20,WR,10,28,276,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Isaiah Ford' AND Anio = 2020),"3),"
(' Olamide Zaccheaus',2,WR,11,20,274,51,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Olamide Zaccheaus' AND Anio = 2020),"3),"
(' Collin Johnson',15,WR,14,18,272,46,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Collin Johnson' AND Anio = 2020),"3),"
(' Devin Singletary',4,RB,16,38,269,34,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Devin Singletary' AND Anio = 2020),"3),"
(' Miles Boykin',3,WR,16,19,266,43,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Miles Boykin' AND Anio = 2020),"3),"
(' Steven Sims',32,WR,12,27,265,30,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Steven Sims' AND Anio = 2020),"3),"
(' James O'Shaughnessy',15,TE,15,28,262,26,0,(SELECT Player_ID FROM Player_season WHERE Name = 'James O'Shaughnessy' AND Anio = 2020),"3),"
(' Marcus Johnson',14,WR,11,14,255,55,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marcus Johnson' AND Anio = 2020),"3),"
(' Jerick McKinnon',28,RB,16,33,253,26,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jerick McKinnon' AND Anio = 2020),"3),"
(' Jack Doyle',14,TE,14,23,251,28,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Jack Doyle' AND Anio = 2020),"3),"
(' Will Dissly',29,TE,16,24,251,28,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Will Dissly' AND Anio = 2020),"3),"
(' Trey Burton',14,TE,13,28,250,20,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Trey Burton' AND Anio = 2020),"3),"
(' Duke Johnson',13,RB,11,28,249,48,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Duke Johnson' AND Anio = 2020),"3),"
(' Antonio Gibson',32,RB,14,36,247,40,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Antonio Gibson' AND Anio = 2020),"3),"
(' Ross Dwelley',28,TE,16,19,245,36,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ross Dwelley' AND Anio = 2020),"3),"
(' Cole Kmet',6,TE,16,28,243,38,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Cole Kmet' AND Anio = 2020),"3),"
(' Greg Olsen',29,TE,11,24,239,22,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Greg Olsen' AND Anio = 2020),"3),"
(' Harrison Bryant',8,TE,15,24,238,35,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Harrison Bryant' AND Anio = 2020),"3),"
(' Josh Jacobs',17,RB,15,33,238,29,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Jacobs' AND Anio = 2020),"3),"
(' DeSean Jackson',26,WR,5,14,236,81,1,(SELECT Player_ID FROM Player_season WHERE Name = 'DeSean Jackson' AND Anio = 2020),"3),"
(' Jamaal Williams',12,RB,14,31,236,29,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamaal Williams' AND Anio = 2020),"3),"
(' Chad Hansen',13,WR,5,17,236,38,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Chad Hansen' AND Anio = 2020),"3),"
(' Leonard Fournette',30,RB,13,36,233,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Leonard Fournette' AND Anio = 2020),"3),"
(' Jordan Reed',28,TE,10,26,231,26,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Reed' AND Anio = 2020),"3),"
(' Adam Humphries',31,WR,7,23,228,23,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Adam Humphries' AND Anio = 2020),"3),"
(' Andy Isabella',1,WR,13,21,224,54,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Andy Isabella' AND Anio = 2020),"3),"
(' Van Jefferson',19,WR,16,19,220,31,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Van Jefferson' AND Anio = 2020),"3),"
(' James Conner',27,RB,13,35,215,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'James Conner' AND Anio = 2020),"3),"
(' David Njoku',8,TE,13,19,213,28,2,(SELECT Player_ID FROM Player_season WHERE Name = 'David Njoku' AND Anio = 2020),"3),"
(' Marquez Callaway',23,WR,11,21,213,27,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marquez Callaway' AND Anio = 2020),"3),"
(' Boston Scott',26,RB,16,25,212,18,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Boston Scott' AND Anio = 2020),"3),"
(' Lynn Bowden Jr.',20,WR,10,28,211,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Lynn Bowden Jr.' AND Anio = 2020),"3),"
(' Jacob Hollister',29,TE,16,25,209,20,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Jacob Hollister' AND Anio = 2020),"3),"
(' Durham Smythe',20,TE,15,26,208,19,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Durham Smythe' AND Anio = 2020),"3),"
(' Kyle Juszczyk',28,FB,16,19,202,41,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Juszczyk' AND Anio = 2020),"3),"
(' Chad Beebe',21,WR,14,20,201,40,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Chad Beebe' AND Anio = 2020),"3),"
(' Devin Duvernay',3,WR,16,20,201,39,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Devin Duvernay' AND Anio = 2020),"3),"
(' Ryan Izzo',22,TE,12,13,199,50,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Izzo' AND Anio = 2020),"3),"
(' Brian Hill',2,RB,16,25,199,26,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brian Hill' AND Anio = 2020),"3),"
(' Isaiah Wright',32,WR,14,27,197,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Isaiah Wright' AND Anio = 2020),"3),"
(' Miles Sanders',26,RB,12,28,197,28,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Miles Sanders' AND Anio = 2020),"3),"
(' Tyler Conklin',21,TE,16,19,194,30,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Conklin' AND Anio = 2020),"3),"
(' Bryan Edwards',17,WR,12,11,193,34,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Bryan Edwards' AND Anio = 2020),"3),"
(' Rex Burkhead',22,RB,10,25,192,24,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Rex Burkhead' AND Anio = 2020),"3),"
(' Tony Pollard',9,RB,16,28,192,30,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tony Pollard' AND Anio = 2020),"3),"
(' Bisi Johnson',21,WR,16,14,189,29,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Bisi Johnson' AND Anio = 2020),"3),"
(' Cedrick Wilson Jr.',9,WR,16,17,189,42,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Cedrick Wilson Jr.' AND Anio = 2020),"3),"
(' Mohamed Sanu',11,WR,10,17,187,21,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Mohamed Sanu' AND Anio = 2020),"3),"
(' Kalif Raymond',31,WR,15,9,187,61,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kalif Raymond' AND Anio = 2020),"3),"
(' Kerryon Johnson',11,RB,16,19,187,20,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kerryon Johnson' AND Anio = 2020),"3),"
(' Deonte Harty',23,WR,9,20,186,40,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Deonte Harty' AND Anio = 2020),"3),"
(' KhaDarel Hodge',8,WR,9,11,180,42,0,(SELECT Player_ID FROM Player_season WHERE Name = 'KhaDarel Hodge' AND Anio = 2020),"3),"
(' Latavius Murray',23,RB,15,23,176,25,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Latavius Murray' AND Anio = 2020),"3),"
(' Mack Hollins',20,WR,16,16,176,34,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Mack Hollins' AND Anio = 2020),"3),"
(' Justin Jackson',18,RB,9,19,173,34,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Jackson' AND Anio = 2020),"3),"
(' KeeSean Johnson',1,WR,8,15,173,45,0,(SELECT Player_ID FROM Player_season WHERE Name = 'KeeSean Johnson' AND Anio = 2020),"3),"
(' Adam Trautman',23,TE,15,15,171,41,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Adam Trautman' AND Anio = 2020),"3),"
(' Tyler Johnson',30,WR,14,12,169,35,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Johnson' AND Anio = 2020),"3),"
(' Jeff Smith',25,WR,12,17,167,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeff Smith' AND Anio = 2020),"3),"
(' John Hightower',26,WR,13,10,167,59,0,(SELECT Player_ID FROM Player_season WHERE Name = 'John Hightower' AND Anio = 2020),"3),"
(' Kalen Ballage',25,RB,11,29,166,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kalen Ballage' AND Anio = 2020),"3),"
(' Ronald Jones',30,RB,14,28,165,37,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ronald Jones' AND Anio = 2020),"3),"
(' Todd Gurley II',2,RB,15,25,164,26,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Todd Gurley II' AND Anio = 2020),"3),"
(' Dontrelle Inman',32,WR,10,18,163,17,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Dontrelle Inman' AND Anio = 2020),"3),"
(' Pharaoh Brown',13,TE,13,14,163,29,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Pharaoh Brown' AND Anio = 2020),"3),"
(' Malcolm Brown',19,RB,16,23,162,30,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Malcolm Brown' AND Anio = 2020),"3),"
(' Byron Pringle',16,WR,13,13,160,37,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Byron Pringle' AND Anio = 2020),"3),"
(' Donald Parham Jr.',18,TE,13,10,159,26,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Donald Parham Jr.' AND Anio = 2020),"3),"
(' Freddie Swain',29,WR,16,13,159,23,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Freddie Swain' AND Anio = 2020),"3),"
(' Darrell Henderson Jr.',19,RB,15,16,159,28,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Darrell Henderson Jr.' AND Anio = 2020),"3),"
(' Melvin Gordon III',10,RB,15,32,158,20,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Melvin Gordon III' AND Anio = 2020),"3),"
(' Raheem Mostert',28,RB,8,16,156,76,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Raheem Mostert' AND Anio = 2020),"3),"
(' Zay Jones',17,WR,16,14,154,37,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Zay Jones' AND Anio = 2020),"3),"
(' Noah Brown',9,WR,16,14,154,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Noah Brown' AND Anio = 2020),"3),"
(' Nick Chubb',8,RB,12,16,150,26,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Chubb' AND Anio = 2020),"3),"
(' Auden Tate',7,WR,9,14,150,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Auden Tate' AND Anio = 2020),"3),"
(' Adam Shaheen',20,TE,16,12,150,43,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Adam Shaheen' AND Anio = 2020),"3),"
(' Christian McCaffrey',5,RB,3,17,149,24,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian McCaffrey' AND Anio = 2020),"3),"
(' Joshua Kelley',18,RB,14,23,148,35,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Joshua Kelley' AND Anio = 2020),"3),"
(' Chris Thompson',15,RB,8,20,146,15,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Thompson' AND Anio = 2020),"3),"
(' O.J. Howard',30,TE,4,11,146,33,2,(SELECT Player_ID FROM Player_season WHERE Name = 'O.J. Howard' AND Anio = 2020),"3),"
(' Ian Thomas',5,TE,16,20,145,21,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ian Thomas' AND Anio = 2020),"3),"
(' Kenny Stills',13,WR,10,11,144,24,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenny Stills' AND Anio = 2020),"3),"
(' Christian Blake',2,WR,16,13,141,25,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian Blake' AND Anio = 2020),"3),"
(' Foster Moreau',17,TE,16,7,140,47,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Foster Moreau' AND Anio = 2020),"3),"
(' Alex Erickson',7,WR,16,12,139,42,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Alex Erickson' AND Anio = 2020),"3),"
(' Le'Veon Bell',25,RB,11,16,138,30,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Le'Veon Bell' AND Anio = 2020),"3),"
(' Jalen Richard',17,RB,13,19,138,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Richard' AND Anio = 2020),"3),"
(' Joe Mixon',7,RB,6,21,138,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Joe Mixon' AND Anio = 2020),"3),"
(' Kenyan Drake',1,RB,15,25,137,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenyan Drake' AND Anio = 2020),"3),"
(' Jeff Wilson Jr.',28,RB,12,13,133,21,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeff Wilson Jr.' AND Anio = 2020),"3),"
(' Cordarrelle Patterson',6,RB,16,21,132,25,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cordarrelle Patterson' AND Anio = 2020),"3),"
(' Mike Thomas',7,WR,14,13,132,29,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Thomas' AND Anio = 2020),"3),"
(' Jesse James',11,TE,16,14,129,31,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jesse James' AND Anio = 2020),"3),"
(' Gus Edwards',3,RB,16,9,129,34,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Gus Edwards' AND Anio = 2020),"3),"
(' Dion Lewis',24,RB,16,19,127,17,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Dion Lewis' AND Anio = 2020),"3),"
(' Alexander Mattison',21,RB,13,13,125,28,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Alexander Mattison' AND Anio = 2020),"3),"
(' Cam Akers',19,RB,13,11,123,38,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Cam Akers' AND Anio = 2020),"3),"
(' Albert Okwuegbunam Jr.',10,TE,4,11,121,27,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Albert Okwuegbunam Jr.' AND Anio = 2020),"3),"
(' J.K. Dobbins',3,RB,15,18,120,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'J.K. Dobbins' AND Anio = 2020),"3),"
(' Tyler Kroft',4,TE,10,12,119,38,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Kroft' AND Anio = 2020),"3),"
(' Chris Hogan',25,WR,5,14,118,27,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Hogan' AND Anio = 2020),"3),"
(' Equanimeous St. Brown',12,WR,12,7,117,24,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Equanimeous St. Brown' AND Anio = 2020),"3),"
(' Darrel Williams',16,RB,16,18,116,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Darrel Williams' AND Anio = 2020),"3),"
(' Alshon Jeffery',26,WR,7,6,115,39,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Alshon Jeffery' AND Anio = 2020),"3),"
(' Derrick Henry',31,RB,16,19,114,53,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Derrick Henry' AND Anio = 2020),"3),"
(' Wayne Gallman',24,RB,15,21,114,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Wayne Gallman' AND Anio = 2020),"3),"
(' Sony Michel',22,RB,9,7,114,31,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Sony Michel' AND Anio = 2020),"3),"
(' Jace Sternberger',12,TE,12,12,114,27,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jace Sternberger' AND Anio = 2020),"3),"
(' Nick Boyle',3,TE,9,14,113,21,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Boyle' AND Anio = 2020),"3),"
(' Kaden Smith',24,TE,15,18,112,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kaden Smith' AND Anio = 2020),"3),"
(' DeeJay Dallas',29,RB,12,17,111,13,1,(SELECT Player_ID FROM Player_season WHERE Name = 'DeeJay Dallas' AND Anio = 2020),"3),"
(' Blake Bell',9,TE,16,11,110,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Blake Bell' AND Anio = 2020),"3),"
(' Alec Ingold',17,FB,16,12,110,23,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Alec Ingold' AND Anio = 2020),"3),"
(' Marcedes Lewis',12,TE,15,10,107,36,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Marcedes Lewis' AND Anio = 2020),"3),"
(' Stephen Anderson',18,TE,16,8,106,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Stephen Anderson' AND Anio = 2020),"3),"
(' Quez Watkins',26,WR,6,7,106,43,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Quez Watkins' AND Anio = 2020),"3),"
(' Jordan Wilkins',14,RB,15,12,105,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Wilkins' AND Anio = 2020),"3),"
(' Maxx Williams',1,TE,9,8,102,42,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Maxx Williams' AND Anio = 2020),"3),"
(' Adrian Peterson',11,RB,16,12,101,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Adrian Peterson' AND Anio = 2020),"3),"
(' LeSean McCoy',30,RB,10,15,101,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'LeSean McCoy' AND Anio = 2020),"3),"
(' C.J. Board',24,WR,14,11,101,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Board' AND Anio = 2020),"3),"
(' Cameron Batson',31,WR,12,12,100,18,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Cameron Batson' AND Anio = 2020),"3),"
(' Vance McDonald',27,TE,14,15,99,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Vance McDonald' AND Anio = 2020),"3),"
(' Ty Johnson',25,RB,13,16,99,18,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ty Johnson' AND Anio = 2020),"3),"
(' Taysom Hill',23,QB,16,8,98,21,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Taysom Hill' AND Anio = 2020),"3),"
(' C.J. Ham',21,FB,15,8,97,30,1,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Ham' AND Anio = 2020),"3),"
(' Matt Breida',20,RB,12,9,96,31,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Breida' AND Anio = 2020),"3),"
(' Nick Vannett',10,TE,15,14,95,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Vannett' AND Anio = 2020),"3),"
(' Zack Moss',4,RB,13,14,95,20,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Zack Moss' AND Anio = 2020),"3),"
(' Justin Watson',30,WR,11,7,94,36,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Watson' AND Anio = 2020),"3),"
(' Carlos Hyde',29,RB,10,16,93,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Carlos Hyde' AND Anio = 2020),"3),"
(' Darrell Daniels',1,TE,12,8,92,31,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Darrell Daniels' AND Anio = 2020),"3),"
(' Malcolm Perry',20,RB,9,9,92,25,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Malcolm Perry' AND Anio = 2020),"3),"
(' Austin Mack',24,WR,11,7,91,50,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Austin Mack' AND Anio = 2020),"3),"
(' Travis Homer',29,RB,9,9,90,50,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Travis Homer' AND Anio = 2020),"3),"
(' Frank Gore',25,RB,15,16,89,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Frank Gore' AND Anio = 2020),"3),"
(' Jamal Agnew',11,WR,14,13,89,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamal Agnew' AND Anio = 2020),"3),"
(' C.J. Uzomah',7,TE,2,8,87,23,1,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Uzomah' AND Anio = 2020),"3),"
(' Ryan Griffin',25,TE,15,9,86,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Griffin' AND Anio = 2020),"3),"
(' Trent Taylor',28,WR,12,10,86,29,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trent Taylor' AND Anio = 2020),"3),"
(' J.J. Arcega-Whiteside',26,WR,8,4,85,37,0,(SELECT Player_ID FROM Player_season WHERE Name = 'J.J. Arcega-Whiteside' AND Anio = 2020),"3),"
(' Tyler Ervin',12,RB,8,11,84,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Ervin' AND Anio = 2020),"3),"
(' Devontae Booker',17,RB,16,17,84,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Devontae Booker' AND Anio = 2020),"3),"
(' Geoff Swaim',31,TE,10,9,83,16,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Geoff Swaim' AND Anio = 2020),"3),"
(' Royce Freeman',10,RB,16,12,81,28,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Royce Freeman' AND Anio = 2020),"3),"
(' Troy Fumagalli',10,TE,8,8,80,29,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Troy Fumagalli' AND Anio = 2020),"3),"
(' DeMichael Harris',14,WR,7,10,79,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DeMichael Harris' AND Anio = 2020),"3),"
(' Ray-Ray McCloud III',27,WR,16,20,77,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ray-Ray McCloud III' AND Anio = 2020),"3),"
(' Dante Pettis',24,WR,7,4,76,33,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Dante Pettis' AND Anio = 2020),"3),"
(' Ito Smith',2,RB,14,17,75,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ito Smith' AND Anio = 2020),"3),"
(' Pharoh Cooper',5,WR,16,5,73,32,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Pharoh Cooper' AND Anio = 2020),"3),"
(' KJ Hill Jr.',18,WR,15,7,73,25,0,(SELECT Player_ID FROM Player_season WHERE Name = 'KJ Hill Jr.' AND Anio = 2020),"3),"
(' Parris Campbell',14,WR,2,6,71,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Parris Campbell' AND Anio = 2020),"3),"
(' Jason Witten',17,TE,16,13,69,15,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jason Witten' AND Anio = 2020),"3),"
(' Brandon Powell',2,WR,15,12,69,13,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Powell' AND Anio = 2020),"3),"
(' Patrick Laird',20,RB,16,10,68,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Patrick Laird' AND Anio = 2020),"3),"
(' Ryan Nall',6,FB,16,8,67,18,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Nall' AND Anio = 2020),"3),"
(' Samaje Perine',7,RB,16,11,66,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Samaje Perine' AND Anio = 2020),"3),"
(' Courtland Sutton',10,WR,1,3,66,45,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Courtland Sutton' AND Anio = 2020),"3),"
(' Malik Taylor',12,WR,15,5,66,26,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Malik Taylor' AND Anio = 2020),"3),"
(' Darwin Thompson',16,RB,14,7,65,37,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Darwin Thompson' AND Anio = 2020),"3),"
(' Luke Stocker',2,TE,16,7,63,25,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Luke Stocker' AND Anio = 2020),"3),"
(' Damion Ratley',24,WR,5,4,63,29,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Damion Ratley' AND Anio = 2020),"3),"
(' La'Mical Perine',25,RB,10,11,63,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'La'Mical Perine' AND Anio = 2020),"3),"
(' Tyrie Cleveland',10,WR,10,6,63,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyrie Cleveland' AND Anio = 2020),"3),"
(' Nick Keizer',16,TE,16,6,63,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Keizer' AND Anio = 2020),"3),"
(' Gunner Olszewski',22,WR,13,5,62,38,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Gunner Olszewski' AND Anio = 2020),"3),"
(' Benny Snell Jr.',27,RB,16,10,61,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Benny Snell Jr.' AND Anio = 2020),"3),"
(' Salvon Ahmed',20,RB,6,11,61,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Salvon Ahmed' AND Anio = 2020),"3),"
(' Steven Mitchell Jr.',13,WR,6,5,60,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Steven Mitchell Jr.' AND Anio = 2020),"3),"
(' Ja'Marcus Bradley',8,WR,3,5,60,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ja'Marcus Bradley' AND Anio = 2020),"3),"
(' Saquon Barkley',24,RB,2,6,60,38,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Saquon Barkley' AND Anio = 2020),"3),"
(' Keith Smith',2,FB,16,11,59,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Keith Smith' AND Anio = 2020),"3),"
(' Rodney Smith',5,RB,7,9,59,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Rodney Smith' AND Anio = 2020),"3),"
(' Devonta Freeman',24,RB,5,7,58,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Devonta Freeman' AND Anio = 2020),"3),"
(' Ameer Abdullah',21,RB,16,8,58,22,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Ameer Abdullah' AND Anio = 2020),"3),"
(' Jaydon Mickens',30,WR,10,7,58,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaydon Mickens' AND Anio = 2020),"3),"
(' Jeremy McNichols',31,RB,16,12,55,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeremy McNichols' AND Anio = 2020),"3),"
(' Dare Ogunbowale',15,RB,14,10,54,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dare Ogunbowale' AND Anio = 2020),"3),"
(' Anthony McFarland Jr.',27,RB,11,6,54,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Anthony McFarland Jr.' AND Anio = 2020),"3),"
(' Cethan Carter',7,TE,15,5,53,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cethan Carter' AND Anio = 2020),"3),"
(' Johnny Mundt',19,TE,16,4,53,34,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Johnny Mundt' AND Anio = 2020),"3),"
(' Ashton Dulin',14,WR,13,3,53,34,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ashton Dulin' AND Anio = 2020),"3),"
(' Chris Manhertz',5,TE,16,6,52,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Manhertz' AND Anio = 2020),"3),"
(' Damien Harris',22,RB,10,5,52,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Damien Harris' AND Anio = 2020),"3),"
(' Mark Ingram II',3,RB,11,6,50,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mark Ingram II' AND Anio = 2020),"3),"
(' Virgil Green',18,TE,6,3,50,26,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Virgil Green' AND Anio = 2020),"3),"
(' Trent Sherfield Sr.',1,WR,15,5,50,26,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trent Sherfield Sr.' AND Anio = 2020),"3),"
(' MyCole Pruitt',31,TE,11,5,49,22,2,(SELECT Player_ID FROM Player_season WHERE Name = 'MyCole Pruitt' AND Anio = 2020),"3),"
(' Laquon Treadwell',2,WR,5,6,49,14,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Laquon Treadwell' AND Anio = 2020),"3),"
(' Javon Wims',6,WR,13,6,48,13,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Javon Wims' AND Anio = 2020),"3),"
(' Dez Bryant',3,WR,6,6,47,16,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Dez Bryant' AND Anio = 2020),"3),"
(' Levine Toilolo',24,TE,16,5,46,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Levine Toilolo' AND Anio = 2020),"3),"
(' Josh Hill',23,TE,14,8,46,16,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Hill' AND Anio = 2020),"3),"
(' Jaylen Samuels',27,RB,14,9,46,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaylen Samuels' AND Anio = 2020),"3),"
(' Darrius Shepherd',12,WR,8,5,46,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Darrius Shepherd' AND Anio = 2020),"3),"
(' Lil'Jordan Humphrey',23,WR,3,3,46,17,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Lil'Jordan Humphrey' AND Anio = 2020),"3),"
(' Demetrius Harris',6,TE,15,7,45,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Demetrius Harris' AND Anio = 2020),"3),"
(' Patrick Ricard',3,FB,15,9,45,11,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Patrick Ricard' AND Anio = 2020),"3),"
(' Hunter Bryant',11,TE,5,1,44,44,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Hunter Bryant' AND Anio = 2020),"3),"
(' Theo Riddick',17,RB,4,5,43,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Theo Riddick' AND Anio = 2020),"3),"
(' Troymaine Pope',18,RB,6,8,42,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Troymaine Pope' AND Anio = 2020),"3),"
(' Devine Ozigbo',15,RB,8,9,42,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Devine Ozigbo' AND Anio = 2020),"3),"
(' Tanner Hudson',30,TE,11,3,41,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tanner Hudson' AND Anio = 2020),"3),"
(' River Cracraft',28,WR,9,6,41,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'River Cracraft' AND Anio = 2020),"3),"
(' Tarik Cohen',6,RB,3,6,41,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tarik Cohen' AND Anio = 2020),"3),"
(' Ted Ginn Jr.',6,WR,6,3,40,29,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ted Ginn Jr.' AND Anio = 2020),"3),"
(' Khari Blasingame',31,FB,15,4,39,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Khari Blasingame' AND Anio = 2020),"3),"
(' Juwan Johnson',23,TE,7,4,39,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Juwan Johnson' AND Anio = 2020),"3),"
(' Riley Ridley',6,WR,5,4,39,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Riley Ridley' AND Anio = 2020),"3),"
(' Devin Asiasi',22,TE,9,2,39,26,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Devin Asiasi' AND Anio = 2020),"3),"
(' Robert Foster',32,WR,4,2,37,28,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Robert Foster' AND Anio = 2020),"3),"
(' Deon Yelder',16,TE,14,7,36,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Deon Yelder' AND Anio = 2020),"3),"
(' Charlie Woerner',28,TE,14,3,36,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Charlie Woerner' AND Anio = 2020),"3),"
(' Cam Newton',22,QB,15,2,35,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Cam Newton' AND Anio = 2020),"3),"
(' Lee Smith',4,TE,10,4,35,27,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Lee Smith' AND Anio = 2020),"3),"
(' Jakob Johnson',22,FB,16,8,35,12,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jakob Johnson' AND Anio = 2020),"3),"
(' Lawrence Cager',25,TE,2,2,35,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Lawrence Cager' AND Anio = 2020),"3),"
(' Kahale Warring',13,TE,7,3,35,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kahale Warring' AND Anio = 2020),"3),"
(' Brandon Zylstra',5,WR,16,3,35,28,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Zylstra' AND Anio = 2020),"3),"
(' Andre Roberts',4,WR,15,4,34,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andre Roberts' AND Anio = 2020),"3),"
(' Tevin Coleman',28,RB,8,4,34,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tevin Coleman' AND Anio = 2020),"3),"
(' Ke'Shawn Vaughn',30,RB,10,5,34,13,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ke'Shawn Vaughn' AND Anio = 2020),"3),"
(' JaMycal Hasty',28,RB,8,7,33,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'JaMycal Hasty' AND Anio = 2020),"3),"
(' Nick Westbrook-Ikhine',31,WR,14,3,33,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Westbrook-Ikhine' AND Anio = 2020),"3),"
(' Terry Godwin',15,WR,3,3,32,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Terry Godwin' AND Anio = 2020),"3),"
(' Seth Roberts',5,WR,7,4,31,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Seth Roberts' AND Anio = 2020),"3),"
(' Daniel Brown',25,TE,16,2,31,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Daniel Brown' AND Anio = 2020),"3),"
(' DeAndre Washington',20,RB,4,5,30,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DeAndre Washington' AND Anio = 2020),"3),"
(' Marlon Mack',14,RB,1,3,30,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marlon Mack' AND Anio = 2020),"3),"
(' Trayveon Williams',7,RB,10,5,30,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trayveon Williams' AND Anio = 2020),"3),"
(' Isaiah Zuber',22,WR,4,2,29,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Isaiah Zuber' AND Anio = 2020),"3),"
(' Josh Adams',25,RB,8,6,29,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Adams' AND Anio = 2020),"3),"
(' Michael Burton',23,FB,15,4,28,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Burton' AND Anio = 2020),"3),"
(' Phillip Lindsay',10,RB,11,7,28,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Phillip Lindsay' AND Anio = 2020),"3),"
(' Ty Montgomery II',23,WR,6,3,27,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ty Montgomery II' AND Anio = 2020),"3),"
(' Austin Carr',23,WR,6,3,27,11,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Austin Carr' AND Anio = 2020),"3),"
(' Austin Walter',28,RB,4,1,27,27,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Austin Walter' AND Anio = 2020),"3),"
(' Darrynton Evans',31,RB,5,2,27,24,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Darrynton Evans' AND Anio = 2020),"3),"
(' Diontae Spencer',10,WR,11,3,26,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Diontae Spencer' AND Anio = 2020),"3),"
(' Ezekiel Turner',1,LB,16,1,26,26,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ezekiel Turner' AND Anio = 2020),"3),"
(' Dominique Dafney',12,TE,5,2,26,13,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Dominique Dafney' AND Anio = 2020),"3),"
(' Corey Clement',26,RB,15,5,25,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Corey Clement' AND Anio = 2020),"3),"
(' Jaeden Graham',2,TE,16,3,25,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaeden Graham' AND Anio = 2020),"3),"
(' Gabe Nabers',18,FB,16,5,25,9,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Gabe Nabers' AND Anio = 2020),"3),"
(' Daurice Fountain',14,WR,5,2,23,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Daurice Fountain' AND Anio = 2020),"3),"
(' T.J. Yeldon',4,RB,3,1,22,22,1,(SELECT Player_ID FROM Player_season WHERE Name = 'T.J. Yeldon' AND Anio = 2020),"3),"
(' Jake Kumerow',4,WR,6,1,22,22,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jake Kumerow' AND Anio = 2020),"3),"
(' Jonathan Williams',11,RB,5,4,21,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonathan Williams' AND Anio = 2020),"3),"
(' AJ Dillon',12,RB,11,2,21,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'AJ Dillon' AND Anio = 2020),"3),"
(' Tavon Austin',12,WR,4,5,20,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tavon Austin' AND Anio = 2020),"3),"
(' Elijhaa Penny',24,RB,14,2,20,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Elijhaa Penny' AND Anio = 2020),"3),"
(' Antonio Callaway',20,WR,5,2,20,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Antonio Callaway' AND Anio = 2020),"3),"
(' Justice Hill',3,RB,12,5,20,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Justice Hill' AND Anio = 2020),"3),"
(' Antonio Williams',4,RB,1,1,20,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Antonio Williams' AND Anio = 2020),"3),"
(' Alfred Morris',24,RB,9,3,19,9,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Alfred Morris' AND Anio = 2020),"3),"
(' Deontay Burnett',26,WR,2,3,19,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Deontay Burnett' AND Anio = 2020),"3),"
(' C.J. Prosise',13,RB,10,5,18,10,1,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Prosise' AND Anio = 2020),"3),"
(' Reggie Bonnafon',5,RB,2,2,18,15,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Reggie Bonnafon' AND Anio = 2020),"3),"
(' Alex Armah',5,RB,16,5,18,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Alex Armah' AND Anio = 2020),"3),"
(' John Ross',7,WR,3,2,17,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'John Ross' AND Anio = 2020),"3),"
(' Eric Saubert',15,TE,8,3,16,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Eric Saubert' AND Anio = 2020),"3),"
(' Josh Malone',25,WR,4,4,16,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Malone' AND Anio = 2020),"3),"
(' Reggie Gilliam',4,FB,14,2,16,15,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Reggie Gilliam' AND Anio = 2020),"3),"
(' Jaleel Scott',25,WR,1,1,16,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaleel Scott' AND Anio = 2020),"3),"
(' Dalton Keene',22,TE,6,3,16,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dalton Keene' AND Anio = 2020),"3),"
(' Colby Parkinson',29,TE,6,2,16,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Colby Parkinson' AND Anio = 2020),"3),"
(' Trenton Cannon',5,RB,14,3,16,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trenton Cannon' AND Anio = 2020),"3),"
(' Donte Moncrief',22,WR,6,1,15,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Donte Moncrief' AND Anio = 2020),"3),"
(' Derek Carrier',17,TE,16,1,14,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Derek Carrier' AND Anio = 2020),"3),"
(' D'Ernest Johnson',8,RB,16,3,14,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'D'Ernest Johnson' AND Anio = 2020),"3),"
(' James Proche II',3,WR,14,1,14,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'James Proche II' AND Anio = 2020),"3),"
(' Andy Janovich',8,FB,14,2,13,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andy Janovich' AND Anio = 2020),"3),"
(' Keith Kirkwood',5,WR,1,1,13,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Keith Kirkwood' AND Anio = 2020),"3),"
(' Siran Neal',4,CB,16,1,13,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Siran Neal' AND Anio = 2020),"3),"
(' Vyncint Smith',25,WR,7,1,13,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Vyncint Smith' AND Anio = 2020),"3),"
(' Luke Willson',29,TE,3,1,12,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Luke Willson' AND Anio = 2020),"3),"
(' Blake Jarwin',9,TE,1,1,12,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Blake Jarwin' AND Anio = 2020),"3),"
(' Peyton Barber',32,RB,16,4,12,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Peyton Barber' AND Anio = 2020),"3),"
(' Cody Hollister',31,WR,2,1,12,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cody Hollister' AND Anio = 2020),"3),"
(' Josiah Deguara',12,TE,2,1,12,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Josiah Deguara' AND Anio = 2020),"3),"
(' Josh Allen',4,QB,16,1,12,12,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Allen' AND Anio = 2020),"3),"
(' Bennie Fowler',23,WR,5,2,11,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Bennie Fowler' AND Anio = 2020),"3),"
(' Dak Prescott',9,QB,5,1,11,11,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Dak Prescott' AND Anio = 2020),"3),"
(' Marcus Kemp',16,WR,10,1,11,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marcus Kemp' AND Anio = 2020),"3),"
(' Stephen Carlson',8,TE,16,1,11,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Stephen Carlson' AND Anio = 2020),"3),"
(' Jonathan Ward',1,RB,14,1,11,11,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonathan Ward' AND Anio = 2020),"3),"
(' Temarrick Hemingway',32,TE,8,1,10,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Temarrick Hemingway' AND Anio = 2020),"3),"
(' Gehrig Dieter',16,WR,4,1,10,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Gehrig Dieter' AND Anio = 2020),"3),"
(' Mike Boone',21,RB,16,2,10,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Boone' AND Anio = 2020),"3),"
(' Ben Ellefson',15,TE,7,1,10,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ben Ellefson' AND Anio = 2020),"3),"
(' Nick Bellore',29,LB,16,1,9,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Bellore' AND Anio = 2020),"3),"
(' Chandler Cox',20,FB,8,2,9,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chandler Cox' AND Anio = 2020),"3),"
(' DeAndre Carter',6,WR,13,1,8,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DeAndre Carter' AND Anio = 2020),"3),"
(' Jason Cabinda',11,FB,16,2,8,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jason Cabinda' AND Anio = 2020),"3),"
(' Charlie Heck',13,OT,3,0,8,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Charlie Heck' AND Anio = 2020),"3),"
(' D.J. Foster',1,RB,10,1,7,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'D.J. Foster' AND Anio = 2020),"3),"
(' Colin Thompson',5,TE,15,1,7,7,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Colin Thompson' AND Anio = 2020),"3),"
(' Max Scharping',13,G,15,0,7,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Max Scharping' AND Anio = 2020),"3),"
(' Scottie Phillips',13,RB,8,1,7,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Scottie Phillips' AND Anio = 2020),"3),"
(' Lamar Miller',6,RB,1,2,6,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Lamar Miller' AND Anio = 2020),"3),"
(' Jeremy Sprinkle',32,TE,16,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeremy Sprinkle' AND Anio = 2020),"3),"
(' Baker Mayfield',8,QB,16,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Baker Mayfield' AND Anio = 2020),"3),"
(' Cullen Gillaspia',13,LB,7,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cullen Gillaspia' AND Anio = 2020),"3),"
(' Brandon Dillon',21,TE,3,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Dillon' AND Anio = 2020),"3),"
(' Anthony Sherman',16,FB,13,1,5,5,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Anthony Sherman' AND Anio = 2020),"3),"
(' Tommylee Lewis',23,WR,5,1,5,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tommylee Lewis' AND Anio = 2020),"3),"
(' Jake Butt',10,TE,5,2,5,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jake Butt' AND Anio = 2020),"3),"
(' D'Onta Foreman',31,RB,6,1,5,5,1,(SELECT Player_ID FROM Player_season WHERE Name = 'D'Onta Foreman' AND Anio = 2020),"3),"
(' LeVante Bellamy',10,RB,5,1,5,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'LeVante Bellamy' AND Anio = 2020),"3),"
(' Trenton Irwin',7,WR,1,1,5,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trenton Irwin' AND Anio = 2020),"3),"
(' Trevon Wesco',25,TE,12,1,5,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trevon Wesco' AND Anio = 2020),"3),"
(' Bobby Massie',6,OT,8,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Bobby Massie' AND Anio = 2020),"3),"
(' Alex Collins',29,RB,3,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Alex Collins' AND Anio = 2020),"3),"
(' Dede Westbrook',15,WR,2,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dede Westbrook' AND Anio = 2020),"3),"
(' J.J. Taylor',22,RB,6,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'J.J. Taylor' AND Anio = 2020),"3),"
(' Jason Croom',26,TE,4,1,3,3,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jason Croom' AND Anio = 2020),"3),"
(' Buddy Howell',13,RB,14,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Buddy Howell' AND Anio = 2020),"3),"
(' Penny Hart',29,WR,13,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Penny Hart' AND Anio = 2020),"3),"
(' Antonio Gandy-Golden',32,TE,6,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Antonio Gandy-Golden' AND Anio = 2020),"3),"
(' Isaac Nauta',11,TE,7,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Isaac Nauta' AND Anio = 2020),"3),"
(' Jordan Thomas',22,TE,6,1,3,3,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Thomas' AND Anio = 2020),"3),"
(' Jalen Hurts',26,QB,15,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Hurts' AND Anio = 2020),"3),"
(' Craig Reynolds',15,RB,2,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Craig Reynolds' AND Anio = 2020),"3),"
(' Bruce Miller',15,FB,8,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Bruce Miller' AND Anio = 2020),"3),"
(' Eric Fisher',16,OT,15,1,2,2,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Eric Fisher' AND Anio = 2020),"3),"
(' Marcus Baugh',32,TE,8,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marcus Baugh' AND Anio = 2020),"3),"
(' Dontrell Hilliard',8,RB,5,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dontrell Hilliard' AND Anio = 2020),"3),"
(' Adrian Killins',26,RB,1,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Adrian Killins' AND Anio = 2020),"3),"
(' Kendall Lamm',8,OT,15,1,1,1,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kendall Lamm' AND Anio = 2020),"3),"
(' Ryan Fitzpatrick',20,QB,9,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Fitzpatrick' AND Anio = 2020),"3),"
(' Matthew Stafford',11,QB,16,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Matthew Stafford' AND Anio = 2020),"3),"
(' Taiwan Jones',4,RB,13,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Taiwan Jones' AND Anio = 2020),"3),"
(' Ryan Tannehill',31,QB,16,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Tannehill' AND Anio = 2020),"3),"
(' Kenjon Barner',30,RB,6,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenjon Barner' AND Anio = 2020),"3),"
(' C.J. Goodwin',9,CB,16,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Goodwin' AND Anio = 2020),"3),"
(' Eric Tomlinson',24,TE,6,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Eric Tomlinson' AND Anio = 2020),"3),"
(' Seth DeValve',1,TE,4,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Seth DeValve' AND Anio = 2020),"3),"
(' Brandon Allen',7,QB,5,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Allen' AND Anio = 2020),"3),"
(' J.P. Holtz',6,TE,16,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'J.P. Holtz' AND Anio = 2020),"3),"
(' Mason Schreck',7,TE,14,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mason Schreck' AND Anio = 2020),"3),"
(' Jerald Hawkins',27,OT,13,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jerald Hawkins' AND Anio = 2020),"3),"
(' Tajae Sharpe',21,WR,4,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tajae Sharpe' AND Anio = 2020),"3),"
(' Kevin Rader',27,TE,1,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kevin Rader' AND Anio = 2020),"3),"
(' PJ Walker',5,QB,4,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'PJ Walker' AND Anio = 2020),"3),"
(' Ricky Seals-Jones',16,TE,2,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ricky Seals-Jones' AND Anio = 2020),"3),"
(' Jeff Badet',32,WR,3,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeff Badet' AND Anio = 2020),"3),"
(' Taywan Taylor',8,WR,3,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Taywan Taylor' AND Anio = 2020),"3),"
(' Nick Gates',24,C,16,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Gates' AND Anio = 2020),"3),"
(' Patrick Mahomes',16,QB,15,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Patrick Mahomes' AND Anio = 2020),"3),"
(' Tyler Davis',15,TE,8,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Davis' AND Anio = 2020),"3),"
(' Hakeem Butler',26,WR,2,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Hakeem Butler' AND Anio = 2020),"3),"
(' Noah Togiai',14,TE,4,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Noah Togiai' AND Anio = 2020),"3),"
(' Joe Reed',18,WR,11,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Joe Reed' AND Anio = 2020),"3),"
(' Gardner Minshew',15,QB,9,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Gardner Minshew' AND Anio = 2020),"3),"
(' Aaron Brewer',31,G,12,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Aaron Brewer' AND Anio = 2020),"3),"
(' Jason Huntley',26,RB,5,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jason Huntley' AND Anio = 2020),"3),"
(' Rico Gafford',17,CB,3,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Rico Gafford' AND Anio = 2020),"3),"
(' Antony Auclair',30,TE,8,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Antony Auclair' AND Anio = 2020),"3),"
(' Cyril Grayson Jr.',30,WR,3,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cyril Grayson Jr.' AND Anio = 2020),"3),"
(' Andy Dalton',9,QB,11,1,-3,-3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andy Dalton' AND Anio = 2020),"3),"
(' Jordan Howard',26,RB,7,1,-3,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Howard' AND Anio = 2020),"3),"
(' Aaron Rodgers',12,QB,16,1,-6,-6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Aaron Rodgers' AND Anio = 2020),"3),"
(' Derrick Henry',31,RB,16,378,2027,94,17,(SELECT Player_ID FROM Player_season WHERE Name = 'Derrick Henry' AND Anio = 2020),"2),"
(' Dalvin Cook',21,RB,14,312,1557,70,16,(SELECT Player_ID FROM Player_season WHERE Name = 'Dalvin Cook' AND Anio = 2020),"2),"
(' Jonathan Taylor',14,RB,15,232,1169,62,11,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonathan Taylor' AND Anio = 2020),"2),"
(' Aaron Jones',12,RB,14,201,1104,77,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Aaron Jones' AND Anio = 2020),"2),"
(' David Montgomery',6,RB,15,247,1070,80,8,(SELECT Player_ID FROM Player_season WHERE Name = 'David Montgomery' AND Anio = 2020),"2),"
(' James Robinson',15,RB,14,240,1070,47,7,(SELECT Player_ID FROM Player_season WHERE Name = 'James Robinson' AND Anio = 2020),"2),"
(' Nick Chubb',8,RB,12,190,1067,59,12,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Chubb' AND Anio = 2020),"2),"
(' Josh Jacobs',17,RB,15,273,1065,28,12,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Jacobs' AND Anio = 2020),"2),"
(' Lamar Jackson',3,QB,15,159,1005,50,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Lamar Jackson' AND Anio = 2020),"2),"
(' Melvin Gordon III',10,RB,15,215,986,65,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Melvin Gordon III' AND Anio = 2020),"2),"
(' Ezekiel Elliott',9,RB,15,244,979,31,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Ezekiel Elliott' AND Anio = 2020),"2),"
(' Ronald Jones',30,RB,14,192,978,98,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Ronald Jones' AND Anio = 2020),"2),"
(' Kenyan Drake',1,RB,15,239,955,69,10,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenyan Drake' AND Anio = 2020),"2),"
(' Alvin Kamara',23,RB,15,187,932,49,16,(SELECT Player_ID FROM Player_season WHERE Name = 'Alvin Kamara' AND Anio = 2020),"2),"
(' Miles Sanders',26,RB,12,164,867,82,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Miles Sanders' AND Anio = 2020),"2),"
(' Kareem Hunt',8,RB,16,198,841,33,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Kareem Hunt' AND Anio = 2020),"2),"
(' Kyler Murray',1,QB,16,133,819,48,11,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyler Murray' AND Anio = 2020),"2),"
(' J.K. Dobbins',3,RB,15,134,805,72,9,(SELECT Player_ID FROM Player_season WHERE Name = 'J.K. Dobbins' AND Anio = 2020),"2),"
(' Clyde Edwards-Helaire',16,RB,13,181,803,31,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Clyde Edwards-Helaire' AND Anio = 2020),"2),"
(' Antonio Gibson',32,RB,14,170,795,40,11,(SELECT Player_ID FROM Player_season WHERE Name = 'Antonio Gibson' AND Anio = 2020),"2),"
(' Gus Edwards',3,RB,16,144,723,36,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Gus Edwards' AND Anio = 2020),"2),"
(' James Conner',27,RB,13,169,721,59,6,(SELECT Player_ID FROM Player_season WHERE Name = 'James Conner' AND Anio = 2020),"2),"
(' David Johnson',13,RB,12,147,691,48,6,(SELECT Player_ID FROM Player_season WHERE Name = 'David Johnson' AND Anio = 2020),"2),"
(' Damien Harris',22,RB,10,137,691,41,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Damien Harris' AND Anio = 2020),"2),"
(' Devin Singletary',4,RB,16,156,687,51,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Devin Singletary' AND Anio = 2020),"2),"
(' Wayne Gallman',24,RB,15,147,682,60,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Wayne Gallman' AND Anio = 2020),"2),"
(' Chris Carson',29,RB,12,141,681,29,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Carson' AND Anio = 2020),"2),"
(' Todd Gurley II',2,RB,15,195,678,35,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Todd Gurley II' AND Anio = 2020),"2),"
(' Latavius Murray',23,RB,15,146,656,36,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Latavius Murray' AND Anio = 2020),"2),"
(' Frank Gore',25,RB,15,187,653,17,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Frank Gore' AND Anio = 2020),"2),"
(' Mike Davis',5,RB,15,165,642,25,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Davis' AND Anio = 2020),"2),"
(' Cam Akers',19,RB,13,145,625,61,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Cam Akers' AND Anio = 2020),"2),"
(' Darrell Henderson Jr.',19,RB,15,138,624,40,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Darrell Henderson Jr.' AND Anio = 2020),"2),"
(' Adrian Peterson',11,RB,16,156,604,38,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Adrian Peterson' AND Anio = 2020),"2),"
(' Jeff Wilson Jr.',28,RB,12,126,600,34,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeff Wilson Jr.' AND Anio = 2020),"2),"
(' Cam Newton',22,QB,15,137,592,49,12,(SELECT Player_ID FROM Player_season WHERE Name = 'Cam Newton' AND Anio = 2020),"2),"
(' Myles Gaskin',20,RB,10,142,584,26,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Myles Gaskin' AND Anio = 2020),"2),"
(' Austin Ekeler',18,RB,10,116,530,27,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Austin Ekeler' AND Anio = 2020),"2),"
(' Raheem Mostert',28,RB,8,104,521,80,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Raheem Mostert' AND Anio = 2020),"2),"
(' D'Andre Swift',11,RB,13,114,521,54,8,(SELECT Player_ID FROM Player_season WHERE Name = 'D'Andre Swift' AND Anio = 2020),"2),"
(' Russell Wilson',29,QB,16,83,513,38,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Russell Wilson' AND Anio = 2020),"2),"
(' Jamaal Williams',12,RB,14,119,505,25,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamaal Williams' AND Anio = 2020),"2),"
(' Phillip Lindsay',10,RB,11,118,502,55,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Phillip Lindsay' AND Anio = 2020),"2),"
(' Zack Moss',4,RB,13,112,481,31,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Zack Moss' AND Anio = 2020),"2),"
(' Brian Hill',2,RB,16,100,465,62,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Brian Hill' AND Anio = 2020),"2),"
(' Taysom Hill',23,QB,16,87,457,43,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Taysom Hill' AND Anio = 2020),"2),"
(' Sony Michel',22,RB,9,79,449,48,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Sony Michel' AND Anio = 2020),"2),"
(' Chase Edmonds',1,RB,16,97,448,32,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Chase Edmonds' AND Anio = 2020),"2),"
(' Deshaun Watson',13,QB,16,90,444,16,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Deshaun Watson' AND Anio = 2020),"2),"
(' Tony Pollard',9,RB,16,101,435,42,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Tony Pollard' AND Anio = 2020),"2),"
(' Alexander Mattison',21,RB,13,96,434,25,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Alexander Mattison' AND Anio = 2020),"2),"
(' Joe Mixon',7,RB,6,119,428,34,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Joe Mixon' AND Anio = 2020),"2),"
(' Devontae Booker',17,RB,16,93,423,43,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Devontae Booker' AND Anio = 2020),"2),"
(' Daniel Jones',24,QB,14,65,423,80,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Daniel Jones' AND Anio = 2020),"2),"
(' Josh Allen',4,QB,16,102,421,24,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Allen' AND Anio = 2020),"2),"
(' Malcolm Brown',19,RB,16,101,419,19,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Malcolm Brown' AND Anio = 2020),"2),"
(' Giovani Bernard',7,RB,16,124,416,15,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Giovani Bernard' AND Anio = 2020),"2),"
(' Nyheim Hines',14,RB,16,89,380,31,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Nyheim Hines' AND Anio = 2020),"2),"
(' Boston Scott',26,RB,16,80,374,56,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Boston Scott' AND Anio = 2020),"2),"
(' Benny Snell Jr.',27,RB,16,111,368,30,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Benny Snell Jr.' AND Anio = 2020),"2),"
(' Leonard Fournette',30,RB,13,97,367,46,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Leonard Fournette' AND Anio = 2020),"2),"
(' J.D. McKissic',32,RB,16,85,365,17,1,(SELECT Player_ID FROM Player_season WHERE Name = 'J.D. McKissic' AND Anio = 2020),"2),"
(' Carlos Hyde',29,RB,10,81,356,50,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Carlos Hyde' AND Anio = 2020),"2),"
(' Joshua Kelley',18,RB,14,111,354,33,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Joshua Kelley' AND Anio = 2020),"2),"
(' Jalen Hurts',26,QB,15,63,354,24,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Hurts' AND Anio = 2020),"2),"
(' Le'Veon Bell',25,RB,11,82,328,16,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Le'Veon Bell' AND Anio = 2020),"2),"
(' Jerick McKinnon',28,RB,16,81,319,55,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Jerick McKinnon' AND Anio = 2020),"2),"
(' Salvon Ahmed',20,RB,6,75,319,31,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Salvon Ahmed' AND Anio = 2020),"2),"
(' Jordan Wilkins',14,RB,15,84,308,22,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Wilkins' AND Anio = 2020),"2),"
(' Patrick Mahomes',16,QB,15,62,308,24,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Patrick Mahomes' AND Anio = 2020),"2),"
(' Kalen Ballage',25,RB,11,91,303,17,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Kalen Ballage' AND Anio = 2020),"2),"
(' Samaje Perine',7,RB,16,63,301,46,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Samaje Perine' AND Anio = 2020),"2),"
(' Mark Ingram II',3,RB,11,72,299,30,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Mark Ingram II' AND Anio = 2020),"2),"
(' Teddy Bridgewater',5,QB,15,53,279,18,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Teddy Bridgewater' AND Anio = 2020),"2),"
(' Carson Wentz',26,QB,12,52,276,40,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Carson Wentz' AND Anio = 2020),"2),"
(' Rex Burkhead',22,RB,10,67,274,18,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Rex Burkhead' AND Anio = 2020),"2),"
(' Justin Jackson',18,RB,9,59,270,36,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Jackson' AND Anio = 2020),"2),"
(' Ito Smith',2,RB,14,63,268,24,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ito Smith' AND Anio = 2020),"2),"
(' Ryan Tannehill',31,QB,16,43,266,45,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Tannehill' AND Anio = 2020),"2),"
(' Peyton Barber',32,RB,16,94,258,15,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Peyton Barber' AND Anio = 2020),"2),"
(' Matt Breida',20,RB,12,59,254,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Breida' AND Anio = 2020),"2),"
(' Ty Johnson',25,RB,13,54,254,34,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ty Johnson' AND Anio = 2020),"2),"
(' AJ Dillon',12,RB,11,46,242,30,2,(SELECT Player_ID FROM Player_season WHERE Name = 'AJ Dillon' AND Anio = 2020),"2),"
(' Alfred Morris',24,RB,9,55,238,20,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Alfred Morris' AND Anio = 2020),"2),"
(' Duke Johnson',13,RB,11,77,235,23,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Duke Johnson' AND Anio = 2020),"2),"
(' Justin Herbert',18,QB,15,55,234,31,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Herbert' AND Anio = 2020),"2),"
(' Cordarrelle Patterson',6,RB,16,64,232,13,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Cordarrelle Patterson' AND Anio = 2020),"2),"
(' La'Mical Perine',25,RB,10,64,232,20,2,(SELECT Player_ID FROM Player_season WHERE Name = 'La'Mical Perine' AND Anio = 2020),"2),"
(' Christian McCaffrey',5,RB,3,59,225,15,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian McCaffrey' AND Anio = 2020),"2),"
(' Sam Darnold',25,QB,12,37,217,46,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Sam Darnold' AND Anio = 2020),"2),"
(' Jeremy McNichols',31,RB,16,47,204,20,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeremy McNichols' AND Anio = 2020),"2),"
(' Curtis Samuel',5,WR,15,41,200,45,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Curtis Samuel' AND Anio = 2020),"2),"
(' Mitchell Trubisky',6,QB,10,33,195,45,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Mitchell Trubisky' AND Anio = 2020),"2),"
(' Kerryon Johnson',11,RB,16,52,181,14,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Kerryon Johnson' AND Anio = 2020),"2),"
(' Devonta Freeman',24,RB,5,54,172,14,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Devonta Freeman' AND Anio = 2020),"2),"
(' Royce Freeman',10,RB,16,35,170,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Royce Freeman' AND Anio = 2020),"2),"
(' Darrel Williams',16,RB,16,39,169,13,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Darrel Williams' AND Anio = 2020),"2),"
(' D'Ernest Johnson',8,RB,16,33,166,28,0,(SELECT Player_ID FROM Player_season WHERE Name = 'D'Ernest Johnson' AND Anio = 2020),"2),"
(' Baker Mayfield',8,QB,16,54,165,28,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Baker Mayfield' AND Anio = 2020),"2),"
(' Drew Lock',10,QB,13,44,160,16,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Drew Lock' AND Anio = 2020),"2),"
(' Josh Adams',25,RB,8,29,157,25,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Adams' AND Anio = 2020),"2),"
(' Trayveon Williams',7,RB,10,26,157,55,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trayveon Williams' AND Anio = 2020),"2),"
(' Kirk Cousins',21,QB,16,32,156,16,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kirk Cousins' AND Anio = 2020),"2),"
(' Rodney Smith',5,RB,7,41,156,13,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Rodney Smith' AND Anio = 2020),"2),"
(' Robert Woods',19,WR,16,24,155,40,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Robert Woods' AND Anio = 2020),"2),"
(' Gardner Minshew',15,QB,9,29,153,16,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Gardner Minshew' AND Anio = 2020),"2),"
(' Ryan Fitzpatrick',20,QB,9,30,151,17,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Fitzpatrick' AND Anio = 2020),"2),"
(' Aaron Rodgers',12,QB,16,38,149,14,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Aaron Rodgers' AND Anio = 2020),"2),"
(' JaMycal Hasty',28,RB,8,39,148,20,1,(SELECT Player_ID FROM Player_season WHERE Name = 'JaMycal Hasty' AND Anio = 2020),"2),"
(' Dare Ogunbowale',15,RB,14,32,145,25,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dare Ogunbowale' AND Anio = 2020),"2),"
(' Joe Burrow',7,QB,10,37,142,23,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Joe Burrow' AND Anio = 2020),"2),"
(' Derek Carr',17,QB,16,39,140,18,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Derek Carr' AND Anio = 2020),"2),"
(' Jalen Richard',17,RB,13,22,123,20,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Richard' AND Anio = 2020),"2),"
(' Tyreek Hill',16,WR,15,13,123,32,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyreek Hill' AND Anio = 2020),"2),"
(' James White',22,RB,14,35,121,10,2,(SELECT Player_ID FROM Player_season WHERE Name = 'James White' AND Anio = 2020),"2),"
(' Dion Lewis',24,RB,16,29,115,19,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Dion Lewis' AND Anio = 2020),"2),"
(' Andy Dalton',9,QB,11,28,114,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andy Dalton' AND Anio = 2020),"2),"
(' Anthony McFarland Jr.',27,RB,11,33,113,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Anthony McFarland Jr.' AND Anio = 2020),"2),"
(' Matthew Stafford',11,QB,16,29,112,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Matthew Stafford' AND Anio = 2020),"2),"
(' J.J. Taylor',22,RB,6,23,110,28,0,(SELECT Player_ID FROM Player_season WHERE Name = 'J.J. Taylor' AND Anio = 2020),"2),"
(' Ke'Shawn Vaughn',30,RB,10,26,109,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ke'Shawn Vaughn' AND Anio = 2020),"2),"
(' Tua Tagovailoa',20,QB,10,36,109,17,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Tua Tagovailoa' AND Anio = 2020),"2),"
(' DeeJay Dallas',29,RB,12,34,108,13,2,(SELECT Player_ID FROM Player_season WHERE Name = 'DeeJay Dallas' AND Anio = 2020),"2),"
(' Ty Montgomery II',23,WR,6,19,101,36,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ty Montgomery II' AND Anio = 2020),"2),"
(' Jared Goff',19,QB,15,51,99,10,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Jared Goff' AND Anio = 2020),"2),"
(' Darwin Thompson',16,RB,14,27,97,14,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Darwin Thompson' AND Anio = 2020),"2),"
(' D'Onta Foreman',31,RB,6,22,95,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'D'Onta Foreman' AND Anio = 2020),"2),"
(' Dak Prescott',9,QB,5,18,93,12,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Dak Prescott' AND Anio = 2020),"2),"
(' Matt Ryan',2,QB,16,29,92,16,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Ryan' AND Anio = 2020),"2),"
(' DeAndre Washington',20,RB,4,31,91,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DeAndre Washington' AND Anio = 2020),"2),"
(' Laviska Shenault Jr.',15,WR,14,18,91,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Laviska Shenault Jr.' AND Anio = 2020),"2),"
(' Marcus Mariota',17,QB,1,9,88,26,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Marcus Mariota' AND Anio = 2020),"2),"
(' Travis Homer',29,RB,9,25,88,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Travis Homer' AND Anio = 2020),"2),"
(' CeeDee Lamb',9,WR,16,10,82,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'CeeDee Lamb' AND Anio = 2020),"2),"
(' Alex Collins',29,RB,3,18,77,13,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Alex Collins' AND Anio = 2020),"2),"
(' Brandon Aiyuk',28,WR,12,6,77,38,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Aiyuk' AND Anio = 2020),"2),"
(' Troymaine Pope',18,RB,6,15,76,26,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Troymaine Pope' AND Anio = 2020),"2),"
(' Corey Clement',26,RB,15,21,75,7,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Corey Clement' AND Anio = 2020),"2),"
(' Tarik Cohen',6,RB,3,14,74,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tarik Cohen' AND Anio = 2020),"2),"
(' Odell Beckham Jr.',8,WR,7,3,72,50,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Odell Beckham Jr.' AND Anio = 2020),"2),"
(' Patrick Laird',20,RB,16,13,72,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Patrick Laird' AND Anio = 2020),"2),"
(' T.J. Yeldon',4,RB,3,10,70,34,0,(SELECT Player_ID FROM Player_season WHERE Name = 'T.J. Yeldon' AND Anio = 2020),"2),"
(' Devin Duvernay',3,WR,16,4,70,42,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Devin Duvernay' AND Anio = 2020),"2),"
(' Robert Griffin III',3,QB,4,12,69,39,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Robert Griffin III' AND Anio = 2020),"2),"
(' Reggie Bonnafon',5,RB,2,12,69,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Reggie Bonnafon' AND Anio = 2020),"2),"
(' Tyler Ervin',12,RB,8,13,67,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Ervin' AND Anio = 2020),"2),"
(' Ryan Finley',7,QB,5,11,66,23,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Finley' AND Anio = 2020),"2),"
(' Ray-Ray McCloud III',27,WR,16,4,65,58,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ray-Ray McCloud III' AND Anio = 2020),"2),"
(' Kyle Juszczyk',28,FB,16,17,64,10,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Juszczyk' AND Anio = 2020),"2),"
(' Buddy Howell',13,RB,14,16,64,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Buddy Howell' AND Anio = 2020),"2),"
(' Antonio Williams',4,RB,1,12,63,18,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Antonio Williams' AND Anio = 2020),"2),"
(' David Moore',29,WR,16,8,61,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'David Moore' AND Anio = 2020),"2),"
(' Jordan Howard',26,RB,7,35,60,11,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Howard' AND Anio = 2020),"2),"
(' Justice Hill',3,RB,12,12,60,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Justice Hill' AND Anio = 2020),"2),"
(' Mike Boone',21,RB,16,11,59,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Boone' AND Anio = 2020),"2),"
(' John Wolford',19,QB,1,6,56,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'John Wolford' AND Anio = 2020),"2),"
(' Darrynton Evans',31,RB,5,14,54,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Darrynton Evans' AND Anio = 2020),"2),"
(' Tevin Coleman',28,RB,8,28,53,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tevin Coleman' AND Anio = 2020),"2),"
(' Deonte Harty',23,WR,9,6,51,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Deonte Harty' AND Anio = 2020),"2),"
(' Sterling Shepard',24,WR,12,6,49,23,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Sterling Shepard' AND Anio = 2020),"2),"
(' Tyler Boyd',7,WR,15,5,49,25,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Boyd' AND Anio = 2020),"2),"
(' Henry Ruggs III',17,WR,13,9,49,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Henry Ruggs III' AND Anio = 2020),"2),"
(' Dontrell Hilliard',8,RB,5,9,48,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dontrell Hilliard' AND Anio = 2020),"2),"
(' Shawn Williams',7,S,13,2,46,39,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Shawn Williams' AND Anio = 2020),"2),"
(' Dwayne Haskins',32,QB,7,20,46,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Dwayne Haskins' AND Anio = 2020),"2),"
(' DeMichael Harris',14,WR,7,6,46,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DeMichael Harris' AND Anio = 2020),"2),"
(' Ameer Abdullah',21,RB,16,8,42,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ameer Abdullah' AND Anio = 2020),"2),"
(' KJ Hamler',10,WR,13,9,40,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'KJ Hamler' AND Anio = 2020),"2),"
(' Rashaad Penny',29,RB,3,11,34,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Rashaad Penny' AND Anio = 2020),"2),"
(' Saquon Barkley',24,RB,2,19,34,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Saquon Barkley' AND Anio = 2020),"2),"
(' Artavis Pierce',6,RB,5,6,34,23,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Artavis Pierce' AND Anio = 2020),"2),"
(' Cooper Kupp',19,WR,15,4,33,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cooper Kupp' AND Anio = 2020),"2),"
(' Jamal Agnew',11,WR,14,6,33,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamal Agnew' AND Anio = 2020),"2),"
(' Trenton Cannon',5,RB,14,10,33,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trenton Cannon' AND Anio = 2020),"2),"
(' Lynn Bowden Jr.',20,WR,10,9,32,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Lynn Bowden Jr.' AND Anio = 2020),"2),"
(' LeSean McCoy',30,RB,10,10,31,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'LeSean McCoy' AND Anio = 2020),"2),"
(' Bo Scarbrough',29,RB,1,6,31,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Bo Scarbrough' AND Anio = 2020),"2),"
(' Mecole Hardman',16,WR,16,4,31,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mecole Hardman' AND Anio = 2020),"2),"
(' Terry McLaurin',32,WR,15,2,30,27,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Terry McLaurin' AND Anio = 2020),"2),"
(' Braxton Berrios',25,WR,16,3,29,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Braxton Berrios' AND Anio = 2020),"2),"
(' Joe Reed',18,WR,11,5,29,8,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Joe Reed' AND Anio = 2020),"2),"
(' Jeremy Chinn',5,S,15,2,29,28,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeremy Chinn' AND Anio = 2020),"2),"
(' Garrett Gilbert',9,QB,1,3,28,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Garrett Gilbert' AND Anio = 2020),"2),"
(' Jeff Driskel',10,QB,3,6,28,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeff Driskel' AND Anio = 2020),"2),"
(' C.J. Beathard',28,QB,6,6,28,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Beathard' AND Anio = 2020),"2),"
(' Jaylen Samuels',27,RB,14,9,28,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaylen Samuels' AND Anio = 2020),"2),"
(' Tee Higgins',7,WR,16,5,28,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tee Higgins' AND Anio = 2020),"2),"
(' Brandon Allen',7,QB,5,13,27,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Allen' AND Anio = 2020),"2),"
(' Evan Engram',24,TE,16,6,26,9,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Evan Engram' AND Anio = 2020),"2),"
(' Kyle Allen',32,QB,4,7,26,13,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Allen' AND Anio = 2020),"2),"
(' Deebo Samuel Sr.',28,WR,7,8,26,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Deebo Samuel Sr.' AND Anio = 2020),"2),"
(' Marlon Mack',14,RB,1,4,26,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marlon Mack' AND Anio = 2020),"2),"
(' Michael Pittman Jr.',14,WR,13,3,26,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Pittman Jr.' AND Anio = 2020),"2),"
(' Jalen Reagor',26,WR,11,4,26,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Reagor' AND Anio = 2020),"2),"
(' Jimmy Garoppolo',28,QB,6,10,25,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jimmy Garoppolo' AND Anio = 2020),"2),"
(' Tommy Stevens',5,TE,1,4,24,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tommy Stevens' AND Anio = 2020),"2),"
(' Rico Dowdle',9,RB,15,7,24,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Rico Dowdle' AND Anio = 2020),"2),"
(' Clayton Fejedelem',20,S,13,2,23,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Clayton Fejedelem' AND Anio = 2020),"2),"
(' Tyler Huntley',3,QB,2,10,23,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Huntley' AND Anio = 2020),"2),"
(' Gunner Olszewski',22,WR,13,5,23,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Gunner Olszewski' AND Anio = 2020),"2),"
(' Joe Flacco',25,QB,5,6,22,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Joe Flacco' AND Anio = 2020),"2),"
(' Julian Edelman',22,WR,6,2,22,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Julian Edelman' AND Anio = 2020),"2),"
(' Taylor Heinicke',32,QB,1,3,22,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Taylor Heinicke' AND Anio = 2020),"2),"
(' Ben DiNucci',9,QB,3,6,22,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ben DiNucci' AND Anio = 2020),"2),"
(' DJ Moore',5,WR,15,2,22,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DJ Moore' AND Anio = 2020),"2),"
(' Antonio Gandy-Golden',32,TE,6,1,22,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Antonio Gandy-Golden' AND Anio = 2020),"2),"
(' Isaiah Zuber',22,WR,4,2,21,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Isaiah Zuber' AND Anio = 2020),"2),"
(' Chris Thompson',15,RB,8,7,20,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Thompson' AND Anio = 2020),"2),"
(' Jakeem Grant Sr.',20,WR,14,3,20,29,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jakeem Grant Sr.' AND Anio = 2020),"2),"
(' Joshua Dobbs',27,QB,1,2,20,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Joshua Dobbs' AND Anio = 2020),"2),"
(' Cameron Batson',31,WR,12,4,20,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cameron Batson' AND Anio = 2020),"2),"
(' Darnell Mooney',6,WR,16,4,20,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Darnell Mooney' AND Anio = 2020),"2),"
(' Diontae Spencer',10,WR,11,3,19,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Diontae Spencer' AND Anio = 2020),"2),"
(' Jacoby Brissett',14,QB,11,17,19,5,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Jacoby Brissett' AND Anio = 2020),"2),"
(' C.J. Prosise',13,RB,10,10,19,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Prosise' AND Anio = 2020),"2),"
(' Penny Hart',29,WR,13,1,19,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Penny Hart' AND Anio = 2020),"2),"
(' Jason Huntley',26,RB,5,5,19,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jason Huntley' AND Anio = 2020),"2),"
(' Michael Burton',23,FB,15,7,18,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Burton' AND Anio = 2020),"2),"
(' David Blough',11,QB,1,1,18,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'David Blough' AND Anio = 2020),"2),"
(' Steven Sims',32,WR,12,1,18,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Steven Sims' AND Anio = 2020),"2),"
(' C.J. Ham',21,FB,15,5,18,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Ham' AND Anio = 2020),"2),"
(' Mike Glennon',15,QB,5,6,17,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Glennon' AND Anio = 2020),"2),"
(' George Kittle',28,TE,8,2,17,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'George Kittle' AND Anio = 2020),"2),"
(' Trace McSorley',3,QB,2,5,17,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trace McSorley' AND Anio = 2020),"2),"
(' Allen Lazard',12,WR,10,2,17,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Allen Lazard' AND Anio = 2020),"2),"
(' Tyron Billy-Johnson',18,WR,12,3,17,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyron Billy-Johnson' AND Anio = 2020),"2),"
(' Chase Daniel',11,QB,4,2,16,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chase Daniel' AND Anio = 2020),"2),"
(' Blaine Gabbert',30,QB,4,9,16,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Blaine Gabbert' AND Anio = 2020),"2),"
(' Parris Campbell',14,WR,2,2,16,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Parris Campbell' AND Anio = 2020),"2),"
(' Isaiah Wright',32,WR,14,3,16,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Isaiah Wright' AND Anio = 2020),"2),"
(' Chase Claypool',27,WR,16,10,16,8,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Chase Claypool' AND Anio = 2020),"2),"
(' Adam Thielen',21,WR,15,3,15,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Adam Thielen' AND Anio = 2020),"2),"
(' Robbie Chosen',5,WR,16,4,15,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Robbie Chosen' AND Anio = 2020),"2),"
(' Elijhaa Penny',24,RB,14,6,15,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Elijhaa Penny' AND Anio = 2020),"2),"
(' Damiere Byrd',22,WR,16,2,15,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Damiere Byrd' AND Anio = 2020),"2),"
(' Dwayne Washington',23,RB,11,8,15,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dwayne Washington' AND Anio = 2020),"2),"
(' Chris Streveler',1,QB,5,4,15,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Streveler' AND Anio = 2020),"2),"
(' Diontae Johnson',27,WR,15,3,15,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Diontae Johnson' AND Anio = 2020),"2),"
(' Theo Riddick',17,RB,4,6,14,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Theo Riddick' AND Anio = 2020),"2),"
(' Tommylee Lewis',23,WR,5,2,14,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tommylee Lewis' AND Anio = 2020),"2),"
(' Jamison Crowder',25,WR,12,1,14,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamison Crowder' AND Anio = 2020),"2),"
(' Amari Cooper',9,WR,16,6,14,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Amari Cooper' AND Anio = 2020),"2),"
(' Scotty Miller',30,WR,16,3,14,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Scotty Miller' AND Anio = 2020),"2),"
(' Marquez Valdes-Scantling',12,WR,16,4,13,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marquez Valdes-Scantling' AND Anio = 2020),"2),"
(' Jake Luton',15,QB,3,1,13,13,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jake Luton' AND Anio = 2020),"2),"
(' Tony Jones Jr.',23,RB,1,3,13,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tony Jones Jr.' AND Anio = 2020),"2),"
(' DeSean Jackson',26,WR,5,1,12,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DeSean Jackson' AND Anio = 2020),"2),"
(' Colt McCoy',24,QB,4,9,12,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Colt McCoy' AND Anio = 2020),"2),"
(' Emmanuel Sanders',23,WR,14,1,12,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Emmanuel Sanders' AND Anio = 2020),"2),"
(' Nate Sudfeld',26,QB,1,2,12,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nate Sudfeld' AND Anio = 2020),"2),"
(' Anthony Miller',6,WR,16,2,12,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Anthony Miller' AND Anio = 2020),"2),"
(' Josh Malone',25,WR,4,1,12,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Malone' AND Anio = 2020),"2),"
(' Ben Roethlisberger',27,QB,15,25,11,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ben Roethlisberger' AND Anio = 2020),"2),"
(' Barkevious Mingo',6,LB,16,1,11,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Barkevious Mingo' AND Anio = 2020),"2),"
(' LeVante Bellamy',10,RB,5,4,11,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'LeVante Bellamy' AND Anio = 2020),"2),"
(' Ashton Dulin',14,WR,13,2,11,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ashton Dulin' AND Anio = 2020),"2),"
(' Jarvis Landry',8,WR,15,4,10,5,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jarvis Landry' AND Anio = 2020),"2),"
(' Logan Woodside',31,QB,6,7,10,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Logan Woodside' AND Anio = 2020),"2),"
(' Senorise Perry',31,RB,7,2,9,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Senorise Perry' AND Anio = 2020),"2),"
(' Nathan Peterman',17,QB,1,1,9,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nathan Peterman' AND Anio = 2020),"2),"
(' Russell Gage',2,WR,16,2,9,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Russell Gage' AND Anio = 2020),"2),"
(' Isaiah McKenzie',4,WR,16,10,9,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Isaiah McKenzie' AND Anio = 2020),"2),"
(' Jakobi Meyers',22,WR,14,2,9,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jakobi Meyers' AND Anio = 2020),"2),"
(' Alex Armah',5,RB,16,6,9,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Alex Armah' AND Anio = 2020),"2),"
(' Scottie Phillips',13,RB,8,2,9,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Scottie Phillips' AND Anio = 2020),"2),"
(' Malik Taylor',12,WR,15,1,9,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Malik Taylor' AND Anio = 2020),"2),"
(' Brian Hoyer',22,QB,1,1,8,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brian Hoyer' AND Anio = 2020),"2),"
(' Anthony Sherman',16,FB,13,3,8,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Anthony Sherman' AND Anio = 2020),"2),"
(' Nick Mullens',28,QB,10,9,8,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Mullens' AND Anio = 2020),"2),"
(' Dexter Williams',12,RB,3,2,8,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dexter Williams' AND Anio = 2020),"2),"
(' Tyrod Taylor',18,QB,2,6,7,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyrod Taylor' AND Anio = 2020),"2),"
(' Keith Smith',2,FB,16,4,7,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Keith Smith' AND Anio = 2020),"2),"
(' Alex Erickson',7,WR,16,5,7,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Alex Erickson' AND Anio = 2020),"2),"
(' Brandon Powell',2,WR,15,2,7,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Powell' AND Anio = 2020),"2),"
(' Kendall Hinton',10,WR,1,2,7,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kendall Hinton' AND Anio = 2020),"2),"
(' Jarrett Stidham',22,QB,5,7,7,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jarrett Stidham' AND Anio = 2020),"2),"
(' Equanimeous St. Brown',12,WR,12,1,7,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Equanimeous St. Brown' AND Anio = 2020),"2),"
(' Gabe Nabers',18,FB,16,2,7,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Gabe Nabers' AND Anio = 2020),"2),"
(' Tom Brady',30,QB,16,30,6,4,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Tom Brady' AND Anio = 2020),"2),"
(' Breshad Perriman',25,WR,12,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Breshad Perriman' AND Anio = 2020),"2),"
(' John Lovett',12,FB,8,3,6,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'John Lovett' AND Anio = 2020),"2),"
(' Nick Bellore',29,LB,16,1,5,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Bellore' AND Anio = 2020),"2),"
(' Logan Thomas',32,TE,16,3,5,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Logan Thomas' AND Anio = 2020),"2),"
(' Jonathan Williams',11,RB,5,1,5,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonathan Williams' AND Anio = 2020),"2),"
(' Josh Reynolds',19,WR,16,1,5,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Reynolds' AND Anio = 2020),"2),"
(' Cam Sims',32,WR,16,1,5,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cam Sims' AND Anio = 2020),"2),"
(' Malcolm Perry',20,RB,9,3,5,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Malcolm Perry' AND Anio = 2020),"2),"
(' Donte Moncrief',22,WR,6,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Donte Moncrief' AND Anio = 2020),"2),"
(' Andy Janovich',8,FB,14,2,4,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andy Janovich' AND Anio = 2020),"2),"
(' Jonnu Smith',31,TE,15,2,4,3,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonnu Smith' AND Anio = 2020),"2),"
(' Noah Brown',9,WR,16,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Noah Brown' AND Anio = 2020),"2),"
(' Jordan Akins',13,TE,13,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Akins' AND Anio = 2020),"2),"
(' Tony Brooks-James',2,RB,1,3,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tony Brooks-James' AND Anio = 2020),"2),"
(' Alec Ingold',17,FB,16,3,4,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Alec Ingold' AND Anio = 2020),"2),"
(' Amani Hooker',31,S,16,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Amani Hooker' AND Anio = 2020),"2),"
(' Craig Reynolds',15,RB,2,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Craig Reynolds' AND Anio = 2020),"2),"
(' Alex Smith',32,QB,8,10,3,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Alex Smith' AND Anio = 2020),"2),"
(' Mohamed Sanu',11,WR,10,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mohamed Sanu' AND Anio = 2020),"2),"
(' Sammy Watkins',16,WR,10,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Sammy Watkins' AND Anio = 2020),"2),"
(' Trey Burton',14,TE,13,2,3,2,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Trey Burton' AND Anio = 2020),"2),"
(' Darian Thompson',9,S,15,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Darian Thompson' AND Anio = 2020),"2),"
(' JoJo Natson',8,WR,3,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'JoJo Natson' AND Anio = 2020),"2),"
(' C.J. Board',24,WR,14,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Board' AND Anio = 2020),"2),"
(' Austin Walter',28,RB,4,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Austin Walter' AND Anio = 2020),"2),"
(' Qadree Ollison',2,RB,3,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Qadree Ollison' AND Anio = 2020),"2),"
(' Tre'Quan Smith',23,WR,14,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tre'Quan Smith' AND Anio = 2020),"2),"
(' C.J. Moore',11,S,12,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Moore' AND Anio = 2020),"2),"
(' Christian Kirk',1,WR,14,2,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian Kirk' AND Anio = 2020),"2),"
(' Terry Godwin',15,WR,3,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Terry Godwin' AND Anio = 2020),"2),"
(' Danny Amendola',11,WR,14,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Danny Amendola' AND Anio = 2020),"2),"
(' Blake Bell',9,TE,16,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Blake Bell' AND Anio = 2020),"2),"
(' D.J. Foster',1,RB,10,2,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'D.J. Foster' AND Anio = 2020),"2),"
(' Sharrod Neasman',2,S,16,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Sharrod Neasman' AND Anio = 2020),"2),"
(' Keelan Cole Sr.',15,WR,16,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Keelan Cole Sr.' AND Anio = 2020),"2),"
(' Gerald Everett',19,TE,16,1,2,2,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Gerald Everett' AND Anio = 2020),"2),"
(' Javon Wims',6,WR,13,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Javon Wims' AND Anio = 2020),"2),"
(' Myles Hartsfield',5,S,16,2,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Myles Hartsfield' AND Anio = 2020),"2),"
(' Justin Jefferson',21,WR,16,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Jefferson' AND Anio = 2020),"2),"
(' Nick Foles',6,QB,9,16,1,7,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Foles' AND Anio = 2020),"2),"
(' DeAndre Hopkins',1,WR,16,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DeAndre Hopkins' AND Anio = 2020),"2),"
(' Jeff Heath',17,S,13,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeff Heath' AND Anio = 2020),"2),"
(' Tyler Higbee',19,TE,15,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Higbee' AND Anio = 2020),"2),"
(' Marvin Hall',11,WR,12,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marvin Hall' AND Anio = 2020),"2),"
(' Stefon Diggs',4,WR,16,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Stefon Diggs' AND Anio = 2020),"2),"
(' Michael Thomas',23,WR,7,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Thomas' AND Anio = 2020),"2),"
(' Mike Williams',18,WR,15,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Williams' AND Anio = 2020),"2),"
(' Mike Thomas',7,WR,14,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Thomas' AND Anio = 2020),"2),"
(' Devine Ozigbo',15,RB,8,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Devine Ozigbo' AND Anio = 2020),"2),"
(' Calvin Ridley',2,WR,15,5,1,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Calvin Ridley' AND Anio = 2020),"2),"
(' Marquise Brown',3,WR,16,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marquise Brown' AND Anio = 2020),"2),"
(' Brandon Zylstra',5,WR,16,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Zylstra' AND Anio = 2020),"2),"
(' John Hightower',26,WR,13,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'John Hightower' AND Anio = 2020),"2),"
(' Chris Jones',9,P,8,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Jones' AND Anio = 2020),"2),"
(' Sam Martin',10,P,16,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Sam Martin' AND Anio = 2020),"2),"
(' Matt Skura',3,C,15,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Skura' AND Anio = 2020),"2),"
(' William Fuller V',13,WR,11,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'William Fuller V' AND Anio = 2020),"2),"
(' Jason Cabinda',11,FB,16,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jason Cabinda' AND Anio = 2020),"2),"
(' Ryan Nall',6,FB,16,3,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Nall' AND Anio = 2020),"2),"
(' AJ Cole',17,P,16,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'AJ Cole' AND Anio = 2020),"2),"
(' Olamide Zaccheaus',2,WR,11,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Olamide Zaccheaus' AND Anio = 2020),"2),"
(' Jalen Guyton',18,WR,16,2,0,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Guyton' AND Anio = 2020),"2),"
(' T.J. Hockenson',11,TE,16,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'T.J. Hockenson' AND Anio = 2020),"2),"
(' Trevon Wesco',25,TE,12,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trevon Wesco' AND Anio = 2020),"2),"
(' N'Keal Harry',22,WR,14,2,0,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'N'Keal Harry' AND Anio = 2020),"2),"
(' Gabe Davis',4,WR,16,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Gabe Davis' AND Anio = 2020),"2),"
(' Keenan Allen',18,WR,14,1,-1,-1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Keenan Allen' AND Anio = 2020),"2),"
(' Allen Robinson II',6,WR,16,1,-1,-1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Allen Robinson II' AND Anio = 2020),"2),"
(' Patrick Ricard',3,FB,15,1,-1,-1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Patrick Ricard' AND Anio = 2020),"2),"
(' Darius Slayton',24,WR,16,2,-1,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Darius Slayton' AND Anio = 2020),"2),"
(' Van Jefferson',19,WR,16,1,-1,-1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Van Jefferson' AND Anio = 2020),"2),"
(' Drew Brees',23,QB,12,18,-2,3,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Drew Brees' AND Anio = 2020),"2),"
(' Chad Henne',16,QB,3,7,-2,1,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Chad Henne' AND Anio = 2020),"2),"
(' Antonio Brown',30,WR,8,2,-2,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Antonio Brown' AND Anio = 2020),"2),"
(' Geno Smith',29,QB,1,2,-2,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Geno Smith' AND Anio = 2020),"2),"
(' PJ Walker',5,QB,4,5,-2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'PJ Walker' AND Anio = 2020),"2),"
(' Easton Stick',18,QB,1,1,-2,-2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Easton Stick' AND Anio = 2020),"2),"
(' Jamie Gillan',8,P,16,1,-2,-2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamie Gillan' AND Anio = 2020),"2),"
(' Andre Roberts',4,WR,15,1,-3,-3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andre Roberts' AND Anio = 2020),"2),"
(' Kalif Raymond',31,WR,15,1,-3,-3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kalif Raymond' AND Anio = 2020),"2),"
(' Cole Kmet',6,TE,16,1,-3,-3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cole Kmet' AND Anio = 2020),"2),"
(' Matt Schaub',2,QB,1,3,-4,-1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Schaub' AND Anio = 2020),"2),"
(' Greg Ward',26,WR,16,2,-4,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Greg Ward' AND Anio = 2020),"2),"
(' Brett Rypien',10,QB,3,5,-5,-1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brett Rypien' AND Anio = 2020),"2),"
(' Matt Barkley',4,QB,5,6,-6,-1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Barkley' AND Anio = 2020),"2),"
(' Jameis Winston',23,QB,4,8,-6,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jameis Winston' AND Anio = 2020),"2),"
(' Mason Rudolph',27,QB,5,7,-6,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mason Rudolph' AND Anio = 2020),"2),"
(' Andy Isabella',1,WR,13,1,-6,-6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andy Isabella' AND Anio = 2020),"2),"
(' Philip Rivers',14,QB,16,18,-8,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Philip Rivers' AND Anio = 2020),"2),"
(' Tim Boyle',12,QB,8,13,-9,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tim Boyle' AND Anio = 2020),"2),"
(' Cedrick Wilson Jr.',9,WR,16,3,-12,-1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cedrick Wilson Jr.' AND Anio = 2020),"2),"
(' Adrian Killins',26,RB,1,1,-12,-12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Adrian Killins' AND Anio = 2020),"2),"
(' Ty Long',18,P,16,1,-28,-28,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ty Long' AND Anio = 2020),"2),"
(' Tom Brady ',30,QB,17,719,5316,62,43,(SELECT Player_ID FROM Player_season WHERE Name = 'Tom Brady ' AND Anio = 2021),"1),"
(' Justin Herbert ',18,QB,17,672,5014,72,38,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Herbert ' AND Anio = 2021),"1),"
(' Matthew Stafford ',19,QB,17,601,4886,79,41,(SELECT Player_ID FROM Player_season WHERE Name = 'Matthew Stafford ' AND Anio = 2021),"1),"
(' Patrick Mahomes ',16,QB,17,658,4839,75,37,(SELECT Player_ID FROM Player_season WHERE Name = 'Patrick Mahomes ' AND Anio = 2021),"1),"
(' Derek Carr ',17,QB,17,626,4804,61,23,(SELECT Player_ID FROM Player_season WHERE Name = 'Derek Carr ' AND Anio = 2021),"1),"
(' Joe Burrow ',7,QB,16,520,4611,82,34,(SELECT Player_ID FROM Player_season WHERE Name = 'Joe Burrow ' AND Anio = 2021),"1),"
(' Dak Prescott ',9,QB,16,596,4449,51,37,(SELECT Player_ID FROM Player_season WHERE Name = 'Dak Prescott ' AND Anio = 2021),"1),"
(' Josh Allen ',4,QB,17,646,4407,61,36,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Allen ' AND Anio = 2021),"1),"
(' Kirk Cousins ',21,QB,16,561,4221,64,33,(SELECT Player_ID FROM Player_season WHERE Name = 'Kirk Cousins ' AND Anio = 2021),"1),"
(' Aaron Rodgers ',12,QB,16,531,4115,75,37,(SELECT Player_ID FROM Player_season WHERE Name = 'Aaron Rodgers ' AND Anio = 2021),"1),"
(' Matt Ryan ',2,QB,17,560,3968,64,20,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Ryan ' AND Anio = 2021),"1),"
(' Jimmy Garoppolo ',28,QB,15,441,3810,83,20,(SELECT Player_ID FROM Player_season WHERE Name = 'Jimmy Garoppolo ' AND Anio = 2021),"1),"
(' Mac Jones ',22,QB,17,521,3801,75,22,(SELECT Player_ID FROM Player_season WHERE Name = 'Mac Jones ' AND Anio = 2021),"1),"
(' Kyler Murray ',1,QB,14,481,3787,77,24,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyler Murray ' AND Anio = 2021),"1),"
(' Ben Roethlisberger ',27,QB,16,605,3740,59,22,(SELECT Player_ID FROM Player_season WHERE Name = 'Ben Roethlisberger ' AND Anio = 2021),"1),"
(' Ryan Tannehill ',31,QB,17,531,3734,57,21,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Tannehill ' AND Anio = 2021),"1),"
(' Trevor Lawrence ',15,QB,17,602,3641,58,12,(SELECT Player_ID FROM Player_season WHERE Name = 'Trevor Lawrence ' AND Anio = 2021),"1),"
(' Carson Wentz ',14,QB,17,516,3563,76,27,(SELECT Player_ID FROM Player_season WHERE Name = 'Carson Wentz ' AND Anio = 2021),"1),"
(' Taylor Heinicke ',32,QB,16,494,3419,73,20,(SELECT Player_ID FROM Player_season WHERE Name = 'Taylor Heinicke ' AND Anio = 2021),"1),"
(' Jared Goff ',11,QB,14,494,3245,63,19,(SELECT Player_ID FROM Player_season WHERE Name = 'Jared Goff ' AND Anio = 2021),"1),"
(' Jalen Hurts ',26,QB,15,432,3144,91,16,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Hurts ' AND Anio = 2021),"1),"
(' Russell Wilson ',29,QB,14,400,3113,69,25,(SELECT Player_ID FROM Player_season WHERE Name = 'Russell Wilson ' AND Anio = 2021),"1),"
(' Lamar Jackson ',3,QB,12,382,2882,49,16,(SELECT Player_ID FROM Player_season WHERE Name = 'Lamar Jackson ' AND Anio = 2021),"1),"
(' Davis Mills ',13,QB,13,394,2664,67,16,(SELECT Player_ID FROM Player_season WHERE Name = 'Davis Mills ' AND Anio = 2021),"1),"
(' Tua Tagovailoa ',20,QB,13,388,2653,65,16,(SELECT Player_ID FROM Player_season WHERE Name = 'Tua Tagovailoa ' AND Anio = 2021),"1),"
(' Sam Darnold ',5,QB,12,406,2527,63,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Sam Darnold ' AND Anio = 2021),"1),"
(' Zach Wilson ',25,QB,13,383,2334,54,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Wilson ' AND Anio = 2021),"1),"
(' Andy Dalton ',6,QB,8,236,1515,60,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Andy Dalton ' AND Anio = 2021),"1),"
(' Jacoby Brissett ',20,QB,11,225,1283,52,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Jacoby Brissett ' AND Anio = 2021),"1),"
(' Trevor Siemian ',23,QB,6,188,1154,46,11,(SELECT Player_ID FROM Player_season WHERE Name = 'Trevor Siemian ' AND Anio = 2021),"1),"
(' Tyler Huntley ',3,QB,7,188,1081,43,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Huntley ' AND Anio = 2021),"1),"
(' Taysom Hill ',23,QB,12,134,978,70,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Taysom Hill ' AND Anio = 2021),"1),"
(' Tyrod Taylor ',13,QB,6,150,966,52,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyrod Taylor ' AND Anio = 2021),"1),"
(' Mike White ',25,QB,4,132,953,28,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike White ' AND Anio = 2021),"1),"
(' Mike Glennon ',24,QB,6,167,790,60,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Glennon ' AND Anio = 2021),"1),"
(' Drew Lock ',10,QB,6,111,787,44,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Drew Lock ' AND Anio = 2021),"1),"
(' Colt McCoy ',1,QB,8,99,740,50,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Colt McCoy ' AND Anio = 2021),"1),"
(' Geno Smith ',29,QB,4,95,702,84,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Geno Smith ' AND Anio = 2021),"1),"
(' Cam Newton ',5,QB,8,126,684,64,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Cam Newton ' AND Anio = 2021),"1),"
(' Josh Johnson ',25,QB,4,85,638,28,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Johnson ' AND Anio = 2021),"1),"
(' Trey Lance ',28,QB,6,71,603,76,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Trey Lance ' AND Anio = 2021),"1),"
(' Tim Boyle ',11,QB,5,94,526,42,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Tim Boyle ' AND Anio = 2021),"1),"
(' Case Keenum ',8,QB,7,72,462,34,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Case Keenum ' AND Anio = 2021),"1),"
(' Gardner Minshew ',26,QB,4,60,439,36,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Gardner Minshew ' AND Anio = 2021),"1),"
(' Cooper Rush ',9,QB,5,47,422,73,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Cooper Rush ' AND Anio = 2021),"1),"
(' Jordan Love ',12,QB,6,62,411,62,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Love ' AND Anio = 2021),"1),"
(' PJ Walker ',5,QB,5,66,362,24,1,(SELECT Player_ID FROM Player_season WHERE Name = 'PJ Walker ' AND Anio = 2021),"1),"
(' Joe Flacco ',25,QB,2,42,338,62,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Joe Flacco ' AND Anio = 2021),"1),"
(' Mason Rudolph ',27,QB,2,58,277,36,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Mason Rudolph ' AND Anio = 2021),"1),"
(' Nick Foles ',6,QB,1,35,250,30,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Foles ' AND Anio = 2021),"1),"
(' Brian Hoyer ',22,QB,5,11,227,48,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Brian Hoyer ' AND Anio = 2021),"1),"
(' Jake Fromm ',24,QB,3,60,210,36,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jake Fromm ' AND Anio = 2021),"1),"
(' Garrett Gilbert ',32,QB,1,31,194,46,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Garrett Gilbert ' AND Anio = 2021),"1),"
(' Sean Mannion ',21,QB,1,36,189,30,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Sean Mannion ' AND Anio = 2021),"1),"
(' Brandon Allen ',7,QB,6,34,149,26,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Allen ' AND Anio = 2021),"1),"
(' Nick Mullens ',8,QB,1,30,147,25,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Mullens ' AND Anio = 2021),"1),"
(' Ian Book ',23,QB,1,20,135,56,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ian Book ' AND Anio = 2021),"1),"
(' Kyle Allen ',32,QB,2,19,120,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Allen ' AND Anio = 2021),"1),"
(' Cedrick Wilson Jr.',9,WR,16,3,88,35,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cedrick Wilson Jr.' AND Anio = 2021),"1),"
(' Chad Henne ',16,QB,4,16,82,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chad Henne ' AND Anio = 2021),"1),"
(' Tom Kennedy ',11,WR,12,1,75,75,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tom Kennedy ' AND Anio = 2021),"1),"
(' Blaine Gabbert ',30,QB,6,11,67,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Blaine Gabbert ' AND Anio = 2021),"1),"
(' Tyler Boyd ',7,WR,16,1,46,46,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Boyd ' AND Anio = 2021),"1),"
(' Jakobi Meyers ',22,WR,17,2,45,30,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jakobi Meyers ' AND Anio = 2021),"1),"
(' Mitchell Trubisky ',4,QB,6,8,43,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mitchell Trubisky ' AND Anio = 2021),"1),"
(' Jack Fox ',11,P,17,3,38,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jack Fox ' AND Anio = 2021),"1),"
(' Justin Jefferson ',21,WR,17,4,35,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Jefferson ' AND Anio = 2021),"1),"
(' Christian Kirk ',1,WR,17,1,33,33,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian Kirk ' AND Anio = 2021),"1),"
(' Kendrick Bourne ',22,WR,17,1,25,25,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kendrick Bourne ' AND Anio = 2021),"1),"
(' Jacob Eason ',14,QB,1,5,25,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jacob Eason ' AND Anio = 2021),"1),"
(' Deebo Samuel ',28,WR,16,2,24,24,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Deebo Samuel ' AND Anio = 2021),"1),"
(' Chris Banjo ',1,S,16,1,23,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Banjo ' AND Anio = 2021),"1),"
(' Josh Rosen ',2,QB,4,11,19,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Rosen ' AND Anio = 2021),"1),"
(' Kadarius Toney ',24,WR,10,3,19,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kadarius Toney ' AND Anio = 2021),"1),"
(' Courtland Sutton ',10,WR,17,1,16,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Courtland Sutton ' AND Anio = 2021),"1),"
(' Tommy Townsend ',16,P,16,1,16,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tommy Townsend ' AND Anio = 2021),"1),"
(' Matthias Farley ',31,S,17,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Matthias Farley ' AND Anio = 2021),"1),"
(' Derrick Henry ',31,RB,8,1,5,5,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Derrick Henry ' AND Anio = 2021),"1),"
(' John Wolford ',19,QB,3,4,5,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'John Wolford ' AND Anio = 2021),"1),"
(' Kellen Mond ',21,QB,1,3,5,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kellen Mond ' AND Anio = 2021),"1),"
(' Marcus Mariota ',17,QB,10,2,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marcus Mariota ' AND Anio = 2021),"1),"
(' Ezekiel Elliott ',9,RB,17,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ezekiel Elliott ' AND Anio = 2021),"1),"
(' Johnny Hekker ',19,P,17,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Johnny Hekker ' AND Anio = 2021),"1),"
(' Greg Ward ',26,WR,17,2,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Greg Ward ' AND Anio = 2021),"1),"
(' Kendall Hinton ',10,WR,16,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kendall Hinton ' AND Anio = 2021),"1),"
(' Sam Koch ',3,P,17,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Sam Koch ' AND Anio = 2021),"1),"
(' Danny Amendola ',13,WR,8,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Danny Amendola ' AND Anio = 2021),"1),"
(' Cole Beasley ',4,WR,16,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cole Beasley ' AND Anio = 2021),"1),"
(' Cordarrelle Patterson ',2,RB,16,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cordarrelle Patterson ' AND Anio = 2021),"1),"
(' Keenan Allen ',18,WR,16,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Keenan Allen ' AND Anio = 2021),"1),"
(' Rex Burkhead ',13,RB,16,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Rex Burkhead ' AND Anio = 2021),"1),"
(' Jarvis Landry ',8,WR,12,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jarvis Landry ' AND Anio = 2021),"1),"
(' Albert Wilson ',20,WR,14,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Albert Wilson ' AND Anio = 2021),"1),"
(' Chris Boswell ',27,PK,17,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Boswell ' AND Anio = 2021),"1),"
(' Jamison Crowder ',25,WR,12,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamison Crowder ' AND Anio = 2021),"1),"
(' Riley Dixon ',24,P,17,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Riley Dixon ' AND Anio = 2021),"1),"
(' Ty Long ',18,P,17,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ty Long ' AND Anio = 2021),"1),"
(' Stefon Diggs ',4,WR,17,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Stefon Diggs ' AND Anio = 2021),"1),"
(' Cooper Kupp ',19,WR,17,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cooper Kupp ' AND Anio = 2021),"1),"
(' Keelan Cole Sr.',25,WR,15,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Keelan Cole Sr.' AND Anio = 2021),"1),"
(' Mike Gesicki ',20,TE,17,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Gesicki ' AND Anio = 2021),"1),"
(' David Blough ',11,QB,1,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'David Blough ' AND Anio = 2021),"1),"
(' Brett Rypien ',10,QB,1,2,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brett Rypien ' AND Anio = 2021),"1),"
(' Feleipe Franks ',2,TE,9,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Feleipe Franks ' AND Anio = 2021),"1),"
(' David Montgomery ',6,RB,13,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'David Montgomery ' AND Anio = 2021),"1),"
(' Blake Gillikin ',23,P,17,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Blake Gillikin ' AND Anio = 2021),"1),"
(' A.J. Brown ',31,WR,13,2,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'A.J. Brown ' AND Anio = 2021),"1),"
(' D'Andre Swift ',11,RB,13,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'D'Andre Swift ' AND Anio = 2021),"1),"
(' Brandon Zylstra ',5,WR,14,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Zylstra ' AND Anio = 2021),"1),"
(' Cooper Kupp ',19,WR,17,145,1947,59,16,(SELECT Player_ID FROM Player_season WHERE Name = 'Cooper Kupp ' AND Anio = 2021),"3),"
(' Justin Jefferson ',21,WR,17,108,1616,56,10,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Jefferson ' AND Anio = 2021),"3),"
(' Davante Adams ',12,WR,16,123,1553,59,11,(SELECT Player_ID FROM Player_season WHERE Name = 'Davante Adams ' AND Anio = 2021),"3),"
(' Ja'Marr Chase ',7,WR,17,81,1455,82,13,(SELECT Player_ID FROM Player_season WHERE Name = 'Ja'Marr Chase ' AND Anio = 2021),"3),"
(' Deebo Samuel Sr.',28,WR,16,77,1405,83,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Deebo Samuel Sr.' AND Anio = 2021),"3),"
(' Mark Andrews ',3,TE,17,107,1361,43,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Mark Andrews ' AND Anio = 2021),"3),"
(' Tyreek Hill ',16,WR,17,111,1239,75,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyreek Hill ' AND Anio = 2021),"3),"
(' Stefon Diggs ',4,WR,17,103,1225,61,10,(SELECT Player_ID FROM Player_season WHERE Name = 'Stefon Diggs ' AND Anio = 2021),"3),"
(' Tyler Lockett ',29,WR,16,73,1175,69,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Lockett ' AND Anio = 2021),"3),"
(' Diontae Johnson ',27,WR,16,107,1161,50,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Diontae Johnson ' AND Anio = 2021),"3),"
(' DJ Moore ',5,WR,17,93,1157,64,4,(SELECT Player_ID FROM Player_season WHERE Name = 'DJ Moore ' AND Anio = 2021),"3),"
(' Mike Williams ',18,WR,16,76,1146,72,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Williams ' AND Anio = 2021),"3),"
(' Keenan Allen ',18,WR,16,106,1138,42,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Keenan Allen ' AND Anio = 2021),"3),"
(' Travis Kelce ',16,TE,16,92,1125,69,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Travis Kelce ' AND Anio = 2021),"3),"
(' CeeDee Lamb ',9,WR,16,79,1102,49,6,(SELECT Player_ID FROM Player_season WHERE Name = 'CeeDee Lamb ' AND Anio = 2021),"3),"
(' Tee Higgins ',7,WR,14,74,1091,54,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Tee Higgins ' AND Anio = 2021),"3),"
(' Michael Pittman Jr.',14,WR,17,88,1082,57,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Pittman Jr.' AND Anio = 2021),"3),"
(' Darnell Mooney ',6,WR,17,81,1055,64,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Darnell Mooney ' AND Anio = 2021),"3),"
(' Terry McLaurin ',32,WR,17,77,1053,46,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Terry McLaurin ' AND Anio = 2021),"3),"
(' Hunter Renfrow ',17,WR,17,103,1038,54,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Hunter Renfrow ' AND Anio = 2021),"3),"
(' Brandin Cooks ',13,WR,16,90,1037,52,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandin Cooks ' AND Anio = 2021),"3),"
(' Mike Evans ',30,WR,16,74,1035,46,14,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Evans ' AND Anio = 2021),"3),"
(' Kyle Pitts ',2,TE,17,68,1026,61,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Pitts ' AND Anio = 2021),"3),"
(' Jaylen Waddle ',20,WR,16,104,1015,57,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaylen Waddle ' AND Anio = 2021),"3),"
(' Marquise Brown ',3,WR,16,91,1008,49,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Marquise Brown ' AND Anio = 2021),"3),"
(' Christian Kirk ',1,WR,17,77,982,50,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian Kirk ' AND Anio = 2021),"3),"
(' DK Metcalf ',29,WR,17,75,967,84,12,(SELECT Player_ID FROM Player_season WHERE Name = 'DK Metcalf ' AND Anio = 2021),"3),"
(' DeVonta Smith ',26,WR,17,64,916,46,5,(SELECT Player_ID FROM Player_season WHERE Name = 'DeVonta Smith ' AND Anio = 2021),"3),"
(' Amon-Ra St. Brown',11,WR,17,90,912,37,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Amon-Ra St. Brown' AND Anio = 2021),"3),"
(' George Kittle ',28,TE,14,71,910,48,6,(SELECT Player_ID FROM Player_season WHERE Name = 'George Kittle ' AND Anio = 2021),"3),"
(' A.J. Brown ',31,WR,13,63,869,57,5,(SELECT Player_ID FROM Player_season WHERE Name = 'A.J. Brown ' AND Anio = 2021),"3),"
(' Jakobi Meyers ',22,WR,17,83,866,39,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jakobi Meyers ' AND Anio = 2021),"3),"
(' Amari Cooper ',9,WR,15,68,865,41,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Amari Cooper ' AND Anio = 2021),"3),"
(' Chase Claypool ',27,WR,15,59,860,59,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Chase Claypool ' AND Anio = 2021),"3),"
(' A.J. Green ',1,WR,16,54,848,42,3,(SELECT Player_ID FROM Player_season WHERE Name = 'A.J. Green ' AND Anio = 2021),"3),"
(' Marvin Jones Jr.',15,WR,17,73,832,33,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Marvin Jones Jr.' AND Anio = 2021),"3),"
(' Dallas Goedert ',26,TE,15,56,830,45,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Dallas Goedert ' AND Anio = 2021),"3),"
(' Tyler Boyd ',7,WR,16,67,828,68,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Boyd ' AND Anio = 2021),"3),"
(' Brandon Aiyuk ',28,WR,17,56,826,43,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Aiyuk ' AND Anio = 2021),"3),"
(' Dalton Schultz ',9,TE,17,78,808,32,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Dalton Schultz ' AND Anio = 2021),"3),"
(' Rob Gronkowski ',30,TE,12,55,802,42,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Rob Gronkowski ' AND Anio = 2021),"3),"
(' Van Jefferson ',19,WR,17,50,802,79,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Van Jefferson ' AND Anio = 2021),"3),"
(' Kendrick Bourne ',22,WR,17,55,800,75,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Kendrick Bourne ' AND Anio = 2021),"3),"
(' Mike Gesicki ',20,TE,17,73,780,40,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Gesicki ' AND Anio = 2021),"3),"
(' Courtland Sutton ',10,WR,17,58,776,55,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Courtland Sutton ' AND Anio = 2021),"3),"
(' Russell Gage ',2,WR,14,66,770,49,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Russell Gage ' AND Anio = 2021),"3),"
(' Zach Ertz ',26,TE,17,74,763,47,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Ertz ' AND Anio = 2021),"3),"
(' Tim Patrick ',10,WR,16,53,734,44,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Tim Patrick ' AND Anio = 2021),"3),"
(' Marquez Callaway ',23,WR,17,46,698,58,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Marquez Callaway ' AND Anio = 2021),"3),"
(' Cole Beasley ',4,WR,16,82,693,29,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Cole Beasley ' AND Anio = 2021),"3),"
(' Mecole Hardman ',16,WR,17,59,693,53,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Mecole Hardman ' AND Anio = 2021),"3),"
(' Noah Fant ',10,TE,16,68,670,35,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Noah Fant ' AND Anio = 2021),"3),"
(' Darren Waller ',17,TE,11,55,665,33,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Darren Waller ' AND Anio = 2021),"3),"
(' K.J. Osborn ',21,WR,17,50,655,64,7,(SELECT Player_ID FROM Player_season WHERE Name = 'K.J. Osborn ' AND Anio = 2021),"3),"
(' Austin Ekeler ',18,RB,16,70,647,40,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Austin Ekeler ' AND Anio = 2021),"3),"
(' Quez Watkins ',26,WR,17,43,647,91,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Quez Watkins ' AND Anio = 2021),"3),"
(' Emmanuel Sanders ',4,WR,14,42,626,41,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Emmanuel Sanders ' AND Anio = 2021),"3),"
(' Laviska Shenault Jr.',15,WR,16,63,619,58,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Laviska Shenault Jr.' AND Anio = 2021),"3),"
(' Cole Kmet ',6,TE,17,60,612,25,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cole Kmet ' AND Anio = 2021),"3),"
(' Hunter Henry ',22,TE,17,50,603,35,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Hunter Henry ' AND Anio = 2021),"3),"
(' Cedrick Wilson Jr.',9,WR,16,45,602,73,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Cedrick Wilson Jr.' AND Anio = 2021),"3),"
(' Donovan Peoples-Jones ',8,WR,14,34,597,60,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Donovan Peoples-Jones ' AND Anio = 2021),"3),"
(' Tyler Conklin ',21,TE,17,61,593,40,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Conklin ' AND Anio = 2021),"3),"
(' Dawson Knox ',4,TE,15,49,587,53,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Dawson Knox ' AND Anio = 2021),"3),"
(' Kalif Raymond ',11,WR,16,48,576,75,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Kalif Raymond ' AND Anio = 2021),"3),"
(' Bryan Edwards ',17,WR,17,34,571,51,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Bryan Edwards ' AND Anio = 2021),"3),"
(' Jarvis Landry ',8,WR,12,52,570,38,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jarvis Landry ' AND Anio = 2021),"3),"
(' Deonte Harty ',23,WR,13,36,570,72,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Deonte Harty ' AND Anio = 2021),"3),"
(' Byron Pringle ',16,WR,17,42,568,40,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Byron Pringle ' AND Anio = 2021),"3),"
(' Jared Cook ',18,TE,16,48,564,42,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Jared Cook ' AND Anio = 2021),"3),"
(' Tyler Higbee ',19,TE,15,61,560,37,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Higbee ' AND Anio = 2021),"3),"
(' Gabe Davis ',4,WR,16,35,549,49,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Gabe Davis ' AND Anio = 2021),"3),"
(' Cordarrelle Patterson ',2,RB,16,52,548,64,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Cordarrelle Patterson ' AND Anio = 2021),"3),"
(' Zay Jones ',17,WR,17,47,546,43,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Zay Jones ' AND Anio = 2021),"3),"
(' Odell Beckham Jr.',8,WR,14,44,537,54,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Odell Beckham Jr.' AND Anio = 2021),"3),"
(' Kenny Golladay ',24,WR,14,37,521,36,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenny Golladay ' AND Anio = 2021),"3),"
(' Robbie Chosen ',5,WR,17,53,519,57,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Robbie Chosen ' AND Anio = 2021),"3),"
(' DeVante Parker ',20,WR,10,40,515,42,2,(SELECT Player_ID FROM Player_season WHERE Name = 'DeVante Parker ' AND Anio = 2021),"3),"
(' Rashod Bateman ',3,WR,12,46,515,36,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Rashod Bateman ' AND Anio = 2021),"3),"
(' Allen Lazard ',12,WR,15,40,513,42,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Allen Lazard ' AND Anio = 2021),"3),"
(' Pat Freiermuth ',27,TE,16,60,497,24,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Pat Freiermuth ' AND Anio = 2021),"3),"
(' C.J. Uzomah ',7,TE,16,49,493,55,5,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Uzomah ' AND Anio = 2021),"3),"
(' Gerald Everett ',29,TE,15,48,478,41,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Gerald Everett ' AND Anio = 2021),"3),"
(' Nick Westbrook-Ikhine ',31,WR,16,38,476,46,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Westbrook-Ikhine ' AND Anio = 2021),"3),"
(' David Njoku ',8,TE,16,36,475,71,4,(SELECT Player_ID FROM Player_season WHERE Name = 'David Njoku ' AND Anio = 2021),"3),"
(' Nelson Agholor ',22,WR,15,37,473,44,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Nelson Agholor ' AND Anio = 2021),"3),"
(' Najee Harris ',27,RB,17,74,467,25,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Najee Harris ' AND Anio = 2021),"3),"
(' Jerry Jeudy ',10,WR,10,38,467,40,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jerry Jeudy ' AND Anio = 2021),"3),"
(' DeSean Jackson ',19,WR,16,20,454,75,2,(SELECT Player_ID FROM Player_season WHERE Name = 'DeSean Jackson ' AND Anio = 2021),"3),"
(' Darrel Williams ',16,RB,17,47,452,38,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Darrel Williams ' AND Anio = 2021),"3),"
(' D'Andre Swift ',11,RB,13,62,452,63,2,(SELECT Player_ID FROM Player_season WHERE Name = 'D'Andre Swift ' AND Anio = 2021),"3),"
(' Keelan Cole Sr.',25,WR,15,28,449,54,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Keelan Cole Sr.' AND Anio = 2021),"3),"
(' Jalen Guyton ',18,WR,16,31,448,59,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Guyton ' AND Anio = 2021),"3),"
(' Jamison Crowder ',25,WR,12,51,447,29,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamison Crowder ' AND Anio = 2021),"3),"
(' Nico Collins ',13,WR,14,33,446,32,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Nico Collins ' AND Anio = 2021),"3),"
(' Alvin Kamara ',23,RB,13,47,439,31,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Alvin Kamara ' AND Anio = 2021),"3),"
(' Rondale Moore ',1,WR,14,54,435,77,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Rondale Moore ' AND Anio = 2021),"3),"
(' Julio Jones ',31,WR,10,31,434,51,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Julio Jones ' AND Anio = 2021),"3),"
(' Laquon Treadwell ',15,WR,12,33,434,41,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Laquon Treadwell ' AND Anio = 2021),"3),"
(' Marquez Valdes-Scantling ',12,WR,11,26,430,75,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Marquez Valdes-Scantling ' AND Anio = 2021),"3),"
(' Kadarius Toney ',24,WR,10,39,420,38,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kadarius Toney ' AND Anio = 2021),"3),"
(' Allen Robinson II',6,WR,12,38,410,39,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Allen Robinson II' AND Anio = 2021),"3),"
(' Evan Engram ',24,TE,15,46,408,30,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Evan Engram ' AND Anio = 2021),"3),"
(' Olamide Zaccheaus ',2,WR,17,31,406,49,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Olamide Zaccheaus ' AND Anio = 2021),"3),"
(' Brandon Bolden ',22,RB,17,41,405,28,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Bolden ' AND Anio = 2021),"3),"
(' Josh Reynolds ',31,WR,12,29,396,39,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Reynolds ' AND Anio = 2021),"3),"
(' Sammy Watkins ',3,WR,13,27,394,49,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Sammy Watkins ' AND Anio = 2021),"3),"
(' Aaron Jones ',12,RB,15,52,391,26,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Aaron Jones ' AND Anio = 2021),"3),"
(' Zach Pascal ',14,WR,16,38,384,41,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Pascal ' AND Anio = 2021),"3),"
(' Adam Humphries ',32,WR,17,41,383,27,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Adam Humphries ' AND Anio = 2021),"3),"
(' Tre'Quan Smith ',23,WR,11,32,377,34,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Tre'Quan Smith ' AND Anio = 2021),"3),"
(' James Conner ',1,RB,15,37,375,45,3,(SELECT Player_ID FROM Player_season WHERE Name = 'James Conner ' AND Anio = 2021),"3),"
(' Foster Moreau ',17,TE,17,30,373,44,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Foster Moreau ' AND Anio = 2021),"3),"
(' Ty Johnson ',25,RB,16,34,372,23,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Ty Johnson ' AND Anio = 2021),"3),"
(' Tyler Johnson ',30,WR,17,36,360,31,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Johnson ' AND Anio = 2021),"3),"
(' Jonathan Taylor ',14,RB,17,40,360,76,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonathan Taylor ' AND Anio = 2021),"3),"
(' Durham Smythe ',20,TE,17,34,357,25,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Durham Smythe ' AND Anio = 2021),"3),"
(' Joshua Palmer ',18,WR,17,33,353,36,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Joshua Palmer ' AND Anio = 2021),"3),"
(' Josh Jacobs ',17,RB,15,54,348,29,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Jacobs ' AND Anio = 2021),"3),"
(' Austin Hooper ',8,TE,16,38,345,34,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Austin Hooper ' AND Anio = 2021),"3),"
(' Freddie Swain ',29,WR,17,25,343,68,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Freddie Swain ' AND Anio = 2021),"3),"
(' Darius Slayton ',24,WR,13,26,339,42,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Darius Slayton ' AND Anio = 2021),"3),"
(' Tony Pollard ',9,RB,15,39,337,32,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tony Pollard ' AND Anio = 2021),"3),"
(' T.Y. Hilton ',14,WR,10,23,331,52,3,(SELECT Player_ID FROM Player_season WHERE Name = 'T.Y. Hilton ' AND Anio = 2021),"3),"
(' Albert Okwuegbunam Jr.',10,TE,14,33,330,64,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Albert Okwuegbunam Jr.' AND Anio = 2021),"3),"
(' Damiere Byrd ',6,WR,17,26,329,54,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Damiere Byrd ' AND Anio = 2021),"3),"
(' Michael Carter ',25,RB,14,36,325,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Carter ' AND Anio = 2021),"3),"
(' Chris Conley ',13,WR,16,22,323,41,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Conley ' AND Anio = 2021),"3),"
(' Mo Alie-Cox ',14,TE,17,24,316,37,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Mo Alie-Cox ' AND Anio = 2021),"3),"
(' Javonte Williams ',10,RB,17,43,316,42,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Javonte Williams ' AND Anio = 2021),"3),"
(' Joe Mixon ',7,RB,16,42,314,52,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Joe Mixon ' AND Anio = 2021),"3),"
(' Marquise Goodwin ',6,WR,14,20,313,50,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Marquise Goodwin ' AND Anio = 2021),"3),"
(' AJ Dillon ',12,RB,17,34,313,50,2,(SELECT Player_ID FROM Player_season WHERE Name = 'AJ Dillon ' AND Anio = 2021),"3),"
(' Chase Edmonds ',1,RB,12,43,311,36,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chase Edmonds ' AND Anio = 2021),"3),"
(' Nyheim Hines ',14,RB,17,40,310,36,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Nyheim Hines ' AND Anio = 2021),"3),"
(' Jack Doyle ',14,TE,17,29,302,34,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Jack Doyle ' AND Anio = 2021),"3),"
(' Chester Rogers ',31,WR,16,30,301,39,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Chester Rogers ' AND Anio = 2021),"3),"
(' David Montgomery ',6,RB,13,42,301,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'David Montgomery ' AND Anio = 2021),"3),"
(' Jalen Reagor ',26,WR,17,33,299,34,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Reagor ' AND Anio = 2021),"3),"
(' Kyle Juszczyk ',28,FB,17,30,296,26,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Juszczyk ' AND Anio = 2021),"3),"
(' DeAndre Carter ',32,WR,17,24,296,26,3,(SELECT Player_ID FROM Player_season WHERE Name = 'DeAndre Carter ' AND Anio = 2021),"3),"
(' Jonnu Smith ',22,TE,16,28,294,28,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonnu Smith ' AND Anio = 2021),"3),"
(' Antonio Gibson ',32,RB,16,42,294,73,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Antonio Gibson ' AND Anio = 2021),"3),"
(' Anthony Firkser ',31,TE,15,34,291,24,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Anthony Firkser ' AND Anio = 2021),"3),"
(' Ameer Abdullah ',5,RB,17,38,289,23,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ameer Abdullah ' AND Anio = 2021),"3),"
(' Ezekiel Elliott ',9,RB,17,47,287,21,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Ezekiel Elliott ' AND Anio = 2021),"3),"
(' Jauan Jennings ',28,WR,16,24,282,34,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Jauan Jennings ' AND Anio = 2021),"3),"
(' Ray-Ray McCloud III',27,WR,16,39,277,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ray-Ray McCloud III' AND Anio = 2021),"3),"
(' Rashard Higgins ',8,WR,15,24,275,21,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Rashard Higgins ' AND Anio = 2021),"3),"
(' Devin Duvernay ',3,WR,16,33,272,21,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Devin Duvernay ' AND Anio = 2021),"3),"
(' Devontae Booker ',24,RB,16,40,268,41,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Devontae Booker ' AND Anio = 2021),"3),"
(' Demarcus Robinson ',16,WR,17,25,264,33,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Demarcus Robinson ' AND Anio = 2021),"3),"
(' Adam Trautman ',23,TE,13,27,263,32,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Adam Trautman ' AND Anio = 2021),"3),"
(' Saquon Barkley ',24,RB,13,41,263,54,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Saquon Barkley ' AND Anio = 2021),"3),"
(' Mike Davis ',2,RB,17,44,259,20,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Davis ' AND Anio = 2021),"3),"
(' Kyle Rudolph ',24,TE,16,26,257,60,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Rudolph ' AND Anio = 2021),"3),"
(' Kenneth Gainwell ',26,RB,16,33,253,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenneth Gainwell ' AND Anio = 2021),"3),"
(' Brandon Zylstra ',5,WR,14,18,250,55,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Zylstra ' AND Anio = 2021),"3),"
(' Lil'Jordan Humphrey ',23,WR,10,13,249,56,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Lil'Jordan Humphrey ' AND Anio = 2021),"3),"
(' John Bates ',32,TE,17,20,249,32,1,(SELECT Player_ID FROM Player_season WHERE Name = 'John Bates ' AND Anio = 2021),"3),"
(' Danny Amendola ',13,WR,8,24,248,39,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Danny Amendola ' AND Anio = 2021),"3),"
(' Cameron Brate ',30,TE,17,30,245,18,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Cameron Brate ' AND Anio = 2021),"3),"
(' Josiah Deguara ',12,TE,16,25,245,62,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Josiah Deguara ' AND Anio = 2021),"3),"
(' James O'Shaughnessy ',15,TE,7,24,244,30,0,(SELECT Player_ID FROM Player_season WHERE Name = 'James O'Shaughnessy ' AND Anio = 2021),"3),"
(' Myles Gaskin ',20,RB,17,49,234,24,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Myles Gaskin ' AND Anio = 2021),"3),"
(' Harrison Bryant ',8,TE,16,21,233,41,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Harrison Bryant ' AND Anio = 2021),"3),"
(' Will Dissly ',29,TE,15,21,231,39,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Will Dissly ' AND Anio = 2021),"3),"
(' Tajae Sharpe ',2,WR,15,25,230,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tajae Sharpe ' AND Anio = 2021),"3),"
(' Devin Singletary ',4,RB,17,40,228,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Devin Singletary ' AND Anio = 2021),"3),"
(' Alexander Mattison ',21,RB,16,32,228,24,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Alexander Mattison ' AND Anio = 2021),"3),"
(' Chris Moore ',13,WR,12,21,227,67,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Moore ' AND Anio = 2021),"3),"
(' David Johnson ',13,RB,13,32,225,16,1,(SELECT Player_ID FROM Player_season WHERE Name = 'David Johnson ' AND Anio = 2021),"3),"
(' John Ross ',24,WR,10,11,224,52,1,(SELECT Player_ID FROM Player_season WHERE Name = 'John Ross ' AND Anio = 2021),"3),"
(' Dalvin Cook ',21,RB,13,34,224,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dalvin Cook ' AND Anio = 2021),"3),"
(' Mack Hollins ',20,WR,17,14,223,65,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Mack Hollins ' AND Anio = 2021),"3),"
(' Hayden Hurst ',2,TE,13,26,221,33,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Hayden Hurst ' AND Anio = 2021),"3),"
(' Marcedes Lewis ',12,TE,17,23,214,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marcedes Lewis ' AND Anio = 2021),"3),"
(' Jordan Akins ',13,TE,13,24,214,31,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Akins ' AND Anio = 2021),"3),"
(' Tavon Austin ',15,WR,13,24,213,25,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tavon Austin ' AND Anio = 2021),"3),"
(' Albert Wilson ',20,WR,14,25,213,64,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Albert Wilson ' AND Anio = 2021),"3),"
(' Melvin Gordon III',10,RB,16,28,213,30,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Melvin Gordon III' AND Anio = 2021),"3),"
(' Cyril Grayson Jr.',30,WR,5,10,212,62,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Cyril Grayson Jr.' AND Anio = 2021),"3),"
(' Cam Sims ',32,WR,14,15,211,43,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Cam Sims ' AND Anio = 2021),"3),"
(' Geoff Swaim ',31,TE,16,31,210,26,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Geoff Swaim ' AND Anio = 2021),"3),"
(' Antoine Wesley ',1,WR,15,19,208,33,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Antoine Wesley ' AND Anio = 2021),"3),"
(' James Proche II',3,WR,14,16,202,32,0,(SELECT Player_ID FROM Player_season WHERE Name = 'James Proche II' AND Anio = 2021),"3),"
(' Zack Moss ',4,RB,13,23,197,24,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Zack Moss ' AND Anio = 2021),"3),"
(' Samaje Perine ',7,RB,16,27,196,23,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Samaje Perine ' AND Anio = 2021),"3),"
(' Devonta Freeman ',3,RB,16,34,190,15,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Devonta Freeman ' AND Anio = 2021),"3),"
(' Ian Thomas ',5,TE,17,18,188,41,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ian Thomas ' AND Anio = 2021),"3),"
(' Rex Burkhead ',13,RB,16,25,186,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Rex Burkhead ' AND Anio = 2021),"3),"
(' Noah Brown ',9,WR,13,16,184,27,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Noah Brown ' AND Anio = 2021),"3),"
(' N'Keal Harry ',22,WR,12,12,184,43,0,(SELECT Player_ID FROM Player_season WHERE Name = 'N'Keal Harry ' AND Anio = 2021),"3),"
(' Demetric Felton ',8,RB,16,18,181,33,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Demetric Felton ' AND Anio = 2021),"3),"
(' Tommy Tremble ',5,TE,16,20,180,30,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tommy Tremble ' AND Anio = 2021),"3),"
(' Justin Jackson ',18,RB,14,22,178,25,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Jackson ' AND Anio = 2021),"3),"
(' Isaiah McKenzie ',4,WR,15,20,178,28,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Isaiah McKenzie ' AND Anio = 2021),"3),"
(' Brevin Jordan ',13,TE,9,20,178,27,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Brevin Jordan ' AND Anio = 2021),"3),"
(' Kendall Hinton ',10,WR,16,15,175,40,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kendall Hinton ' AND Anio = 2021),"3),"
(' Kareem Hunt ',8,RB,8,22,174,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kareem Hunt ' AND Anio = 2021),"3),"
(' Nick Chubb ',8,RB,14,20,174,40,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Chubb ' AND Anio = 2021),"3),"
(' Chuba Hubbard ',5,RB,17,25,174,33,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Chuba Hubbard ' AND Anio = 2021),"3),"
(' Tyler Kroft ',25,TE,9,16,173,26,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Kroft ' AND Anio = 2021),"3),"
(' Ashton Dulin ',14,WR,17,13,173,62,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Ashton Dulin ' AND Anio = 2021),"3),"
(' Pharaoh Brown ',13,TE,15,23,171,29,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Pharaoh Brown ' AND Anio = 2021),"3),"
(' Jimmy Graham ',6,TE,15,14,167,28,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Jimmy Graham ' AND Anio = 2021),"3),"
(' Breshad Perriman ',30,WR,6,11,167,58,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Breshad Perriman ' AND Anio = 2021),"3),"
(' Zach Gentry ',27,TE,17,19,167,25,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Gentry ' AND Anio = 2021),"3),"
(' Stephen Anderson ',18,TE,17,16,165,34,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Stephen Anderson ' AND Anio = 2021),"3),"
(' Dyami Brown ',32,WR,15,12,165,48,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dyami Brown ' AND Anio = 2021),"3),"
(' Mark Ingram II',23,RB,14,27,162,34,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mark Ingram II' AND Anio = 2021),"3),"
(' Parris Campbell ',14,WR,6,10,162,51,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Parris Campbell ' AND Anio = 2021),"3),"
(' Isaiah Ford ',20,WR,13,12,161,52,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Isaiah Ford ' AND Anio = 2021),"3),"
(' Travis Homer ',29,RB,14,16,161,31,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Travis Homer ' AND Anio = 2021),"3),"
(' Juwan Johnson ',23,TE,14,13,159,27,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Juwan Johnson ' AND Anio = 2021),"3),"
(' Miles Sanders ',26,RB,12,26,158,25,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Miles Sanders ' AND Anio = 2021),"3),"
(' Jamaal Williams ',11,RB,13,26,157,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamaal Williams ' AND Anio = 2021),"3),"
(' KhaDarel Hodge ',11,WR,16,13,157,42,0,(SELECT Player_ID FROM Player_season WHERE Name = 'KhaDarel Hodge ' AND Anio = 2021),"3),"
(' JaMycal Hasty ',28,RB,11,23,157,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'JaMycal Hasty ' AND Anio = 2021),"3),"
(' Derrick Henry ',31,RB,8,18,154,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Derrick Henry ' AND Anio = 2021),"3),"
(' Chris Evans ',7,RB,14,15,151,24,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Evans ' AND Anio = 2021),"3),"
(' Malik Turner ',9,WR,14,12,149,61,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Malik Turner ' AND Anio = 2021),"3),"
(' D'Ernest Johnson ',8,RB,17,19,137,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'D'Ernest Johnson ' AND Anio = 2021),"3),"
(' Elijah Mitchell ',28,RB,11,19,137,14,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Elijah Mitchell ' AND Anio = 2021),"3),"
(' O.J. Howard ',30,TE,17,14,135,21,1,(SELECT Player_ID FROM Player_season WHERE Name = 'O.J. Howard ' AND Anio = 2021),"3),"
(' Anthony Schwartz ',8,WR,14,10,135,44,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Anthony Schwartz ' AND Anio = 2021),"3),"
(' Nick Vannett ',23,TE,7,9,133,30,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Vannett ' AND Anio = 2021),"3),"
(' Denzel Mims ',25,WR,11,8,133,40,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Denzel Mims ' AND Anio = 2021),"3),"
(' Ben Skowronek ',19,WR,14,11,133,35,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ben Skowronek ' AND Anio = 2021),"3),"
(' DeeJay Dallas ',29,RB,17,21,133,29,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DeeJay Dallas ' AND Anio = 2021),"3),"
(' Damien Harris ',22,RB,15,18,132,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Damien Harris ' AND Anio = 2021),"3),"
(' Clyde Edwards-Helaire ',16,RB,10,19,129,29,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Clyde Edwards-Helaire ' AND Anio = 2021),"3),"
(' Sony Michel ',19,RB,17,21,128,24,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Sony Michel ' AND Anio = 2021),"3),"
(' C.J. Ham ',21,FB,17,17,125,27,0,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Ham ' AND Anio = 2021),"3),"
(' D'Onta Foreman ',31,RB,9,9,123,39,0,(SELECT Player_ID FROM Player_season WHERE Name = 'D'Onta Foreman ' AND Anio = 2021),"3),"
(' Rhamondre Stevenson ',22,RB,12,14,123,41,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Rhamondre Stevenson ' AND Anio = 2021),"3),"
(' Brock Wright ',11,TE,10,12,117,36,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Brock Wright ' AND Anio = 2021),"3),"
(' Salvon Ahmed ',20,RB,12,12,117,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Salvon Ahmed ' AND Anio = 2021),"3),"
(' Ihmir Smith-Marsette ',21,WR,8,5,116,44,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Ihmir Smith-Marsette ' AND Anio = 2021),"3),"
(' Dare Ogunbowale ',15,RB,17,13,114,28,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Dare Ogunbowale ' AND Anio = 2021),"3),"
(' Jeff Smith ',25,WR,12,8,113,35,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeff Smith ' AND Anio = 2021),"3),"
(' Adam Shaheen ',20,TE,12,12,110,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Adam Shaheen ' AND Anio = 2021),"3),"
(' Jerick McKinnon ',16,RB,13,13,107,14,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jerick McKinnon ' AND Anio = 2021),"3),"
(' Kylen Granson ',14,TE,17,11,106,27,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kylen Granson ' AND Anio = 2021),"3),"
(' Derrick Gore ',16,RB,11,8,105,50,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Derrick Gore ' AND Anio = 2021),"3),"
(' Collin Johnson ',24,WR,12,11,105,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Collin Johnson ' AND Anio = 2021),"3),"
(' Damien Williams ',6,RB,12,16,103,23,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Damien Williams ' AND Anio = 2021),"3),"
(' Trinity Benson ',11,WR,8,10,103,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trinity Benson ' AND Anio = 2021),"3),"
(' Equanimeous St. Brown',12,WR,13,9,98,26,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Equanimeous St. Brown' AND Anio = 2021),"3),"
(' Blake Jarwin ',9,TE,8,11,96,20,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Blake Jarwin ' AND Anio = 2021),"3),"
(' Khalil Herbert ',6,RB,17,14,96,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Khalil Herbert ' AND Anio = 2021),"3),"
(' Ty Montgomery II',23,WR,14,16,95,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ty Montgomery II' AND Anio = 2021),"3),"
(' Greg Ward ',26,WR,17,7,95,27,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Greg Ward ' AND Anio = 2021),"3),"
(' Blake Bell ',16,TE,16,9,87,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Blake Bell ' AND Anio = 2021),"3),"
(' Trent Sherfield Sr.',28,WR,17,9,87,18,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Trent Sherfield Sr.' AND Anio = 2021),"3),"
(' Dontrell Hilliard ',31,RB,8,19,87,28,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dontrell Hilliard ' AND Anio = 2021),"3),"
(' Ty'Son Williams ',3,RB,13,9,84,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ty'Son Williams ' AND Anio = 2021),"3),"
(' Boston Scott ',26,RB,16,13,83,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Boston Scott ' AND Anio = 2021),"3),"
(' Dax Milne ',32,WR,13,9,83,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dax Milne ' AND Anio = 2021),"3),"
(' Drew Sample ',7,TE,17,11,81,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Drew Sample ' AND Anio = 2021),"3),"
(' Royce Freeman ',5,RB,15,10,77,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Royce Freeman ' AND Anio = 2021),"3),"
(' Latavius Murray ',3,RB,14,10,75,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Latavius Murray ' AND Anio = 2021),"3),"
(' Jaret Patterson ',32,RB,17,10,73,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaret Patterson ' AND Anio = 2021),"3),"
(' Jalen Richard ',17,RB,10,12,72,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Richard ' AND Anio = 2021),"3),"
(' Matt Breida ',4,RB,9,7,72,23,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Breida ' AND Anio = 2021),"3),"
(' Chris Manhertz ',15,TE,17,6,71,22,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Manhertz ' AND Anio = 2021),"3),"
(' Preston Williams ',20,WR,8,6,71,34,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Preston Williams ' AND Anio = 2021),"3),"
(' Kenny Stills ',23,WR,13,6,68,22,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenny Stills ' AND Anio = 2021),"3),"
(' Dede Westbrook ',21,WR,15,10,68,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dede Westbrook ' AND Anio = 2021),"3),"
(' Peyton Barber ',17,RB,10,10,67,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Peyton Barber ' AND Anio = 2021),"3),"
(' Josh Oliver ',3,TE,14,9,66,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Oliver ' AND Anio = 2021),"3),"
(' Lee Smith ',2,TE,16,9,65,22,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Lee Smith ' AND Anio = 2021),"3),"
(' Ronald Jones ',30,RB,16,10,64,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ronald Jones ' AND Anio = 2021),"3),"
(' Ja'Marcus Bradley ',8,WR,5,4,64,37,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ja'Marcus Bradley ' AND Anio = 2021),"3),"
(' Dee Eskridge ',29,WR,10,10,64,17,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Dee Eskridge ' AND Anio = 2021),"3),"
(' Jesse James ',6,TE,14,7,62,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jesse James ' AND Anio = 2021),"3),"
(' Godwin Igwebuike ',11,RB,17,7,60,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Godwin Igwebuike ' AND Anio = 2021),"3),"
(' Penny Hart ',29,WR,17,7,59,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Penny Hart ' AND Anio = 2021),"3),"
(' Juwann Winfree ',12,WR,7,8,58,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Juwann Winfree ' AND Anio = 2021),"3),"
(' Keith Smith ',2,FB,17,9,56,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Keith Smith ' AND Anio = 2021),"3),"
(' Luke Farrell ',15,TE,15,7,56,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Luke Farrell ' AND Anio = 2021),"3),"
(' Jason Moore ',18,WR,2,3,56,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jason Moore ' AND Anio = 2021),"3),"
(' Alex Erickson ',5,WR,17,3,55,25,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Alex Erickson ' AND Anio = 2021),"3),"
(' Jacob Hollister ',15,TE,7,9,55,11,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jacob Hollister ' AND Anio = 2021),"3),"
(' Tom Kennedy ',11,WR,12,6,54,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tom Kennedy ' AND Anio = 2021),"3),"
(' Taysom Hill ',23,QB,12,4,52,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Taysom Hill ' AND Anio = 2021),"3),"
(' Mike Thomas ',7,WR,12,5,52,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Thomas ' AND Anio = 2021),"3),"
(' Charlie Woerner ',28,TE,17,5,52,27,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Charlie Woerner ' AND Anio = 2021),"3),"
(' Craig Reynolds ',11,RB,5,7,52,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Craig Reynolds ' AND Anio = 2021),"3),"
(' Ross Dwelley ',28,TE,17,4,51,21,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ross Dwelley ' AND Anio = 2021),"3),"
(' Tevin Coleman ',25,RB,11,11,49,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tevin Coleman ' AND Anio = 2021),"3),"
(' Dez Fitzpatrick ',31,WR,4,5,49,18,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Dez Fitzpatrick ' AND Anio = 2021),"3),"
(' Rashaad Penny ',29,RB,10,6,48,27,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Rashaad Penny ' AND Anio = 2021),"3),"
(' Eric Saubert ',10,TE,17,8,47,11,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Eric Saubert ' AND Anio = 2021),"3),"
(' Antony Auclair ',13,TE,16,5,47,15,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Antony Auclair ' AND Anio = 2021),"3),"
(' Phillip Lindsay ',20,RB,14,4,45,22,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Phillip Lindsay ' AND Anio = 2021),"3),"
(' Amari Rodgers ',12,WR,16,4,45,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Amari Rodgers ' AND Anio = 2021),"3),"
(' Tre' McKitty ',18,TE,11,6,45,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tre' McKitty ' AND Anio = 2021),"3),"
(' Tommy Sweeney ',4,TE,13,9,44,13,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tommy Sweeney ' AND Anio = 2021),"3),"
(' Jakob Johnson ',22,FB,17,4,43,29,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jakob Johnson ' AND Anio = 2021),"3),"
(' Parker Hesse ',2,TE,8,5,43,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Parker Hesse ' AND Anio = 2021),"3),"
(' Jaelon Darden ',30,WR,9,6,43,29,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaelon Darden ' AND Anio = 2021),"3),"
(' Eno Benjamin ',1,RB,9,6,42,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Eno Benjamin ' AND Anio = 2021),"3),"
(' Duke Johnson ',20,RB,5,4,41,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Duke Johnson ' AND Anio = 2021),"3),"
(' Chris Herndon ',21,TE,16,4,40,17,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Herndon ' AND Anio = 2021),"3),"
(' Auden Tate ',7,WR,7,3,39,18,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Auden Tate ' AND Anio = 2021),"3),"
(' Kevin White ',23,WR,6,1,38,38,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kevin White ' AND Anio = 2021),"3),"
(' Joshua Kelley ',18,RB,10,5,38,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Joshua Kelley ' AND Anio = 2021),"3),"
(' Scotty Miller ',30,WR,9,5,38,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Scotty Miller ' AND Anio = 2021),"3),"
(' Kendall Blanton ',19,TE,11,4,37,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kendall Blanton ' AND Anio = 2021),"3),"
(' Kenny Yeboah ',25,TE,9,2,36,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenny Yeboah ' AND Anio = 2021),"3),"
(' Noah Gray ',16,TE,16,7,36,8,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Noah Gray ' AND Anio = 2021),"3),"
(' D.J. Montgomery ',25,WR,3,3,36,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'D.J. Montgomery ' AND Anio = 2021),"3),"
(' Andre Roberts ',18,WR,16,1,35,35,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andre Roberts ' AND Anio = 2021),"3),"
(' Tyler Davis ',12,TE,14,4,35,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Davis ' AND Anio = 2021),"3),"
(' Trenton Irwin ',7,WR,7,2,34,25,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trenton Irwin ' AND Anio = 2021),"3),"
(' Dominique Dafney ',12,TE,10,2,34,26,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dominique Dafney ' AND Anio = 2021),"3),"
(' Jonathan Ward ',1,RB,13,3,34,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonathan Ward ' AND Anio = 2021),"3),"
(' Seth Williams ',10,WR,2,1,34,34,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Seth Williams ' AND Anio = 2021),"3),"
(' Shane Zylstra ',11,TE,4,3,34,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Shane Zylstra ' AND Anio = 2021),"3),"
(' Cody Hollister ',31,WR,3,4,33,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cody Hollister ' AND Anio = 2021),"3),"
(' Cody White ',27,WR,15,5,33,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cody White ' AND Anio = 2021),"3),"
(' Colby Parkinson ',29,TE,14,5,33,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Colby Parkinson ' AND Anio = 2021),"3),"
(' Josh Gordon ',16,WR,12,5,32,11,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Gordon ' AND Anio = 2021),"3),"
(' Michael Burton ',16,FB,16,3,31,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Burton ' AND Anio = 2021),"3),"
(' Jeremy Sprinkle ',9,TE,17,3,31,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeremy Sprinkle ' AND Anio = 2021),"3),"
(' Jeff Wilson Jr.',28,RB,9,7,31,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeff Wilson Jr.' AND Anio = 2021),"3),"
(' Gunner Olszewski ',22,WR,16,2,31,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Gunner Olszewski ' AND Anio = 2021),"3),"
(' Le'Veon Bell ',30,RB,8,5,30,15,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Le'Veon Bell ' AND Anio = 2021),"3),"
(' Elijhaa Penny ',24,RB,17,9,30,16,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Elijhaa Penny ' AND Anio = 2021),"3),"
(' Corey Clement ',9,RB,17,6,29,8,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Corey Clement ' AND Anio = 2021),"3),"
(' Tony Jones Jr.',23,RB,11,5,29,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tony Jones Jr.' AND Anio = 2021),"3),"
(' Jonathan Williams ',32,RB,5,4,28,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonathan Williams ' AND Anio = 2021),"3),"
(' Jake Kumerow ',4,WR,15,2,28,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jake Kumerow ' AND Anio = 2021),"3),"
(' Curtis Samuel ',32,WR,5,6,27,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Curtis Samuel ' AND Anio = 2021),"3),"
(' Sean McKeon ',9,TE,9,4,27,12,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Sean McKeon ' AND Anio = 2021),"3),"
(' Ke'Shawn Vaughn ',30,RB,12,4,26,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ke'Shawn Vaughn ' AND Anio = 2021),"3),"
(' Trey Sermon ',28,RB,9,3,26,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trey Sermon ' AND Anio = 2021),"3),"
(' Mike Strachan ',14,WR,6,2,26,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Strachan ' AND Anio = 2021),"3),"
(' Christian Blake ',2,WR,16,4,25,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian Blake ' AND Anio = 2021),"3),"
(' Marcus Kemp ',16,WR,16,2,24,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marcus Kemp ' AND Anio = 2021),"3),"
(' Reggie Gilliam ',4,FB,16,3,23,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Reggie Gilliam ' AND Anio = 2021),"3),"
(' Dazz Newsome ',6,WR,3,2,23,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dazz Newsome ' AND Anio = 2021),"3),"
(' Tylan Wallace ',3,WR,17,2,23,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tylan Wallace ' AND Anio = 2021),"3),"
(' Jermar Jefferson ',11,RB,7,4,23,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jermar Jefferson ' AND Anio = 2021),"3),"
(' Mike Boone ',10,RB,8,2,22,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Boone ' AND Anio = 2021),"3),"
(' Jack Stoll ',26,TE,16,4,22,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jack Stoll ' AND Anio = 2021),"3),"
(' Wayne Gallman ',21,RB,8,1,21,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Wayne Gallman ' AND Anio = 2021),"3),"
(' Garrett Bradbury ',21,C,13,1,21,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Garrett Bradbury ' AND Anio = 2021),"3),"
(' Dezmon Patmon ',14,WR,8,2,21,14,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Dezmon Patmon ' AND Anio = 2021),"3),"
(' Nick Bawden ',25,FB,9,1,20,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Bawden ' AND Anio = 2021),"3),"
(' Jordan Howard ',26,RB,7,2,19,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Howard ' AND Anio = 2021),"3),"
(' David Sills V',24,WR,4,2,17,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'David Sills V' AND Anio = 2021),"3),"
(' Bobby Price ',11,CB,15,1,17,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Bobby Price ' AND Anio = 2021),"3),"
(' Gabe Nabers ',18,FB,10,3,17,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Gabe Nabers ' AND Anio = 2021),"3),"
(' Cethan Carter ',20,TE,16,2,16,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cethan Carter ' AND Anio = 2021),"3),"
(' Jason Cabinda ',11,FB,14,4,16,6,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jason Cabinda ' AND Anio = 2021),"3),"
(' Tyron Billy-Johnson ',15,WR,10,2,16,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyron Billy-Johnson ' AND Anio = 2021),"3),"
(' Mitchell Wilcox ',7,TE,15,3,16,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mitchell Wilcox ' AND Anio = 2021),"3),"
(' Ryquell Armstead ',15,RB,2,3,16,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryquell Armstead ' AND Anio = 2021),"3),"
(' Adam Prentice ',23,FB,7,3,16,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Adam Prentice ' AND Anio = 2021),"3),"
(' Derek Watt ',27,FB,17,3,15,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Derek Watt ' AND Anio = 2021),"3),"
(' Greg Dortch ',1,WR,5,3,15,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Greg Dortch ' AND Anio = 2021),"3),"
(' Frank Darby ',2,WR,10,1,14,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Frank Darby ' AND Anio = 2021),"3),"
(' Derek Carrier ',17,TE,5,2,13,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Derek Carrier ' AND Anio = 2021),"3),"
(' Andy Isabella ',1,WR,8,1,13,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andy Isabella ' AND Anio = 2021),"3),"
(' Benny Snell Jr.',27,RB,17,2,13,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Benny Snell Jr.' AND Anio = 2021),"3),"
(' Luke Stocker ',21,TE,12,2,12,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Luke Stocker ' AND Anio = 2021),"3),"
(' Dwayne Washington ',23,RB,14,2,12,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dwayne Washington ' AND Anio = 2021),"3),"
(' Reggie Bonnafon ',5,RB,4,2,12,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Reggie Bonnafon ' AND Anio = 2021),"3),"
(' Qadree Ollison ',2,RB,8,4,12,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Qadree Ollison ' AND Anio = 2021),"3),"
(' Stanley Morgan Jr.',7,WR,17,2,11,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Stanley Morgan Jr.' AND Anio = 2021),"3),"
(' C.J. Saunders ',5,WR,2,2,11,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Saunders ' AND Anio = 2021),"3),"
(' Anthony McFarland Jr.',27,RB,2,1,11,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Anthony McFarland Jr.' AND Anio = 2021),"3),"
(' Demetrius Harris ',1,TE,14,3,10,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Demetrius Harris ' AND Anio = 2021),"3),"
(' Jaydon Mickens ',15,WR,11,2,10,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaydon Mickens ' AND Anio = 2021),"3),"
(' Cam Akers ',19,RB,1,3,10,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cam Akers ' AND Anio = 2021),"3),"
(' Tarik Black ',25,WR,1,1,10,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tarik Black ' AND Anio = 2021),"3),"
(' Andy Janovich ',8,FB,13,3,9,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andy Janovich ' AND Anio = 2021),"3),"
(' Austin Walter ',25,RB,4,2,9,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Austin Walter ' AND Anio = 2021),"3),"
(' Brycen Hopkins ',19,TE,5,1,9,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brycen Hopkins ' AND Anio = 2021),"3),"
(' Kene Nwangwu ',21,RB,11,4,9,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kene Nwangwu ' AND Anio = 2021),"3),"
(' Kevin Rader ',27,TE,6,2,8,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kevin Rader ' AND Anio = 2021),"3),"
(' Ethan Wolf ',23,TE,2,2,8,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ethan Wolf ' AND Anio = 2021),"3),"
(' Kalen Ballage ',27,RB,17,2,8,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kalen Ballage ' AND Anio = 2021),"3),"
(' Marlon Mack ',14,RB,6,2,8,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marlon Mack ' AND Anio = 2021),"3),"
(' J.J. Taylor ',22,RB,5,4,8,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'J.J. Taylor ' AND Anio = 2021),"3),"
(' Hunter Long ',20,TE,7,1,8,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Hunter Long ' AND Anio = 2021),"3),"
(' Racey McMath ',31,WR,9,2,8,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Racey McMath ' AND Anio = 2021),"3),"
(' Eric Tomlinson ',3,TE,17,1,7,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Eric Tomlinson ' AND Anio = 2021),"3),"
(' Johnny Stanton IV',8,FB,4,2,7,6,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Johnny Stanton IV' AND Anio = 2021),"3),"
(' Kyler Murray ',1,QB,14,0,7,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyler Murray ' AND Anio = 2021),"3),"
(' Miles Boykin ',3,WR,8,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Miles Boykin ' AND Anio = 2021),"3),"
(' Amani Hooker ',31,S,12,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Amani Hooker ' AND Anio = 2021),"3),"
(' Lane Johnson ',26,OT,13,1,5,5,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Lane Johnson ' AND Anio = 2021),"3),"
(' Keke Coutee ',14,WR,2,1,5,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Keke Coutee ' AND Anio = 2021),"3),"
(' Easop Winston Jr.',23,WR,3,1,5,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Easop Winston Jr.' AND Anio = 2021),"3),"
(' Nick Bellore ',29,LB,17,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Bellore ' AND Anio = 2021),"3),"
(' Taylor Decker ',11,OT,9,2,4,6,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Taylor Decker ' AND Anio = 2021),"3),"
(' Khari Blasingame ',31,FB,11,2,4,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Khari Blasingame ' AND Anio = 2021),"3),"
(' Ryan Nall ',6,FB,9,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Nall ' AND Anio = 2021),"3),"
(' Trayveon Williams ',7,RB,5,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trayveon Williams ' AND Anio = 2021),"3),"
(' Patrick Taylor Jr.',12,RB,9,2,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Patrick Taylor Jr.' AND Anio = 2021),"3),"
(' Danny Pinter ',14,C,16,1,2,2,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Danny Pinter ' AND Anio = 2021),"3),"
(' Andrew Thomas ',24,OT,13,1,2,2,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Andrew Thomas ' AND Anio = 2021),"3),"
(' Conor McDermott ',25,OT,6,1,1,1,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Conor McDermott ' AND Anio = 2021),"3),"
(' Christian Wilkins ',20,DT,17,1,1,1,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian Wilkins ' AND Anio = 2021),"3),"
(' Terence Steele ',9,OT,16,1,1,1,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Terence Steele ' AND Anio = 2021),"3),"
(' Drew Lock ',10,QB,6,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Drew Lock ' AND Anio = 2021),"3),"
(' Alex Armah ',23,RB,11,1,1,1,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Alex Armah ' AND Anio = 2021),"3),"
(' Trent Williams ',28,OT,15,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trent Williams ' AND Anio = 2021),"3),"
(' Travis Benjamin ',28,WR,10,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Travis Benjamin ' AND Anio = 2021),"3),"
(' Colin Thompson ',5,TE,11,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Colin Thompson ' AND Anio = 2021),"3),"
(' Dion Dawkins ',4,OT,16,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dion Dawkins ' AND Anio = 2021),"3),"
(' Darrell Daniels ',1,TE,15,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Darrell Daniels ' AND Anio = 2021),"3),"
(' Keion Crossen ',24,CB,16,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Keion Crossen ' AND Anio = 2021),"3),"
(' Matt Nelson ',11,OT,13,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Nelson ' AND Anio = 2021),"3),"
(' Giovanni Ricci ',5,FB,16,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Giovanni Ricci ' AND Anio = 2021),"3),"
(' Ben Ellefson ',21,TE,5,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ben Ellefson ' AND Anio = 2021),"3),"
(' Tyrie Cleveland ',10,WR,7,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyrie Cleveland ' AND Anio = 2021),"3),"
(' Stephen Sullivan ',5,TE,3,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Stephen Sullivan ' AND Anio = 2021),"3),"
(' Jalen Hurts ',26,QB,15,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Hurts ' AND Anio = 2021),"3),"
(' Jason Huntley ',26,RB,1,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jason Huntley ' AND Anio = 2021),"3),"
(' Tory Carter ',31,FB,7,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tory Carter ' AND Anio = 2021),"3),"
(' Isaiah Coulter ',6,WR,2,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Isaiah Coulter ' AND Anio = 2021),"3),"
(' Zach Wilson ',25,QB,13,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Wilson ' AND Anio = 2021),"3),"
(' Mekhi Sargent ',31,RB,7,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mekhi Sargent ' AND Anio = 2021),"3),"
(' Tevaughn Campbell ',18,CB,16,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tevaughn Campbell ' AND Anio = 2021),"3),"
(' Larry Rountree III',18,RB,12,1,-1,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Larry Rountree III' AND Anio = 2021),"3),"
(' Mike Remmers ',16,OT,4,1,-2,-2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Remmers ' AND Anio = 2021),"3),"
(' Taylor Heinicke ',32,QB,16,1,-2,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Taylor Heinicke ' AND Anio = 2021),"3),"
(' Diontae Spencer ',10,WR,15,1,-3,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Diontae Spencer ' AND Anio = 2021),"3),"
(' Aaron Rodgers ',12,QB,16,1,-4,-4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Aaron Rodgers ' AND Anio = 2021),"3),"
(' Jonathan Taylor ',14,RB,17,332,1811,83,18,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonathan Taylor ' AND Anio = 2021),"2),"
(' Nick Chubb ',8,RB,14,228,1259,70,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Chubb ' AND Anio = 2021),"2),"
(' Joe Mixon ',7,RB,16,292,1205,32,13,(SELECT Player_ID FROM Player_season WHERE Name = 'Joe Mixon ' AND Anio = 2021),"2),"
(' Najee Harris ',27,RB,17,307,1200,37,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Najee Harris ' AND Anio = 2021),"2),"
(' Dalvin Cook ',21,RB,13,249,1159,66,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Dalvin Cook ' AND Anio = 2021),"2),"
(' Antonio Gibson ',32,RB,16,258,1037,27,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Antonio Gibson ' AND Anio = 2021),"2),"
(' Ezekiel Elliott ',9,RB,17,237,1002,47,10,(SELECT Player_ID FROM Player_season WHERE Name = 'Ezekiel Elliott ' AND Anio = 2021),"2),"
(' Elijah Mitchell ',28,RB,11,207,963,39,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Elijah Mitchell ' AND Anio = 2021),"2),"
(' Derrick Henry ',31,RB,8,219,937,76,10,(SELECT Player_ID FROM Player_season WHERE Name = 'Derrick Henry ' AND Anio = 2021),"2),"
(' Damien Harris ',22,RB,15,202,929,64,15,(SELECT Player_ID FROM Player_season WHERE Name = 'Damien Harris ' AND Anio = 2021),"2),"
(' Melvin Gordon III',10,RB,16,203,918,70,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Melvin Gordon III' AND Anio = 2021),"2),"
(' Austin Ekeler ',18,RB,16,206,911,28,12,(SELECT Player_ID FROM Player_season WHERE Name = 'Austin Ekeler ' AND Anio = 2021),"2),"
(' Javonte Williams ',10,RB,17,203,903,49,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Javonte Williams ' AND Anio = 2021),"2),"
(' Alvin Kamara ',23,RB,13,240,898,30,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Alvin Kamara ' AND Anio = 2021),"2),"
(' Josh Jacobs ',17,RB,15,217,872,28,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Jacobs ' AND Anio = 2021),"2),"
(' Devin Singletary ',4,RB,17,188,870,46,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Devin Singletary ' AND Anio = 2021),"2),"
(' David Montgomery ',6,RB,13,225,849,41,7,(SELECT Player_ID FROM Player_season WHERE Name = 'David Montgomery ' AND Anio = 2021),"2),"
(' Sony Michel ',19,RB,17,208,845,39,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Sony Michel ' AND Anio = 2021),"2),"
(' AJ Dillon ',12,RB,17,187,803,36,5,(SELECT Player_ID FROM Player_season WHERE Name = 'AJ Dillon ' AND Anio = 2021),"2),"
(' Aaron Jones ',12,RB,15,171,799,57,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Aaron Jones ' AND Anio = 2021),"2),"
(' Jalen Hurts ',26,QB,15,139,784,31,10,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Hurts ' AND Anio = 2021),"2),"
(' Lamar Jackson ',3,QB,12,133,767,31,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Lamar Jackson ' AND Anio = 2021),"2),"
(' Josh Allen ',4,QB,17,122,763,34,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Allen ' AND Anio = 2021),"2),"
(' Miles Sanders ',26,RB,12,137,754,38,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Miles Sanders ' AND Anio = 2021),"2),"
(' James Conner ',1,RB,15,202,752,35,15,(SELECT Player_ID FROM Player_season WHERE Name = 'James Conner ' AND Anio = 2021),"2),"
(' Rashaad Penny ',29,RB,10,119,749,62,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Rashaad Penny ' AND Anio = 2021),"2),"
(' Tony Pollard ',9,RB,15,130,719,58,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Tony Pollard ' AND Anio = 2021),"2),"
(' Michael Carter ',25,RB,14,147,639,55,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Carter ' AND Anio = 2021),"2),"
(' Cordarrelle Patterson ',2,RB,16,153,618,39,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Cordarrelle Patterson ' AND Anio = 2021),"2),"
(' D'Andre Swift ',11,RB,13,151,617,57,5,(SELECT Player_ID FROM Player_season WHERE Name = 'D'Andre Swift ' AND Anio = 2021),"2),"
(' Myles Gaskin ',20,RB,17,173,612,30,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Myles Gaskin ' AND Anio = 2021),"2),"
(' Chuba Hubbard ',5,RB,17,172,612,26,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Chuba Hubbard ' AND Anio = 2021),"2),"
(' Rhamondre Stevenson ',22,RB,12,133,606,21,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Rhamondre Stevenson ' AND Anio = 2021),"2),"
(' Jamaal Williams ',11,RB,13,153,601,20,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamaal Williams ' AND Anio = 2021),"2),"
(' Devontae Booker ',24,RB,16,145,593,31,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Devontae Booker ' AND Anio = 2021),"2),"
(' Saquon Barkley ',24,RB,13,162,593,41,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Saquon Barkley ' AND Anio = 2021),"2),"
(' Chase Edmonds ',1,RB,12,116,592,54,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Chase Edmonds ' AND Anio = 2021),"2),"
(' Devonta Freeman ',3,RB,16,133,576,32,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Devonta Freeman ' AND Anio = 2021),"2),"
(' D'Onta Foreman ',31,RB,9,133,566,35,3,(SELECT Player_ID FROM Player_season WHERE Name = 'D'Onta Foreman ' AND Anio = 2021),"2),"
(' Darrel Williams ',16,RB,17,144,558,21,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Darrel Williams ' AND Anio = 2021),"2),"
(' Mark Ingram II',23,RB,14,160,554,28,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Mark Ingram II' AND Anio = 2021),"2),"
(' D'Ernest Johnson ',8,RB,17,100,534,30,3,(SELECT Player_ID FROM Player_season WHERE Name = 'D'Ernest Johnson ' AND Anio = 2021),"2),"
(' Clyde Edwards-Helaire ',16,RB,10,119,517,17,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Clyde Edwards-Helaire ' AND Anio = 2021),"2),"
(' Mike Davis ',2,RB,17,138,503,18,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Davis ' AND Anio = 2021),"2),"
(' Latavius Murray ',3,RB,14,119,501,46,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Latavius Murray ' AND Anio = 2021),"2),"
(' Alexander Mattison ',21,RB,16,134,491,48,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Alexander Mattison ' AND Anio = 2021),"2),"
(' Khalil Herbert ',6,RB,17,103,433,29,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Khalil Herbert ' AND Anio = 2021),"2),"
(' Ronald Jones ',30,RB,16,101,428,30,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Ronald Jones ' AND Anio = 2021),"2),"
(' Rex Burkhead ',13,RB,16,122,427,36,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Rex Burkhead ' AND Anio = 2021),"2),"
(' Kyler Murray ',1,QB,14,88,423,57,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyler Murray ' AND Anio = 2021),"2),"
(' Jordan Howard ',26,RB,7,86,406,25,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Howard ' AND Anio = 2021),"2),"
(' Kareem Hunt ',8,RB,8,78,386,33,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Kareem Hunt ' AND Anio = 2021),"2),"
(' Patrick Mahomes ',16,QB,17,66,381,32,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Patrick Mahomes ' AND Anio = 2021),"2),"
(' Taysom Hill ',23,QB,12,70,374,44,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Taysom Hill ' AND Anio = 2021),"2),"
(' Boston Scott ',26,RB,16,87,373,23,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Boston Scott ' AND Anio = 2021),"2),"
(' Deebo Samuel ',28,WR,16,59,365,49,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Deebo Samuel ' AND Anio = 2021),"2),"
(' Justin Jackson ',18,RB,14,68,364,75,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Jackson ' AND Anio = 2021),"2),"
(' Tevin Coleman ',25,RB,11,84,356,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tevin Coleman ' AND Anio = 2021),"2),"
(' Dontrell Hilliard ',31,RB,8,56,350,68,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Dontrell Hilliard ' AND Anio = 2021),"2),"
(' Zack Moss ',4,RB,13,96,345,17,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Zack Moss ' AND Anio = 2021),"2),"
(' Trevor Lawrence ',15,QB,17,73,334,26,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Trevor Lawrence ' AND Anio = 2021),"2),"
(' Duke Johnson ',20,RB,5,71,330,27,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Duke Johnson ' AND Anio = 2021),"2),"
(' Taylor Heinicke ',32,QB,16,60,313,38,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Taylor Heinicke ' AND Anio = 2021),"2),"
(' Justin Herbert ',18,QB,17,63,302,36,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Herbert ' AND Anio = 2021),"2),"
(' Jeff Wilson Jr.',28,RB,9,79,294,17,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeff Wilson Jr.' AND Anio = 2021),"2),"
(' Tyler Huntley ',3,QB,7,47,294,21,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Huntley ' AND Anio = 2021),"2),"
(' Kenneth Gainwell ',26,RB,16,68,291,18,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenneth Gainwell ' AND Anio = 2021),"2),"
(' Nyheim Hines ',14,RB,17,56,276,34,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Nyheim Hines ' AND Anio = 2021),"2),"
(' Ryan Tannehill ',31,QB,17,55,270,28,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Tannehill ' AND Anio = 2021),"2),"
(' Jaret Patterson ',32,RB,17,68,266,13,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaret Patterson ' AND Anio = 2021),"2),"
(' Derrick Gore ',16,RB,11,51,256,51,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Derrick Gore ' AND Anio = 2021),"2),"
(' Phillip Lindsay ',20,RB,14,88,249,35,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Phillip Lindsay ' AND Anio = 2021),"2),"
(' Samaje Perine ',7,RB,16,55,246,46,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Samaje Perine ' AND Anio = 2021),"2),"
(' Ty Johnson ',25,RB,16,61,238,24,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Ty Johnson ' AND Anio = 2021),"2),"
(' Cam Newton ',5,QB,8,47,230,33,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Cam Newton ' AND Anio = 2021),"2),"
(' Craig Reynolds ',11,RB,5,55,230,35,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Craig Reynolds ' AND Anio = 2021),"2),"
(' David Johnson ',13,RB,13,67,228,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'David Johnson ' AND Anio = 2021),"2),"
(' Brandon Bolden ',22,RB,17,44,226,24,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Bolden ' AND Anio = 2021),"2),"
(' Sam Darnold ',5,QB,12,48,222,30,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Sam Darnold ' AND Anio = 2021),"2),"
(' Carson Wentz ',14,QB,17,57,215,18,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Carson Wentz ' AND Anio = 2021),"2),"
(' Peyton Barber ',17,RB,10,55,212,27,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Peyton Barber ' AND Anio = 2021),"2),"
(' Ty'Son Williams ',3,RB,13,35,185,35,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ty'Son Williams ' AND Anio = 2021),"2),"
(' Zach Wilson ',25,QB,13,29,185,52,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Wilson ' AND Anio = 2021),"2),"
(' Russell Wilson ',29,QB,14,43,183,17,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Russell Wilson ' AND Anio = 2021),"2),"
(' Ke'Shawn Vaughn ',30,RB,12,36,180,55,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Ke'Shawn Vaughn ' AND Anio = 2021),"2),"
(' Travis Homer ',29,RB,14,21,177,73,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Travis Homer ' AND Anio = 2021),"2),"
(' Royce Freeman ',5,RB,15,56,169,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Royce Freeman ' AND Anio = 2021),"2),"
(' Trey Lance ',28,QB,6,38,168,15,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Trey Lance ' AND Anio = 2021),"2),"
(' Trey Sermon ',28,RB,9,41,167,16,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Trey Sermon ' AND Anio = 2021),"2),"
(' Ameer Abdullah ',5,RB,17,51,166,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ameer Abdullah ' AND Anio = 2021),"2),"
(' Damien Williams ',6,RB,12,40,164,23,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Damien Williams ' AND Anio = 2021),"2),"
(' Tyrod Taylor ',13,QB,6,19,151,30,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyrod Taylor ' AND Anio = 2021),"2),"
(' Salvon Ahmed ',20,RB,12,54,149,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Salvon Ahmed ' AND Anio = 2021),"2),"
(' Dak Prescott ',9,QB,16,48,146,21,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Dak Prescott ' AND Anio = 2021),"2),"
(' Tony Jones Jr.',23,RB,11,54,142,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tony Jones Jr.' AND Anio = 2021),"2),"
(' Corey Clement ',9,RB,17,33,140,38,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Corey Clement ' AND Anio = 2021),"2),"
(' DeeJay Dallas ',29,RB,17,33,138,15,2,(SELECT Player_ID FROM Player_season WHERE Name = 'DeeJay Dallas ' AND Anio = 2021),"2),"
(' Dare Ogunbowale ',15,RB,17,43,137,12,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Dare Ogunbowale ' AND Anio = 2021),"2),"
(' Mac Jones ',22,QB,17,44,129,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mac Jones ' AND Anio = 2021),"2),"
(' Tua Tagovailoa ',20,QB,13,42,128,23,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Tua Tagovailoa ' AND Anio = 2021),"2),"
(' Kendrick Bourne ',22,WR,17,12,125,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kendrick Bourne ' AND Anio = 2021),"2),"
(' Matt Breida ',4,RB,9,26,125,28,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Breida ' AND Anio = 2021),"2),"
(' Godwin Igwebuike ',11,RB,17,18,118,42,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Godwin Igwebuike ' AND Anio = 2021),"2),"
(' Joe Burrow ',7,QB,16,40,118,12,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Joe Burrow ' AND Anio = 2021),"2),"
(' Eno Benjamin ',1,RB,9,34,118,21,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Eno Benjamin ' AND Anio = 2021),"2),"
(' Kirk Cousins ',21,QB,16,29,115,29,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kirk Cousins ' AND Anio = 2021),"2),"
(' Derek Carr ',17,QB,17,40,108,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Derek Carr ' AND Anio = 2021),"2),"
(' Qadree Ollison ',2,RB,8,21,105,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Qadree Ollison ' AND Anio = 2021),"2),"
(' Wayne Gallman ',21,RB,8,28,104,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Wayne Gallman ' AND Anio = 2021),"2),"
(' Joshua Kelley ',18,RB,10,33,102,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Joshua Kelley ' AND Anio = 2021),"2),"
(' Aaron Rodgers ',12,QB,16,33,101,18,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Aaron Rodgers ' AND Anio = 2021),"2),"
(' Le'Veon Bell ',30,RB,8,39,101,12,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Le'Veon Bell ' AND Anio = 2021),"2),"
(' Austin Walter ',25,RB,4,26,101,14,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Austin Walter ' AND Anio = 2021),"2),"
(' Marlon Mack ',14,RB,6,28,101,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marlon Mack ' AND Anio = 2021),"2),"
(' Elijhaa Penny ',24,RB,17,24,99,12,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Elijhaa Penny ' AND Anio = 2021),"2),"
(' Benny Snell Jr.',27,RB,17,36,98,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Benny Snell Jr.' AND Anio = 2021),"2),"
(' Tyreek Hill ',16,WR,17,9,96,33,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyreek Hill ' AND Anio = 2021),"2),"
(' Chase Claypool ',27,WR,15,14,96,25,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chase Claypool ' AND Anio = 2021),"2),"
(' DeAndre Carter ',32,WR,17,10,89,27,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DeAndre Carter ' AND Anio = 2021),"2),"
(' Patrick Taylor Jr.',12,RB,9,23,89,12,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Patrick Taylor Jr.' AND Anio = 2021),"2),"
(' Marcus Mariota ',17,QB,10,13,87,31,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Marcus Mariota ' AND Anio = 2021),"2),"
(' Jared Goff ',11,QB,14,17,87,26,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jared Goff ' AND Anio = 2021),"2),"
(' Larry Rountree III',18,RB,12,36,87,13,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Larry Rountree III' AND Anio = 2021),"2),"
(' Matt Ryan ',2,QB,17,40,82,17,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Ryan ' AND Anio = 2021),"2),"
(' Tom Brady ',30,QB,17,28,81,13,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Tom Brady ' AND Anio = 2021),"2),"
(' Ryquell Armstead ',15,RB,2,15,80,26,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryquell Armstead ' AND Anio = 2021),"2),"
(' Jonathan Williams ',32,RB,5,17,79,23,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonathan Williams ' AND Anio = 2021),"2),"
(' Chris Evans ',7,RB,14,17,77,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Evans ' AND Anio = 2021),"2),"
(' Andy Dalton ',6,QB,8,16,76,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andy Dalton ' AND Anio = 2021),"2),"
(' CeeDee Lamb ',9,WR,16,9,76,33,0,(SELECT Player_ID FROM Player_season WHERE Name = 'CeeDee Lamb ' AND Anio = 2021),"2),"
(' Rondale Moore ',1,WR,14,18,76,26,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Rondale Moore ' AND Anio = 2021),"2),"
(' Jermar Jefferson ',11,RB,7,15,74,28,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jermar Jefferson ' AND Anio = 2021),"2),"
(' Jacoby Brissett ',20,QB,11,19,70,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jacoby Brissett ' AND Anio = 2021),"2),"
(' JaMycal Hasty ',28,RB,11,16,68,21,1,(SELECT Player_ID FROM Player_season WHERE Name = 'JaMycal Hasty ' AND Anio = 2021),"2),"
(' Jake Fromm ',24,QB,3,8,65,27,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jake Fromm ' AND Anio = 2021),"2),"
(' Jerick McKinnon ',16,RB,13,12,62,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jerick McKinnon ' AND Anio = 2021),"2),"
(' Kene Nwangwu ',21,RB,11,13,61,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kene Nwangwu ' AND Anio = 2021),"2),"
(' Amon-Ra St. Brown',11,WR,17,7,61,26,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Amon-Ra St. Brown' AND Anio = 2021),"2),"
(' Dee Eskridge ',29,WR,10,4,59,30,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dee Eskridge ' AND Anio = 2021),"2),"
(' Mason Rudolph ',27,QB,2,5,53,26,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mason Rudolph ' AND Anio = 2021),"2),"
(' Drew Lock ',10,QB,6,10,53,23,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Drew Lock ' AND Anio = 2021),"2),"
(' Diontae Johnson ',27,WR,16,5,53,25,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Diontae Johnson ' AND Anio = 2021),"2),"
(' Jimmy Garoppolo ',28,QB,15,38,51,7,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Jimmy Garoppolo ' AND Anio = 2021),"2),"
(' Trayveon Williams ',7,RB,5,15,51,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trayveon Williams ' AND Anio = 2021),"2),"
(' Jason Huntley ',26,RB,1,13,51,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jason Huntley ' AND Anio = 2021),"2),"
(' Devin Duvernay ',3,WR,16,7,50,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Devin Duvernay ' AND Anio = 2021),"2),"
(' DJ Moore ',5,WR,17,8,48,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DJ Moore ' AND Anio = 2021),"2),"
(' Isaiah McKenzie ',4,WR,15,9,47,10,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Isaiah McKenzie ' AND Anio = 2021),"2),"
(' Mecole Hardman ',16,WR,17,8,46,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mecole Hardman ' AND Anio = 2021),"2),"
(' Ty Montgomery II',23,WR,14,15,44,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ty Montgomery II' AND Anio = 2021),"2),"
(' Michael Pittman Jr.',14,WR,17,5,44,25,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Pittman Jr.' AND Anio = 2021),"2),"
(' Davis Mills ',13,QB,13,18,44,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Davis Mills ' AND Anio = 2021),"2),"
(' Matthew Stafford ',19,QB,17,32,43,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Matthew Stafford ' AND Anio = 2021),"2),"
(' Scotty Miller ',30,WR,9,2,43,33,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Scotty Miller ' AND Anio = 2021),"2),"
(' Geno Smith ',29,QB,4,9,42,12,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Geno Smith ' AND Anio = 2021),"2),"
(' Laviska Shenault Jr.',15,WR,16,11,41,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Laviska Shenault Jr.' AND Anio = 2021),"2),"
(' Deonte Harty ',23,WR,13,5,41,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Deonte Harty ' AND Anio = 2021),"2),"
(' Jarvis Landry ',8,WR,12,6,40,16,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jarvis Landry ' AND Anio = 2021),"2),"
(' Jalen Richard ',17,RB,10,9,40,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Richard ' AND Anio = 2021),"2),"
(' Jonnu Smith ',22,TE,16,9,40,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonnu Smith ' AND Anio = 2021),"2),"
(' Anthony Schwartz ',8,WR,14,6,39,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Anthony Schwartz ' AND Anio = 2021),"2),"
(' Colt McCoy ',1,QB,8,22,37,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Colt McCoy ' AND Anio = 2021),"2),"
(' J.J. Taylor ',22,RB,5,19,37,15,2,(SELECT Player_ID FROM Player_season WHERE Name = 'J.J. Taylor ' AND Anio = 2021),"2),"
(' Robbie Chosen ',5,WR,17,3,36,30,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Robbie Chosen ' AND Anio = 2021),"2),"
(' Kalen Ballage ',27,RB,17,12,36,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kalen Ballage ' AND Anio = 2021),"2),"
(' Mike Boone ',10,RB,8,4,35,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Boone ' AND Anio = 2021),"2),"
(' Jalen Guyton ',18,WR,16,7,34,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Guyton ' AND Anio = 2021),"2),"
(' C.J. Ham ',21,FB,17,7,34,30,0,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Ham ' AND Anio = 2021),"2),"
(' Mike Glennon ',24,QB,6,7,33,13,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Glennon ' AND Anio = 2021),"2),"
(' Jonathan Ward ',1,RB,13,9,33,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonathan Ward ' AND Anio = 2021),"2),"
(' Allen Lazard ',12,WR,15,3,32,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Allen Lazard ' AND Anio = 2021),"2),"
(' Freddie Swain ',29,WR,17,5,32,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Freddie Swain ' AND Anio = 2021),"2),"
(' Darnell Mooney ',6,WR,17,6,32,15,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Darnell Mooney ' AND Anio = 2021),"2),"
(' Ashton Dulin ',14,WR,17,3,32,37,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ashton Dulin ' AND Anio = 2021),"2),"
(' Jalen Reagor ',26,WR,17,10,32,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Reagor ' AND Anio = 2021),"2),"
(' Emmanuel Sanders ',4,WR,14,2,31,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Emmanuel Sanders ' AND Anio = 2021),"2),"
(' Keith Smith ',2,FB,17,9,31,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Keith Smith ' AND Anio = 2021),"2),"
(' La'Mical Perine ',25,RB,4,8,31,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'La'Mical Perine ' AND Anio = 2021),"2),"
(' Deon Jackson ',14,RB,9,13,31,10,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Deon Jackson ' AND Anio = 2021),"2),"
(' Josh Johnson ',25,QB,4,9,28,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Johnson ' AND Anio = 2021),"2),"
(' Kalif Raymond ',11,WR,16,4,28,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kalif Raymond ' AND Anio = 2021),"2),"
(' C.J. Moore ',11,S,17,1,28,28,0,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Moore ' AND Anio = 2021),"2),"
(' Jordan Love ',12,QB,6,12,27,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Love ' AND Anio = 2021),"2),"
(' Michael Burton ',16,FB,16,8,26,7,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Burton ' AND Anio = 2021),"2),"
(' Mitchell Trubisky ',4,QB,6,13,24,22,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Mitchell Trubisky ' AND Anio = 2021),"2),"
(' Demetric Felton ',8,RB,16,7,24,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Demetric Felton ' AND Anio = 2021),"2),"
(' Greg Dortch ',1,WR,5,1,24,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Greg Dortch ' AND Anio = 2021),"2),"
(' Jason Cabinda ',11,FB,14,3,23,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jason Cabinda ' AND Anio = 2021),"2),"
(' Case Keenum ',8,QB,7,12,22,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Case Keenum ' AND Anio = 2021),"2),"
(' Kyle Juszczyk ',28,FB,17,8,22,6,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Juszczyk ' AND Anio = 2021),"2),"
(' Tyler Boyd ',7,WR,16,2,22,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Boyd ' AND Anio = 2021),"2),"
(' Tavon Austin ',15,WR,13,3,21,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tavon Austin ' AND Anio = 2021),"2),"
(' Brandin Cooks ',13,WR,16,2,21,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandin Cooks ' AND Anio = 2021),"2),"
(' Zach Pascal ',14,WR,16,2,21,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Pascal ' AND Anio = 2021),"2),"
(' Gardner Minshew ',26,QB,4,9,21,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Gardner Minshew ' AND Anio = 2021),"2),"
(' Alex Armah ',23,RB,11,5,21,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Alex Armah ' AND Anio = 2021),"2),"
(' Ja'Marr Chase ',7,WR,17,7,21,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ja'Marr Chase ' AND Anio = 2021),"2),"
(' Trevor Siemian ',23,QB,6,9,20,17,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Trevor Siemian ' AND Anio = 2021),"2),"
(' George Kittle ',28,TE,14,3,20,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'George Kittle ' AND Anio = 2021),"2),"
(' Gerald Everett ',29,TE,15,3,20,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Gerald Everett ' AND Anio = 2021),"2),"
(' Van Jefferson ',19,WR,17,2,20,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Van Jefferson ' AND Anio = 2021),"2),"
(' Andre Roberts ',18,WR,16,3,19,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andre Roberts ' AND Anio = 2021),"2),"
(' Cooper Kupp ',19,WR,17,4,18,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cooper Kupp ' AND Anio = 2021),"2),"
(' Albert Wilson ',20,WR,14,4,17,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Albert Wilson ' AND Anio = 2021),"2),"
(' Brandon Aiyuk ',28,WR,17,5,17,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Aiyuk ' AND Anio = 2021),"2),"
(' Dwayne Washington ',23,RB,14,4,16,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dwayne Washington ' AND Anio = 2021),"2),"
(' John Ross ',24,WR,10,1,16,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'John Ross ' AND Anio = 2021),"2),"
(' Ray-Ray McCloud III',27,WR,16,2,15,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ray-Ray McCloud III' AND Anio = 2021),"2),"
(' Odell Beckham Jr.',8,WR,14,2,14,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Odell Beckham Jr.' AND Anio = 2021),"2),"
(' Sean Mannion ',21,QB,1,2,14,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Sean Mannion ' AND Anio = 2021),"2),"
(' Sean Chandler ',5,S,15,1,14,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Sean Chandler ' AND Anio = 2021),"2),"
(' Equanimeous St. Brown',12,WR,13,3,14,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Equanimeous St. Brown' AND Anio = 2021),"2),"
(' Cyril Grayson Jr.',30,WR,5,1,14,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cyril Grayson Jr.' AND Anio = 2021),"2),"
(' Justin Jefferson ',21,WR,17,6,14,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Jefferson ' AND Anio = 2021),"2),"
(' Tim Boyle ',11,QB,5,2,13,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tim Boyle ' AND Anio = 2021),"2),"
(' PJ Walker ',5,QB,5,7,13,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'PJ Walker ' AND Anio = 2021),"2),"
(' Terry McLaurin ',32,WR,17,1,12,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Terry McLaurin ' AND Anio = 2021),"2),"
(' Nelson Agholor ',22,WR,15,3,11,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nelson Agholor ' AND Anio = 2021),"2),"
(' Kyle Allen ',32,QB,2,2,11,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Allen ' AND Anio = 2021),"2),"
(' Curtis Samuel ',32,WR,5,4,11,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Curtis Samuel ' AND Anio = 2021),"2),"
(' Buddy Howell ',19,RB,10,5,11,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Buddy Howell ' AND Anio = 2021),"2),"
(' Christian Kirk ',1,WR,17,1,11,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian Kirk ' AND Anio = 2021),"2),"
(' Cedrick Wilson Jr.',9,WR,16,2,11,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cedrick Wilson Jr.' AND Anio = 2021),"2),"
(' Amari Rodgers ',12,WR,16,1,11,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Amari Rodgers ' AND Anio = 2021),"2),"
(' Jaelon Darden ',30,WR,9,1,11,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaelon Darden ' AND Anio = 2021),"2),"
(' Tommy Tremble ',5,TE,16,3,11,7,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tommy Tremble ' AND Anio = 2021),"2),"
(' Mekhi Sargent ',31,RB,7,5,11,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mekhi Sargent ' AND Anio = 2021),"2),"
(' Mike Evans ',30,WR,16,1,10,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Evans ' AND Anio = 2021),"2),"
(' Blake Bell ',16,TE,16,4,10,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Blake Bell ' AND Anio = 2021),"2),"
(' K.J. Osborn ',21,WR,17,1,10,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'K.J. Osborn ' AND Anio = 2021),"2),"
(' A.J. Brown ',31,WR,13,2,10,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'A.J. Brown ' AND Anio = 2021),"2),"
(' Tyler Lockett ',29,WR,16,2,9,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Lockett ' AND Anio = 2021),"2),"
(' Chester Rogers ',31,WR,16,1,9,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chester Rogers ' AND Anio = 2021),"2),"
(' Jakobi Meyers ',22,WR,17,1,9,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jakobi Meyers ' AND Anio = 2021),"2),"
(' Sam Ehlinger ',14,QB,3,3,9,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Sam Ehlinger ' AND Anio = 2021),"2),"
(' Gunner Olszewski ',22,WR,16,1,9,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Gunner Olszewski ' AND Anio = 2021),"2),"
(' Nick Foles ',6,QB,1,4,8,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Foles ' AND Anio = 2021),"2),"
(' Gabe Nabers ',18,FB,10,3,8,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Gabe Nabers ' AND Anio = 2021),"2),"
(' Cam Sims ',32,WR,14,1,7,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cam Sims ' AND Anio = 2021),"2),"
(' Tremon Smith ',13,CB,17,1,7,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tremon Smith ' AND Anio = 2021),"2),"
(' Preston Williams ',20,WR,8,1,7,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Preston Williams ' AND Anio = 2021),"2),"
(' Dallin Leavitt ',17,S,16,2,6,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dallin Leavitt ' AND Anio = 2021),"2),"
(' David Blough ',11,QB,1,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'David Blough ' AND Anio = 2021),"2),"
(' Khari Blasingame ',31,FB,11,3,6,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Khari Blasingame ' AND Anio = 2021),"2),"
(' Feleipe Franks ',2,TE,9,3,6,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Feleipe Franks ' AND Anio = 2021),"2),"
(' Ian Book ',23,QB,1,3,6,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ian Book ' AND Anio = 2021),"2),"
(' DK Metcalf ',29,WR,17,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DK Metcalf ' AND Anio = 2021),"2),"
(' Kadarius Toney ',24,WR,10,3,6,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kadarius Toney ' AND Anio = 2021),"2),"
(' Joshua Palmer ',18,WR,17,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Joshua Palmer ' AND Anio = 2021),"2),"
(' Ben Roethlisberger ',27,QB,16,20,5,8,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ben Roethlisberger ' AND Anio = 2021),"2),"
(' Johnny Stanton IV',8,FB,4,3,5,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Johnny Stanton IV' AND Anio = 2021),"2),"
(' Adam Prentice ',23,FB,7,3,5,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Adam Prentice ' AND Anio = 2021),"2),"
(' Jake Funk ',19,RB,10,2,5,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jake Funk ' AND Anio = 2021),"2),"
(' Marquise Brown ',3,WR,16,1,5,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marquise Brown ' AND Anio = 2021),"2),"
(' DeSean Jackson ',19,WR,16,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DeSean Jackson ' AND Anio = 2021),"2),"
(' Zach Ertz ',26,TE,17,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Ertz ' AND Anio = 2021),"2),"
(' Reggie Bonnafon ',5,RB,4,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Reggie Bonnafon ' AND Anio = 2021),"2),"
(' Ryan Nall ',6,FB,9,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Nall ' AND Anio = 2021),"2),"
(' Andrew Wingard ',15,S,15,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andrew Wingard ' AND Anio = 2021),"2),"
(' Dawson Knox ',4,TE,15,0,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dawson Knox ' AND Anio = 2021),"2),"
(' Braden Mann ',25,P,10,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Braden Mann ' AND Anio = 2021),"2),"
(' Joe Flacco ',25,QB,2,2,3,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Joe Flacco ' AND Anio = 2021),"2),"
(' Travis Kelce ',16,TE,16,2,3,4,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Travis Kelce ' AND Anio = 2021),"2),"
(' Chris Conley ',13,WR,16,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Conley ' AND Anio = 2021),"2),"
(' Durham Smythe ',20,TE,17,2,3,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Durham Smythe ' AND Anio = 2021),"2),"
(' Zay Jones ',17,WR,17,2,3,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Zay Jones ' AND Anio = 2021),"2),"
(' Jordan Akins ',13,TE,13,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Akins ' AND Anio = 2021),"2),"
(' Hunter Renfrow ',17,WR,17,3,3,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Hunter Renfrow ' AND Anio = 2021),"2),"
(' Stanley Morgan Jr.',7,WR,17,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Stanley Morgan Jr.' AND Anio = 2021),"2),"
(' Nathan Cottrell ',15,RB,4,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nathan Cottrell ' AND Anio = 2021),"2),"
(' Maurice Ffrench ',18,WR,3,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Maurice Ffrench ' AND Anio = 2021),"2),"
(' Reggie Gilliam ',4,FB,16,3,3,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Reggie Gilliam ' AND Anio = 2021),"2),"
(' Quez Watkins ',26,WR,17,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Quez Watkins ' AND Anio = 2021),"2),"
(' Cam Akers ',19,RB,1,5,3,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cam Akers ' AND Anio = 2021),"2),"
(' Jerry Jeudy ',10,WR,10,2,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jerry Jeudy ' AND Anio = 2021),"2),"
(' Anthony McFarland Jr.',27,RB,2,3,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Anthony McFarland Jr.' AND Anio = 2021),"2),"
(' Jaylen Waddle ',20,WR,16,2,3,2,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaylen Waddle ' AND Anio = 2021),"2),"
(' Olamide Zaccheaus ',2,WR,17,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Olamide Zaccheaus ' AND Anio = 2021),"2),"
(' Kenny Stills ',23,WR,13,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenny Stills ' AND Anio = 2021),"2),"
(' Michael Palardy ',20,P,17,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Palardy ' AND Anio = 2021),"2),"
(' Derek Watt ',27,FB,17,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Derek Watt ' AND Anio = 2021),"2),"
(' David Njoku ',8,TE,16,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'David Njoku ' AND Anio = 2021),"2),"
(' Dax Milne ',32,WR,13,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dax Milne ' AND Anio = 2021),"2),"
(' Andy Lee ',1,P,16,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andy Lee ' AND Anio = 2021),"2),"
(' Chad Henne ',16,QB,4,8,0,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chad Henne ' AND Anio = 2021),"2),"
(' Johnny Hekker ',19,P,17,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Johnny Hekker ' AND Anio = 2021),"2),"
(' Andy Janovich ',8,FB,13,2,0,1,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Andy Janovich ' AND Anio = 2021),"2),"
(' Clayton Fejedelem ',20,S,16,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Clayton Fejedelem ' AND Anio = 2021),"2),"
(' Mark Andrews ',3,TE,17,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mark Andrews ' AND Anio = 2021),"2),"
(' Bryan Edwards ',17,WR,17,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Bryan Edwards ' AND Anio = 2021),"2),"
(' Cole Kmet ',6,TE,17,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cole Kmet ' AND Anio = 2021),"2),"
(' Marquise Goodwin ',6,WR,14,2,-1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marquise Goodwin ' AND Anio = 2021),"2),"
(' Brandon Allen ',7,QB,6,7,-1,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Allen ' AND Anio = 2021),"2),"
(' Mike White ',25,QB,4,5,-1,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike White ' AND Anio = 2021),"2),"
(' John Wolford ',19,QB,3,2,-1,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'John Wolford ' AND Anio = 2021),"2),"
(' Jeff Smith ',25,WR,12,1,-1,-1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeff Smith ' AND Anio = 2021),"2),"
(' Chase Daniel ',18,QB,1,2,-2,-1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chase Daniel ' AND Anio = 2021),"2),"
(' Breshad Perriman ',30,WR,6,1,-3,-3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Breshad Perriman ' AND Anio = 2021),"2),"
(' Evan Engram ',24,TE,15,1,-3,-3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Evan Engram ' AND Anio = 2021),"2),"
(' Alex Bachman ',24,WR,3,1,-3,-3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Alex Bachman ' AND Anio = 2021),"2),"
(' Dyami Brown ',32,WR,15,1,-4,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dyami Brown ' AND Anio = 2021),"2),"
(' Logan Woodside ',31,QB,5,6,-6,-1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Logan Woodside ' AND Anio = 2021),"2),"
(' Blaine Gabbert ',30,QB,6,9,-7,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Blaine Gabbert ' AND Anio = 2021),"2),"
(' Brian Hoyer ',22,QB,5,11,-8,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brian Hoyer ' AND Anio = 2021),"2),"
(' Cooper Rush ',9,QB,5,9,-8,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cooper Rush ' AND Anio = 2021),"2),"
(' Darius Slayton ',24,WR,13,1,-13,-13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Darius Slayton ' AND Anio = 2021),"2),"
(' Patrick Mahomes ',16,QB,17,648,5250,67,41,(SELECT Player_ID FROM Player_season WHERE Name = 'Patrick Mahomes ' AND Anio = 2022),"1),"
(' Justin Herbert ',18,QB,17,699,4739,55,25,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Herbert ' AND Anio = 2022),"1),"
(' Tom Brady ',30,QB,17,733,4694,63,25,(SELECT Player_ID FROM Player_season WHERE Name = 'Tom Brady ' AND Anio = 2022),"1),"
(' Kirk Cousins ',21,QB,17,643,4547,66,29,(SELECT Player_ID FROM Player_season WHERE Name = 'Kirk Cousins ' AND Anio = 2022),"1),"
(' Joe Burrow ',7,QB,16,606,4475,60,35,(SELECT Player_ID FROM Player_season WHERE Name = 'Joe Burrow ' AND Anio = 2022),"1),"
(' Jared Goff ',11,QB,17,587,4438,81,29,(SELECT Player_ID FROM Player_season WHERE Name = 'Jared Goff ' AND Anio = 2022),"1),"
(' Josh Allen ',4,QB,16,567,4283,98,35,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Allen ' AND Anio = 2022),"1),"
(' Geno Smith ',29,QB,17,572,4282,54,30,(SELECT Player_ID FROM Player_season WHERE Name = 'Geno Smith ' AND Anio = 2022),"1),"
(' Trevor Lawrence ',15,QB,17,584,4113,59,25,(SELECT Player_ID FROM Player_season WHERE Name = 'Trevor Lawrence ' AND Anio = 2022),"1),"
(' Jalen Hurts ',26,QB,15,460,3701,68,22,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Hurts ' AND Anio = 2022),"1),"
(' Aaron Rodgers ',12,QB,17,542,3695,58,26,(SELECT Player_ID FROM Player_season WHERE Name = 'Aaron Rodgers ' AND Anio = 2022),"1),"
(' Tua Tagovailoa ',20,QB,13,400,3548,84,25,(SELECT Player_ID FROM Player_season WHERE Name = 'Tua Tagovailoa ' AND Anio = 2022),"1),"
(' Russell Wilson ',10,QB,15,483,3524,67,16,(SELECT Player_ID FROM Player_season WHERE Name = 'Russell Wilson ' AND Anio = 2022),"1),"
(' Derek Carr ',17,QB,15,502,3522,60,24,(SELECT Player_ID FROM Player_season WHERE Name = 'Derek Carr ' AND Anio = 2022),"1),"
(' Daniel Jones ',24,QB,16,472,3205,65,15,(SELECT Player_ID FROM Player_season WHERE Name = 'Daniel Jones ' AND Anio = 2022),"1),"
(' Davis Mills ',13,QB,15,479,3118,58,17,(SELECT Player_ID FROM Player_season WHERE Name = 'Davis Mills ' AND Anio = 2022),"1),"
(' Matt Ryan ',14,QB,12,461,3057,45,14,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Ryan ' AND Anio = 2022),"1),"
(' Mac Jones ',22,QB,14,442,2997,48,14,(SELECT Player_ID FROM Player_season WHERE Name = 'Mac Jones ' AND Anio = 2022),"1),"
(' Andy Dalton ',23,QB,14,378,2871,64,18,(SELECT Player_ID FROM Player_season WHERE Name = 'Andy Dalton ' AND Anio = 2022),"1),"
(' Dak Prescott ',9,QB,12,394,2860,68,23,(SELECT Player_ID FROM Player_season WHERE Name = 'Dak Prescott ' AND Anio = 2022),"1),"
(' Jacoby Brissett ',8,QB,16,369,2608,55,12,(SELECT Player_ID FROM Player_season WHERE Name = 'Jacoby Brissett ' AND Anio = 2022),"1),"
(' Ryan Tannehill ',31,QB,12,325,2536,69,13,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Tannehill ' AND Anio = 2022),"1),"
(' Jimmy Garoppolo ',28,QB,11,308,2437,57,16,(SELECT Player_ID FROM Player_season WHERE Name = 'Jimmy Garoppolo ' AND Anio = 2022),"1),"
(' Kenny Pickett ',27,QB,13,389,2404,57,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenny Pickett ' AND Anio = 2022),"1),"
(' Kyler Murray ',1,QB,11,390,2368,38,14,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyler Murray ' AND Anio = 2022),"1),"
(' Lamar Jackson ',3,QB,12,326,2242,75,17,(SELECT Player_ID FROM Player_season WHERE Name = 'Lamar Jackson ' AND Anio = 2022),"1),"
(' Justin Fields ',6,QB,15,318,2242,56,17,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Fields ' AND Anio = 2022),"1),"
(' Marcus Mariota ',2,QB,13,300,2219,75,15,(SELECT Player_ID FROM Player_season WHERE Name = 'Marcus Mariota ' AND Anio = 2022),"1),"
(' Baker Mayfield ',5,QB,12,335,2163,75,10,(SELECT Player_ID FROM Player_season WHERE Name = 'Baker Mayfield ' AND Anio = 2022),"1),"
(' Matthew Stafford ',19,QB,9,303,2087,75,10,(SELECT Player_ID FROM Player_season WHERE Name = 'Matthew Stafford ' AND Anio = 2022),"1),"
(' Taylor Heinicke ',32,QB,9,259,1859,61,12,(SELECT Player_ID FROM Player_season WHERE Name = 'Taylor Heinicke ' AND Anio = 2022),"1),"
(' Carson Wentz ',32,QB,8,276,1755,75,11,(SELECT Player_ID FROM Player_season WHERE Name = 'Carson Wentz ' AND Anio = 2022),"1),"
(' Zach Wilson ',25,QB,9,242,1688,79,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Wilson ' AND Anio = 2022),"1),"
(' Brock Purdy ',28,QB,9,170,1374,54,13,(SELECT Player_ID FROM Player_season WHERE Name = 'Brock Purdy ' AND Anio = 2022),"1),"
(' Mitchell Trubisky ',27,QB,7,180,1252,45,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Mitchell Trubisky ' AND Anio = 2022),"1),"
(' Mike White ',25,QB,4,175,1192,60,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike White ' AND Anio = 2022),"1),"
(' Sam Darnold ',5,QB,6,140,1143,52,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Sam Darnold ' AND Anio = 2022),"1),"
(' Deshaun Watson ',8,QB,6,170,1102,46,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Deshaun Watson ' AND Anio = 2022),"1),"
(' Joe Flacco ',25,QB,5,191,1051,66,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Joe Flacco ' AND Anio = 2022),"1),"
(' Cooper Rush ',9,QB,9,162,1051,46,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Cooper Rush ' AND Anio = 2022),"1),"
(' Jameis Winston ',23,QB,3,115,858,51,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Jameis Winston ' AND Anio = 2022),"1),"
(' Bailey Zappe ',22,QB,4,92,781,53,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Bailey Zappe ' AND Anio = 2022),"1),"
(' Colt McCoy ',1,QB,4,132,780,47,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Colt McCoy ' AND Anio = 2022),"1),"
(' PJ Walker ',5,QB,6,106,731,62,3,(SELECT Player_ID FROM Player_season WHERE Name = 'PJ Walker ' AND Anio = 2022),"1),"
(' Desmond Ridder ',2,QB,4,115,708,40,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Desmond Ridder ' AND Anio = 2022),"1),"
(' Teddy Bridgewater ',20,QB,5,79,683,64,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Teddy Bridgewater ' AND Anio = 2022),"1),"
(' Gardner Minshew ',26,QB,5,76,663,78,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Gardner Minshew ' AND Anio = 2022),"1),"
(' Tyler Huntley ',3,QB,6,112,658,40,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Huntley ' AND Anio = 2022),"1),"
(' Jarrett Stidham ',17,QB,5,83,656,60,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Jarrett Stidham ' AND Anio = 2022),"1),"
(' Sam Ehlinger ',14,QB,4,101,573,47,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Sam Ehlinger ' AND Anio = 2022),"1),"
(' Skylar Thompson ',20,QB,7,105,534,32,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Skylar Thompson ' AND Anio = 2022),"1),"
(' Brett Rypien ',10,QB,4,88,483,45,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Brett Rypien ' AND Anio = 2022),"1),"
(' Kyle Allen ',13,QB,2,78,416,39,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Allen ' AND Anio = 2022),"1),"
(' Trace McSorley ',1,QB,6,83,412,47,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trace McSorley ' AND Anio = 2022),"1),"
(' Joshua Dobbs ',31,QB,2,68,411,39,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Joshua Dobbs ' AND Anio = 2022),"1),"
(' David Blough ',1,QB,2,58,402,77,2,(SELECT Player_ID FROM Player_season WHERE Name = 'David Blough ' AND Anio = 2022),"1),"
(' John Wolford ',19,QB,3,62,390,30,1,(SELECT Player_ID FROM Player_season WHERE Name = 'John Wolford ' AND Anio = 2022),"1),"
(' Anthony Brown Jr. ',3,QB,2,49,302,47,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Anthony Brown Jr. ' AND Anio = 2022),"1),"
(' Malik Willis ',31,QB,8,61,276,48,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Malik Willis ' AND Anio = 2022),"1),"
(' Taysom Hill ',23,QB,16,19,240,68,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Taysom Hill ' AND Anio = 2022),"1),"
(' Nick Foles ',14,QB,3,42,224,49,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Foles ' AND Anio = 2022),"1),"
(' Nick Mullens ',21,QB,4,25,224,37,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Mullens ' AND Anio = 2022),"1),"
(' Jordan Love ',12,QB,4,21,195,63,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Love ' AND Anio = 2022),"1),"
(' Trey Lance ',28,QB,2,31,194,44,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trey Lance ' AND Anio = 2022),"1),"
(' Trevor Siemian ',6,QB,2,26,184,33,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Trevor Siemian ' AND Anio = 2022),"1),"
(' Sam Howell ',32,QB,1,19,169,52,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Sam Howell ' AND Anio = 2022),"1),"
(' Davis Webb ',24,QB,1,40,168,25,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Davis Webb ' AND Anio = 2022),"1),"
(' Bryce Perkins ',19,QB,5,34,161,20,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Bryce Perkins ' AND Anio = 2022),"1),"
(' Nathan Peterman ',6,QB,3,25,139,28,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Nathan Peterman ' AND Anio = 2022),"1),"
(' Jeff Driskel ',13,QB,7,20,108,28,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeff Driskel ' AND Anio = 2022),"1),"
(' Chris Streveler ',25,QB,2,15,90,30,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Streveler ' AND Anio = 2022),"1),"
(' Jacob Eason ',5,QB,1,5,59,49,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jacob Eason ' AND Anio = 2022),"1),"
(' Tyrod Taylor ',24,QB,3,8,58,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyrod Taylor ' AND Anio = 2022),"1),"
(' Chase Daniel ',18,QB,4,12,52,13,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Chase Daniel ' AND Anio = 2022),"1),"
(' Brian Hoyer ',22,QB,1,6,37,27,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brian Hoyer ' AND Anio = 2022),"1),"
(' C.J. Beathard ',15,QB,4,11,35,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Beathard ' AND Anio = 2022),"1),"
(' Christian McCaffrey ',5,RB,17,1,34,34,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian McCaffrey ' AND Anio = 2022),"1),"
(' Justin Jefferson ',21,WR,17,2,34,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Jefferson ' AND Anio = 2022),"1),"
(' Tim Boyle ',6,QB,1,8,33,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tim Boyle ' AND Anio = 2022),"1),"
(' Blaine Gabbert ',30,QB,1,8,29,13,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Blaine Gabbert ' AND Anio = 2022),"1),"
(' Tyler Boyd ',7,WR,16,1,23,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Boyd ' AND Anio = 2022),"1),"
(' Kyle Trask ',30,QB,1,9,23,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Trask ' AND Anio = 2022),"1),"
(' Brandon Allen ',7,QB,1,3,22,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Allen ' AND Anio = 2022),"1),"
(' Riley Dixon ',19,P,17,2,18,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Riley Dixon ' AND Anio = 2022),"1),"
(' Braden Mann ',25,P,17,2,17,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Braden Mann ' AND Anio = 2022),"1),"
(' Ryan Wright ',21,P,17,2,13,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Wright ' AND Anio = 2022),"1),"
(' Josh Johnson ',28,QB,2,2,10,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Johnson ' AND Anio = 2022),"1),"
(' Case Keenum ',4,QB,2,7,8,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Case Keenum ' AND Anio = 2022),"1),"
(' Jack Fox ',11,P,17,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jack Fox ' AND Anio = 2022),"1),"
(' Andy Lee ',1,P,17,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andy Lee ' AND Anio = 2022),"1),"
(' Mack Hollins ',17,WR,17,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mack Hollins ' AND Anio = 2022),"1),"
(' Derrick Henry ',31,RB,16,2,4,3,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Derrick Henry ' AND Anio = 2022),"1),"
(' Najee Harris ',27,RB,17,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Najee Harris ' AND Anio = 2022),"1),"
(' Braxton Berrios ',25,WR,17,1,2,2,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Braxton Berrios ' AND Anio = 2022),"1),"
(' Chase Claypool ',6,WR,15,1,1,1,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Chase Claypool ' AND Anio = 2022),"1),"
(' Chad Henne ',16,QB,3,2,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chad Henne ' AND Anio = 2022),"1),"
(' Rex Burkhead ',13,RB,16,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Rex Burkhead ' AND Anio = 2022),"1),"
(' Davante Adams ',17,WR,17,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Davante Adams ' AND Anio = 2022),"1),"
(' Phillip Dorsett ',13,WR,15,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Phillip Dorsett ' AND Anio = 2022),"1),"
(' Amari Cooper ',8,WR,17,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Amari Cooper ' AND Anio = 2022),"1),"
(' Cooper Kupp ',19,WR,9,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cooper Kupp ' AND Anio = 2022),"1),"
(' Nate Sudfeld ',11,QB,2,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nate Sudfeld ' AND Anio = 2022),"1),"
(' Leonard Fournette ',30,RB,16,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Leonard Fournette ' AND Anio = 2022),"1),"
(' Dalvin Cook ',21,RB,17,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dalvin Cook ' AND Anio = 2022),"1),"
(' Christian Kirk ',15,WR,17,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian Kirk ' AND Anio = 2022),"1),"
(' Tommy Townsend ',16,P,17,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tommy Townsend ' AND Anio = 2022),"1),"
(' James Proche II ',3,WR,15,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'James Proche II ' AND Anio = 2022),"1),"
(' Lawrence Cager ',25,TE,7,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Lawrence Cager ' AND Anio = 2022),"1),"
(' Jamie Gillan ',24,P,17,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamie Gillan ' AND Anio = 2022),"1),"
(' Cedrick Wilson Jr. ',20,WR,15,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cedrick Wilson Jr. ' AND Anio = 2022),"1),"
(' DeeJay Dallas ',29,RB,15,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DeeJay Dallas ' AND Anio = 2022),"1),"
(' Ja'Marr Chase ',7,WR,12,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ja'Marr Chase ' AND Anio = 2022),"1),"
(' Garrett Wilson ',25,WR,17,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Garrett Wilson ' AND Anio = 2022),"1),"
(' Justin Jefferson ',21,WR,17,128,1809,64,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Jefferson ' AND Anio = 2022),"3),"
(' Tyreek Hill ',20,WR,17,119,1710,64,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyreek Hill ' AND Anio = 2022),"3),"
(' Davante Adams ',17,WR,17,100,1516,60,14,(SELECT Player_ID FROM Player_season WHERE Name = 'Davante Adams ' AND Anio = 2022),"3),"
(' A.J. Brown ',26,WR,17,88,1496,78,11,(SELECT Player_ID FROM Player_season WHERE Name = 'A.J. Brown ' AND Anio = 2022),"3),"
(' Stefon Diggs ',4,WR,16,108,1429,53,11,(SELECT Player_ID FROM Player_season WHERE Name = 'Stefon Diggs ' AND Anio = 2022),"3),"
(' CeeDee Lamb ',9,WR,17,107,1359,39,9,(SELECT Player_ID FROM Player_season WHERE Name = 'CeeDee Lamb ' AND Anio = 2022),"3),"
(' Jaylen Waddle ',20,WR,17,75,1356,84,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaylen Waddle ' AND Anio = 2022),"3),"
(' Travis Kelce ',16,TE,17,110,1338,52,12,(SELECT Player_ID FROM Player_season WHERE Name = 'Travis Kelce ' AND Anio = 2022),"3),"
(' DeVonta Smith ',26,WR,17,95,1196,45,7,(SELECT Player_ID FROM Player_season WHERE Name = 'DeVonta Smith ' AND Anio = 2022),"3),"
(' Terry McLaurin ',32,WR,17,77,1191,52,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Terry McLaurin ' AND Anio = 2022),"3),"
(' Amon-Ra St. Brown',11,WR,16,106,1161,49,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Amon-Ra St. Brown' AND Anio = 2022),"3),"
(' Amari Cooper ',8,WR,17,78,1160,55,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Amari Cooper ' AND Anio = 2022),"3),"
(' Mike Evans ',30,WR,15,77,1124,63,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Evans ' AND Anio = 2022),"3),"
(' Christian Kirk ',15,WR,17,84,1108,49,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian Kirk ' AND Anio = 2022),"3),"
(' Garrett Wilson ',25,WR,17,83,1103,60,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Garrett Wilson ' AND Anio = 2022),"3),"
(' DK Metcalf ',29,WR,17,90,1048,54,6,(SELECT Player_ID FROM Player_season WHERE Name = 'DK Metcalf ' AND Anio = 2022),"3),"
(' Ja'Marr Chase ',7,WR,12,87,1046,60,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Ja'Marr Chase ' AND Anio = 2022),"3),"
(' Chris Olave ',23,WR,15,72,1042,53,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Olave ' AND Anio = 2022),"3),"
(' Tyler Lockett ',29,WR,16,84,1033,40,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Lockett ' AND Anio = 2022),"3),"
(' Tee Higgins ',7,WR,16,74,1029,59,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Tee Higgins ' AND Anio = 2022),"3),"
(' Chris Godwin ',30,WR,15,104,1023,44,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Godwin ' AND Anio = 2022),"3),"
(' Brandon Aiyuk ',28,WR,17,78,1015,54,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Aiyuk ' AND Anio = 2022),"3),"
(' Jerry Jeudy ',10,WR,15,67,972,67,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Jerry Jeudy ' AND Anio = 2022),"3),"
(' JuJu Smith-Schuster ',16,WR,16,78,933,53,3,(SELECT Player_ID FROM Player_season WHERE Name = 'JuJu Smith-Schuster ' AND Anio = 2022),"3),"
(' Michael Pittman Jr.',14,WR,16,99,925,28,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Pittman Jr.' AND Anio = 2022),"3),"
(' T.J. Hockenson ',11,TE,17,86,914,81,6,(SELECT Player_ID FROM Player_season WHERE Name = 'T.J. Hockenson ' AND Anio = 2022),"3),"
(' Mike Williams ',18,WR,13,63,895,55,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Williams ' AND Anio = 2022),"3),"
(' DJ Moore ',5,WR,17,63,888,62,7,(SELECT Player_ID FROM Player_season WHERE Name = 'DJ Moore ' AND Anio = 2022),"3),"
(' Diontae Johnson ',27,WR,17,86,882,37,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Diontae Johnson ' AND Anio = 2022),"3),"
(' Drake London ',2,WR,17,72,866,40,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Drake London ' AND Anio = 2022),"3),"
(' Mark Andrews ',3,TE,15,73,847,36,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Mark Andrews ' AND Anio = 2022),"3),"
(' Donovan Peoples-Jones ',8,WR,17,61,839,42,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Donovan Peoples-Jones ' AND Anio = 2022),"3),"
(' Gabe Davis ',4,WR,15,48,836,98,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Gabe Davis ' AND Anio = 2022),"3),"
(' Courtland Sutton ',10,WR,15,64,829,51,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Courtland Sutton ' AND Anio = 2022),"3),"
(' Zay Jones ',15,WR,16,82,823,59,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Zay Jones ' AND Anio = 2022),"3),"
(' Cooper Kupp ',19,WR,9,75,812,75,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Cooper Kupp ' AND Anio = 2022),"3),"
(' Jakobi Meyers ',22,WR,14,67,804,48,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Jakobi Meyers ' AND Anio = 2022),"3),"
(' George Pickens ',27,WR,17,52,801,42,4,(SELECT Player_ID FROM Player_season WHERE Name = 'George Pickens ' AND Anio = 2022),"3),"
(' Allen Lazard ',12,WR,15,60,788,47,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Allen Lazard ' AND Anio = 2022),"3),"
(' Joshua Palmer ',18,WR,16,72,769,50,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Joshua Palmer ' AND Anio = 2022),"3),"
(' Evan Engram ',15,TE,17,73,766,36,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Evan Engram ' AND Anio = 2022),"3),"
(' George Kittle ',28,TE,15,60,765,54,11,(SELECT Player_ID FROM Player_season WHERE Name = 'George Kittle ' AND Anio = 2022),"3),"
(' Tyler Boyd ',7,WR,16,58,762,60,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Boyd ' AND Anio = 2022),"3),"
(' Keenan Allen ',18,WR,10,66,752,46,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Keenan Allen ' AND Anio = 2022),"3),"
(' Christian McCaffrey ',5,RB,17,85,741,49,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian McCaffrey ' AND Anio = 2022),"3),"
(' Pat Freiermuth ',27,TE,16,63,732,57,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Pat Freiermuth ' AND Anio = 2022),"3),"
(' Darius Slayton ',24,WR,16,46,724,55,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Darius Slayton ' AND Anio = 2022),"3),"
(' Austin Ekeler ',18,RB,17,107,722,23,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Austin Ekeler ' AND Anio = 2022),"3),"
(' DeAndre Hopkins ',1,WR,9,64,717,33,3,(SELECT Player_ID FROM Player_season WHERE Name = 'DeAndre Hopkins ' AND Anio = 2022),"3),"
(' Adam Thielen ',21,WR,17,70,716,36,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Adam Thielen ' AND Anio = 2022),"3),"
(' Marquise Brown ',1,WR,12,67,709,47,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Marquise Brown ' AND Anio = 2022),"3),"
(' Dallas Goedert ',26,TE,12,55,702,31,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Dallas Goedert ' AND Anio = 2022),"3),"
(' Brandin Cooks ',13,WR,13,57,699,44,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandin Cooks ' AND Anio = 2022),"3),"
(' Mack Hollins ',17,WR,17,57,690,60,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Mack Hollins ' AND Anio = 2022),"3),"
(' Marquez Valdes-Scantling ',16,WR,17,42,687,57,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Marquez Valdes-Scantling ' AND Anio = 2022),"3),"
(' Curtis Samuel ',32,WR,17,64,656,49,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Curtis Samuel ' AND Anio = 2022),"3),"
(' K.J. Osborn ',21,WR,17,60,650,66,5,(SELECT Player_ID FROM Player_season WHERE Name = 'K.J. Osborn ' AND Anio = 2022),"3),"
(' Deebo Samuel ',28,WR,13,56,632,57,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Deebo Samuel ' AND Anio = 2022),"3),"
(' David Njoku ',8,TE,14,58,628,38,4,(SELECT Player_ID FROM Player_season WHERE Name = 'David Njoku ' AND Anio = 2022),"3),"
(' Parris Campbell ',14,WR,17,63,623,49,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Parris Campbell ' AND Anio = 2022),"3),"
(' Tyler Higbee ',19,TE,17,72,620,26,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Higbee ' AND Anio = 2022),"3),"
(' Kalif Raymond ',11,WR,17,47,616,56,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kalif Raymond ' AND Anio = 2022),"3),"
(' Christian Watson ',12,WR,14,41,611,63,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian Watson ' AND Anio = 2022),"3),"
(' Alec Pierce ',14,WR,16,41,593,47,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Alec Pierce ' AND Anio = 2022),"3),"
(' Dalton Schultz ',9,TE,15,57,577,30,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Dalton Schultz ' AND Anio = 2022),"3),"
(' Richie James ',24,WR,17,57,569,33,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Richie James ' AND Anio = 2022),"3),"
(' Noah Brown ',9,WR,16,43,555,51,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Noah Brown ' AND Anio = 2022),"3),"
(' Gerald Everett ',18,TE,16,58,555,26,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Gerald Everett ' AND Anio = 2022),"3),"
(' Tyler Conklin ',25,TE,17,58,552,30,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Conklin ' AND Anio = 2022),"3),"
(' Chris Moore ',13,WR,16,48,548,52,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Moore ' AND Anio = 2022),"3),"
(' Cole Kmet ',6,TE,17,50,544,50,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Cole Kmet ' AND Anio = 2022),"3),"
(' DeVante Parker ',22,WR,13,31,539,43,3,(SELECT Player_ID FROM Player_season WHERE Name = 'DeVante Parker ' AND Anio = 2022),"3),"
(' DeAndre Carter ',18,WR,17,46,538,35,3,(SELECT Player_ID FROM Player_season WHERE Name = 'DeAndre Carter ' AND Anio = 2022),"3),"
(' Corey Davis ',25,WR,13,32,536,66,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Corey Davis ' AND Anio = 2022),"3),"
(' Olamide Zaccheaus ',2,WR,17,40,533,45,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Olamide Zaccheaus ' AND Anio = 2022),"3),"
(' Marvin Jones Jr.',15,WR,16,46,529,37,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Marvin Jones Jr.' AND Anio = 2022),"3),"
(' Robert Woods ',31,WR,17,53,527,41,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Robert Woods ' AND Anio = 2022),"3),"
(' Leonard Fournette ',30,RB,16,73,523,44,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Leonard Fournette ' AND Anio = 2022),"3),"
(' Jahan Dotson ',32,WR,12,35,523,61,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Jahan Dotson ' AND Anio = 2022),"3),"
(' Dawson Knox ',4,TE,15,48,517,45,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Dawson Knox ' AND Anio = 2022),"3),"
(' Jerick McKinnon ',16,RB,17,56,512,56,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Jerick McKinnon ' AND Anio = 2022),"3),"
(' Hunter Henry ',22,TE,17,41,509,39,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Hunter Henry ' AND Anio = 2022),"3),"
(' Juwan Johnson ',23,TE,16,42,508,41,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Juwan Johnson ' AND Anio = 2022),"3),"
(' DJ Chark Jr.',11,WR,11,30,502,51,3,(SELECT Player_ID FROM Player_season WHERE Name = 'DJ Chark Jr.' AND Anio = 2022),"3),"
(' Jordan Akins ',13,TE,15,37,495,46,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Akins ' AND Anio = 2022),"3),"
(' Darnell Mooney ',6,WR,12,40,493,56,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Darnell Mooney ' AND Anio = 2022),"3),"
(' Alvin Kamara ',23,RB,15,57,490,54,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Alvin Kamara ' AND Anio = 2022),"3),"
(' Terrace Marshall Jr.',5,WR,14,28,490,43,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Terrace Marshall Jr.' AND Anio = 2022),"3),"
(' Rashid Shaheed ',23,WR,12,28,488,68,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Rashid Shaheed ' AND Anio = 2022),"3),"
(' Noah Fant ',29,TE,17,50,486,51,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Noah Fant ' AND Anio = 2022),"3),"
(' Nico Collins ',13,WR,10,37,481,58,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Nico Collins ' AND Anio = 2022),"3),"
(' Josh Reynolds ',11,WR,14,38,479,31,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Reynolds ' AND Anio = 2022),"3),"
(' Robert Tonyan ',12,TE,17,53,470,24,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Robert Tonyan ' AND Anio = 2022),"3),"
(' Greg Dortch ',1,WR,16,52,467,47,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Greg Dortch ' AND Anio = 2022),"3),"
(' Demarcus Robinson ',3,WR,17,48,458,31,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Demarcus Robinson ' AND Anio = 2022),"3),"
(' Chase Claypool ',6,WR,15,46,451,31,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Chase Claypool ' AND Anio = 2022),"3),"
(' Chigoziem Okonkwo ',31,TE,17,32,450,48,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Chigoziem Okonkwo ' AND Anio = 2022),"3),"
(' Elijah Moore ',25,WR,16,37,446,42,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Elijah Moore ' AND Anio = 2022),"3),"
(' Austin Hooper ',31,TE,17,41,444,24,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Austin Hooper ' AND Anio = 2022),"3),"
(' Treylon Burks ',31,WR,11,33,444,51,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Treylon Burks ' AND Anio = 2022),"3),"
(' Joe Mixon ',7,RB,14,60,441,35,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Joe Mixon ' AND Anio = 2022),"3),"
(' Kendrick Bourne ',22,WR,16,35,434,41,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kendrick Bourne ' AND Anio = 2022),"3),"
(' Russell Gage ',30,WR,13,51,426,23,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Russell Gage ' AND Anio = 2022),"3),"
(' Romeo Doubs ',12,WR,13,42,425,26,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Romeo Doubs ' AND Anio = 2022),"3),"
(' Michael Gallup ',9,WR,14,39,424,27,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Gallup ' AND Anio = 2022),"3),"
(' Isaiah McKenzie ',4,WR,15,42,423,30,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Isaiah McKenzie ' AND Anio = 2022),"3),"
(' Rhamondre Stevenson ',22,RB,17,69,421,40,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Rhamondre Stevenson ' AND Anio = 2022),"3),"
(' Foster Moreau ',17,TE,15,33,420,33,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Foster Moreau ' AND Anio = 2022),"3),"
(' Randall Cobb ',12,WR,13,34,417,40,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Randall Cobb ' AND Anio = 2022),"3),"
(' Trent Sherfield Sr.',20,WR,17,30,417,75,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Trent Sherfield Sr.' AND Anio = 2022),"3),"
(' Jauan Jennings ',28,WR,16,35,416,44,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jauan Jennings ' AND Anio = 2022),"3),"
(' Hayden Hurst ',7,TE,13,52,414,29,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Hayden Hurst ' AND Anio = 2022),"3),"
(' Rondale Moore ',1,WR,8,41,414,38,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Rondale Moore ' AND Anio = 2022),"3),"
(' Greg Dulcich ',10,TE,10,33,411,39,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Greg Dulcich ' AND Anio = 2022),"3),"
(' Devin Duvernay ',3,WR,14,37,407,31,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Devin Duvernay ' AND Anio = 2022),"3),"
(' Zach Ertz ',1,TE,10,47,406,32,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Ertz ' AND Anio = 2022),"3),"
(' Josh Jacobs ',17,RB,17,53,400,43,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Jacobs ' AND Anio = 2022),"3),"
(' Derrick Henry ',31,RB,16,33,398,69,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Derrick Henry ' AND Anio = 2022),"3),"
(' Nick Westbrook-Ikhine ',31,WR,17,25,397,63,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Westbrook-Ikhine ' AND Anio = 2022),"3),"
(' Aaron Jones ',12,RB,17,59,395,30,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Aaron Jones ' AND Anio = 2022),"3),"
(' Isaiah Hodgins ',24,WR,10,37,392,29,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Isaiah Hodgins ' AND Anio = 2022),"3),"
(' Cade Otton ',30,TE,16,42,391,35,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Cade Otton ' AND Anio = 2022),"3),"
(' D'Andre Swift ',11,RB,14,48,389,25,3,(SELECT Player_ID FROM Player_season WHERE Name = 'D'Andre Swift ' AND Anio = 2022),"3),"
(' Darren Waller ',17,TE,9,28,388,34,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Darren Waller ' AND Anio = 2022),"3),"
(' Marquise Goodwin ',29,WR,13,27,387,38,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Marquise Goodwin ' AND Anio = 2022),"3),"
(' Ben Skowronek ',19,WR,14,39,376,32,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ben Skowronek ' AND Anio = 2022),"3),"
(' Isaiah Likely ',3,TE,16,36,373,34,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Isaiah Likely ' AND Anio = 2022),"3),"
(' Tony Pollard ',9,RB,16,39,371,68,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Tony Pollard ' AND Anio = 2022),"3),"
(' Van Jefferson ',19,WR,11,24,369,39,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Van Jefferson ' AND Anio = 2022),"3),"
(' Nelson Agholor ',22,WR,16,31,362,44,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Nelson Agholor ' AND Anio = 2022),"3),"
(' Mike Gesicki ',20,TE,17,32,362,32,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Gesicki ' AND Anio = 2022),"3),"
(' Kyle Pitts ',2,TE,10,28,356,33,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Pitts ' AND Anio = 2022),"3),"
(' Quez Watkins ',26,WR,17,33,354,53,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Quez Watkins ' AND Anio = 2022),"3),"
(' Antonio Gibson ',32,RB,15,46,353,26,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Antonio Gibson ' AND Anio = 2022),"3),"
(' Will Dissly ',29,TE,15,34,349,38,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Will Dissly ' AND Anio = 2022),"3),"
(' Allen Robinson II',19,WR,10,33,339,29,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Allen Robinson II' AND Anio = 2022),"3),"
(' Saquon Barkley ',24,RB,16,57,338,41,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Saquon Barkley ' AND Anio = 2022),"3),"
(' Hunter Renfrow ',17,WR,10,36,330,27,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Hunter Renfrow ' AND Anio = 2022),"3),"
(' Sammy Watkins ',12,WR,12,16,325,55,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Sammy Watkins ' AND Anio = 2022),"3),"
(' Logan Thomas ',32,TE,14,39,323,27,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Logan Thomas ' AND Anio = 2022),"3),"
(' Equanimeous St. Brown',6,WR,16,21,323,56,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Equanimeous St. Brown' AND Anio = 2022),"3),"
(' Colby Parkinson ',29,TE,17,25,322,39,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Colby Parkinson ' AND Anio = 2022),"3),"
(' David Montgomery ',6,RB,16,34,316,32,1,(SELECT Player_ID FROM Player_season WHERE Name = 'David Montgomery ' AND Anio = 2022),"3),"
(' Travis Etienne Jr.',15,RB,17,35,316,30,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Travis Etienne Jr.' AND Anio = 2022),"3),"
(' Justin Watson ',16,WR,17,15,315,67,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Watson ' AND Anio = 2022),"3),"
(' Jelani Woods ',14,TE,15,25,312,36,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Jelani Woods ' AND Anio = 2022),"3),"
(' Kendall Hinton ',10,WR,12,24,311,35,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kendall Hinton ' AND Anio = 2022),"3),"
(' Kylen Granson ',14,TE,13,31,302,32,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kylen Granson ' AND Anio = 2022),"3),"
(' James Conner ',1,RB,13,46,300,22,1,(SELECT Player_ID FROM Player_season WHERE Name = 'James Conner ' AND Anio = 2022),"3),"
(' Julio Jones ',30,WR,10,24,299,48,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Julio Jones ' AND Anio = 2022),"3),"
(' Noah Gray ',16,TE,17,28,299,27,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Noah Gray ' AND Anio = 2022),"3),"
(' Tutu Atwell ',19,WR,13,18,298,62,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tutu Atwell ' AND Anio = 2022),"3),"
(' Mecole Hardman ',16,WR,8,25,297,36,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Mecole Hardman ' AND Anio = 2022),"3),"
(' Shi Smith ',5,WR,17,22,296,38,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Shi Smith ' AND Anio = 2022),"3),"
(' Dalvin Cook ',21,RB,17,39,295,64,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Dalvin Cook ' AND Anio = 2022),"3),"
(' Rachaad White ',30,RB,17,50,290,20,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Rachaad White ' AND Anio = 2022),"3),"
(' Michael Carter ',25,RB,16,41,288,37,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Carter ' AND Anio = 2022),"3),"
(' Samaje Perine ',7,RB,16,38,287,32,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Samaje Perine ' AND Anio = 2022),"3),"
(' Rashod Bateman ',3,WR,7,15,285,75,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Rashod Bateman ' AND Anio = 2022),"3),"
(' Robbie Chosen ',5,WR,16,20,282,75,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Robbie Chosen ' AND Anio = 2022),"3),"
(' Devin Singletary ',4,RB,16,38,280,22,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Devin Singletary ' AND Anio = 2022),"3),"
(' Tre'Quan Smith ',23,WR,15,19,278,48,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tre'Quan Smith ' AND Anio = 2022),"3),"
(' Jarvis Landry ',23,WR,9,25,272,40,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jarvis Landry ' AND Anio = 2022),"3),"
(' Laviska Shenault Jr.',5,WR,13,27,272,67,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Laviska Shenault Jr.' AND Anio = 2022),"3),"
(' Damiere Byrd ',2,WR,14,13,268,75,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Damiere Byrd ' AND Anio = 2022),"3),"
(' Daniel Bellinger ',24,TE,12,30,268,24,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Daniel Bellinger ' AND Anio = 2022),"3),"
(' Trey McBride ',1,TE,16,29,265,29,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Trey McBride ' AND Anio = 2022),"3),"
(' Phillip Dorsett ',13,WR,15,20,257,34,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Phillip Dorsett ' AND Anio = 2022),"3),"
(' Skyy Moore ',16,WR,16,22,250,30,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Skyy Moore ' AND Anio = 2022),"3),"
(' Tyquan Thornton ',22,WR,13,22,247,29,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyquan Thornton ' AND Anio = 2022),"3),"
(' Jonnu Smith ',22,TE,14,27,245,53,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonnu Smith ' AND Anio = 2022),"3),"
(' Dante Pettis ',6,WR,17,19,245,51,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Dante Pettis ' AND Anio = 2022),"3),"
(' Ray-Ray McCloud III',28,WR,17,14,243,42,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ray-Ray McCloud III' AND Anio = 2022),"3),"
(' Nyheim Hines ',4,RB,16,30,241,22,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Nyheim Hines ' AND Anio = 2022),"3),"
(' Nick Chubb ',8,RB,17,27,239,26,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Chubb ' AND Anio = 2022),"3),"
(' Harrison Bryant ',8,TE,17,31,239,30,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Harrison Bryant ' AND Anio = 2022),"3),"
(' A.J. Green ',1,WR,15,24,236,77,2,(SELECT Player_ID FROM Player_season WHERE Name = 'A.J. Green ' AND Anio = 2022),"3),"
(' C.J. Uzomah ',25,TE,15,21,232,40,2,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Uzomah ' AND Anio = 2022),"3),"
(' Trenton Irwin ',7,WR,9,15,231,45,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Trenton Irwin ' AND Anio = 2022),"3),"
(' Najee Harris ',27,RB,17,41,229,19,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Najee Harris ' AND Anio = 2022),"3),"
(' Wan'Dale Robinson ',24,WR,6,23,227,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Wan'Dale Robinson ' AND Anio = 2022),"3),"
(' Melvin Gordon III',10,RB,10,25,223,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Melvin Gordon III' AND Anio = 2022),"3),"
(' Breece Hall ',25,RB,7,19,218,79,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Breece Hall ' AND Anio = 2022),"3),"
(' Brock Wright ',11,TE,17,18,216,51,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Brock Wright ' AND Anio = 2022),"3),"
(' Jaylen Warren ',27,RB,16,28,214,26,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaylen Warren ' AND Anio = 2022),"3),"
(' David Bell ',8,WR,16,24,214,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'David Bell ' AND Anio = 2022),"3),"
(' Ameer Abdullah ',17,RB,17,25,211,23,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ameer Abdullah ' AND Anio = 2022),"3),"
(' Kareem Hunt ',8,RB,17,35,210,24,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kareem Hunt ' AND Anio = 2022),"3),"
(' Deon Jackson ',14,RB,16,30,209,27,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Deon Jackson ' AND Anio = 2022),"3),"
(' Adam Trautman ',23,TE,15,18,207,22,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Adam Trautman ' AND Anio = 2022),"3),"
(' Ashton Dulin ',14,WR,12,15,207,39,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ashton Dulin ' AND Anio = 2022),"3),"
(' AJ Dillon ',12,RB,17,28,206,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'AJ Dillon ' AND Anio = 2022),"3),"
(' Rex Burkhead ',13,RB,16,37,204,17,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Rex Burkhead ' AND Anio = 2022),"3),"
(' Amari Rodgers ',12,WR,16,16,204,37,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Amari Rodgers ' AND Anio = 2022),"3),"
(' Raheem Mostert ',20,RB,16,31,202,25,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Raheem Mostert ' AND Anio = 2022),"3),"
(' KhaDarel Hodge ',2,WR,17,13,202,39,1,(SELECT Player_ID FROM Player_season WHERE Name = 'KhaDarel Hodge ' AND Anio = 2022),"3),"
(' Kyle Juszczyk ',28,FB,16,19,200,35,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Juszczyk ' AND Anio = 2022),"3),"
(' Ian Thomas ',5,TE,17,21,197,50,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ian Thomas ' AND Anio = 2022),"3),"
(' Eno Benjamin ',23,RB,15,25,193,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Eno Benjamin ' AND Anio = 2022),"3),"
(' Mo Alie-Cox ',14,TE,17,19,189,34,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Mo Alie-Cox ' AND Anio = 2022),"3),"
(' Jamal Agnew ',15,WR,15,23,187,24,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamal Agnew ' AND Anio = 2022),"3),"
(' Denzel Mims ',25,WR,10,11,186,63,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Denzel Mims ' AND Anio = 2022),"3),"
(' Jeff Wilson Jr.',20,RB,16,22,185,16,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeff Wilson Jr.' AND Anio = 2022),"3),"
(' Scotty Miller ',30,WR,15,23,185,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Scotty Miller ' AND Anio = 2022),"3),"
(' Irv Smith Jr.',21,TE,8,25,182,17,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Irv Smith Jr.' AND Anio = 2022),"3),"
(' James Cook ',4,RB,16,21,180,41,1,(SELECT Player_ID FROM Player_season WHERE Name = 'James Cook ' AND Anio = 2022),"3),"
(' Jalen Nailor ',21,WR,15,9,179,47,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Nailor ' AND Anio = 2022),"3),"
(' Dontrell Hilliard ',31,RB,12,21,177,31,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Dontrell Hilliard ' AND Anio = 2022),"3),"
(' Cameron Brate ',30,TE,11,20,174,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cameron Brate ' AND Anio = 2022),"3),"
(' Jake Ferguson ',9,TE,16,19,174,30,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jake Ferguson ' AND Anio = 2022),"3),"
(' Tommy Tremble ',5,TE,17,19,174,29,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Tommy Tremble ' AND Anio = 2022),"3),"
(' J.D. McKissic ',32,RB,8,27,173,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'J.D. McKissic ' AND Anio = 2022),"3),"
(' Michael Thomas ',23,WR,3,16,171,21,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Thomas ' AND Anio = 2022),"3),"
(' Kadarius Toney ',24,WR,9,16,171,38,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Kadarius Toney ' AND Anio = 2022),"3),"
(' Chuba Hubbard ',5,RB,15,14,171,45,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chuba Hubbard ' AND Anio = 2022),"3),"
(' Kenneth Gainwell ',26,RB,17,23,169,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenneth Gainwell ' AND Anio = 2022),"3),"
(' KJ Hamler ',10,WR,7,7,165,55,0,(SELECT Player_ID FROM Player_season WHERE Name = 'KJ Hamler ' AND Anio = 2022),"3),"
(' Dameon Pierce ',13,RB,13,30,165,16,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Dameon Pierce ' AND Anio = 2022),"3),"
(' Kenneth Walker III',29,RB,15,27,165,33,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenneth Walker III' AND Anio = 2022),"3),"
(' Khalil Shakir ',4,WR,14,10,161,31,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Khalil Shakir ' AND Anio = 2022),"3),"
(' Marquez Callaway ',23,WR,14,16,158,33,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Marquez Callaway ' AND Anio = 2022),"3),"
(' Chase Edmonds ',10,RB,13,16,157,27,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Chase Edmonds ' AND Anio = 2022),"3),"
(' Travis Homer ',29,RB,10,16,157,27,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Travis Homer ' AND Anio = 2022),"3),"
(' Brandon Powell ',19,WR,17,24,156,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Powell ' AND Anio = 2022),"3),"
(' Sterling Shepard ',24,WR,3,13,154,65,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Sterling Shepard ' AND Anio = 2022),"3),"
(' DeSean Jackson ',3,WR,7,9,153,62,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DeSean Jackson ' AND Anio = 2022),"3),"
(' Connor Heyward ',27,TE,17,12,151,45,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Connor Heyward ' AND Anio = 2022),"3),"
(' Clyde Edwards-Helaire ',16,RB,10,17,151,25,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Clyde Edwards-Helaire ' AND Anio = 2022),"3),"
(' MyCole Pruitt ',2,TE,13,16,150,29,4,(SELECT Player_ID FROM Player_season WHERE Name = 'MyCole Pruitt ' AND Anio = 2022),"3),"
(' Zach Pascal ',26,WR,17,15,150,34,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Pascal ' AND Anio = 2022),"3),"
(' Josh Oliver ',3,TE,17,14,149,40,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Oliver ' AND Anio = 2022),"3),"
(' Eric Saubert ',10,TE,17,15,148,25,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Eric Saubert ' AND Anio = 2022),"3),"
(' O.J. Howard ',13,TE,13,10,145,26,2,(SELECT Player_ID FROM Player_season WHERE Name = 'O.J. Howard ' AND Anio = 2022),"3),"
(' Braxton Berrios ',25,WR,17,18,145,25,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Braxton Berrios ' AND Anio = 2022),"3),"
(' Jonathan Taylor ',14,RB,11,28,143,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonathan Taylor ' AND Anio = 2022),"3),"
(' Dyami Brown ',32,WR,15,5,143,75,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Dyami Brown ' AND Anio = 2022),"3),"
(' Keelan Cole Sr.',17,WR,14,10,141,30,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Keelan Cole Sr.' AND Anio = 2022),"3),"
(' Tom Kennedy ',11,WR,7,8,141,44,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tom Kennedy ' AND Anio = 2022),"3),"
(' Johnny Mundt ',21,TE,17,19,140,17,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Johnny Mundt ' AND Anio = 2022),"3),"
(' Mitchell Wilcox ',7,TE,16,17,139,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Mitchell Wilcox ' AND Anio = 2022),"3),"
(' Tyler Allgeier ',2,RB,16,16,139,26,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Allgeier ' AND Anio = 2022),"3),"
(' Cedrick Wilson Jr.',20,WR,15,12,136,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cedrick Wilson Jr.' AND Anio = 2022),"3),"
(' Byron Pringle ',6,WR,11,10,135,35,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Byron Pringle ' AND Anio = 2022),"3),"
(' Dan Arnold ',15,TE,17,9,135,26,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dan Arnold ' AND Anio = 2022),"3),"
(' Jeff Smith ',25,WR,11,8,134,50,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeff Smith ' AND Anio = 2022),"3),"
(' Latavius Murray ',10,RB,13,27,132,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Latavius Murray ' AND Anio = 2022),"3),"
(' Tanner Hudson ',24,TE,11,10,132,27,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tanner Hudson ' AND Anio = 2022),"3),"
(' Zach Gentry ',27,TE,17,19,132,32,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Gentry ' AND Anio = 2022),"3),"
(' Donald Parham Jr.',18,TE,6,10,130,24,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Donald Parham Jr.' AND Anio = 2022),"3),"
(' Isiah Pacheco ',16,RB,17,13,130,32,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Isiah Pacheco ' AND Anio = 2022),"3),"
(' Durham Smythe ',20,TE,16,15,129,26,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Durham Smythe ' AND Anio = 2022),"3),"
(' Brevin Jordan ',13,TE,11,14,128,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brevin Jordan ' AND Anio = 2022),"3),"
(' JaMycal Hasty ',15,RB,17,20,126,28,1,(SELECT Player_ID FROM Player_season WHERE Name = 'JaMycal Hasty ' AND Anio = 2022),"3),"
(' DeeJay Dallas ',29,RB,15,17,126,41,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DeeJay Dallas ' AND Anio = 2022),"3),"
(' Jack Stoll ',26,TE,17,11,123,26,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jack Stoll ' AND Anio = 2022),"3),"
(' Cordarrelle Patterson ',2,RB,13,21,122,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cordarrelle Patterson ' AND Anio = 2022),"3),"
(' T.Y. Hilton ',9,WR,3,7,121,52,0,(SELECT Player_ID FROM Player_season WHERE Name = 'T.Y. Hilton ' AND Anio = 2022),"3),"
(' Matt Breida ',24,RB,17,20,118,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Breida ' AND Anio = 2022),"3),"
(' Lawrence Cager ',25,TE,7,13,118,20,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Lawrence Cager ' AND Anio = 2022),"3),"
(' Pharaoh Brown ',8,TE,16,12,117,30,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Pharaoh Brown ' AND Anio = 2022),"3),"
(' Cam Akers ',19,RB,15,13,117,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cam Akers ' AND Anio = 2022),"3),"
(' N'Keal Harry ',6,WR,7,7,116,49,1,(SELECT Player_ID FROM Player_season WHERE Name = 'N'Keal Harry ' AND Anio = 2022),"3),"
(' Craig Reynolds ',11,RB,9,9,116,36,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Craig Reynolds ' AND Anio = 2022),"3),"
(' Josiah Deguara ',12,TE,17,13,114,25,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Josiah Deguara ' AND Anio = 2022),"3),"
(' James Mitchell ',11,TE,14,11,113,22,1,(SELECT Player_ID FROM Player_season WHERE Name = 'James Mitchell ' AND Anio = 2022),"3),"
(' Teagan Quitoriano ',13,TE,9,7,113,52,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Teagan Quitoriano ' AND Anio = 2022),"3),"
(' Breshad Perriman ',30,WR,11,9,110,28,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Breshad Perriman ' AND Anio = 2022),"3),"
(' Brycen Hopkins ',19,TE,14,7,109,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brycen Hopkins ' AND Anio = 2022),"3),"
(' John Bates ',32,TE,16,14,108,20,1,(SELECT Player_ID FROM Player_season WHERE Name = 'John Bates ' AND Anio = 2022),"3),"
(' Jody Fortson Jr.',16,TE,13,9,108,40,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jody Fortson Jr.' AND Anio = 2022),"3),"
(' Velus Jones Jr.',6,WR,12,7,107,44,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Velus Jones Jr.' AND Anio = 2022),"3),"
(' David Sills V',24,WR,9,11,106,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'David Sills V' AND Anio = 2022),"3),"
(' Ross Dwelley ',28,TE,12,3,105,56,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ross Dwelley ' AND Anio = 2022),"3),"
(' Alec Ingold ',20,FB,17,15,105,17,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Alec Ingold ' AND Anio = 2022),"3),"
(' Dare Ogunbowale ',13,RB,17,20,104,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dare Ogunbowale ' AND Anio = 2022),"3),"
(' Steven Sims ',27,WR,12,14,104,28,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Steven Sims ' AND Anio = 2022),"3),"
(' Jalen Reagor ',21,WR,17,8,104,38,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Reagor ' AND Anio = 2022),"3),"
(' Peyton Hendershot ',9,TE,17,11,103,29,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Peyton Hendershot ' AND Anio = 2022),"3),"
(' River Cracraft ',20,WR,11,9,102,22,2,(SELECT Player_ID FROM Player_season WHERE Name = 'River Cracraft ' AND Anio = 2022),"3),"
(' Darrell Henderson Jr.',19,RB,10,17,102,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Darrell Henderson Jr.' AND Anio = 2022),"3),"
(' Justin Jackson ',11,RB,16,12,101,15,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Jackson ' AND Anio = 2022),"3),"
(' Joshua Kelley ',18,RB,13,14,101,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Joshua Kelley ' AND Anio = 2022),"3),"
(' Anthony Firkser ',2,TE,11,9,100,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Anthony Firkser ' AND Anio = 2022),"3),"
(' Giovanni Ricci ',5,FB,15,8,100,32,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Giovanni Ricci ' AND Anio = 2022),"3),"
(' Zonovan Knight ',25,RB,7,13,100,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Zonovan Knight ' AND Anio = 2022),"3),"
(' Marcus Johnson ',24,WR,14,9,99,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marcus Johnson ' AND Anio = 2022),"3),"
(' Marlon Mack ',10,RB,8,8,99,66,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Marlon Mack ' AND Anio = 2022),"3),"
(' Damien Harris ',22,RB,11,17,97,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Damien Harris ' AND Anio = 2022),"3),"
(' Mike Boone ',10,RB,9,9,96,34,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Boone ' AND Anio = 2022),"3),"
(' Albert Okwuegbunam Jr.',10,TE,8,10,95,25,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Albert Okwuegbunam Jr.' AND Anio = 2022),"3),"
(' Raheem Blackshear ',5,RB,13,10,93,27,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Raheem Blackshear ' AND Anio = 2022),"3),"
(' Ezekiel Elliott ',9,RB,15,17,92,31,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ezekiel Elliott ' AND Anio = 2022),"3),"
(' Alexander Mattison ',21,RB,17,15,91,16,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Alexander Mattison ' AND Anio = 2022),"3),"
(' Kenyan Drake ',3,RB,12,17,89,15,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenyan Drake ' AND Anio = 2022),"3),"
(' Cam Sims ',32,WR,17,8,89,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cam Sims ' AND Anio = 2022),"3),"
(' Parker Hesse ',2,TE,17,9,89,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Parker Hesse ' AND Anio = 2022),"3),"
(' Michael Bandy ',18,WR,10,10,89,25,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Bandy ' AND Anio = 2022),"3),"
(' Ty Johnson ',25,RB,17,12,88,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ty Johnson ' AND Anio = 2022),"3),"
(' C.J. Ham ',21,FB,17,10,86,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Ham ' AND Anio = 2022),"3),"
(' Quintin Morris ',4,TE,14,8,84,26,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Quintin Morris ' AND Anio = 2022),"3),"
(' Samori Toure ',12,WR,11,5,82,37,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Samori Toure ' AND Anio = 2022),"3),"
(' Kenny Golladay ',24,WR,12,6,81,25,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenny Golladay ' AND Anio = 2022),"3),"
(' Grant Calcaterra ',26,TE,15,5,81,40,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Grant Calcaterra ' AND Anio = 2022),"3),"
(' Ko Kieft ',30,TE,17,7,80,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ko Kieft ' AND Anio = 2022),"3),"
(' Eric Tomlinson ',10,TE,17,9,79,18,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Eric Tomlinson ' AND Anio = 2022),"3),"
(' Miles Sanders ',26,RB,17,20,78,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Miles Sanders ' AND Anio = 2022),"3),"
(' Marcus Jones ',22,CB,15,4,78,48,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Marcus Jones ' AND Anio = 2022),"3),"
(' Kyle Philips ',31,WR,4,8,78,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Philips ' AND Anio = 2022),"3),"
(' Taysom Hill ',23,QB,16,9,77,30,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Taysom Hill ' AND Anio = 2022),"3),"
(' Javonte Williams ',10,RB,4,16,76,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Javonte Williams ' AND Anio = 2022),"3),"
(' Kyren Williams ',19,RB,10,9,76,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyren Williams ' AND Anio = 2022),"3),"
(' Jalen Virgil ',10,WR,9,2,75,66,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Virgil ' AND Anio = 2022),"3),"
(' Patrick Ricard ',3,FB,17,11,74,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Patrick Ricard ' AND Anio = 2022),"3),"
(' Kevin White ',23,WR,7,2,74,64,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kevin White ' AND Anio = 2022),"3),"
(' Freddie Swain ',10,WR,4,4,74,52,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Freddie Swain ' AND Anio = 2022),"3),"
(' Jamaal Williams ',11,RB,17,12,73,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamaal Williams ' AND Anio = 2022),"3),"
(' Tre' McKitty ',18,TE,17,10,72,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tre' McKitty ' AND Anio = 2022),"3),"
(' Andrew Beck ',10,FB,13,5,69,27,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andrew Beck ' AND Anio = 2022),"3),"
(' Reggie Gilliam ',4,FB,15,8,69,14,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Reggie Gilliam ' AND Anio = 2022),"3),"
(' Mark Ingram II',23,RB,10,16,68,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mark Ingram II' AND Anio = 2022),"3),"
(' Marcedes Lewis ',12,TE,17,6,66,31,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Marcedes Lewis ' AND Anio = 2022),"3),"
(' Chris Myarick ',24,TE,16,7,65,23,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Myarick ' AND Anio = 2022),"3),"
(' Jake Kumerow ',4,WR,6,4,64,39,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jake Kumerow ' AND Anio = 2022),"3),"
(' Jalen Guyton ',18,WR,3,2,64,54,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Guyton ' AND Anio = 2022),"3),"
(' Armani Rogers ',32,TE,11,5,64,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Armani Rogers ' AND Anio = 2022),"3),"
(' Malik Davis ',9,RB,12,6,63,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Malik Davis ' AND Anio = 2022),"3),"
(' Trent Taylor ',7,WR,16,6,62,34,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trent Taylor ' AND Anio = 2022),"3),"
(' James Proche II',3,WR,15,8,62,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'James Proche II' AND Anio = 2022),"3),"
(' Avery Williams ',2,RB,17,13,61,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Avery Williams ' AND Anio = 2022),"3),"
(' Jamison Crowder ',4,WR,4,6,60,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamison Crowder ' AND Anio = 2022),"3),"
(' Brian Robinson Jr.',32,RB,12,9,60,18,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Brian Robinson Jr.' AND Anio = 2022),"3),"
(' Shane Zylstra ',11,TE,13,11,60,14,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Shane Zylstra ' AND Anio = 2022),"3),"
(' Mike Strachan ',14,WR,13,3,59,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Strachan ' AND Anio = 2022),"3),"
(' Geoff Swaim ',31,TE,17,12,58,13,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Geoff Swaim ' AND Anio = 2022),"3),"
(' Justice Hill ',3,RB,15,12,58,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Justice Hill ' AND Anio = 2022),"3),"
(' Dee Eskridge ',29,WR,10,7,58,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dee Eskridge ' AND Anio = 2022),"3),"
(' Brandon Bolden ',17,RB,16,9,57,18,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Bolden ' AND Anio = 2022),"3),"
(' Tyler Kroft ',28,TE,11,4,57,28,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Kroft ' AND Anio = 2022),"3),"
(' Khalil Herbert ',6,RB,13,9,57,25,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Khalil Herbert ' AND Anio = 2022),"3),"
(' Hassan Haskins ',31,RB,15,11,57,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Hassan Haskins ' AND Anio = 2022),"3),"
(' Nick Vannett ',24,TE,9,6,55,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Vannett ' AND Anio = 2022),"3),"
(' Corey Clement ',1,RB,9,5,54,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Corey Clement ' AND Anio = 2022),"3),"
(' Cody Hollister ',31,WR,11,3,54,27,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cody Hollister ' AND Anio = 2022),"3),"
(' Sony Michel ',18,RB,10,9,53,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Sony Michel ' AND Anio = 2022),"3),"
(' Gunner Olszewski ',27,WR,16,5,53,31,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Gunner Olszewski ' AND Anio = 2022),"3),"
(' James Robinson ',25,RB,11,11,51,10,2,(SELECT Player_ID FROM Player_season WHERE Name = 'James Robinson ' AND Anio = 2022),"3),"
(' Anthony Schwartz ',8,WR,11,4,51,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Anthony Schwartz ' AND Anio = 2022),"3),"
(' Charlie Kolar ',3,TE,2,4,49,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Charlie Kolar ' AND Anio = 2022),"3),"
(' David Johnson ',23,RB,5,4,47,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'David Johnson ' AND Anio = 2022),"3),"
(' Chris Conley ',31,WR,9,4,46,27,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Conley ' AND Anio = 2022),"3),"
(' Stephen Sullivan ',5,TE,14,2,46,33,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Stephen Sullivan ' AND Anio = 2022),"3),"
(' Andre Baccellia ',1,WR,8,7,45,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andre Baccellia ' AND Anio = 2022),"3),"
(' Michael Woods II',8,WR,10,5,45,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Woods II' AND Anio = 2022),"3),"
(' Tevin Coleman ',28,RB,5,3,44,30,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tevin Coleman ' AND Anio = 2022),"3),"
(' John Brown ',4,WR,3,1,42,42,1,(SELECT Player_ID FROM Player_season WHERE Name = 'John Brown ' AND Anio = 2022),"3),"
(' Chris Manhertz ',15,TE,17,6,42,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Manhertz ' AND Anio = 2022),"3),"
(' Laquon Treadwell ',29,WR,6,6,42,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Laquon Treadwell ' AND Anio = 2022),"3),"
(' Brandon Johnson ',10,WR,7,6,42,12,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Johnson ' AND Anio = 2022),"3),"
(' J.K. Dobbins ',3,RB,8,7,42,20,1,(SELECT Player_ID FROM Player_season WHERE Name = 'J.K. Dobbins ' AND Anio = 2022),"3),"
(' Pierre Strong Jr.',22,RB,15,7,42,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Pierre Strong Jr.' AND Anio = 2022),"3),"
(' Julius Chestnut ',31,RB,6,3,41,33,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Julius Chestnut ' AND Anio = 2022),"3),"
(' Jameson Williams ',11,WR,6,1,41,41,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jameson Williams ' AND Anio = 2022),"3),"
(' Jonathan Williams ',32,RB,13,7,40,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonathan Williams ' AND Anio = 2022),"3),"
(' Luke Farrell ',15,TE,17,4,40,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Luke Farrell ' AND Anio = 2022),"3),"
(' Racey McMath ',31,WR,5,2,40,39,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Racey McMath ' AND Anio = 2022),"3),"
(' Zack Moss ',4,RB,13,11,39,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Zack Moss ' AND Anio = 2022),"3),"
(' Gary Brightwell ',24,RB,17,5,39,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Gary Brightwell ' AND Anio = 2022),"3),"
(' Mike Thomas ',7,WR,10,2,38,33,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Thomas ' AND Anio = 2022),"3),"
(' Chris Evans ',7,RB,12,3,38,26,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Evans ' AND Anio = 2022),"3),"
(' Malcolm Brown ',19,RB,11,5,37,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Malcolm Brown ' AND Anio = 2022),"3),"
(' Dax Milne ',32,WR,15,6,37,12,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Dax Milne ' AND Anio = 2022),"3),"
(' Cole Beasley ',30,WR,4,6,35,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cole Beasley ' AND Anio = 2022),"3),"
(' Kendall Blanton ',19,TE,4,2,35,28,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kendall Blanton ' AND Anio = 2022),"3),"
(' Royce Freeman ',13,RB,4,6,33,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Royce Freeman ' AND Anio = 2022),"3),"
(' Darrynton Evans ',6,RB,6,1,33,33,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Darrynton Evans ' AND Anio = 2022),"3),"
(' Tylan Wallace ',3,WR,9,4,33,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tylan Wallace ' AND Anio = 2022),"3),"
(' Deven Thompkins ',30,WR,5,5,32,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Deven Thompkins ' AND Anio = 2022),"3),"
(' Trayveon Williams ',7,RB,8,2,30,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trayveon Williams ' AND Anio = 2022),"3),"
(' Tony Jones Jr.',23,RB,6,5,30,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tony Jones Jr.' AND Anio = 2022),"3),"
(' Tim Jones ',15,WR,17,3,30,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tim Jones ' AND Anio = 2022),"3),"
(' Jordan Wilkins ',14,RB,4,6,29,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Wilkins ' AND Anio = 2022),"3),"
(' Ronnie Rivers ',19,RB,8,5,29,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ronnie Rivers ' AND Anio = 2022),"3),"
(' Kyle Rudolph ',30,TE,9,3,28,12,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Rudolph ' AND Anio = 2022),"3),"
(' Myles Gaskin ',20,RB,4,4,28,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Myles Gaskin ' AND Anio = 2022),"3),"
(' Tyrie Cleveland ',10,WR,6,2,28,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyrie Cleveland ' AND Anio = 2022),"3),"
(' Ryan Griffin ',6,TE,15,4,26,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Griffin ' AND Anio = 2022),"3),"
(' D'Onta Foreman ',5,RB,17,5,26,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'D'Onta Foreman ' AND Anio = 2022),"3),"
(' Tyler Davis ',12,TE,17,4,26,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Davis ' AND Anio = 2022),"3),"
(' Ben Ellefson ',21,TE,4,3,26,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ben Ellefson ' AND Anio = 2022),"3),"
(' Trevon Wesco ',6,TE,14,2,26,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trevon Wesco ' AND Anio = 2022),"3),"
(' Jaelon Darden ',8,WR,14,2,26,25,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaelon Darden ' AND Anio = 2022),"3),"
(' Daylen Baldwin ',8,WR,1,2,25,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Daylen Baldwin ' AND Anio = 2022),"3),"
(' Dezmon Patmon ',14,WR,1,2,24,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dezmon Patmon ' AND Anio = 2022),"3),"
(' Simi Fehoko ',9,WR,5,3,24,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Simi Fehoko ' AND Anio = 2022),"3),"
(' Tyler Badie ',10,RB,1,1,24,24,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Badie ' AND Anio = 2022),"3),"
(' Dareke Young ',29,WR,13,2,24,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dareke Young ' AND Anio = 2022),"3),"
(' Cole Turner ',32,TE,10,2,23,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cole Turner ' AND Anio = 2022),"3),"
(' Ronald Jones ',16,RB,6,1,22,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ronald Jones ' AND Anio = 2022),"3),"
(' Andy Isabella ',3,WR,5,2,21,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andy Isabella ' AND Anio = 2022),"3),"
(' Cade Johnson ',29,WR,3,2,21,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cade Johnson ' AND Anio = 2022),"3),"
(' Kene Nwangwu ',21,RB,17,2,21,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kene Nwangwu ' AND Anio = 2022),"3),"
(' Keaontay Ingram ',1,RB,12,4,21,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Keaontay Ingram ' AND Anio = 2022),"3),"
(' Blake Bell ',16,TE,3,2,20,17,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Blake Bell ' AND Anio = 2022),"3),"
(' Keke Coutee ',14,WR,8,1,20,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Keke Coutee ' AND Anio = 2022),"3),"
(' Penny Hart ',29,WR,9,3,20,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Penny Hart ' AND Anio = 2022),"3),"
(' Lil'Jordan Humphrey ',22,WR,6,2,20,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Lil'Jordan Humphrey ' AND Anio = 2022),"3),"
(' Phillip Lindsay ',14,RB,3,6,19,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Phillip Lindsay ' AND Anio = 2022),"3),"
(' Ke'Shawn Vaughn ',30,RB,15,3,19,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ke'Shawn Vaughn ' AND Anio = 2022),"3),"
(' Jesper Horsted ',17,TE,15,3,19,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jesper Horsted ' AND Anio = 2022),"3),"
(' Troy Hairston ',13,FB,16,5,19,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Troy Hairston ' AND Anio = 2022),"3),"
(' Maxx Williams ',1,TE,11,3,18,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Maxx Williams ' AND Anio = 2022),"3),"
(' Keith Kirkwood ',23,WR,5,2,18,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Keith Kirkwood ' AND Anio = 2022),"3),"
(' Juwann Winfree ',12,WR,3,1,17,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Juwann Winfree ' AND Anio = 2022),"3),"
(' Benny Snell Jr.',27,RB,17,2,17,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Benny Snell Jr.' AND Anio = 2022),"3),"
(' Patrick Taylor Jr.',12,RB,14,1,17,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Patrick Taylor Jr.' AND Anio = 2022),"3),"
(' Stone Smartt ',18,TE,7,4,17,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Stone Smartt ' AND Anio = 2022),"3),"
(' Braylon Sanders ',20,WR,3,2,17,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Braylon Sanders ' AND Anio = 2022),"3),"
(' Rashaad Penny ',29,RB,5,4,16,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Rashaad Penny ' AND Anio = 2022),"3),"
(' Dennis Houston ',9,WR,2,2,16,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dennis Houston ' AND Anio = 2022),"3),"
(' Ty Montgomery II',22,WR,1,3,15,7,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ty Montgomery II' AND Anio = 2022),"3),"
(' Boston Scott ',26,RB,15,5,15,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Boston Scott ' AND Anio = 2022),"3),"
(' Quintez Cephus ',11,WR,4,2,15,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Quintez Cephus ' AND Anio = 2022),"3),"
(' Bryan Edwards ',2,WR,7,3,15,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Bryan Edwards ' AND Anio = 2022),"3),"
(' Frank Darby ',2,WR,5,1,15,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Frank Darby ' AND Anio = 2022),"3),"
(' Ihmir Smith-Marsette ',6,WR,8,1,15,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ihmir Smith-Marsette ' AND Anio = 2022),"3),"
(' Nsimba Webster ',6,WR,2,2,14,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nsimba Webster ' AND Anio = 2022),"3),"
(' Larry Rountree III',18,RB,4,2,14,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Larry Rountree III' AND Anio = 2022),"3),"
(' Austin Trammell ',19,WR,6,2,13,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Austin Trammell ' AND Anio = 2022),"3),"
(' Deonte Harty ',23,WR,4,2,13,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Deonte Harty ' AND Anio = 2022),"3),"
(' Isaiah Spiller ',18,RB,6,3,13,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Isaiah Spiller ' AND Anio = 2022),"3),"
(' Jake Gervase ',19,S,14,1,12,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jake Gervase ' AND Anio = 2022),"3),"
(' Jalen Tolbert ',9,WR,8,2,12,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Tolbert ' AND Anio = 2022),"3),"
(' Michael Burton ',16,FB,17,2,11,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Burton ' AND Anio = 2022),"3),"
(' Derek Watt ',27,FB,17,5,11,5,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Derek Watt ' AND Anio = 2022),"3),"
(' Miles Boykin ',27,WR,16,2,11,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Miles Boykin ' AND Anio = 2022),"3),"
(' Sean McKeon ',9,TE,13,2,11,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Sean McKeon ' AND Anio = 2022),"3),"
(' Anthony McFarland Jr.',27,RB,1,2,11,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Anthony McFarland Jr.' AND Anio = 2022),"3),"
(' Jakob Johnson ',17,FB,17,5,10,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jakob Johnson ' AND Anio = 2022),"3),"
(' Spencer Brown ',5,RB,2,2,10,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Spencer Brown ' AND Anio = 2022),"3),"
(' Danny Gray ',28,WR,13,1,10,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Danny Gray ' AND Anio = 2022),"3),"
(' Stephen Anderson ',1,TE,16,3,9,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Stephen Anderson ' AND Anio = 2022),"3),"
(' Darrel Williams ',1,RB,6,4,9,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Darrel Williams ' AND Anio = 2022),"3),"
(' KaVontae Turpin ',9,WR,17,1,9,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'KaVontae Turpin ' AND Anio = 2022),"3),"
(' Adam Prentice ',23,FB,11,3,9,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Adam Prentice ' AND Anio = 2022),"3),"
(' Penei Sewell ',11,OT,17,1,9,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Penei Sewell ' AND Anio = 2022),"3),"
(' Keith Smith ',2,FB,17,1,8,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Keith Smith ' AND Anio = 2022),"3),"
(' Tyron Billy-Johnson ',17,WR,4,1,8,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyron Billy-Johnson ' AND Anio = 2022),"3),"
(' Demetric Felton ',8,RB,8,2,8,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Demetric Felton ' AND Anio = 2022),"3),"
(' J.J. Taylor ',22,RB,1,1,8,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'J.J. Taylor ' AND Anio = 2022),"3),"
(' Salvon Ahmed ',20,RB,12,1,8,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Salvon Ahmed ' AND Anio = 2022),"3),"
(' Trestan Ebner ',6,RB,17,2,8,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trestan Ebner ' AND Anio = 2022),"3),"
(' Zander Horvath ',18,FB,15,5,8,5,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Zander Horvath ' AND Anio = 2022),"3),"
(' Jeremy Ruckert ',25,TE,9,1,8,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeremy Ruckert ' AND Anio = 2022),"3),"
(' Dwayne Washington ',23,RB,12,1,7,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dwayne Washington ' AND Anio = 2022),"3),"
(' Tommy Sweeney ',4,TE,5,1,7,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tommy Sweeney ' AND Anio = 2022),"3),"
(' D'Ernest Johnson ',8,RB,15,3,7,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'D'Ernest Johnson ' AND Anio = 2022),"3),"
(' Maurice Alexander ',11,WR,4,1,7,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Maurice Alexander ' AND Anio = 2022),"3),"
(' Tyler Mabry ',29,TE,2,1,7,7,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Mabry ' AND Anio = 2022),"3),"
(' Jalen Camp ',13,WR,2,1,7,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Camp ' AND Anio = 2022),"3),"
(' Jonathan Ward ',31,RB,8,2,7,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonathan Ward ' AND Anio = 2022),"3),"
(' Elijah Mitchell ',28,RB,5,3,7,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Elijah Mitchell ' AND Anio = 2022),"3),"
(' Mason Schreck ',13,TE,3,2,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mason Schreck ' AND Anio = 2022),"3),"
(' C.J. Board ',31,WR,4,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Board ' AND Anio = 2022),"3),"
(' Pharoh Cooper ',1,WR,5,2,6,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Pharoh Cooper ' AND Anio = 2022),"3),"
(' Patrick Mahomes ',16,QB,17,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Patrick Mahomes ' AND Anio = 2022),"3),"
(' Jacob Harris ',19,WR,7,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jacob Harris ' AND Anio = 2022),"3),"
(' Jared Goff ',11,QB,17,1,5,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jared Goff ' AND Anio = 2022),"3),"
(' Jason Cabinda ',11,FB,8,1,5,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jason Cabinda ' AND Anio = 2022),"3),"
(' Ty'Son Williams ',1,RB,1,1,5,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ty'Son Williams ' AND Anio = 2022),"3),"
(' Devin Asiasi ',7,TE,12,2,5,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Devin Asiasi ' AND Anio = 2022),"3),"
(' Jason Moore ',18,WR,6,1,5,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jason Moore ' AND Anio = 2022),"3),"
(' Richard Rodgers ',18,TE,10,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Richard Rodgers ' AND Anio = 2022),"3),"
(' Jeff Driskel ',13,QB,7,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeff Driskel ' AND Anio = 2022),"3),"
(' Mike Davis ',3,RB,8,2,4,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Davis ' AND Anio = 2022),"3),"
(' Kamu Grugier-Hill ',13,LB,15,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kamu Grugier-Hill ' AND Anio = 2022),"3),"
(' Godwin Igwebuike ',29,RB,5,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Godwin Igwebuike ' AND Anio = 2022),"3),"
(' Devine Ozigbo ',10,RB,4,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Devine Ozigbo ' AND Anio = 2022),"3),"
(' Mason Kinsey ',31,WR,2,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mason Kinsey ' AND Anio = 2022),"3),"
(' Caleb Huntley ',2,RB,12,2,3,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Caleb Huntley ' AND Anio = 2022),"3),"
(' Erik Ezukanma ',20,WR,1,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Erik Ezukanma ' AND Anio = 2022),"3),"
(' Cody White ',27,WR,1,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cody White ' AND Anio = 2022),"3),"
(' Montrell Washington ',10,WR,15,4,2,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Montrell Washington ' AND Anio = 2022),"3),"
(' Zach Wilson ',25,QB,9,1,2,2,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Wilson ' AND Anio = 2022),"3),"
(' Russell Wilson ',10,QB,15,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Russell Wilson ' AND Anio = 2022),"3),"
(' Tom Brady ',30,QB,17,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tom Brady ' AND Anio = 2022),"3),"
(' Josh Gordon ',31,WR,2,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Gordon ' AND Anio = 2022),"3),"
(' David Bakhtiari ',12,OT,11,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'David Bakhtiari ' AND Anio = 2022),"3),"
(' Jack Conklin ',8,OT,14,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jack Conklin ' AND Anio = 2022),"3),"
(' Tanner Gentry ',4,WR,3,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tanner Gentry ' AND Anio = 2022),"3),"
(' Gus Edwards ',3,RB,9,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Gus Edwards ' AND Anio = 2022),"3),"
(' Khari Blasingame ',6,FB,16,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Khari Blasingame ' AND Anio = 2022),"3),"
(' James Washington ',9,WR,2,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'James Washington ' AND Anio = 2022),"3),"
(' Stanley Morgan Jr.',7,WR,14,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Stanley Morgan Jr.' AND Anio = 2022),"3),"
(' Noah Togiai ',26,TE,2,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Noah Togiai ' AND Anio = 2022),"3),"
(' Feleipe Franks ',2,TE,11,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Feleipe Franks ' AND Anio = 2022),"3),"
(' Charlie Woerner ',28,TE,17,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Charlie Woerner ' AND Anio = 2022),"3),"
(' DJ Turner ',17,WR,9,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DJ Turner ' AND Anio = 2022),"3),"
(' Miller Forristall ',8,TE,4,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Miller Forristall ' AND Anio = 2022),"3),"
(' Tanner Conner ',20,TE,13,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tanner Conner ' AND Anio = 2022),"3),"
(' Lance McCutcheon ',19,WR,10,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Lance McCutcheon ' AND Anio = 2022),"3),"
(' Jake Tonges ',6,TE,4,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jake Tonges ' AND Anio = 2022),"3),"
(' Josh Ali ',2,WR,2,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Ali ' AND Anio = 2022),"3),"
(' Jaret Patterson ',32,RB,3,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaret Patterson ' AND Anio = 2022),"3),"
(' Tyrion Davis-Price ',28,RB,6,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyrion Davis-Price ' AND Anio = 2022),"3),"
(' Giovani Bernard ',30,RB,8,2,-1,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Giovani Bernard ' AND Anio = 2022),"3),"
(' Drew Sample ',7,TE,2,2,-2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Drew Sample ' AND Anio = 2022),"3),"
(' Joe Flacco ',25,QB,5,0,-3,-3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Joe Flacco ' AND Anio = 2022),"3),"
(' Bailey Zappe ',22,QB,4,1,-6,-6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Bailey Zappe ' AND Anio = 2022),"3),"
(' Justin Herbert ',18,QB,17,2,-10,-2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Herbert ' AND Anio = 2022),"3),"
(' Josh Jacobs ',17,RB,17,340,1653,86,12,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Jacobs ' AND Anio = 2022),"2),"
(' Derrick Henry ',31,RB,16,349,1538,56,13,(SELECT Player_ID FROM Player_season WHERE Name = 'Derrick Henry ' AND Anio = 2022),"2),"
(' Nick Chubb ',8,RB,17,302,1525,41,12,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Chubb ' AND Anio = 2022),"2),"
(' Saquon Barkley ',24,RB,16,295,1312,68,10,(SELECT Player_ID FROM Player_season WHERE Name = 'Saquon Barkley ' AND Anio = 2022),"2),"
(' Miles Sanders ',26,RB,17,259,1269,40,11,(SELECT Player_ID FROM Player_season WHERE Name = 'Miles Sanders ' AND Anio = 2022),"2),"
(' Dalvin Cook ',21,RB,17,264,1173,81,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Dalvin Cook ' AND Anio = 2022),"2),"
(' Justin Fields ',6,QB,15,160,1143,67,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Fields ' AND Anio = 2022),"2),"
(' Christian McCaffrey ',5,RB,17,244,1139,49,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian McCaffrey ' AND Anio = 2022),"2),"
(' Travis Etienne Jr.',15,RB,17,220,1125,62,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Travis Etienne Jr.' AND Anio = 2022),"2),"
(' Aaron Jones ',12,RB,17,213,1121,36,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Aaron Jones ' AND Anio = 2022),"2),"
(' Jamaal Williams ',11,RB,17,262,1066,58,17,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamaal Williams ' AND Anio = 2022),"2),"
(' Kenneth Walker III',29,RB,15,228,1050,74,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenneth Walker III' AND Anio = 2022),"2),"
(' Rhamondre Stevenson ',22,RB,17,210,1040,49,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Rhamondre Stevenson ' AND Anio = 2022),"2),"
(' Tyler Allgeier ',2,RB,16,210,1035,44,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Allgeier ' AND Anio = 2022),"2),"
(' Najee Harris ',27,RB,17,272,1034,36,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Najee Harris ' AND Anio = 2022),"2),"
(' Tony Pollard ',9,RB,16,193,1007,57,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Tony Pollard ' AND Anio = 2022),"2),"
(' Dameon Pierce ',13,RB,13,220,939,75,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Dameon Pierce ' AND Anio = 2022),"2),"
(' Austin Ekeler ',18,RB,17,204,915,72,13,(SELECT Player_ID FROM Player_season WHERE Name = 'Austin Ekeler ' AND Anio = 2022),"2),"
(' D'Onta Foreman ',5,RB,17,203,914,60,5,(SELECT Player_ID FROM Player_season WHERE Name = 'D'Onta Foreman ' AND Anio = 2022),"2),"
(' Alvin Kamara ',23,RB,15,223,897,27,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Alvin Kamara ' AND Anio = 2022),"2),"
(' Raheem Mostert ',20,RB,16,181,891,67,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Raheem Mostert ' AND Anio = 2022),"2),"
(' Ezekiel Elliott ',9,RB,15,231,876,27,12,(SELECT Player_ID FROM Player_season WHERE Name = 'Ezekiel Elliott ' AND Anio = 2022),"2),"
(' Jonathan Taylor ',14,RB,11,192,861,66,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonathan Taylor ' AND Anio = 2022),"2),"
(' Jeff Wilson Jr.',20,RB,16,176,860,41,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeff Wilson Jr.' AND Anio = 2022),"2),"
(' Isiah Pacheco ',16,RB,17,170,830,31,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Isiah Pacheco ' AND Anio = 2022),"2),"
(' Devin Singletary ',4,RB,16,177,819,33,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Devin Singletary ' AND Anio = 2022),"2),"
(' Joe Mixon ',7,RB,14,210,814,40,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Joe Mixon ' AND Anio = 2022),"2),"
(' David Montgomery ',6,RB,16,201,801,28,5,(SELECT Player_ID FROM Player_season WHERE Name = 'David Montgomery ' AND Anio = 2022),"2),"
(' Brian Robinson Jr.',32,RB,12,205,797,24,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Brian Robinson Jr.' AND Anio = 2022),"2),"
(' Cam Akers ',19,RB,15,188,786,42,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Cam Akers ' AND Anio = 2022),"2),"
(' James Conner ',1,RB,13,183,782,23,7,(SELECT Player_ID FROM Player_season WHERE Name = 'James Conner ' AND Anio = 2022),"2),"
(' AJ Dillon ',12,RB,17,186,770,27,7,(SELECT Player_ID FROM Player_season WHERE Name = 'AJ Dillon ' AND Anio = 2022),"2),"
(' Lamar Jackson ',3,QB,12,112,764,79,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Lamar Jackson ' AND Anio = 2022),"2),"
(' Josh Allen ',4,QB,16,124,762,44,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Allen ' AND Anio = 2022),"2),"
(' Latavius Murray ',10,RB,13,171,760,52,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Latavius Murray ' AND Anio = 2022),"2),"
(' Jalen Hurts ',26,QB,15,165,760,42,13,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Hurts ' AND Anio = 2022),"2),"
(' Khalil Herbert ',6,RB,13,129,731,63,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Khalil Herbert ' AND Anio = 2022),"2),"
(' Daniel Jones ',24,QB,16,120,708,25,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Daniel Jones ' AND Anio = 2022),"2),"
(' Cordarrelle Patterson ',2,RB,13,144,695,40,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Cordarrelle Patterson ' AND Anio = 2022),"2),"
(' Leonard Fournette ',30,RB,16,189,668,23,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Leonard Fournette ' AND Anio = 2022),"2),"
(' Taysom Hill ',23,QB,16,96,575,60,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Taysom Hill ' AND Anio = 2022),"2),"
(' Antonio Gibson ',32,RB,15,149,546,20,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Antonio Gibson ' AND Anio = 2022),"2),"
(' D'Andre Swift ',11,RB,14,99,542,50,5,(SELECT Player_ID FROM Player_season WHERE Name = 'D'Andre Swift ' AND Anio = 2022),"2),"
(' J.K. Dobbins ',3,RB,8,92,520,44,2,(SELECT Player_ID FROM Player_season WHERE Name = 'J.K. Dobbins ' AND Anio = 2022),"2),"
(' James Cook ',4,RB,16,89,507,33,2,(SELECT Player_ID FROM Player_season WHERE Name = 'James Cook ' AND Anio = 2022),"2),"
(' Kenyan Drake ',3,RB,12,109,482,40,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenyan Drake ' AND Anio = 2022),"2),"
(' Rachaad White ',30,RB,17,129,481,35,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Rachaad White ' AND Anio = 2022),"2),"
(' Kareem Hunt ',8,RB,17,123,468,24,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Kareem Hunt ' AND Anio = 2022),"2),"
(' Chuba Hubbard ',5,RB,15,95,466,35,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Chuba Hubbard ' AND Anio = 2022),"2),"
(' Breece Hall ',25,RB,7,80,463,62,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Breece Hall ' AND Anio = 2022),"2),"
(' Damien Harris ',22,RB,11,106,462,30,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Damien Harris ' AND Anio = 2022),"2),"
(' Zack Moss ',4,RB,13,93,456,43,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Zack Moss ' AND Anio = 2022),"2),"
(' Marcus Mariota ',2,QB,13,85,438,30,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Marcus Mariota ' AND Anio = 2022),"2),"
(' Gus Edwards ',3,RB,9,87,433,37,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Gus Edwards ' AND Anio = 2022),"2),"
(' James Robinson ',25,RB,11,110,425,50,3,(SELECT Player_ID FROM Player_season WHERE Name = 'James Robinson ' AND Anio = 2022),"2),"
(' Kyler Murray ',1,QB,11,67,418,42,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyler Murray ' AND Anio = 2022),"2),"
(' Michael Carter ',25,RB,16,114,402,25,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Carter ' AND Anio = 2022),"2),"
(' Samaje Perine ',7,RB,16,95,394,29,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Samaje Perine ' AND Anio = 2022),"2),"
(' Jaylen Warren ',27,RB,16,77,379,31,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaylen Warren ' AND Anio = 2022),"2),"
(' Geno Smith ',29,QB,17,68,366,25,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Geno Smith ' AND Anio = 2022),"2),"
(' Caleb Huntley ',2,RB,12,76,366,30,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Caleb Huntley ' AND Anio = 2022),"2),"
(' Patrick Mahomes ',16,QB,17,61,358,20,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Patrick Mahomes ' AND Anio = 2022),"2),"
(' Rashaad Penny ',29,RB,5,57,346,41,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Rashaad Penny ' AND Anio = 2022),"2),"
(' Melvin Gordon III',10,RB,10,90,318,17,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Melvin Gordon III' AND Anio = 2022),"2),"
(' Eno Benjamin ',23,RB,15,77,313,45,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Eno Benjamin ' AND Anio = 2022),"2),"
(' Clyde Edwards-Helaire ',16,RB,10,71,302,52,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Clyde Edwards-Helaire ' AND Anio = 2022),"2),"
(' Zonovan Knight ',25,RB,7,85,300,48,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Zonovan Knight ' AND Anio = 2022),"2),"
(' Jerick McKinnon ',16,RB,17,72,291,30,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jerick McKinnon ' AND Anio = 2022),"2),"
(' Trevor Lawrence ',15,QB,17,62,291,24,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Trevor Lawrence ' AND Anio = 2022),"2),"
(' Joshua Kelley ',18,RB,13,69,287,22,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Joshua Kelley ' AND Anio = 2022),"2),"
(' Darrell Henderson Jr.',19,RB,10,70,283,23,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Darrell Henderson Jr.' AND Anio = 2022),"2),"
(' Alexander Mattison ',21,RB,17,74,283,15,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Alexander Mattison ' AND Anio = 2022),"2),"
(' Elijah Mitchell ',28,RB,5,45,279,37,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Elijah Mitchell ' AND Anio = 2022),"2),"
(' Russell Wilson ',10,QB,15,55,277,19,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Russell Wilson ' AND Anio = 2022),"2),"
(' Justice Hill ',3,RB,15,49,262,34,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Justice Hill ' AND Anio = 2022),"2),"
(' Jordan Mason ',28,RB,16,43,258,55,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Mason ' AND Anio = 2022),"2),"
(' Joe Burrow ',7,QB,16,75,257,23,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Joe Burrow ' AND Anio = 2022),"2),"
(' Chase Edmonds ',10,RB,13,68,245,28,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Chase Edmonds ' AND Anio = 2022),"2),"
(' Jacoby Brissett ',8,QB,16,49,243,22,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jacoby Brissett ' AND Anio = 2022),"2),"
(' Kenneth Gainwell ',26,RB,17,53,240,13,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenneth Gainwell ' AND Anio = 2022),"2),"
(' Kenny Pickett ',27,QB,13,55,237,23,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenny Pickett ' AND Anio = 2022),"2),"
(' Deon Jackson ',14,RB,16,68,236,17,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Deon Jackson ' AND Anio = 2022),"2),"
(' Mark Ingram II',23,RB,10,62,233,14,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Mark Ingram II' AND Anio = 2022),"2),"
(' Deebo Samuel Sr.',28,WR,13,42,232,51,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Deebo Samuel Sr.' AND Anio = 2022),"2),"
(' Matt Breida ',24,RB,17,54,220,18,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Breida ' AND Anio = 2022),"2),"
(' Boston Scott ',26,RB,15,54,217,21,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Boston Scott ' AND Anio = 2022),"2),"
(' Javonte Williams ',10,RB,4,47,204,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Javonte Williams ' AND Anio = 2022),"2),"
(' JaMycal Hasty ',15,RB,17,46,194,61,2,(SELECT Player_ID FROM Player_season WHERE Name = 'JaMycal Hasty ' AND Anio = 2022),"2),"
(' Curtis Samuel ',32,WR,17,38,187,21,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Curtis Samuel ' AND Anio = 2022),"2),"
(' DeeJay Dallas ',29,RB,15,35,186,27,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DeeJay Dallas ' AND Anio = 2022),"2),"
(' Dak Prescott ',9,QB,12,45,182,25,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Dak Prescott ' AND Anio = 2022),"2),"
(' Deshaun Watson ',8,QB,6,36,175,21,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Deshaun Watson ' AND Anio = 2022),"2),"
(' Justin Jackson ',11,RB,16,42,170,27,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Jackson ' AND Anio = 2022),"2),"
(' Malik Davis ',9,RB,12,38,161,23,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Malik Davis ' AND Anio = 2022),"2),"
(' Ty Johnson ',25,RB,17,30,160,32,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ty Johnson ' AND Anio = 2022),"2),"
(' Jonathan Williams ',32,RB,13,37,152,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonathan Williams ' AND Anio = 2022),"2),"
(' Justin Herbert ',18,QB,17,54,147,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Herbert ' AND Anio = 2022),"2),"
(' Dontrell Hilliard ',31,RB,12,22,145,30,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dontrell Hilliard ' AND Anio = 2022),"2),"
(' Gary Brightwell ',24,RB,17,31,141,25,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Gary Brightwell ' AND Anio = 2022),"2),"
(' Kyren Williams ',19,RB,10,35,139,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyren Williams ' AND Anio = 2022),"2),"
(' Tyler Huntley ',3,QB,6,43,137,14,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Huntley ' AND Anio = 2022),"2),"
(' Dare Ogunbowale ',13,RB,17,42,123,11,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Dare Ogunbowale ' AND Anio = 2022),"2),"
(' Malik Willis ',31,QB,8,27,123,17,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Malik Willis ' AND Anio = 2022),"2),"
(' Royce Freeman ',13,RB,4,41,117,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Royce Freeman ' AND Anio = 2022),"2),"
(' Avery Williams ',2,RB,17,22,109,21,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Avery Williams ' AND Anio = 2022),"2),"
(' Davis Mills ',13,QB,15,32,108,17,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Davis Mills ' AND Anio = 2022),"2),"
(' Sony Michel ',18,RB,10,36,106,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Sony Michel ' AND Anio = 2022),"2),"
(' Sam Darnold ',5,QB,6,26,106,26,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Sam Darnold ' AND Anio = 2022),"2),"
(' Velus Jones Jr.',6,WR,12,9,103,42,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Velus Jones Jr.' AND Anio = 2022),"2),"
(' Derek Carr ',17,QB,15,24,102,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Derek Carr ' AND Anio = 2022),"2),"
(' Darrel Williams ',1,RB,6,21,102,30,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Darrel Williams ' AND Anio = 2022),"2),"
(' Mike Boone ',10,RB,9,24,102,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Boone ' AND Anio = 2022),"2),"
(' Mac Jones ',22,QB,14,47,102,15,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Mac Jones ' AND Anio = 2022),"2),"
(' Zach Wilson ',25,QB,9,28,102,18,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Wilson ' AND Anio = 2022),"2),"
(' Craig Reynolds ',11,RB,9,23,102,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Craig Reynolds ' AND Anio = 2022),"2),"
(' Pierre Strong Jr.',22,RB,15,10,100,44,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Pierre Strong Jr.' AND Anio = 2022),"2),"
(' Tyrion Davis-Price ',28,RB,6,34,99,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyrion Davis-Price ' AND Anio = 2022),"2),"
(' Ryan Tannehill ',31,QB,12,34,98,17,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Tannehill ' AND Anio = 2022),"2),"
(' Kirk Cousins ',21,QB,17,31,97,19,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Kirk Cousins ' AND Anio = 2022),"2),"
(' Taylor Heinicke ',32,QB,9,28,96,15,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Taylor Heinicke ' AND Anio = 2022),"2),"
(' J.D. McKissic ',32,RB,8,22,95,33,0,(SELECT Player_ID FROM Player_season WHERE Name = 'J.D. McKissic ' AND Anio = 2022),"2),"
(' Amon-Ra St. Brown',11,WR,16,9,95,58,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Amon-Ra St. Brown' AND Anio = 2022),"2),"
(' Aaron Rodgers ',12,QB,17,34,94,18,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Aaron Rodgers ' AND Anio = 2022),"2),"
(' Hassan Haskins ',31,RB,15,25,93,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Hassan Haskins ' AND Anio = 2022),"2),"
(' Braxton Berrios ',25,WR,17,9,91,25,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Braxton Berrios ' AND Anio = 2022),"2),"
(' Bryce Perkins ',19,QB,5,19,90,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Bryce Perkins ' AND Anio = 2022),"2),"
(' Benny Snell Jr.',27,RB,17,20,90,16,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Benny Snell Jr.' AND Anio = 2022),"2),"
(' Baker Mayfield ',5,QB,12,31,89,17,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Baker Mayfield ' AND Anio = 2022),"2),"
(' Sam Ehlinger ',14,QB,4,17,87,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Sam Ehlinger ' AND Anio = 2022),"2),"
(' Carson Wentz ',32,QB,8,22,86,18,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Carson Wentz ' AND Anio = 2022),"2),"
(' Jamal Agnew ',15,WR,15,12,86,30,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamal Agnew ' AND Anio = 2022),"2),"
(' Marlon Mack ',10,RB,8,16,84,17,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Marlon Mack ' AND Anio = 2022),"2),"
(' Jarrett Stidham ',17,QB,5,14,84,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jarrett Stidham ' AND Anio = 2022),"2),"
(' Devin Duvernay ',3,WR,14,12,84,18,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Devin Duvernay ' AND Anio = 2022),"2),"
(' Kadarius Toney ',24,WR,9,7,82,32,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kadarius Toney ' AND Anio = 2022),"2),"
(' Malcolm Brown ',19,RB,11,18,81,23,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Malcolm Brown ' AND Anio = 2022),"2),"
(' Rex Burkhead ',13,RB,16,26,80,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Rex Burkhead ' AND Anio = 2022),"2),"
(' Brandon Powell ',19,WR,17,17,80,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Powell ' AND Anio = 2022),"2),"
(' Christian Watson ',12,WR,14,7,80,46,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian Watson ' AND Anio = 2022),"2),"
(' Ray-Ray McCloud III',28,WR,17,4,78,71,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ray-Ray McCloud III' AND Anio = 2022),"2),"
(' Jaret Patterson ',32,RB,3,17,78,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaret Patterson ' AND Anio = 2022),"2),"
(' Raheem Blackshear ',5,RB,13,23,77,16,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Raheem Blackshear ' AND Anio = 2022),"2),"
(' Jeff Driskel ',13,QB,7,20,75,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeff Driskel ' AND Anio = 2022),"2),"
(' Travis Homer ',29,RB,10,19,74,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Travis Homer ' AND Anio = 2022),"2),"
(' Jared Goff ',11,QB,17,29,73,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jared Goff ' AND Anio = 2022),"2),"
(' Matt Ryan ',14,QB,12,27,70,39,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Ryan ' AND Anio = 2022),"2),"
(' Tyrod Taylor ',24,QB,3,5,70,32,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyrod Taylor ' AND Anio = 2022),"2),"
(' Ronald Jones ',16,RB,6,17,70,13,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ronald Jones ' AND Anio = 2022),"2),"
(' Steven Sims ',27,WR,12,13,70,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Steven Sims ' AND Anio = 2022),"2),"
(' Tua Tagovailoa ',20,QB,13,24,70,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tua Tagovailoa ' AND Anio = 2022),"2),"
(' Zamir White ',17,RB,14,17,70,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Zamir White ' AND Anio = 2022),"2),"
(' Trey Lance ',28,QB,2,16,67,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trey Lance ' AND Anio = 2022),"2),"
(' Brandon Bolden ',17,RB,16,17,66,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Bolden ' AND Anio = 2022),"2),"
(' Laviska Shenault Jr.',5,WR,13,9,65,41,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Laviska Shenault Jr.' AND Anio = 2022),"2),"
(' Darrynton Evans ',6,RB,6,14,64,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Darrynton Evans ' AND Anio = 2022),"2),"
(' Desmond Ridder ',2,QB,4,16,64,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Desmond Ridder ' AND Anio = 2022),"2),"
(' Salvon Ahmed ',20,RB,12,12,64,11,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Salvon Ahmed ' AND Anio = 2022),"2),"
(' Trace McSorley ',1,QB,6,15,61,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trace McSorley ' AND Anio = 2022),"2),"
(' Keaontay Ingram ',1,RB,12,27,60,13,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Keaontay Ingram ' AND Anio = 2022),"2),"
(' Chase Claypool ',6,WR,15,9,59,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chase Claypool ' AND Anio = 2022),"2),"
(' Jordan Wilkins ',14,RB,4,13,58,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Wilkins ' AND Anio = 2022),"2),"
(' Parris Campbell ',14,WR,17,5,58,28,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Parris Campbell ' AND Anio = 2022),"2),"
(' Rashid Shaheed ',23,WR,12,4,57,44,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Rashid Shaheed ' AND Anio = 2022),"2),"
(' Anthony Schwartz ',8,WR,11,4,57,31,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Anthony Schwartz ' AND Anio = 2022),"2),"
(' Corey Clement ',1,RB,9,15,55,12,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Corey Clement ' AND Anio = 2022),"2),"
(' Isaiah McKenzie ',4,WR,15,9,55,18,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Isaiah McKenzie ' AND Anio = 2022),"2),"
(' C.J. Moore ',11,S,11,2,55,42,0,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Moore ' AND Anio = 2022),"2),"
(' Andy Dalton ',23,QB,14,30,54,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andy Dalton ' AND Anio = 2022),"2),"
(' Chris Streveler ',25,QB,2,9,54,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Streveler ' AND Anio = 2022),"2),"
(' Equanimeous St. Brown',6,WR,16,6,54,41,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Equanimeous St. Brown' AND Anio = 2022),"2),"
(' Trestan Ebner ',6,RB,17,24,54,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trestan Ebner ' AND Anio = 2022),"2),"
(' DJ Moore ',5,WR,17,10,53,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DJ Moore ' AND Anio = 2022),"2),"
(' Ke'Shawn Vaughn ',30,RB,15,17,53,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ke'Shawn Vaughn ' AND Anio = 2022),"2),"
(' Cooper Kupp ',19,WR,9,9,52,20,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Cooper Kupp ' AND Anio = 2022),"2),"
(' Kevin Harris ',22,RB,5,18,52,14,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kevin Harris ' AND Anio = 2022),"2),"
(' Phillip Lindsay ',14,RB,3,15,49,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Phillip Lindsay ' AND Anio = 2022),"2),"
(' CeeDee Lamb ',9,WR,17,10,47,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'CeeDee Lamb ' AND Anio = 2022),"2),"
(' Treylon Burks ',31,WR,11,4,47,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Treylon Burks ' AND Anio = 2022),"2),"
(' Julio Jones ',30,WR,10,5,45,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Julio Jones ' AND Anio = 2022),"2),"
(' Joshua Dobbs ',31,QB,2,8,44,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Joshua Dobbs ' AND Anio = 2022),"2),"
(' Greg Dortch ',1,WR,16,7,44,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Greg Dortch ' AND Anio = 2022),"2),"
(' Spencer Brown ',5,RB,2,9,43,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Spencer Brown ' AND Anio = 2022),"2),"
(' Snoop Conner ',15,RB,8,12,42,8,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Snoop Conner ' AND Anio = 2022),"2),"
(' Davis Webb ',24,QB,1,6,41,14,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Davis Webb ' AND Anio = 2022),"2),"
(' Isaiah Spiller ',18,RB,6,18,41,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Isaiah Spiller ' AND Anio = 2022),"2),"
(' Mack Hollins ',17,WR,17,4,40,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mack Hollins ' AND Anio = 2022),"2),"
(' Jerry Jeudy ',10,WR,15,4,40,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jerry Jeudy ' AND Anio = 2022),"2),"
(' Jameson Williams ',11,WR,6,1,40,40,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jameson Williams ' AND Anio = 2022),"2),"
(' Kendrick Bourne ',22,WR,16,6,39,29,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kendrick Bourne ' AND Anio = 2022),"2),"
(' PJ Walker ',5,QB,6,6,39,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'PJ Walker ' AND Anio = 2022),"2),"
(' Gunner Olszewski ',27,WR,16,8,39,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Gunner Olszewski ' AND Anio = 2022),"2),"
(' Dwayne Washington ',23,RB,12,11,38,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dwayne Washington ' AND Anio = 2022),"2),"
(' Mitchell Trubisky ',27,QB,7,19,38,9,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Mitchell Trubisky ' AND Anio = 2022),"2),"
(' Dante Pettis ',6,WR,17,2,37,29,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dante Pettis ' AND Anio = 2022),"2),"
(' Colt McCoy ',1,QB,4,14,36,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Colt McCoy ' AND Anio = 2022),"2),"
(' Kalif Raymond ',11,WR,17,7,36,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kalif Raymond ' AND Anio = 2022),"2),"
(' Sam Howell ',32,QB,1,5,35,10,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Sam Howell ' AND Anio = 2022),"2),"
(' Tutu Atwell ',19,WR,13,9,34,11,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tutu Atwell ' AND Anio = 2022),"2),"
(' Jimmy Garoppolo ',28,QB,11,23,33,6,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jimmy Garoppolo ' AND Anio = 2022),"2),"
(' Nyheim Hines ',4,RB,16,24,33,9,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Nyheim Hines ' AND Anio = 2022),"2),"
(' Tyreek Hill ',20,WR,17,7,32,10,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyreek Hill ' AND Anio = 2022),"2),"
(' John Wolford ',19,QB,3,8,32,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'John Wolford ' AND Anio = 2022),"2),"
(' Mecole Hardman ',16,WR,8,4,31,25,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Mecole Hardman ' AND Anio = 2022),"2),"
(' Patrick Taylor Jr.',12,RB,14,10,31,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Patrick Taylor Jr.' AND Anio = 2022),"2),"
(' Trayveon Williams ',7,RB,8,6,30,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trayveon Williams ' AND Anio = 2022),"2),"
(' Michael Pittman Jr.',14,WR,16,3,30,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Pittman Jr.' AND Anio = 2022),"2),"
(' Anthony McFarland Jr.',27,RB,1,6,30,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Anthony McFarland Jr.' AND Anio = 2022),"2),"
(' Montrell Washington ',10,WR,15,5,30,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Montrell Washington ' AND Anio = 2022),"2),"
(' Terry McLaurin ',32,WR,17,7,29,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Terry McLaurin ' AND Anio = 2022),"2),"
(' Giovani Bernard ',30,RB,8,8,28,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Giovani Bernard ' AND Anio = 2022),"2),"
(' Teddy Bridgewater ',20,QB,5,3,27,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Teddy Bridgewater ' AND Anio = 2022),"2),"
(' Connor Heyward ',27,TE,17,2,27,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Connor Heyward ' AND Anio = 2022),"2),"
(' Kyle Juszczyk ',28,FB,16,7,26,9,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Juszczyk ' AND Anio = 2022),"2),"
(' Tevin Coleman ',28,RB,5,12,26,14,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tevin Coleman ' AND Anio = 2022),"2),"
(' Myles Gaskin ',20,RB,4,10,26,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Myles Gaskin ' AND Anio = 2022),"2),"
(' DJ Turner ',17,WR,9,4,26,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DJ Turner ' AND Anio = 2022),"2),"
(' Armani Rogers ',32,TE,11,2,26,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Armani Rogers ' AND Anio = 2022),"2),"
(' Jaylen Waddle ',20,WR,17,3,26,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaylen Waddle ' AND Anio = 2022),"2),"
(' Deven Thompkins ',30,WR,5,2,26,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Deven Thompkins ' AND Anio = 2022),"2),"
(' Diontae Johnson ',27,WR,17,7,25,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Diontae Johnson ' AND Anio = 2022),"2),"
(' Jonathan Ward ',31,RB,8,5,25,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonathan Ward ' AND Anio = 2022),"2),"
(' Jalen Reagor ',21,WR,17,4,25,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Reagor ' AND Anio = 2022),"2),"
(' David Johnson ',23,RB,5,12,24,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'David Johnson ' AND Anio = 2022),"2),"
(' Tony Jones Jr.',23,RB,6,10,24,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tony Jones Jr.' AND Anio = 2022),"2),"
(' Justin Jefferson ',21,WR,17,4,24,10,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Jefferson ' AND Anio = 2022),"2),"
(' George Pickens ',27,WR,17,3,24,22,1,(SELECT Player_ID FROM Player_season WHERE Name = 'George Pickens ' AND Anio = 2022),"2),"
(' Skyy Moore ',16,WR,16,3,24,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Skyy Moore ' AND Anio = 2022),"2),"
(' KJ Hamler ',10,WR,7,2,23,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'KJ Hamler ' AND Anio = 2022),"2),"
(' Brandon Aiyuk ',28,WR,17,2,23,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Aiyuk ' AND Anio = 2022),"2),"
(' Derek Watt ',27,FB,17,9,21,4,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Derek Watt ' AND Anio = 2022),"2),"
(' Skylar Thompson ',20,QB,7,14,21,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Skylar Thompson ' AND Anio = 2022),"2),"
(' Ronnie Rivers ',19,RB,8,9,21,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ronnie Rivers ' AND Anio = 2022),"2),"
(' Ameer Abdullah ',17,RB,17,4,20,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ameer Abdullah ' AND Anio = 2022),"2),"
(' Ty Chandler ',21,RB,3,6,20,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ty Chandler ' AND Anio = 2022),"2),"
(' Larry Rountree III',18,RB,4,13,19,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Larry Rountree III' AND Anio = 2022),"2),"
(' Trey Sermon ',26,RB,2,2,19,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trey Sermon ' AND Anio = 2022),"2),"
(' Mike Davis ',3,RB,8,8,18,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Davis ' AND Anio = 2022),"2),"
(' Zay Jones ',15,WR,16,4,18,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Zay Jones ' AND Anio = 2022),"2),"
(' D'Ernest Johnson ',8,RB,15,4,17,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'D'Ernest Johnson ' AND Anio = 2022),"2),"
(' KaVontae Turpin ',9,WR,17,3,17,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'KaVontae Turpin ' AND Anio = 2022),"2),"
(' Ben Skowronek ',19,WR,14,1,17,17,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ben Skowronek ' AND Anio = 2022),"2),"
(' Jameis Winston ',23,QB,3,5,16,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jameis Winston ' AND Anio = 2022),"2),"
(' Patrick Ricard ',3,FB,17,7,16,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Patrick Ricard ' AND Anio = 2022),"2),"
(' Tyquan Thornton ',22,WR,13,3,16,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyquan Thornton ' AND Anio = 2022),"2),"
(' Trent Taylor ',7,WR,16,4,15,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trent Taylor ' AND Anio = 2022),"2),"
(' Pharoh Cooper ',1,WR,5,4,15,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Pharoh Cooper ' AND Anio = 2022),"2),"
(' Dyami Brown ',32,WR,15,1,15,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dyami Brown ' AND Anio = 2022),"2),"
(' Kene Nwangwu ',21,RB,17,9,14,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kene Nwangwu ' AND Anio = 2022),"2),"
(' Evan Engram ',15,TE,17,2,13,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Evan Engram ' AND Anio = 2022),"2),"
(' Kyle Allen ',13,QB,2,6,13,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Allen ' AND Anio = 2022),"2),"
(' Kendall Hinton ',10,WR,12,2,13,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kendall Hinton ' AND Anio = 2022),"2),"
(' Brock Purdy ',28,QB,9,22,13,13,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Brock Purdy ' AND Anio = 2022),"2),"
(' Julius Chestnut ',31,RB,6,9,12,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Julius Chestnut ' AND Anio = 2022),"2),"
(' Jerome Ford ',8,RB,13,8,12,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jerome Ford ' AND Anio = 2022),"2),"
(' Christian Kirk ',15,WR,17,5,11,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian Kirk ' AND Anio = 2022),"2),"
(' Trenton Irwin ',7,WR,9,1,11,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trenton Irwin ' AND Anio = 2022),"2),"
(' Romeo Doubs ',12,WR,13,1,11,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Romeo Doubs ' AND Anio = 2022),"2),"
(' Dee Eskridge ',29,WR,10,2,10,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dee Eskridge ' AND Anio = 2022),"2),"
(' Matthew Stafford ',19,QB,9,13,9,4,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Matthew Stafford ' AND Anio = 2022),"2),"
(' Mike White ',25,QB,4,6,9,4,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike White ' AND Anio = 2022),"2),"
(' Adam Prentice ',23,FB,11,4,9,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Adam Prentice ' AND Anio = 2022),"2),"
(' J.J. Taylor ',22,RB,1,10,9,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'J.J. Taylor ' AND Anio = 2022),"2),"
(' Cole Kmet ',6,TE,17,2,9,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cole Kmet ' AND Anio = 2022),"2),"
(' Danny Gray ',28,WR,13,1,9,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Danny Gray ' AND Anio = 2022),"2),"
(' Nick Foles ',14,QB,3,2,8,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Foles ' AND Anio = 2022),"2),"
(' Keenan Allen ',18,WR,10,1,8,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Keenan Allen ' AND Anio = 2022),"2),"
(' Trevor Siemian ',6,QB,2,4,8,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trevor Siemian ' AND Anio = 2022),"2),"
(' Nick Mullens ',21,QB,4,4,8,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Mullens ' AND Anio = 2022),"2),"
(' Mark Andrews ',3,TE,15,3,8,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mark Andrews ' AND Anio = 2022),"2),"
(' Reggie Bonnafon ',32,RB,1,3,8,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Reggie Bonnafon ' AND Anio = 2022),"2),"
(' Scotty Miller ',30,WR,15,1,8,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Scotty Miller ' AND Anio = 2022),"2),"
(' Alec Ingold ',20,FB,17,6,8,2,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Alec Ingold ' AND Anio = 2022),"2),"
(' Cedrick Wilson Jr.',20,WR,15,1,8,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cedrick Wilson Jr.' AND Anio = 2022),"2),"
(' Harrison Bryant ',8,TE,17,1,8,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Harrison Bryant ' AND Anio = 2022),"2),"
(' Ashton Dulin ',14,WR,12,2,8,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ashton Dulin ' AND Anio = 2022),"2),"
(' Zander Horvath ',18,FB,15,4,8,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Zander Horvath ' AND Anio = 2022),"2),"
(' Ja'Marr Chase ',7,WR,12,5,8,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ja'Marr Chase ' AND Anio = 2022),"2),"
(' Brandin Cooks ',13,WR,13,2,7,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandin Cooks ' AND Anio = 2022),"2),"
(' Michael Burton ',16,FB,17,5,7,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Burton ' AND Anio = 2022),"2),"
(' Nathan Peterman ',6,QB,3,2,7,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nathan Peterman ' AND Anio = 2022),"2),"
(' Brett Rypien ',10,QB,4,6,7,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brett Rypien ' AND Anio = 2022),"2),"
(' Olamide Zaccheaus ',2,WR,17,2,7,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Olamide Zaccheaus ' AND Anio = 2022),"2),"
(' C.J. Ham ',21,FB,17,4,7,3,2,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Ham ' AND Anio = 2022),"2),"
(' Amari Rodgers ',12,WR,16,2,7,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Amari Rodgers ' AND Anio = 2022),"2),"
(' Kylin Hill ',12,RB,2,1,7,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kylin Hill ' AND Anio = 2022),"2),"
(' Joe Flacco ',25,QB,5,3,6,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Joe Flacco ' AND Anio = 2022),"2),"
(' Cooper Rush ',9,QB,9,9,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cooper Rush ' AND Anio = 2022),"2),"
(' Richie James ',24,WR,17,2,6,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Richie James ' AND Anio = 2022),"2),"
(' K.J. Osborn ',21,WR,17,3,6,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'K.J. Osborn ' AND Anio = 2022),"2),"
(' Marquise Goodwin ',29,WR,13,2,5,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marquise Goodwin ' AND Anio = 2022),"2),"
(' Travis Kelce ',16,TE,17,2,5,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Travis Kelce ' AND Anio = 2022),"2),"
(' Jonnu Smith ',22,TE,14,1,5,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonnu Smith ' AND Anio = 2022),"2),"
(' Chris Godwin ',30,WR,15,3,5,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Godwin ' AND Anio = 2022),"2),"
(' David Blough ',1,QB,2,4,5,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'David Blough ' AND Anio = 2022),"2),"
(' Courtland Sutton ',10,WR,15,1,5,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Courtland Sutton ' AND Anio = 2022),"2),"
(' Elijah Moore ',25,WR,16,5,5,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Elijah Moore ' AND Anio = 2022),"2),"
(' Chase Daniel ',18,QB,4,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chase Daniel ' AND Anio = 2022),"2),"
(' Adam Thielen ',21,WR,17,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Adam Thielen ' AND Anio = 2022),"2),"
(' Duke Johnson ',4,RB,1,2,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Duke Johnson ' AND Anio = 2022),"2),"
(' Godwin Igwebuike ',29,RB,5,3,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Godwin Igwebuike ' AND Anio = 2022),"2),"
(' Marcus Allen ',27,LB,15,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marcus Allen ' AND Anio = 2022),"2),"
(' Jason Cabinda ',11,FB,8,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jason Cabinda ' AND Anio = 2022),"2),"
(' Devine Ozigbo ',10,RB,4,3,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Devine Ozigbo ' AND Anio = 2022),"2),"
(' Racey McMath ',31,WR,5,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Racey McMath ' AND Anio = 2022),"2),"
(' Joshua Palmer ',18,WR,16,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Joshua Palmer ' AND Anio = 2022),"2),"
(' Garrett Wilson ',25,WR,17,4,4,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Garrett Wilson ' AND Anio = 2022),"2),"
(' Josh Johnson ',28,QB,2,2,3,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Johnson ' AND Anio = 2022),"2),"
(' Nick Bellore ',29,LB,16,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Bellore ' AND Anio = 2022),"2),"
(' Chris Moore ',13,WR,16,3,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Moore ' AND Anio = 2022),"2),"
(' M.J. Stewart ',13,S,17,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'M.J. Stewart ' AND Anio = 2022),"2),"
(' Tyler Conklin ',25,TE,17,2,3,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Conklin ' AND Anio = 2022),"2),"
(' Gardner Minshew ',26,QB,5,7,3,3,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Gardner Minshew ' AND Anio = 2022),"2),"
(' Keith Smith ',2,FB,17,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Keith Smith ' AND Anio = 2022),"2),"
(' Damien Williams ',2,RB,1,2,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Damien Williams ' AND Anio = 2022),"2),"
(' Sean Chandler ',5,S,17,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Sean Chandler ' AND Anio = 2022),"2),"
(' Foster Moreau ',17,TE,15,0,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Foster Moreau ' AND Anio = 2022),"2),"
(' Ashtyn Davis ',25,S,14,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ashtyn Davis ' AND Anio = 2022),"2),"
(' Darnell Mooney ',6,WR,12,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Darnell Mooney ' AND Anio = 2022),"2),"
(' Jaelon Darden ',8,WR,14,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaelon Darden ' AND Anio = 2022),"2),"
(' Donovan Peoples-Jones ',8,WR,17,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Donovan Peoples-Jones ' AND Anio = 2022),"2),"
(' Peyton Hendershot ',9,TE,17,1,2,2,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Peyton Hendershot ' AND Anio = 2022),"2),"
(' Chigoziem Okonkwo ',31,TE,17,3,2,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chigoziem Okonkwo ' AND Anio = 2022),"2),"
(' Daniel Bellinger ',24,TE,12,1,2,2,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Daniel Bellinger ' AND Anio = 2022),"2),"
(' Durham Smythe ',20,TE,16,2,1,1,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Durham Smythe ' AND Anio = 2022),"2),"
(' Jordan Howard ',23,RB,2,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Howard ' AND Anio = 2022),"2),"
(' Andy Isabella ',3,WR,5,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andy Isabella ' AND Anio = 2022),"2),"
(' Quez Watkins ',26,WR,17,3,1,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Quez Watkins ' AND Anio = 2022),"2),"
(' Noah Gray ',16,TE,17,1,1,1,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Noah Gray ' AND Anio = 2022),"2),"
(' Marquise Brown ',1,WR,12,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marquise Brown ' AND Anio = 2022),"2),"
(' Bryan Anger ',9,P,17,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Bryan Anger ' AND Anio = 2022),"2),"
(' Case Keenum ',4,QB,2,5,0,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Case Keenum ' AND Anio = 2022),"2),"
(' Zach Pascal ',26,WR,17,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Pascal ' AND Anio = 2022),"2),"
(' Clayton Fejedelem ',20,S,13,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Clayton Fejedelem ' AND Anio = 2022),"2),"
(' Dallin Leavitt ',12,S,17,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dallin Leavitt ' AND Anio = 2022),"2),"
(' Andrew Beck ',10,FB,13,2,0,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andrew Beck ' AND Anio = 2022),"2),"
(' Allen Lazard ',12,WR,15,2,0,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Allen Lazard ' AND Anio = 2022),"2),"
(' Gerald Everett ',18,TE,16,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Gerald Everett ' AND Anio = 2022),"2),"
(' Feleipe Franks ',2,TE,11,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Feleipe Franks ' AND Anio = 2022),"2),"
(' Kylen Granson ',14,TE,13,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kylen Granson ' AND Anio = 2022),"2),"
(' Bailey Zappe ',22,QB,4,10,0,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Bailey Zappe ' AND Anio = 2022),"2),"
(' Tyler Badie ',10,RB,1,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Badie ' AND Anio = 2022),"2),"
(' Tom Brady ',30,QB,17,29,-1,2,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tom Brady ' AND Anio = 2022),"2),"
(' Davante Adams ',17,WR,17,3,-1,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Davante Adams ' AND Anio = 2022),"2),"
(' Brandon Allen ',7,QB,1,3,-1,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Allen ' AND Anio = 2022),"2),"
(' Jordan Love ',12,QB,4,1,-1,-1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Love ' AND Anio = 2022),"2),"
(' Ihmir Smith-Marsette ',6,WR,8,1,-1,-1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ihmir Smith-Marsette ' AND Anio = 2022),"2),"
(' Wan'Dale Robinson ',24,WR,6,2,-1,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Wan'Dale Robinson ' AND Anio = 2022),"2),"
(' Ty Montgomery II',22,WR,1,2,-2,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ty Montgomery II' AND Anio = 2022),"2),"
(' Tim Boyle ',6,QB,1,2,-2,-1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tim Boyle ' AND Anio = 2022),"2),"
(' Matthias Farley ',17,S,17,1,-3,-3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Matthias Farley ' AND Anio = 2022),"2),"
(' Stefon Diggs ',4,WR,16,1,-3,-3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Stefon Diggs ' AND Anio = 2022),"2),"
(' Marquez Valdes-Scantling ',16,WR,17,1,-3,-3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marquez Valdes-Scantling ' AND Anio = 2022),"2),"
(' Jamie Gillan ',24,P,17,2,-3,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamie Gillan ' AND Anio = 2022),"2),"
(' Nate Sudfeld ',11,QB,2,5,-4,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nate Sudfeld ' AND Anio = 2022),"2),"
(' C.J. Beathard ',15,QB,4,4,-4,-1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Beathard ' AND Anio = 2022),"2),"
(' Demetric Felton ',8,RB,8,1,-4,-4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Demetric Felton ' AND Anio = 2022),"2),"
(' Chad Henne ',16,QB,3,5,-5,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chad Henne ' AND Anio = 2022),"2),"
(' Anthony Brown Jr.',3,QB,2,3,-5,-1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Anthony Brown Jr.' AND Anio = 2022),"2),"
(' Michael Woods II',8,WR,10,1,-5,-5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Woods II' AND Anio = 2022),"2),"
(' Rondale Moore ',1,WR,8,6,-5,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Rondale Moore ' AND Anio = 2022),"2),"
(' Breshad Perriman ',30,WR,11,2,-7,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Breshad Perriman ' AND Anio = 2022),"2),"
(' Jahan Dotson ',32,WR,12,2,-7,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jahan Dotson ' AND Anio = 2022),"2),"
(' David Njoku ',8,TE,14,2,-8,-2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'David Njoku ' AND Anio = 2022),"2),"
(' Jakobi Meyers ',22,WR,14,2,-11,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jakobi Meyers ' AND Anio = 2022),"2),"
(' DeAndre Carter ',18,WR,17,2,-15,-5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DeAndre Carter ' AND Anio = 2022),"2),"
(' Michael Dickson ',29,P,17,2,-18,-8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Dickson ' AND Anio = 2022),"2),"
(' Tua Tagovailoa',20,QB,17,560,4624,78,29,(SELECT Player_ID FROM Player_season WHERE Name = 'Tua Tagovailoa' AND Anio = 2023),"1),"
(' Jared Goff',11,QB,17,605,4575,70,30,(SELECT Player_ID FROM Player_season WHERE Name = 'Jared Goff' AND Anio = 2023),"1),"
(' Dak Prescott',9,QB,17,590,4516,92,36,(SELECT Player_ID FROM Player_season WHERE Name = 'Dak Prescott' AND Anio = 2023),"1),"
(' Josh Allen',4,QB,17,579,4306,81,29,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Allen' AND Anio = 2023),"1),"
(' Brock Purdy',28,QB,16,444,4280,76,31,(SELECT Player_ID FROM Player_season WHERE Name = 'Brock Purdy' AND Anio = 2023),"1),"
(' Patrick Mahomes',16,QB,16,597,4183,67,27,(SELECT Player_ID FROM Player_season WHERE Name = 'Patrick Mahomes' AND Anio = 2023),"1),"
(' Jordan Love',12,QB,17,579,4159,77,32,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Love' AND Anio = 2023),"1),"
(' C.J. Stroud',13,QB,15,499,4108,75,23,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Stroud' AND Anio = 2023),"1),"
(' Baker Mayfield',30,QB,17,566,4044,75,28,(SELECT Player_ID FROM Player_season WHERE Name = 'Baker Mayfield' AND Anio = 2023),"1),"
(' Trevor Lawrence',15,QB,16,564,4016,65,21,(SELECT Player_ID FROM Player_season WHERE Name = 'Trevor Lawrence' AND Anio = 2023),"1),"
(' Matthew Stafford',19,QB,15,521,3965,80,24,(SELECT Player_ID FROM Player_season WHERE Name = 'Matthew Stafford' AND Anio = 2023),"1),"
(' Sam Howell',32,QB,17,612,3946,51,21,(SELECT Player_ID FROM Player_season WHERE Name = 'Sam Howell' AND Anio = 2023),"1),"
(' Derek Carr',23,QB,17,548,3878,58,25,(SELECT Player_ID FROM Player_season WHERE Name = 'Derek Carr' AND Anio = 2023),"1),"
(' Jalen Hurts',26,QB,17,538,3858,63,23,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Hurts' AND Anio = 2023),"1),"
(' Lamar Jackson',3,QB,16,457,3678,80,24,(SELECT Player_ID FROM Player_season WHERE Name = 'Lamar Jackson' AND Anio = 2023),"1),"
(' Geno Smith',29,QB,15,499,3624,73,20,(SELECT Player_ID FROM Player_season WHERE Name = 'Geno Smith' AND Anio = 2023),"1),"
(' Gardner Minshew',14,QB,17,490,3305,75,15,(SELECT Player_ID FROM Player_season WHERE Name = 'Gardner Minshew' AND Anio = 2023),"1),"
(' Justin Herbert',18,QB,13,456,3134,60,20,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Herbert' AND Anio = 2023),"1),"
(' Russell Wilson',10,QB,15,447,3070,60,26,(SELECT Player_ID FROM Player_season WHERE Name = 'Russell Wilson' AND Anio = 2023),"1),"
(' Bryce Young',5,QB,16,527,2877,48,11,(SELECT Player_ID FROM Player_season WHERE Name = 'Bryce Young' AND Anio = 2023),"1),"
(' Desmond Ridder',2,QB,15,388,2836,71,12,(SELECT Player_ID FROM Player_season WHERE Name = 'Desmond Ridder' AND Anio = 2023),"1),"
(' Justin Fields',6,QB,13,370,2562,58,16,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Fields' AND Anio = 2023),"1),"
(' Joshua Dobbs',21,QB,13,417,2464,69,13,(SELECT Player_ID FROM Player_season WHERE Name = 'Joshua Dobbs' AND Anio = 2023),"1),"
(' Kirk Cousins',21,QB,8,311,2331,62,18,(SELECT Player_ID FROM Player_season WHERE Name = 'Kirk Cousins' AND Anio = 2023),"1),"
(' Joe Burrow',7,QB,10,365,2309,64,15,(SELECT Player_ID FROM Player_season WHERE Name = 'Joe Burrow' AND Anio = 2023),"1),"
(' Zach Wilson',25,QB,12,368,2271,68,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Wilson' AND Anio = 2023),"1),"
(' Aidan O'Connell',17,QB,11,343,2218,50,12,(SELECT Player_ID FROM Player_season WHERE Name = 'Aidan O'Connell' AND Anio = 2023),"1),"
(' Mac Jones',22,QB,11,345,2120,58,10,(SELECT Player_ID FROM Player_season WHERE Name = 'Mac Jones' AND Anio = 2023),"1),"
(' Kenny Pickett',27,QB,12,324,2070,72,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenny Pickett' AND Anio = 2023),"1),"
(' Jake Browning',7,QB,9,243,1936,80,12,(SELECT Player_ID FROM Player_season WHERE Name = 'Jake Browning' AND Anio = 2023),"1),"
(' Will Levis',31,QB,9,255,1808,61,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Will Levis' AND Anio = 2023),"1),"
(' Kyler Murray',1,QB,8,268,1799,48,10,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyler Murray' AND Anio = 2023),"1),"
(' Joe Flacco',8,QB,5,204,1616,75,13,(SELECT Player_ID FROM Player_season WHERE Name = 'Joe Flacco' AND Anio = 2023),"1),"
(' Ryan Tannehill',31,QB,10,230,1616,70,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Tannehill' AND Anio = 2023),"1),"
(' Tyrod Taylor',24,QB,11,180,1341,80,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyrod Taylor' AND Anio = 2023),"1),"
(' Nick Mullens',21,QB,5,148,1306,47,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Mullens' AND Anio = 2023),"1),"
(' Bailey Zappe',22,QB,10,212,1272,48,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Bailey Zappe' AND Anio = 2023),"1),"
(' Jimmy Garoppolo',17,QB,7,169,1205,32,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Jimmy Garoppolo' AND Anio = 2023),"1),"
(' Easton Stick',18,QB,5,174,1129,79,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Easton Stick' AND Anio = 2023),"1),"
(' Deshaun Watson',8,QB,6,171,1115,59,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Deshaun Watson' AND Anio = 2023),"1),"
(' Tommy DeVito',24,QB,9,178,1101,41,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Tommy DeVito' AND Anio = 2023),"1),"
(' Daniel Jones',24,QB,6,160,909,58,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Daniel Jones' AND Anio = 2023),"1),"
(' Taylor Heinicke',2,QB,5,136,890,75,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Taylor Heinicke' AND Anio = 2023),"1),"
(' Tyson Bagent',6,QB,5,143,859,41,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyson Bagent' AND Anio = 2023),"1),"
(' Trevor Siemian',25,QB,5,153,724,30,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Trevor Siemian' AND Anio = 2023),"1),"
(' Mason Rudolph',27,QB,4,74,719,86,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Mason Rudolph' AND Anio = 2023),"1),"
(' PJ Walker',8,QB,6,111,674,58,1,(SELECT Player_ID FROM Player_season WHERE Name = 'PJ Walker' AND Anio = 2023),"1),"
(' Mitchell Trubisky',27,QB,5,107,632,26,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Mitchell Trubisky' AND Anio = 2023),"1),"
(' Anthony Richardson',14,QB,4,84,577,39,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Anthony Richardson' AND Anio = 2023),"1),"
(' Drew Lock',29,QB,4,76,543,51,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Drew Lock' AND Anio = 2023),"1),"
(' Jarrett Stidham',10,QB,3,66,496,54,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jarrett Stidham' AND Anio = 2023),"1),"
(' Dorian Thompson-Robinson',8,QB,8,112,440,23,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Dorian Thompson-Robinson' AND Anio = 2023),"1),"
(' Andy Dalton',5,QB,3,58,361,47,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Andy Dalton' AND Anio = 2023),"1),"
(' Tim Boyle',25,QB,3,77,360,36,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tim Boyle' AND Anio = 2023),"1),"
(' C.J. Beathard',15,QB,7,53,349,48,1,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Beathard' AND Anio = 2023),"1),"
(' Sam Darnold',28,QB,10,46,297,48,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Sam Darnold' AND Anio = 2023),"1),"
(' Case Keenum',13,QB,2,53,291,41,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Case Keenum' AND Anio = 2023),"1),"
(' Jameis Winston',23,QB,7,47,264,30,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jameis Winston' AND Anio = 2023),"1),"
(' Brian Hoyer',17,QB,3,42,231,48,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brian Hoyer' AND Anio = 2023),"1),"
(' Jacoby Brissett',32,QB,3,23,224,48,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Jacoby Brissett' AND Anio = 2023),"1),"
(' Tyler Huntley',3,QB,5,37,203,27,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Huntley' AND Anio = 2023),"1),"
(' Blaine Gabbert',16,QB,2,35,185,37,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Blaine Gabbert' AND Anio = 2023),"1),"
(' Davis Mills',13,QB,6,39,173,19,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Davis Mills' AND Anio = 2023),"1),"
(' Brett Rypien',19,QB,2,38,172,34,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brett Rypien' AND Anio = 2023),"1),"
(' Jaren Hall',21,QB,3,20,168,47,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaren Hall' AND Anio = 2023),"1),"
(' Jeff Driskel',8,QB,1,26,166,31,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeff Driskel' AND Anio = 2023),"1),"
(' Marcus Mariota',26,QB,3,23,164,22,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Marcus Mariota' AND Anio = 2023),"1),"
(' Carson Wentz',19,QB,2,24,163,29,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Carson Wentz' AND Anio = 2023),"1),"
(' Cooper Rush',9,QB,7,24,144,29,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cooper Rush' AND Anio = 2023),"1),"
(' Taysom Hill',23,QB,16,11,83,44,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Taysom Hill' AND Anio = 2023),"1),"
(' Mike White',20,QB,6,6,74,68,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike White' AND Anio = 2023),"1),"
(' Malik Willis',31,QB,3,5,74,48,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Malik Willis' AND Anio = 2023),"1),"
(' Clayton Tune',1,QB,7,21,62,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Clayton Tune' AND Anio = 2023),"1),"
(' Keenan Allen',18,WR,13,2,49,49,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Keenan Allen' AND Anio = 2023),"1),"
(' Sean Clifford',12,QB,2,1,37,37,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Sean Clifford' AND Anio = 2023),"1),"
(' Jalen Reeves-Maybin',11,LB,17,1,31,31,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Reeves-Maybin' AND Anio = 2023),"1),"
(' Braden Mann',26,P,15,1,28,28,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Braden Mann' AND Anio = 2023),"1),"
(' Logan Woodside',2,QB,1,4,27,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Logan Woodside' AND Anio = 2023),"1),"
(' Drake London',2,WR,16,1,22,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Drake London' AND Anio = 2023),"1),"
(' AJ McCarron',7,QB,2,5,19,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'AJ McCarron' AND Anio = 2023),"1),"
(' Thomas Morstead',25,P,17,1,18,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Thomas Morstead' AND Anio = 2023),"1),"
(' Kenneth Gainwell',26,RB,16,1,17,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenneth Gainwell' AND Anio = 2023),"1),"
(' Derrick Henry',31,RB,17,3,14,12,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Derrick Henry' AND Anio = 2023),"1),"
(' Dontayvion Wicks',12,WR,15,1,14,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dontayvion Wicks' AND Anio = 2023),"1),"
(' Logan Cooke',15,P,17,1,13,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Logan Cooke' AND Anio = 2023),"1),"
(' Jakobi Meyers',17,WR,16,3,12,9,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jakobi Meyers' AND Anio = 2023),"1),"
(' Tommy Townsend',16,P,17,1,11,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tommy Townsend' AND Anio = 2023),"1),"
(' Johnny Hekker',5,P,17,1,7,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Johnny Hekker' AND Anio = 2023),"1),"
(' Devin Singletary',13,RB,17,1,6,6,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Devin Singletary' AND Anio = 2023),"1),"
(' Jerick McKinnon',16,RB,12,1,4,4,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jerick McKinnon' AND Anio = 2023),"1),"
(' Dyami Brown',32,WR,17,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dyami Brown' AND Anio = 2023),"1),"
(' Aaron Rodgers',25,QB,1,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Aaron Rodgers' AND Anio = 2023),"1),"
(' DeAndre Hopkins',31,WR,17,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DeAndre Hopkins' AND Anio = 2023),"1),"
(' Nathan Peterman',6,QB,2,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nathan Peterman' AND Anio = 2023),"1),"
(' Tyler Boyd',7,WR,17,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Boyd' AND Anio = 2023),"1),"
(' Tanner Hudson',7,TE,12,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tanner Hudson' AND Anio = 2023),"1),"
(' Jonnu Smith',2,TE,17,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonnu Smith' AND Anio = 2023),"1),"
(' Chris Godwin',30,WR,17,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Godwin' AND Anio = 2023),"1),"
(' Parris Campbell',24,WR,12,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Parris Campbell' AND Anio = 2023),"1),"
(' Deebo Samuel',28,WR,15,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Deebo Samuel' AND Anio = 2023),"1),"
(' Kyle Trask',30,QB,2,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Trask' AND Anio = 2023),"1),"
(' Cedrick Wilson',20,WR,15,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cedrick Wilson' AND Anio = 2023),"1),"
(' Josh Jacobs',17,RB,13,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Jacobs' AND Anio = 2023),"1),"
(' Cam Akers',21,RB,7,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cam Akers' AND Anio = 2023),"1),"
(' Malik Cunningham',22,WR,2,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Malik Cunningham' AND Anio = 2023),"1),"
(' Kadarius Toney',16,WR,13,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kadarius Toney' AND Anio = 2023),"1),"
(' DeeJay Dallas',29,RB,17,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DeeJay Dallas' AND Anio = 2023),"1),"
(' Connor Heyward',27,TE,17,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Connor Heyward' AND Anio = 2023),"1),"
(' Justin Jefferson',21,WR,10,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Jefferson' AND Anio = 2023),"1),"
(' Tank Dell',13,WR,11,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tank Dell' AND Anio = 2023),"1),"
(' Amon-Ra St. Brown',11,WR,16,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Amon-Ra St. Brown' AND Anio = 2023),"1),"
(' De'Von Achane',20,RB,11,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'De'Von Achane' AND Anio = 2023),"1),"
(' Garrett Wilson',25,WR,17,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Garrett Wilson' AND Anio = 2023),"1),"
(' Christian Kirk',15,WR,12,2,-1,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian Kirk' AND Anio = 2023),"1),"
(' Ja'Marr Chase',7,WR,16,1,-7,-7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ja'Marr Chase' AND Anio = 2023),"1),"
(' Tyreek Hill ',20,WR,16,119,1799,78,13,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyreek Hill ' AND Anio = 2023),"3),"
(' CeeDee Lamb ',9,WR,17,135,1749,92,12,(SELECT Player_ID FROM Player_season WHERE Name = 'CeeDee Lamb ' AND Anio = 2023),"3),"
(' Amon-Ra St. Brown',11,WR,16,119,1515,70,10,(SELECT Player_ID FROM Player_season WHERE Name = 'Amon-Ra St. Brown' AND Anio = 2023),"3),"
(' Puka Nacua ',19,WR,17,105,1486,80,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Puka Nacua ' AND Anio = 2023),"3),"
(' A.J. Brown ',26,WR,17,106,1456,59,7,(SELECT Player_ID FROM Player_season WHERE Name = 'A.J. Brown ' AND Anio = 2023),"3),"
(' DJ Moore ',6,WR,17,96,1364,58,8,(SELECT Player_ID FROM Player_season WHERE Name = 'DJ Moore ' AND Anio = 2023),"3),"
(' Brandon Aiyuk ',28,WR,16,75,1342,76,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Aiyuk ' AND Anio = 2023),"3),"
(' Nico Collins ',13,WR,15,80,1297,75,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Nico Collins ' AND Anio = 2023),"3),"
(' Mike Evans ',30,WR,17,79,1255,75,13,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Evans ' AND Anio = 2023),"3),"
(' Amari Cooper ',8,WR,15,72,1250,75,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Amari Cooper ' AND Anio = 2023),"3),"
(' Keenan Allen ',18,WR,13,108,1243,42,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Keenan Allen ' AND Anio = 2023),"3),"
(' Ja'Marr Chase ',7,WR,16,100,1216,76,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Ja'Marr Chase ' AND Anio = 2023),"3),"
(' Stefon Diggs ',4,WR,17,107,1183,55,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Stefon Diggs ' AND Anio = 2023),"3),"
(' Michael Pittman Jr.',14,WR,16,109,1152,75,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Pittman Jr.' AND Anio = 2023),"3),"
(' Davante Adams ',17,WR,17,103,1144,46,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Davante Adams ' AND Anio = 2023),"3),"
(' George Pickens ',27,WR,17,63,1140,86,5,(SELECT Player_ID FROM Player_season WHERE Name = 'George Pickens ' AND Anio = 2023),"3),"
(' Chris Olave ',23,WR,16,87,1123,51,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Olave ' AND Anio = 2023),"3),"
(' DK Metcalf ',29,WR,16,66,1114,73,8,(SELECT Player_ID FROM Player_season WHERE Name = 'DK Metcalf ' AND Anio = 2023),"3),"
(' Justin Jefferson ',21,WR,10,68,1074,52,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Jefferson ' AND Anio = 2023),"3),"
(' DeVonta Smith ',26,WR,16,81,1066,63,7,(SELECT Player_ID FROM Player_season WHERE Name = 'DeVonta Smith ' AND Anio = 2023),"3),"
(' DeAndre Hopkins ',31,WR,17,75,1057,61,7,(SELECT Player_ID FROM Player_season WHERE Name = 'DeAndre Hopkins ' AND Anio = 2023),"3),"
(' Garrett Wilson ',25,WR,17,95,1042,68,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Garrett Wilson ' AND Anio = 2023),"3),"
(' Chris Godwin ',30,WR,17,83,1024,47,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Godwin ' AND Anio = 2023),"3),"
(' George Kittle ',28,TE,16,65,1020,66,6,(SELECT Player_ID FROM Player_season WHERE Name = 'George Kittle ' AND Anio = 2023),"3),"
(' Calvin Ridley ',15,WR,17,76,1016,59,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Calvin Ridley ' AND Anio = 2023),"3),"
(' Adam Thielen ',5,WR,17,103,1014,32,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Adam Thielen ' AND Anio = 2023),"3),"
(' Jaylen Waddle ',20,WR,14,72,1014,60,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaylen Waddle ' AND Anio = 2023),"3),"
(' Terry McLaurin ',32,WR,17,79,1002,48,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Terry McLaurin ' AND Anio = 2023),"3),"
(' Travis Kelce ',16,TE,15,93,984,53,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Travis Kelce ' AND Anio = 2023),"3),"
(' Evan Engram ',15,TE,17,114,963,34,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Evan Engram ' AND Anio = 2023),"3),"
(' T.J. Hockenson ',21,TE,15,95,960,29,5,(SELECT Player_ID FROM Player_season WHERE Name = 'T.J. Hockenson ' AND Anio = 2023),"3),"
(' Rashee Rice ',16,WR,16,79,938,67,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Rashee Rice ' AND Anio = 2023),"3),"
(' Jordan Addison ',21,WR,17,70,911,62,10,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Addison ' AND Anio = 2023),"3),"
(' Drake London ',2,WR,16,69,905,45,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Drake London ' AND Anio = 2023),"3),"
(' Tyler Lockett ',29,WR,17,79,894,37,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Lockett ' AND Anio = 2023),"3),"
(' Deebo Samuel ',28,WR,15,60,892,54,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Deebo Samuel ' AND Anio = 2023),"3),"
(' Sam LaPorta ',11,TE,17,86,889,48,10,(SELECT Player_ID FROM Player_season WHERE Name = 'Sam LaPorta ' AND Anio = 2023),"3),"
(' David Njoku ',8,TE,16,81,882,43,6,(SELECT Player_ID FROM Player_season WHERE Name = 'David Njoku ' AND Anio = 2023),"3),"
(' Zay Flowers ',3,WR,16,77,858,75,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Zay Flowers ' AND Anio = 2023),"3),"
(' Trey McBride ',1,TE,17,81,825,38,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Trey McBride ' AND Anio = 2023),"3),"
(' Jakobi Meyers ',17,WR,16,71,807,33,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Jakobi Meyers ' AND Anio = 2023),"3),"
(' Jayden Reed ',12,WR,16,64,793,59,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Jayden Reed ' AND Anio = 2023),"3),"
(' Christian Kirk ',15,WR,12,57,787,57,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian Kirk ' AND Anio = 2023),"3),"
(' Courtland Sutton ',10,WR,16,59,772,46,10,(SELECT Player_ID FROM Player_season WHERE Name = 'Courtland Sutton ' AND Anio = 2023),"3),"
(' Josh Downs ',14,WR,17,68,771,59,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Downs ' AND Anio = 2023),"3),"
(' Darius Slayton ',24,WR,17,50,770,80,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Darius Slayton ' AND Anio = 2023),"3),"
(' Jake Ferguson ',9,TE,17,71,761,40,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Jake Ferguson ' AND Anio = 2023),"3),"
(' Jerry Jeudy ',10,WR,16,54,758,47,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jerry Jeudy ' AND Anio = 2023),"3),"
(' Gabe Davis ',4,WR,17,45,746,57,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Gabe Davis ' AND Anio = 2023),"3),"
(' Cooper Kupp ',19,WR,12,59,737,62,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Cooper Kupp ' AND Anio = 2023),"3),"
(' Rashid Shaheed ',23,WR,15,46,719,58,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Rashid Shaheed ' AND Anio = 2023),"3),"
(' Cole Kmet ',6,TE,17,73,719,53,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Cole Kmet ' AND Anio = 2023),"3),"
(' Diontae Johnson ',27,WR,14,51,717,71,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Diontae Johnson ' AND Anio = 2023),"3),"
(' Tank Dell ',13,WR,11,47,709,68,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Tank Dell ' AND Anio = 2023),"3),"
(' Romeo Doubs ',12,WR,17,59,674,36,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Romeo Doubs ' AND Anio = 2023),"3),"
(' Dalton Kincaid ',4,TE,16,73,673,51,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Dalton Kincaid ' AND Anio = 2023),"3),"
(' Tyler Boyd ',7,WR,17,67,667,64,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Boyd ' AND Anio = 2023),"3),"
(' Kyle Pitts ',2,TE,17,53,667,39,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Pitts ' AND Anio = 2023),"3),"
(' Brandin Cooks ',9,WR,16,54,657,37,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandin Cooks ' AND Anio = 2023),"3),"
(' Tee Higgins ',7,WR,12,42,656,80,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Tee Higgins ' AND Anio = 2023),"3),"
(' Elijah Moore ',8,WR,17,59,640,42,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Elijah Moore ' AND Anio = 2023),"3),"
(' Dalton Schultz ',13,TE,15,59,635,31,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Dalton Schultz ' AND Anio = 2023),"3),"
(' Jaxon Smith-Njigba ',29,WR,17,63,628,35,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaxon Smith-Njigba ' AND Anio = 2023),"3),"
(' Tyler Conklin ',25,TE,17,61,621,37,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Conklin ' AND Anio = 2023),"3),"
(' Curtis Samuel ',32,WR,16,62,613,37,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Curtis Samuel ' AND Anio = 2023),"3),"
(' Khalil Shakir ',4,WR,17,39,611,81,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Khalil Shakir ' AND Anio = 2023),"3),"
(' Josh Reynolds ',11,WR,17,40,608,33,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Reynolds ' AND Anio = 2023),"3),"
(' Dallas Goedert ',26,TE,14,59,592,49,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Dallas Goedert ' AND Anio = 2023),"3),"
(' Breece Hall ',25,RB,17,76,591,50,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Breece Hall ' AND Anio = 2023),"3),"
(' Jonnu Smith ',2,TE,17,50,582,60,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonnu Smith ' AND Anio = 2023),"3),"
(' Joshua Palmer ',18,WR,11,38,581,79,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Joshua Palmer ' AND Anio = 2023),"3),"
(' Dontayvion Wicks ',12,WR,15,39,581,35,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Dontayvion Wicks ' AND Anio = 2023),"3),"
(' Marquise Brown ',1,WR,14,51,574,41,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Marquise Brown ' AND Anio = 2023),"3),"
(' Noah Brown ',13,WR,10,33,567,75,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Noah Brown ' AND Anio = 2023),"3),"
(' Odell Beckham Jr.',3,WR,14,35,565,51,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Odell Beckham Jr.' AND Anio = 2023),"3),"
(' Michael Wilson ',1,WR,13,38,565,69,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Wilson ' AND Anio = 2023),"3),"
(' Christian McCaffrey ',28,RB,16,67,564,41,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian McCaffrey ' AND Anio = 2023),"3),"
(' DeMario Douglas ',22,WR,14,49,561,42,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DeMario Douglas ' AND Anio = 2023),"3),"
(' Darren Waller ',24,TE,12,52,552,29,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Darren Waller ' AND Anio = 2023),"3),"
(' Rachaad White ',30,RB,17,64,549,43,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Rachaad White ' AND Anio = 2023),"3),"
(' Mark Andrews ',3,TE,10,45,544,38,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Mark Andrews ' AND Anio = 2023),"3),"
(' K.J. Osborn ',21,WR,16,48,540,47,3,(SELECT Player_ID FROM Player_season WHERE Name = 'K.J. Osborn ' AND Anio = 2023),"3),"
(' Chigoziem Okonkwo ',31,TE,17,54,528,39,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Chigoziem Okonkwo ' AND Anio = 2023),"3),"
(' DJ Chark Jr.',5,WR,15,35,525,47,5,(SELECT Player_ID FROM Player_season WHERE Name = 'DJ Chark Jr.' AND Anio = 2023),"3),"
(' Wan'Dale Robinson ',24,WR,15,60,525,33,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Wan'Dale Robinson ' AND Anio = 2023),"3),"
(' Jahan Dotson ',32,WR,17,49,518,33,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Jahan Dotson ' AND Anio = 2023),"3),"
(' Alec Pierce ',14,WR,17,32,514,58,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Alec Pierce ' AND Anio = 2023),"3),"
(' Logan Thomas ',32,TE,16,55,496,29,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Logan Thomas ' AND Anio = 2023),"3),"
(' Tyler Higbee ',19,TE,15,47,495,33,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Higbee ' AND Anio = 2023),"3),"
(' Kalif Raymond ',11,WR,17,35,489,41,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kalif Raymond ' AND Anio = 2023),"3),"
(' Bijan Robinson ',2,RB,17,58,487,71,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Bijan Robinson ' AND Anio = 2023),"3),"
(' Tutu Atwell ',19,WR,16,39,483,44,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Tutu Atwell ' AND Anio = 2023),"3),"
(' Travis Etienne Jr.',15,RB,17,58,476,56,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Travis Etienne Jr.' AND Anio = 2023),"3),"
(' Alvin Kamara ',23,RB,13,75,466,25,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Alvin Kamara ' AND Anio = 2023),"3),"
(' Justin Watson ',16,WR,16,27,460,41,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Watson ' AND Anio = 2023),"3),"
(' Samaje Perine ',10,RB,17,50,455,29,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Samaje Perine ' AND Anio = 2023),"3),"
(' Cade Otton ',30,TE,17,47,455,27,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Cade Otton ' AND Anio = 2023),"3),"
(' Michael Thomas ',23,WR,10,39,448,31,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Thomas ' AND Anio = 2023),"3),"
(' James Cook ',4,RB,17,44,445,48,4,(SELECT Player_ID FROM Player_season WHERE Name = 'James Cook ' AND Anio = 2023),"3),"
(' Austin Ekeler ',18,RB,14,51,436,39,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Austin Ekeler ' AND Anio = 2023),"3),"
(' Quentin Johnston ',18,WR,17,38,431,57,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Quentin Johnston ' AND Anio = 2023),"3),"
(' Robert Woods ',13,WR,14,40,426,26,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Robert Woods ' AND Anio = 2023),"3),"
(' Chris Moore ',31,WR,17,22,424,49,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Moore ' AND Anio = 2023),"3),"
(' Christian Watson ',12,WR,9,28,422,77,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian Watson ' AND Anio = 2023),"3),"
(' Hunter Henry ',22,TE,14,42,419,24,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Hunter Henry ' AND Anio = 2023),"3),"
(' Michael Gallup ',9,WR,17,34,418,41,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Gallup ' AND Anio = 2023),"3),"
(' Jonathan Mingo ',5,WR,15,43,418,40,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonathan Mingo ' AND Anio = 2023),"3),"
(' Noah Fant ',29,TE,17,32,414,51,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Noah Fant ' AND Anio = 2023),"3),"
(' Darnell Mooney ',6,WR,15,31,414,41,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Darnell Mooney ' AND Anio = 2023),"3),"
(' Gerald Everett ',18,TE,15,51,411,31,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Gerald Everett ' AND Anio = 2023),"3),"
(' Isaiah Likely ',3,TE,17,30,411,54,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Isaiah Likely ' AND Anio = 2023),"3),"
(' Kendrick Bourne ',22,WR,8,37,406,36,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Kendrick Bourne ' AND Anio = 2023),"3),"
(' DeVante Parker ',22,WR,13,33,394,30,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DeVante Parker ' AND Anio = 2023),"3),"
(' Antonio Gibson ',32,RB,16,48,389,41,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Antonio Gibson ' AND Anio = 2023),"3),"
(' Trey Palmer ',30,WR,17,39,385,54,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Trey Palmer ' AND Anio = 2023),"3),"
(' Tyjae Spears ',31,RB,17,52,385,48,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyjae Spears ' AND Anio = 2023),"3),"
(' Nelson Agholor ',3,WR,17,35,381,37,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Nelson Agholor ' AND Anio = 2023),"3),"
(' Marvin Mims Jr.',10,WR,16,22,377,60,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Marvin Mims Jr.' AND Anio = 2023),"3),"
(' Joe Mixon ',7,RB,17,52,376,45,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Joe Mixon ' AND Anio = 2023),"3),"
(' Jalin Hyatt ',24,WR,17,23,373,58,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalin Hyatt ' AND Anio = 2023),"3),"
(' Demarcus Robinson ',19,WR,16,26,371,37,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Demarcus Robinson ' AND Anio = 2023),"3),"
(' Nick Westbrook-Ikhine ',31,WR,14,28,370,33,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Westbrook-Ikhine ' AND Anio = 2023),"3),"
(' Jaylen Warren ',27,RB,17,61,370,30,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaylen Warren ' AND Anio = 2023),"3),"
(' Juwan Johnson ',23,TE,13,37,368,32,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Juwan Johnson ' AND Anio = 2023),"3),"
(' Kylen Granson ',14,TE,15,30,368,46,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kylen Granson ' AND Anio = 2023),"3),"
(' Brian Robinson Jr.',32,RB,15,36,368,51,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Brian Robinson Jr.' AND Anio = 2023),"3),"
(' Rashod Bateman ',3,WR,16,32,367,29,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Rashod Bateman ' AND Anio = 2023),"3),"
(' Durham Smythe ',20,TE,16,35,366,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Durham Smythe ' AND Anio = 2023),"3),"
(' Tucker Kraft ',12,TE,17,31,355,43,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Tucker Kraft ' AND Anio = 2023),"3),"
(' Jameson Williams ',11,WR,12,24,354,63,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jameson Williams ' AND Anio = 2023),"3),"
(' Tanner Hudson ',7,TE,12,39,352,26,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tanner Hudson ' AND Anio = 2023),"3),"
(' Rondale Moore ',1,WR,17,40,352,48,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Rondale Moore ' AND Anio = 2023),"3),"
(' Luke Musgrave ',12,TE,11,34,352,37,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Luke Musgrave ' AND Anio = 2023),"3),"
(' Tre Tucker ',17,WR,16,19,331,50,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Tre Tucker ' AND Anio = 2023),"3),"
(' Brandon Powell ',21,WR,17,29,324,28,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Powell ' AND Anio = 2023),"3),"
(' Zay Jones ',15,WR,9,34,321,36,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Zay Jones ' AND Anio = 2023),"3),"
(' Jerome Ford ',8,RB,17,44,319,50,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Jerome Ford ' AND Anio = 2023),"3),"
(' Trenton Irwin ',7,WR,16,25,316,32,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Trenton Irwin ' AND Anio = 2023),"3),"
(' Jahmyr Gibbs ',11,RB,15,52,316,24,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jahmyr Gibbs ' AND Anio = 2023),"3),"
(' Marquez Valdes-Scantling ',16,WR,16,21,315,46,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Marquez Valdes-Scantling ' AND Anio = 2023),"3),"
(' Ezekiel Elliott ',22,RB,17,51,313,23,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Ezekiel Elliott ' AND Anio = 2023),"3),"
(' Allen Lazard ',25,WR,14,23,311,39,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Allen Lazard ' AND Anio = 2023),"3),"
(' Tony Pollard ',9,RB,17,55,311,60,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tony Pollard ' AND Anio = 2023),"3),"
(' Pat Freiermuth ',27,TE,12,32,308,29,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Pat Freiermuth ' AND Anio = 2023),"3),"
(' Noah Gray ',16,TE,17,28,305,34,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Noah Gray ' AND Anio = 2023),"3),"
(' Michael Mayer ',17,TE,14,27,304,32,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Mayer ' AND Anio = 2023),"3),"
(' Cedrick Wilson Jr.',20,WR,15,22,296,31,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Cedrick Wilson Jr.' AND Anio = 2023),"3),"
(' Josh Jacobs ',17,RB,13,37,296,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Jacobs ' AND Anio = 2023),"3),"
(' Taysom Hill ',23,QB,16,33,291,36,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Taysom Hill ' AND Anio = 2023),"3),"
(' Donald Parham Jr.',18,TE,14,27,285,24,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Donald Parham Jr.' AND Anio = 2023),"3),"
(' Brandon Johnson ',10,WR,13,19,284,50,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Johnson ' AND Anio = 2023),"3),"
(' Allen Robinson II',27,WR,17,34,280,31,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Allen Robinson II' AND Anio = 2023),"3),"
(' Saquon Barkley ',24,RB,14,41,280,46,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Saquon Barkley ' AND Anio = 2023),"3),"
(' Greg Dortch ',1,WR,16,24,280,38,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Greg Dortch ' AND Anio = 2023),"3),"
(' Jalen Tolbert ',9,WR,17,22,268,45,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Tolbert ' AND Anio = 2023),"3),"
(' Jauan Jennings ',28,WR,13,19,265,31,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jauan Jennings ' AND Anio = 2023),"3),"
(' JuJu Smith-Schuster ',22,WR,11,29,260,37,1,(SELECT Player_ID FROM Player_season WHERE Name = 'JuJu Smith-Schuster ' AND Anio = 2023),"3),"
(' Kenneth Walker III',29,RB,15,29,259,64,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenneth Walker III' AND Anio = 2023),"3),"
(' Hunter Renfrow ',17,WR,17,25,255,38,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Hunter Renfrow ' AND Anio = 2023),"3),"
(' Daniel Bellinger ',24,TE,17,25,255,26,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Daniel Bellinger ' AND Anio = 2023),"3),"
(' Mack Hollins ',2,WR,13,18,251,45,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mack Hollins ' AND Anio = 2023),"3),"
(' Mike Williams ',18,WR,3,19,249,49,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Williams ' AND Anio = 2023),"3),"
(' Colby Parkinson ',29,TE,17,25,247,27,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Colby Parkinson ' AND Anio = 2023),"3),"
(' A.T. Perry ',23,WR,10,12,246,44,4,(SELECT Player_ID FROM Player_season WHERE Name = 'A.T. Perry ' AND Anio = 2023),"3),"
(' Mike Gesicki ',22,TE,17,29,244,18,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Gesicki ' AND Anio = 2023),"3),"
(' Isiah Pacheco ',16,RB,14,44,244,33,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Isiah Pacheco ' AND Anio = 2023),"3),"
(' Skyy Moore ',16,WR,14,21,244,54,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Skyy Moore ' AND Anio = 2023),"3),"
(' Braxton Berrios ',20,WR,16,27,238,22,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Braxton Berrios ' AND Anio = 2023),"3),"
(' Rhamondre Stevenson ',22,RB,12,38,238,34,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Rhamondre Stevenson ' AND Anio = 2023),"3),"
(' Austin Hooper ',17,TE,17,25,234,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Austin Hooper ' AND Anio = 2023),"3),"
(' Aaron Jones ',12,RB,11,30,233,51,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Aaron Jones ' AND Anio = 2023),"3),"
(' Chuba Hubbard ',5,RB,17,39,233,25,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chuba Hubbard ' AND Anio = 2023),"3),"
(' Alex Erickson ',18,WR,8,16,232,27,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Alex Erickson ' AND Anio = 2023),"3),"
(' KhaDarel Hodge ',2,WR,17,14,232,52,0,(SELECT Player_ID FROM Player_season WHERE Name = 'KhaDarel Hodge ' AND Anio = 2023),"3),"
(' Isaiah Hodgins ',24,WR,17,21,230,24,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Isaiah Hodgins ' AND Anio = 2023),"3),"
(' Xavier Gipson ',25,WR,17,21,229,36,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Xavier Gipson ' AND Anio = 2023),"3),"
(' Javonte Williams ',10,RB,16,47,228,18,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Javonte Williams ' AND Anio = 2023),"3),"
(' Jamal Agnew ',15,WR,11,14,225,65,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamal Agnew ' AND Anio = 2023),"3),"
(' Cedric Tillman ',8,WR,14,21,224,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cedric Tillman ' AND Anio = 2023),"3),"
(' AJ Dillon ',12,RB,15,22,223,35,0,(SELECT Player_ID FROM Player_season WHERE Name = 'AJ Dillon ' AND Anio = 2023),"3),"
(' Treylon Burks ',31,WR,11,16,221,70,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Treylon Burks ' AND Anio = 2023),"3),"
(' Brevin Jordan ',13,TE,14,17,219,27,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Brevin Jordan ' AND Anio = 2023),"3),"
(' Bo Melton ',12,WR,5,16,218,37,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Bo Melton ' AND Anio = 2023),"3),"
(' Derrick Henry ',31,RB,17,28,214,46,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Derrick Henry ' AND Anio = 2023),"3),"
(' D'Andre Swift ',26,RB,16,39,214,20,1,(SELECT Player_ID FROM Player_season WHERE Name = 'D'Andre Swift ' AND Anio = 2023),"3),"
(' Josh Oliver ',21,TE,17,22,213,33,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Oliver ' AND Anio = 2023),"3),"
(' Van Jefferson ',19,WR,17,20,209,46,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Van Jefferson ' AND Anio = 2023),"3),"
(' Zach Charbonnet ',29,RB,16,33,209,39,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Charbonnet ' AND Anio = 2023),"3),"
(' Roschon Johnson ',6,RB,15,34,209,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Roschon Johnson ' AND Anio = 2023),"3),"
(' Pharaoh Brown ',22,TE,17,13,208,58,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Pharaoh Brown ' AND Anio = 2023),"3),"
(' Will Mallory ',14,TE,12,18,207,43,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Will Mallory ' AND Anio = 2023),"3),"
(' Justice Hill ',3,RB,16,28,206,24,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Justice Hill ' AND Anio = 2023),"3),"
(' Kyren Williams ',19,RB,12,32,206,24,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyren Williams ' AND Anio = 2023),"3),"
(' Adam Trautman ',10,TE,17,22,204,24,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Adam Trautman ' AND Anio = 2023),"3),"
(' De'Von Achane ',20,RB,11,27,197,23,3,(SELECT Player_ID FROM Player_season WHERE Name = 'De'Von Achane ' AND Anio = 2023),"3),"
(' Jake Bobo ',29,WR,17,19,196,31,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jake Bobo ' AND Anio = 2023),"3),"
(' Tommy Tremble ',5,TE,16,23,194,30,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Tommy Tremble ' AND Anio = 2023),"3),"
(' Foster Moreau ',23,TE,15,21,193,23,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Foster Moreau ' AND Anio = 2023),"3),"
(' Devin Singletary ',13,RB,17,30,193,41,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Devin Singletary ' AND Anio = 2023),"3),"
(' Tyler Allgeier ',2,RB,17,18,193,75,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Allgeier ' AND Anio = 2023),"3),"
(' Jerick McKinnon ',16,RB,12,25,192,27,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Jerick McKinnon ' AND Anio = 2023),"3),"
(' Zack Moss ',14,RB,14,27,192,26,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Zack Moss ' AND Anio = 2023),"3),"
(' Alexander Mattison ',21,RB,16,30,192,47,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Alexander Mattison ' AND Anio = 2023),"3),"
(' Clyde Edwards-Helaire ',16,RB,15,17,188,48,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Clyde Edwards-Helaire ' AND Anio = 2023),"3),"
(' Zach Ertz ',1,TE,7,27,187,17,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Ertz ' AND Anio = 2023),"3),"
(' Dawson Knox ',4,TE,13,22,186,17,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Dawson Knox ' AND Anio = 2023),"3),"
(' Hayden Hurst ',5,TE,9,18,184,48,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Hayden Hurst ' AND Anio = 2023),"3),"
(' Kenneth Gainwell ',26,RB,16,30,183,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenneth Gainwell ' AND Anio = 2023),"3),"
(' Kyle Philips ',31,WR,9,15,181,29,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Philips ' AND Anio = 2023),"3),"
(' Gus Edwards ',3,RB,17,12,180,80,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Gus Edwards ' AND Anio = 2023),"3),"
(' Calvin Austin III',27,WR,17,17,180,72,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Calvin Austin III' AND Anio = 2023),"3),"
(' Raheem Mostert ',20,RB,15,25,175,22,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Raheem Mostert ' AND Anio = 2023),"3),"
(' Johnny Mundt ',21,TE,17,17,172,32,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Johnny Mundt ' AND Anio = 2023),"3),"
(' Will Dissly ',29,TE,16,17,172,21,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Will Dissly ' AND Anio = 2023),"3),"
(' Najee Harris ',27,RB,17,29,170,32,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Najee Harris ' AND Anio = 2023),"3),"
(' Kadarius Toney ',16,WR,13,27,169,18,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kadarius Toney ' AND Anio = 2023),"3),"
(' Dyami Brown ',32,WR,17,12,168,35,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Dyami Brown ' AND Anio = 2023),"3),"
(' Tyler Scott ',6,WR,17,17,168,30,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Scott ' AND Anio = 2023),"3),"
(' Connor Heyward ',27,TE,17,23,167,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Connor Heyward ' AND Anio = 2023),"3),"
(' David Bell ',8,WR,15,14,167,41,3,(SELECT Player_ID FROM Player_season WHERE Name = 'David Bell ' AND Anio = 2023),"3),"
(' James Conner ',1,RB,13,27,165,34,2,(SELECT Player_ID FROM Player_season WHERE Name = 'James Conner ' AND Anio = 2023),"3),"
(' Olamide Zaccheaus ',26,WR,17,10,164,34,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Olamide Zaccheaus ' AND Anio = 2023),"3),"
(' Drew Sample ',7,TE,17,22,163,22,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Drew Sample ' AND Anio = 2023),"3),"
(' Elijah Higgins ',1,TE,11,14,163,26,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Elijah Higgins ' AND Anio = 2023),"3),"
(' Lil'Jordan Humphrey ',10,WR,17,13,162,54,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Lil'Jordan Humphrey ' AND Anio = 2023),"3),"
(' Mo Alie-Cox ',14,TE,17,13,161,35,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Mo Alie-Cox ' AND Anio = 2023),"3),"
(' Scotty Miller ',2,WR,17,11,161,56,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Scotty Miller ' AND Anio = 2023),"3),"
(' Byron Pringle ',32,WR,17,14,161,26,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Byron Pringle ' AND Anio = 2023),"3),"
(' Jaleel McLaughlin ',10,RB,17,31,160,22,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaleel McLaughlin ' AND Anio = 2023),"3),"
(' Jamison Crowder ',32,WR,17,16,159,26,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamison Crowder ' AND Anio = 2023),"3),"
(' Ty Chandler ',21,RB,17,21,159,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ty Chandler ' AND Anio = 2023),"3),"
(' John Metchie III',13,WR,16,16,158,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'John Metchie III' AND Anio = 2023),"3),"
(' Chase Brown ',7,RB,12,14,156,54,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Chase Brown ' AND Anio = 2023),"3),"
(' Luke Farrell ',15,TE,17,13,155,42,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Luke Farrell ' AND Anio = 2023),"3),"
(' Stone Smartt ',18,TE,16,11,155,51,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Stone Smartt ' AND Anio = 2023),"3),"
(' Donovan Peoples-Jones ',11,WR,15,13,155,29,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Donovan Peoples-Jones ' AND Anio = 2023),"3),"
(' Miles Sanders ',5,RB,16,27,154,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Miles Sanders ' AND Anio = 2023),"3),"
(' Jonathan Taylor ',14,RB,10,19,153,40,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonathan Taylor ' AND Anio = 2023),"3),"
(' John Bates ',32,TE,17,19,151,35,0,(SELECT Player_ID FROM Player_season WHERE Name = 'John Bates ' AND Anio = 2023),"3),"
(' Jeremy Ruckert ',25,TE,15,16,151,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeremy Ruckert ' AND Anio = 2023),"3),"
(' Deonte Harty ',4,WR,16,15,150,43,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Deonte Harty ' AND Anio = 2023),"3),"
(' Drew Ogletree ',14,TE,12,9,147,33,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Drew Ogletree ' AND Anio = 2023),"3),"
(' Rico Dowdle ',9,RB,16,17,144,32,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Rico Dowdle ' AND Anio = 2023),"3),"
(' Quez Watkins ',26,WR,9,15,142,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Quez Watkins ' AND Anio = 2023),"3),"
(' D'Ernest Johnson ',15,RB,17,10,140,42,0,(SELECT Player_ID FROM Player_season WHERE Name = 'D'Ernest Johnson ' AND Anio = 2023),"3),"
(' Terrace Marshall Jr.',5,WR,9,19,139,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Terrace Marshall Jr.' AND Anio = 2023),"3),"
(' Jalen Reagor ',22,WR,11,7,138,39,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Reagor ' AND Anio = 2023),"3),"
(' Ray-Ray McCloud III',28,WR,12,12,135,41,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ray-Ray McCloud III' AND Anio = 2023),"3),"
(' Khalil Herbert ',6,RB,12,20,134,23,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Khalil Herbert ' AND Anio = 2023),"3),"
(' Jordan Akins ',8,TE,17,15,132,28,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Akins ' AND Anio = 2023),"3),"
(' Parker Washington ',15,WR,9,16,132,19,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Parker Washington ' AND Anio = 2023),"3),"
(' Ameer Abdullah ',17,RB,17,19,131,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ameer Abdullah ' AND Anio = 2023),"3),"
(' KaVontae Turpin ',9,WR,16,12,127,34,3,(SELECT Player_ID FROM Player_season WHERE Name = 'KaVontae Turpin ' AND Anio = 2023),"3),"
(' Robbie Chosen ',20,WR,9,4,126,68,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Robbie Chosen ' AND Anio = 2023),"3),"
(' Stephen Sullivan ',5,TE,11,12,125,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Stephen Sullivan ' AND Anio = 2023),"3),"
(' Malik Heath ',12,WR,13,15,125,16,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Malik Heath ' AND Anio = 2023),"3),"
(' Mecole Hardman ',25,WR,11,15,124,37,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mecole Hardman ' AND Anio = 2023),"3),"
(' River Cracraft ',20,WR,10,9,121,24,1,(SELECT Player_ID FROM Player_season WHERE Name = 'River Cracraft ' AND Anio = 2023),"3),"
(' Cole Turner ',32,TE,12,11,120,29,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cole Turner ' AND Anio = 2023),"3),"
(' Latavius Murray ',4,RB,16,17,119,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Latavius Murray ' AND Anio = 2023),"3),"
(' Kyle Juszczyk ',28,FB,17,14,119,22,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Juszczyk ' AND Anio = 2023),"3),"
(' Alec Ingold ',20,FB,17,13,119,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Alec Ingold ' AND Anio = 2023),"3),"
(' Emari Demercado ',1,RB,14,21,119,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Emari Demercado ' AND Anio = 2023),"3),"
(' David Montgomery ',11,RB,14,16,117,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'David Montgomery ' AND Anio = 2023),"3),"
(' Kendre Miller ',23,RB,8,10,117,33,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kendre Miller ' AND Anio = 2023),"3),"
(' Andrei Iosivas ',7,WR,16,15,116,16,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Andrei Iosivas ' AND Anio = 2023),"3),"
(' Irv Smith Jr.',7,TE,12,18,115,14,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Irv Smith Jr.' AND Anio = 2023),"3),"
(' Richie James ',16,WR,9,10,114,45,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Richie James ' AND Anio = 2023),"3),"
(' Robert Tonyan ',6,TE,17,11,112,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Robert Tonyan ' AND Anio = 2023),"3),"
(' MyCole Pruitt ',2,TE,17,9,110,22,1,(SELECT Player_ID FROM Player_season WHERE Name = 'MyCole Pruitt ' AND Anio = 2023),"3),"
(' Parris Campbell ',24,WR,12,20,104,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Parris Campbell ' AND Anio = 2023),"3),"
(' Darrell Henderson Jr.',19,RB,4,10,103,32,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Darrell Henderson Jr.' AND Anio = 2023),"3),"
(' Michael Carter ',25,RB,15,24,101,10,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Carter ' AND Anio = 2023),"3),"
(' Dameon Pierce ',13,RB,14,13,101,27,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dameon Pierce ' AND Anio = 2023),"3),"
(' Zamir White ',17,RB,17,15,98,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Zamir White ' AND Anio = 2023),"3),"
(' Lucas Krull ',10,TE,7,8,95,35,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Lucas Krull ' AND Anio = 2023),"3),"
(' Davis Allen ',19,TE,15,10,95,21,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Davis Allen ' AND Anio = 2023),"3),"
(' Geoff Swaim ',1,TE,14,10,94,26,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Geoff Swaim ' AND Anio = 2023),"3),"
(' David Moore ',30,WR,7,5,94,52,1,(SELECT Player_ID FROM Player_season WHERE Name = 'David Moore ' AND Anio = 2023),"3),"
(' Josh Whyle ',31,TE,11,9,94,24,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Whyle ' AND Anio = 2023),"3),"
(' Keaton Mitchell ',3,RB,8,9,93,32,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Keaton Mitchell ' AND Anio = 2023),"3),"
(' Brock Wright ',11,TE,14,13,91,25,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Brock Wright ' AND Anio = 2023),"3),"
(' Tyquan Thornton ',22,WR,9,13,91,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyquan Thornton ' AND Anio = 2023),"3),"
(' Xavier Hutchinson ',13,WR,16,8,90,34,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Xavier Hutchinson ' AND Anio = 2023),"3),"
(' Jalen Guyton ',18,WR,8,10,89,18,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Guyton ' AND Anio = 2023),"3),"
(' Matt Breida ',24,RB,17,17,88,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Breida ' AND Anio = 2023),"3),"
(' Salvon Ahmed ',20,RB,8,16,88,20,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Salvon Ahmed ' AND Anio = 2023),"3),"
(' Charlie Kolar ',3,TE,15,7,87,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Charlie Kolar ' AND Anio = 2023),"3),"
(' Trent Sherfield Sr.',4,WR,17,11,86,12,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Trent Sherfield Sr.' AND Anio = 2023),"3),"
(' Jeff Wilson Jr.',20,RB,10,14,85,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeff Wilson Jr.' AND Anio = 2023),"3),"
(' Kareem Hunt ',8,RB,15,15,84,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kareem Hunt ' AND Anio = 2023),"3),"
(' Tim Jones ',15,WR,17,11,83,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tim Jones ' AND Anio = 2023),"3),"
(' Lynn Bowden Jr.',23,WR,15,11,83,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Lynn Bowden Jr.' AND Anio = 2023),"3),"
(' Deven Thompkins ',30,WR,17,17,83,26,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Deven Thompkins ' AND Anio = 2023),"3),"
(' Isaiah McKenzie ',14,WR,13,11,82,30,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Isaiah McKenzie ' AND Anio = 2023),"3),"
(' Chase Edmonds ',30,RB,13,14,81,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chase Edmonds ' AND Anio = 2023),"3),"
(' Harrison Bryant ',8,TE,17,13,81,23,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Harrison Bryant ' AND Anio = 2023),"3),"
(' Dalvin Cook ',25,RB,15,15,78,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dalvin Cook ' AND Anio = 2023),"3),"
(' Brycen Hopkins ',19,TE,15,5,78,29,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brycen Hopkins ' AND Anio = 2023),"3),"
(' Samori Toure ',12,WR,11,8,78,35,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Samori Toure ' AND Anio = 2023),"3),"
(' D'Onta Foreman ',6,RB,9,11,77,17,1,(SELECT Player_ID FROM Player_season WHERE Name = 'D'Onta Foreman ' AND Anio = 2023),"3),"
(' Chase Claypool ',20,WR,12,8,77,20,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Chase Claypool ' AND Anio = 2023),"3),"
(' Julio Jones ',26,WR,11,11,74,22,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Julio Jones ' AND Anio = 2023),"3),"
(' Cam Akers ',21,RB,7,11,70,30,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cam Akers ' AND Anio = 2023),"3),"
(' Chris Conley ',28,WR,8,3,69,48,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Conley ' AND Anio = 2023),"3),"
(' Ronnie Bell ',28,WR,17,6,68,20,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Ronnie Bell ' AND Anio = 2023),"3),"
(' Marquise Goodwin ',8,WR,12,4,67,57,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marquise Goodwin ' AND Anio = 2023),"3),"
(' Ben Skowronek ',19,WR,17,8,66,20,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ben Skowronek ' AND Anio = 2023),"3),"
(' Derius Davis ',18,WR,17,15,66,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Derius Davis ' AND Anio = 2023),"3),"
(' Josiah Deguara ',12,TE,15,8,65,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Josiah Deguara ' AND Anio = 2023),"3),"
(' Luke Schoonmaker ',9,TE,17,8,65,18,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Luke Schoonmaker ' AND Anio = 2023),"3),"
(' Charlie Jones ',7,WR,11,7,64,35,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Charlie Jones ' AND Anio = 2023),"3),"
(' Jalen Brooks ',9,WR,7,6,64,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Brooks ' AND Anio = 2023),"3),"
(' Jamaal Williams ',23,RB,13,18,62,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamaal Williams ' AND Anio = 2023),"3),"
(' Ty Johnson ',4,RB,10,7,62,28,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ty Johnson ' AND Anio = 2023),"3),"
(' Equanimeous St. Brown',6,WR,7,5,62,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Equanimeous St. Brown' AND Anio = 2023),"3),"
(' Darnell Washington ',27,TE,17,7,61,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Darnell Washington ' AND Anio = 2023),"3),"
(' Laviska Shenault Jr.',5,WR,8,10,60,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Laviska Shenault Jr.' AND Anio = 2023),"3),"
(' Rakim Jarrett ',30,WR,10,4,60,41,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Rakim Jarrett ' AND Anio = 2023),"3),"
(' C.J. Uzomah ',25,TE,12,8,58,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Uzomah ' AND Anio = 2023),"3),"
(' Payne Durham ',30,TE,13,5,58,25,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Payne Durham ' AND Anio = 2023),"3),"
(' Kevin Harris ',22,RB,4,3,58,48,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kevin Harris ' AND Anio = 2023),"3),"
(' Sterling Shepard ',24,WR,15,10,57,13,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Sterling Shepard ' AND Anio = 2023),"3),"
(' Mitchell Wilcox ',7,TE,17,9,56,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mitchell Wilcox ' AND Anio = 2023),"3),"
(' Ian Thomas ',5,TE,12,5,56,28,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ian Thomas ' AND Anio = 2023),"3),"
(' D.J. Montgomery ',14,WR,7,3,56,34,1,(SELECT Player_ID FROM Player_season WHERE Name = 'D.J. Montgomery ' AND Anio = 2023),"3),"
(' Jason Brownlee ',25,WR,7,5,56,24,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jason Brownlee ' AND Anio = 2023),"3),"
(' Andrew Beck ',13,FB,15,11,55,26,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Andrew Beck ' AND Anio = 2023),"3),"
(' Justyn Ross ',16,WR,10,6,53,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Justyn Ross ' AND Anio = 2023),"3),"
(' Patrick Ricard ',3,FB,17,5,52,28,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Patrick Ricard ' AND Anio = 2023),"3),"
(' Boston Scott ',26,RB,15,4,52,27,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Boston Scott ' AND Anio = 2023),"3),"
(' Ihmir Smith-Marsette ',5,WR,17,8,51,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ihmir Smith-Marsette ' AND Anio = 2023),"3),"
(' Darrynton Evans ',20,RB,7,7,49,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Darrynton Evans ' AND Anio = 2023),"3),"
(' Patrick Taylor Jr.',12,RB,11,11,49,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Patrick Taylor Jr.' AND Anio = 2023),"3),"
(' Julian Hill ',20,TE,15,6,48,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Julian Hill ' AND Anio = 2023),"3),"
(' Gary Brightwell ',24,RB,7,5,47,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Gary Brightwell ' AND Anio = 2023),"3),"
(' Pierre Strong Jr.',8,RB,17,5,47,41,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Pierre Strong Jr.' AND Anio = 2023),"3),"
(' Craig Reynolds ',11,RB,17,5,47,28,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Craig Reynolds ' AND Anio = 2023),"3),"
(' Melvin Gordon III',3,RB,4,3,46,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Melvin Gordon III' AND Anio = 2023),"3),"
(' Raheem Blackshear ',5,RB,12,6,45,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Raheem Blackshear ' AND Anio = 2023),"3),"
(' Mike Strachan ',5,WR,4,1,45,45,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Strachan ' AND Anio = 2023),"3),"
(' Israel Abanikanda ',25,RB,6,7,43,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Israel Abanikanda ' AND Anio = 2023),"3),"
(' Britain Covey ',26,WR,16,4,42,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Britain Covey ' AND Anio = 2023),"3),"
(' Ty Montgomery II',22,WR,13,5,40,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ty Montgomery II' AND Anio = 2023),"3),"
(' Mike Boone ',13,RB,9,7,40,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Boone ' AND Anio = 2023),"3),"
(' Deuce Vaughn ',9,RB,7,7,40,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Deuce Vaughn ' AND Anio = 2023),"3),"
(' Jimmy Graham ',23,TE,13,6,39,12,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Jimmy Graham ' AND Anio = 2023),"3),"
(' Randall Cobb ',25,WR,11,5,39,15,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Randall Cobb ' AND Anio = 2023),"3),"
(' DeAndre Carter ',17,WR,17,4,39,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DeAndre Carter ' AND Anio = 2023),"3),"
(' Grant Calcaterra ',26,TE,15,4,39,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Grant Calcaterra ' AND Anio = 2023),"3),"
(' Cordarrelle Patterson ',2,RB,14,9,38,11,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Cordarrelle Patterson ' AND Anio = 2023),"3),"
(' Jack Stoll ',26,TE,17,5,38,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jack Stoll ' AND Anio = 2023),"3),"
(' Elijah Cooks ',15,WR,9,3,38,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Elijah Cooks ' AND Anio = 2023),"3),"
(' Peyton Hendershot ',9,TE,8,4,38,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Peyton Hendershot ' AND Anio = 2023),"3),"
(' Keith Kirkwood ',23,WR,13,5,37,13,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Keith Kirkwood ' AND Anio = 2023),"3),"
(' Tony Jones Jr.',23,RB,7,7,37,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tony Jones Jr.' AND Anio = 2023),"3),"
(' Lawrence Cager ',24,TE,11,4,36,10,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Lawrence Cager ' AND Anio = 2023),"3),"
(' Marvin Jones Jr.',11,WR,6,5,35,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marvin Jones Jr.' AND Anio = 2023),"3),"
(' Brenton Strange ',15,TE,14,5,35,17,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Brenton Strange ' AND Anio = 2023),"3),"
(' Isaiah Spiller ',18,RB,9,6,34,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Isaiah Spiller ' AND Anio = 2023),"3),"
(' Tyler Goodson ',14,RB,6,6,34,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Goodson ' AND Anio = 2023),"3),"
(' Keith Smith ',2,FB,13,3,33,28,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Keith Smith ' AND Anio = 2023),"3),"
(' Keelan Doss ',18,WR,5,6,33,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Keelan Doss ' AND Anio = 2023),"3),"
(' La'Mical Perine ',16,RB,5,3,33,25,0,(SELECT Player_ID FROM Player_season WHERE Name = 'La'Mical Perine ' AND Anio = 2023),"3),"
(' Teagan Quitoriano ',13,TE,7,2,33,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Teagan Quitoriano ' AND Anio = 2023),"3),"
(' Joshua Kelley ',18,RB,17,8,32,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Joshua Kelley ' AND Anio = 2023),"3),"
(' Charlie Woerner ',28,TE,17,3,32,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Charlie Woerner ' AND Anio = 2023),"3),"
(' Kenyan Drake ',12,RB,3,2,31,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenyan Drake ' AND Anio = 2023),"3),"
(' Khalil Dorsey ',11,CB,13,1,31,31,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Khalil Dorsey ' AND Anio = 2023),"3),"
(' Jordan Mason ',28,RB,17,3,31,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Mason ' AND Anio = 2023),"3),"
(' Marcedes Lewis ',6,TE,17,4,29,16,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Marcedes Lewis ' AND Anio = 2023),"3),"
(' Austin Trammell ',19,WR,16,4,29,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Austin Trammell ' AND Anio = 2023),"3),"
(' Jalen Nailor ',21,WR,6,3,29,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Nailor ' AND Anio = 2023),"3),"
(' Kenny Yeboah ',25,TE,5,2,28,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenny Yeboah ' AND Anio = 2023),"3),"
(' James Mitchell ',11,TE,15,2,28,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'James Mitchell ' AND Anio = 2023),"3),"
(' Blake Bell ',16,TE,17,5,26,8,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Blake Bell ' AND Anio = 2023),"3),"
(' DeeJay Dallas ',29,RB,17,6,26,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DeeJay Dallas ' AND Anio = 2023),"3),"
(' Quintin Morris ',4,TE,15,2,26,15,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Quintin Morris ' AND Anio = 2023),"3),"
(' Keaontay Ingram ',1,RB,8,4,26,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Keaontay Ingram ' AND Anio = 2023),"3),"
(' Steven Sims ',13,WR,3,3,25,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Steven Sims ' AND Anio = 2023),"3),"
(' C.J. Ham ',21,FB,17,7,25,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Ham ' AND Anio = 2023),"3),"
(' Greg Dulcich ',10,TE,2,3,25,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Greg Dulcich ' AND Anio = 2023),"3),"
(' Emanuel Wilson ',12,RB,7,4,23,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Emanuel Wilson ' AND Anio = 2023),"3),"
(' Ronnie Rivers ',19,RB,9,5,22,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ronnie Rivers ' AND Anio = 2023),"3),"
(' Nick Muse ',21,TE,2,1,22,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Muse ' AND Anio = 2023),"3),"
(' Nate Adkins ',10,TE,10,4,22,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nate Adkins ' AND Anio = 2023),"3),"
(' Eric Gray ',24,RB,13,6,22,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Eric Gray ' AND Anio = 2023),"3),"
(' Nick Bawden ',25,FB,16,3,21,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Bawden ' AND Anio = 2023),"3),"
(' Nick Chubb ',8,RB,2,4,21,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Chubb ' AND Anio = 2023),"3),"
(' Trevon Wesco ',31,TE,15,1,21,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trevon Wesco ' AND Anio = 2023),"3),"
(' Ben Sims ',12,TE,17,4,21,12,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ben Sims ' AND Anio = 2023),"3),"
(' Velus Jones Jr.',6,WR,14,4,20,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Velus Jones Jr.' AND Anio = 2023),"3),"
(' Zach Pascal ',1,WR,14,4,19,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Pascal ' AND Anio = 2023),"3),"
(' Kayshon Boutte ',22,WR,5,2,19,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kayshon Boutte ' AND Anio = 2023),"3),"
(' Dare Ogunbowale ',13,RB,12,2,18,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dare Ogunbowale ' AND Anio = 2023),"3),"
(' Devin Duvernay ',3,WR,13,4,18,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Devin Duvernay ' AND Anio = 2023),"3),"
(' Hunter Luepke ',9,RB,17,3,18,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Hunter Luepke ' AND Anio = 2023),"3),"
(' Brandin Echols ',25,CB,14,1,18,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandin Echols ' AND Anio = 2023),"3),"
(' Miles Boykin ',27,WR,17,3,17,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Miles Boykin ' AND Anio = 2023),"3),"
(' Chris Manhertz ',10,TE,16,2,16,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Manhertz ' AND Anio = 2023),"3),"
(' Laquon Treadwell ',3,WR,5,1,16,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Laquon Treadwell ' AND Anio = 2023),"3),"
(' Damien Harris ',4,RB,6,2,16,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Damien Harris ' AND Anio = 2023),"3),"
(' J.K. Dobbins ',3,RB,1,2,15,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'J.K. Dobbins ' AND Anio = 2023),"3),"
(' Willie Snead IV',28,WR,4,2,14,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Willie Snead IV' AND Anio = 2023),"3),"
(' Deon Jackson ',24,RB,4,5,14,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Deon Jackson ' AND Anio = 2023),"3),"
(' Elijah Mitchell ',28,RB,11,6,14,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Elijah Mitchell ' AND Anio = 2023),"3),"
(' Royce Freeman ',19,RB,14,1,13,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Royce Freeman ' AND Anio = 2023),"3),"
(' Alex Armah ',32,RB,8,3,13,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Alex Armah ' AND Anio = 2023),"3),"
(' Trey Sermon ',14,RB,14,3,13,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trey Sermon ' AND Anio = 2023),"3),"
(' Elijah Dotson ',18,RB,4,2,13,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Elijah Dotson ' AND Anio = 2023),"3),"
(' Malik Taylor ',25,WR,3,2,13,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Malik Taylor ' AND Anio = 2023),"3),"
(' Damien Williams ',1,RB,3,2,12,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Damien Williams ' AND Anio = 2023),"3),"
(' Eric Saubert ',9,TE,10,3,12,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Eric Saubert ' AND Anio = 2023),"3),"
(' Jakob Johnson ',17,FB,13,1,12,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jakob Johnson ' AND Anio = 2023),"3),"
(' Ross Dwelley ',28,TE,12,1,12,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ross Dwelley ' AND Anio = 2023),"3),"
(' Adam Prentice ',23,FB,13,2,12,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Adam Prentice ' AND Anio = 2023),"3),"
(' Jake Funk ',14,RB,4,1,12,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jake Funk ' AND Anio = 2023),"3),"
(' Chris Rodriguez Jr.',32,RB,13,2,12,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Rodriguez Jr.' AND Anio = 2023),"3),"
(' Jashaun Corbin ',24,RB,6,3,12,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jashaun Corbin ' AND Anio = 2023),"3),"
(' John FitzPatrick ',2,TE,9,1,12,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'John FitzPatrick ' AND Anio = 2023),"3),"
(' Collin Johnson ',6,WR,3,1,11,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Collin Johnson ' AND Anio = 2023),"3),"
(' Tylan Wallace ',3,WR,11,1,11,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tylan Wallace ' AND Anio = 2023),"3),"
(' Anthony McFarland Jr.',27,RB,3,2,11,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Anthony McFarland Jr.' AND Anio = 2023),"3),"
(' Cody Thompson ',29,WR,7,1,10,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cody Thompson ' AND Anio = 2023),"3),"
(' Trayveon Williams ',7,RB,17,7,10,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trayveon Williams ' AND Anio = 2023),"3),"
(' Justin Herbert ',18,QB,13,1,10,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Herbert ' AND Anio = 2023),"3),"
(' Trishton Jackson ',21,WR,7,2,9,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trishton Jackson ' AND Anio = 2023),"3),"
(' Tucker Fisk ',2,TE,6,1,9,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tucker Fisk ' AND Anio = 2023),"3),"
(' Simi Fehoko ',18,WR,6,1,9,9,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Simi Fehoko ' AND Anio = 2023),"3),"
(' Sean Tucker ',30,RB,11,2,9,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Sean Tucker ' AND Anio = 2023),"3),"
(' Tyler Johnson ',19,WR,1,2,8,8,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Johnson ' AND Anio = 2023),"3),"
(' Michael Burton ',10,FB,17,3,8,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Burton ' AND Anio = 2023),"3),"
(' Devine Ozigbo ',11,RB,3,1,8,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Devine Ozigbo ' AND Anio = 2023),"3),"
(' Zonovan Knight ',11,RB,2,1,8,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Zonovan Knight ' AND Anio = 2023),"3),"
(' Kevin Rader ',31,TE,14,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kevin Rader ' AND Anio = 2023),"3),"
(' Mason Kinsey ',31,WR,6,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mason Kinsey ' AND Anio = 2023),"3),"
(' Malcolm Rodriguez ',11,LB,17,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Malcolm Rodriguez ' AND Anio = 2023),"3),"
(' Cole Fotheringham ',17,TE,2,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cole Fotheringham ' AND Anio = 2023),"3),"
(' Tank Bigsby ',15,RB,17,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tank Bigsby ' AND Anio = 2023),"3),"
(' Evan Hull ',14,RB,1,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Evan Hull ' AND Anio = 2023),"3),"
(' Greg Van Roten',17,G,17,0,5,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Greg Van Roten' AND Anio = 2023),"3),"
(' Rashaad Penny ',26,RB,3,1,5,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Rashaad Penny ' AND Anio = 2023),"3),"
(' Dan Skipper ',11,OT,11,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dan Skipper ' AND Anio = 2023),"3),"
(' Jesper Horsted ',17,TE,13,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jesper Horsted ' AND Anio = 2023),"3),"
(' Sam Howell ',32,QB,17,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Sam Howell ' AND Anio = 2023),"3),"
(' Nick Vannett ',18,TE,8,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Vannett ' AND Anio = 2023),"3),"
(' Reggie Gilliam ',4,FB,17,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Reggie Gilliam ' AND Anio = 2023),"3),"
(' Cole Strange ',22,G,10,0,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cole Strange ' AND Anio = 2023),"3),"
(' Colton Dowell ',31,WR,10,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Colton Dowell ' AND Anio = 2023),"3),"
(' Khari Blasingame ',6,FB,16,3,2,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Khari Blasingame ' AND Anio = 2023),"3),"
(' Giovanni Ricci ',5,FB,5,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Giovanni Ricci ' AND Anio = 2023),"3),"
(' Ke'Shawn Vaughn ',30,RB,6,2,2,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ke'Shawn Vaughn ' AND Anio = 2023),"3),"
(' Ko Kieft ',30,TE,16,1,2,2,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ko Kieft ' AND Anio = 2023),"3),"
(' Jeffery Simmons ',31,DT,12,1,2,2,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeffery Simmons ' AND Anio = 2023),"3),"
(' Kwamie Lassiter II',7,WR,1,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kwamie Lassiter II' AND Anio = 2023),"3),"
(' Antoine Green ',11,WR,9,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Antoine Green ' AND Anio = 2023),"3),"
(' Ryan Tannehill ',31,QB,10,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Tannehill ' AND Anio = 2023),"3),"
(' Damiere Byrd ',2,WR,1,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Damiere Byrd ' AND Anio = 2023),"3),"
(' Phillip Dorsett ',10,WR,2,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Phillip Dorsett ' AND Anio = 2023),"3),"
(' Donovan Smith ',16,OT,12,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Donovan Smith ' AND Anio = 2023),"3),"
(' Jonathan Williams ',32,RB,1,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonathan Williams ' AND Anio = 2023),"3),"
(' Trent Taylor ',6,WR,17,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trent Taylor ' AND Anio = 2023),"3),"
(' Juwann Winfree ',14,WR,8,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Juwann Winfree ' AND Anio = 2023),"3),"
(' James Proche II',8,WR,10,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'James Proche II' AND Anio = 2023),"3),"
(' JaMycal Hasty ',15,RB,5,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'JaMycal Hasty ' AND Anio = 2023),"3),"
(' Irvin Charles ',25,WR,12,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Irvin Charles ' AND Anio = 2023),"3),"
(' Albert Okwuegbunam Jr.',26,TE,4,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Albert Okwuegbunam Jr.' AND Anio = 2023),"3),"
(' Sean McKeon ',9,TE,9,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Sean McKeon ' AND Anio = 2023),"3),"
(' Travis Homer ',6,RB,16,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Travis Homer ' AND Anio = 2023),"3),"
(' Dee Eskridge ',29,WR,4,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dee Eskridge ' AND Anio = 2023),"3),"
(' Ben Bredeson ',24,G,16,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ben Bredeson ' AND Anio = 2023),"3),"
(' Amari Rodgers ',14,WR,3,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Amari Rodgers ' AND Anio = 2023),"3),"
(' Jordan Mims ',23,RB,2,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Mims ' AND Anio = 2023),"3),"
(' Rodney Williams ',27,TE,13,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Rodney Williams ' AND Anio = 2023),"3),"
(' Shedrick Jackson ',7,WR,3,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Shedrick Jackson ' AND Anio = 2023),"3),"
(' Erik Ezukanma ',20,WR,2,0,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Erik Ezukanma ' AND Anio = 2023),"3),"
(' Gunner Olszewski ',24,WR,12,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Gunner Olszewski ' AND Anio = 2023),"3),"
(' C.J. Stroud ',13,QB,15,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Stroud ' AND Anio = 2023),"3),"
(' Chris Evans ',7,RB,8,1,-1,-1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Evans ' AND Anio = 2023),"3),"
(' Geno Smith ',29,QB,15,1,-2,-2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Geno Smith ' AND Anio = 2023),"3),"
(' James Robinson ',12,RB,1,1,-2,-2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'James Robinson ' AND Anio = 2023),"3),"
(' Robert Hainsey ',30,C,17,0,-3,-3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Robert Hainsey ' AND Anio = 2023),"3),"
(' Desmond Ridder ',2,QB,15,1,-6,-6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Desmond Ridder ' AND Anio = 2023),"3),"
(' Jake Browning ',7,QB,9,1,-7,-7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jake Browning ' AND Anio = 2023),"3),"
(' David Wells ',30,TE,5,2,-10,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'David Wells ' AND Anio = 2023),"3),"
(' Christian McCaffrey',28,RB,16,272,1459,72,14,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian McCaffrey' AND Anio = 2023),"2),"
(' Derrick Henry',31,RB,17,280,1167,69,12,(SELECT Player_ID FROM Player_season WHERE Name = 'Derrick Henry' AND Anio = 2023),"2),"
(' Kyren Williams',19,RB,12,228,1144,56,12,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyren Williams' AND Anio = 2023),"2),"
(' James Cook',4,RB,17,237,1122,42,2,(SELECT Player_ID FROM Player_season WHERE Name = 'James Cook' AND Anio = 2023),"2),"
(' D'Andre Swift',26,RB,16,229,1049,43,5,(SELECT Player_ID FROM Player_season WHERE Name = 'D'Andre Swift' AND Anio = 2023),"2),"
(' James Conner',1,RB,13,208,1040,44,7,(SELECT Player_ID FROM Player_season WHERE Name = 'James Conner' AND Anio = 2023),"2),"
(' Najee Harris',27,RB,17,255,1035,25,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Najee Harris' AND Anio = 2023),"2),"
(' Joe Mixon',7,RB,17,257,1034,44,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Joe Mixon' AND Anio = 2023),"2),"
(' David Montgomery',11,RB,14,219,1015,75,13,(SELECT Player_ID FROM Player_season WHERE Name = 'David Montgomery' AND Anio = 2023),"2),"
(' Raheem Mostert',20,RB,15,209,1012,49,18,(SELECT Player_ID FROM Player_season WHERE Name = 'Raheem Mostert' AND Anio = 2023),"2),"
(' Travis Etienne Jr',15,RB,17,267,1008,62,11,(SELECT Player_ID FROM Player_season WHERE Name = 'Travis Etienne Jr' AND Anio = 2023),"2),"
(' Tony Pollard',9,RB,17,252,1005,31,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Tony Pollard' AND Anio = 2023),"2),"
(' Breece Hall',25,RB,17,223,994,83,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Breece Hall' AND Anio = 2023),"2),"
(' Rachaad White',30,RB,17,272,990,38,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Rachaad White' AND Anio = 2023),"2),"
(' Bijan Robinson',2,RB,17,214,976,38,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Bijan Robinson' AND Anio = 2023),"2),"
(' Saquon Barkley',24,RB,14,247,962,36,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Saquon Barkley' AND Anio = 2023),"2),"
(' Jahmyr Gibbs',11,RB,15,182,945,36,10,(SELECT Player_ID FROM Player_season WHERE Name = 'Jahmyr Gibbs' AND Anio = 2023),"2),"
(' Isiah Pacheco',16,RB,14,205,935,48,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Isiah Pacheco' AND Anio = 2023),"2),"
(' Kenneth Walker III',29,RB,15,219,905,45,8,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenneth Walker III' AND Anio = 2023),"2),"
(' Chuba Hubbard ',5,RB,17,238,902,22,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Chuba Hubbard ' AND Anio = 2023),"2),"
(' Devin Singletary ',13,RB,17,216,898,24,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Devin Singletary ' AND Anio = 2023),"2),"
(' Lamar Jackson ',3,QB,16,148,821,30,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Lamar Jackson ' AND Anio = 2023),"2),"
(' Jerome Ford ',8,RB,17,204,813,69,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Jerome Ford ' AND Anio = 2023),"2),"
(' Gus Edwards ',3,RB,17,198,810,42,13,(SELECT Player_ID FROM Player_season WHERE Name = 'Gus Edwards ' AND Anio = 2023),"2),"
(' Josh Jacobs ',17,RB,13,233,805,63,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Jacobs ' AND Anio = 2023),"2),"
(' De'Von Achane ',20,RB,11,103,800,76,8,(SELECT Player_ID FROM Player_season WHERE Name = 'De'Von Achane ' AND Anio = 2023),"2),"
(' Zack Moss ',14,RB,14,183,794,56,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Zack Moss ' AND Anio = 2023),"2),"
(' Jaylen Warren ',27,RB,17,149,784,74,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaylen Warren ' AND Anio = 2023),"2),"
(' Javonte Williams ',10,RB,16,217,774,21,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Javonte Williams ' AND Anio = 2023),"2),"
(' Jonathan Taylor ',14,RB,10,169,741,49,7,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonathan Taylor ' AND Anio = 2023),"2),"
(' Brian Robinson Jr.',32,RB,15,178,733,29,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Brian Robinson Jr.' AND Anio = 2023),"2),"
(' Alexander Mattison ',21,RB,16,180,700,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Alexander Mattison ' AND Anio = 2023),"2),"
(' Alvin Kamara ',23,RB,13,180,694,17,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Alvin Kamara ' AND Anio = 2023),"2),"
(' Tyler Allgeier ',2,RB,17,186,683,31,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Allgeier ' AND Anio = 2023),"2),"
(' Justin Fields ',6,QB,13,124,657,39,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Fields ' AND Anio = 2023),"2),"
(' Aaron Jones ',12,RB,11,142,656,39,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Aaron Jones ' AND Anio = 2023),"2),"
(' Ezekiel Elliott ',22,RB,17,184,642,17,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Ezekiel Elliott ' AND Anio = 2023),"2),"
(' Austin Ekeler ',18,RB,14,179,628,55,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Austin Ekeler ' AND Anio = 2023),"2),"
(' Rhamondre Stevenson ',22,RB,12,156,619,64,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Rhamondre Stevenson ' AND Anio = 2023),"2),"
(' AJ Dillon ',12,RB,15,178,613,40,2,(SELECT Player_ID FROM Player_season WHERE Name = 'AJ Dillon ' AND Anio = 2023),"2),"
(' Khalil Herbert ',6,RB,12,132,611,38,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Khalil Herbert ' AND Anio = 2023),"2),"
(' Jalen Hurts ',26,QB,17,157,605,24,15,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Hurts ' AND Anio = 2023),"2),"
(' Josh Allen ',4,QB,17,111,524,23,15,(SELECT Player_ID FROM Player_season WHERE Name = 'Josh Allen ' AND Anio = 2023),"2),"
(' Zach Charbonnet ',29,RB,16,108,462,23,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Charbonnet ' AND Anio = 2023),"2),"
(' Ty Chandler ',21,RB,17,102,461,31,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Ty Chandler ' AND Anio = 2023),"2),"
(' Tyjae Spears ',31,RB,17,100,453,23,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyjae Spears ' AND Anio = 2023),"2),"
(' Zamir White ',17,RB,17,104,451,43,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Zamir White ' AND Anio = 2023),"2),"
(' Miles Sanders ',5,RB,16,129,432,48,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Miles Sanders ' AND Anio = 2023),"2),"
(' D'Onta Foreman ',6,RB,9,109,425,22,4,(SELECT Player_ID FROM Player_season WHERE Name = 'D'Onta Foreman ' AND Anio = 2023),"2),"
(' Joshua Dobbs ',21,QB,13,77,421,44,6,(SELECT Player_ID FROM Player_season WHERE Name = 'Joshua Dobbs ' AND Anio = 2023),"2),"
(' Dameon Pierce ',13,RB,14,145,416,22,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Dameon Pierce ' AND Anio = 2023),"2),"
(' Kareem Hunt ',8,RB,15,135,411,16,9,(SELECT Player_ID FROM Player_season WHERE Name = 'Kareem Hunt ' AND Anio = 2023),"2),"
(' Jaleel McLaughlin ',10,RB,17,76,410,38,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaleel McLaughlin ' AND Anio = 2023),"2),"
(' Joshua Kelley ',18,RB,17,107,405,49,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Joshua Kelley ' AND Anio = 2023),"2),"
(' Taysom Hill ',23,QB,16,81,401,27,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Taysom Hill ' AND Anio = 2023),"2),"
(' Keaton Mitchell ',3,RB,8,47,396,60,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Keaton Mitchell ' AND Anio = 2023),"2),"
(' Patrick Mahomes ',16,QB,16,75,389,25,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Patrick Mahomes ' AND Anio = 2023),"2),"
(' Justice Hill ',3,RB,16,84,387,41,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Justice Hill ' AND Anio = 2023),"2),"
(' Kenneth Gainwell ',26,RB,16,84,364,32,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenneth Gainwell ' AND Anio = 2023),"2),"
(' Rico Dowdle ',9,RB,16,89,361,21,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Rico Dowdle ' AND Anio = 2023),"2),"
(' Roschon Johnson ',6,RB,15,81,352,29,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Roschon Johnson ' AND Anio = 2023),"2),"
(' Russell Wilson ',10,QB,15,80,341,21,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Russell Wilson ' AND Anio = 2023),"2),"
(' Trevor Lawrence ',15,QB,16,70,339,26,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Trevor Lawrence ' AND Anio = 2023),"2),"
(' Royce Freeman ',19,RB,14,77,319,23,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Royce Freeman ' AND Anio = 2023),"2),"
(' Jamaal Williams ',23,RB,13,106,306,17,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamaal Williams ' AND Anio = 2023),"2),"
(' Latavius Murray ',4,RB,16,79,300,29,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Latavius Murray ' AND Anio = 2023),"2),"
(' Pierre Strong Jr.',8,RB,17,63,291,40,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Pierre Strong Jr.' AND Anio = 2023),"2),"
(' Emari Demercado ',1,RB,14,58,284,49,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Emari Demercado ' AND Anio = 2023),"2),"
(' Elijah Mitchell ',28,RB,11,75,281,18,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Elijah Mitchell ' AND Anio = 2023),"2),"
(' Antonio Gibson ',32,RB,16,65,265,16,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Antonio Gibson ' AND Anio = 2023),"2),"
(' Sam Howell ',32,QB,17,48,263,24,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Sam Howell ' AND Anio = 2023),"2),"
(' Bryce Young ',5,QB,16,39,253,26,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Bryce Young ' AND Anio = 2023),"2),"
(' Jordan Love ',12,QB,17,50,247,37,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Love ' AND Anio = 2023),"2),"
(' Chris Rodriguez Jr.',32,RB,13,51,247,16,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Rodriguez Jr.' AND Anio = 2023),"2),"
(' Kyler Murray ',1,QB,8,44,244,33,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyler Murray ' AND Anio = 2023),"2),"
(' Dak Prescott ',9,QB,17,55,242,22,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Dak Prescott ' AND Anio = 2023),"2),"
(' Samaje Perine ',10,RB,17,53,238,24,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Samaje Perine ' AND Anio = 2023),"2),"
(' Justin Herbert ',18,QB,13,52,228,35,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Herbert ' AND Anio = 2023),"2),"
(' Deebo Samuel ',28,WR,15,37,225,23,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Deebo Samuel ' AND Anio = 2023),"2),"
(' Clyde Edwards-Helaire ',16,RB,15,70,223,20,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Clyde Edwards-Helaire ' AND Anio = 2023),"2),"
(' Dalvin Cook ',25,RB,15,67,214,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dalvin Cook ' AND Anio = 2023),"2),"
(' Zach Wilson ',25,QB,12,36,211,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Wilson ' AND Anio = 2023),"2),"
(' Daniel Jones ',24,QB,6,40,206,17,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Daniel Jones ' AND Anio = 2023),"2),"
(' Jordan Mason ',28,RB,17,40,206,26,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Mason ' AND Anio = 2023),"2),"
(' Tyrod Taylor ',24,QB,11,38,197,31,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyrod Taylor ' AND Anio = 2023),"2),"
(' Tommy DeVito ',24,QB,9,36,195,26,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Tommy DeVito ' AND Anio = 2023),"2),"
(' Desmond Ridder ',2,QB,15,53,193,23,5,(SELECT Player_ID FROM Player_season WHERE Name = 'Desmond Ridder ' AND Anio = 2023),"2),"
(' Jeff Wilson ',20,RB,10,41,188,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeff Wilson ' AND Anio = 2023),"2),"
(' Michael Carter ',25,RB,15,30,187,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Carter ' AND Anio = 2023),"2),"
(' Cordarrelle Patterson ',2,RB,14,50,181,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cordarrelle Patterson ' AND Anio = 2023),"2),"
(' Chase Brown ',7,RB,12,44,179,31,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chase Brown ' AND Anio = 2023),"2),"
(' Craig Reynolds ',11,RB,17,41,179,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Craig Reynolds ' AND Anio = 2023),"2),"
(' Rondale Moore ',1,WR,17,28,178,45,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Rondale Moore ' AND Anio = 2023),"2),"
(' Chase Edmonds ',30,RB,13,49,176,21,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chase Edmonds ' AND Anio = 2023),"2),"
(' Nick Chubb ',8,RB,2,28,170,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Chubb ' AND Anio = 2023),"2),"
(' Cam Akers ',21,RB,7,60,167,19,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Cam Akers ' AND Anio = 2023),"2),"
(' C.J. Stroud ',13,QB,15,39,167,16,3,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Stroud ' AND Anio = 2023),"2),"
(' Baker Mayfield ',30,QB,17,62,163,31,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Baker Mayfield ' AND Anio = 2023),"2),"
(' Trey Sermon ',14,RB,14,35,160,27,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trey Sermon ' AND Anio = 2023),"2),"
(' Kendre Miller ',23,RB,8,41,156,18,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kendre Miller ' AND Anio = 2023),"2),"
(' Geno Smith ',29,QB,15,37,155,25,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Geno Smith ' AND Anio = 2023),"2),"
(' Matt Breida ',24,RB,17,55,151,9,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Breida ' AND Anio = 2023),"2),"
(' Easton Stick ',18,QB,5,27,144,21,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Easton Stick ' AND Anio = 2023),"2),"
(' Brock Purdy ',28,QB,16,39,144,17,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Brock Purdy ' AND Anio = 2023),"2),"
(' Deshaun Watson ',8,QB,6,26,142,16,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Deshaun Watson ' AND Anio = 2023),"2),"
(' Patrick Taylor ',12,RB,11,32,141,24,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Patrick Taylor ' AND Anio = 2023),"2),"
(' Anthony Richardson ',14,QB,4,25,136,23,4,(SELECT Player_ID FROM Player_season WHERE Name = 'Anthony Richardson ' AND Anio = 2023),"2),"
(' Ty Johnson ',4,RB,10,30,132,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ty Johnson ' AND Anio = 2023),"2),"
(' Tank Bigsby ',15,RB,17,50,132,12,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Tank Bigsby ' AND Anio = 2023),"2),"
(' Ronnie Rivers ',19,RB,9,32,129,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ronnie Rivers ' AND Anio = 2023),"2),"
(' Jake Browning ',7,QB,9,27,127,21,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Jake Browning ' AND Anio = 2023),"2),"
(' Taylor Heinicke ',2,QB,5,15,124,24,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Taylor Heinicke ' AND Anio = 2023),"2),"
(' Darrynton Evans ',20,RB,7,32,121,13,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Darrynton Evans ' AND Anio = 2023),"2),"
(' Jayden Reed ',12,WR,16,11,119,32,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jayden Reed ' AND Anio = 2023),"2),"
(' CeeDee Lamb ',9,WR,17,14,113,24,2,(SELECT Player_ID FROM Player_season WHERE Name = 'CeeDee Lamb ' AND Anio = 2023),"2),"
(' Darrell Henderson ',19,RB,4,46,112,16,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Darrell Henderson ' AND Anio = 2023),"2),"
(' KaVontae Turpin ',9,WR,16,11,110,46,1,(SELECT Player_ID FROM Player_season WHERE Name = 'KaVontae Turpin ' AND Anio = 2023),"2),"
(' Tyson Bagent ',6,QB,5,23,109,20,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyson Bagent ' AND Anio = 2023),"2),"
(' D'Ernest Johnson ',15,RB,17,41,108,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'D'Ernest Johnson ' AND Anio = 2023),"2),"
(' Chris Brooks ',20,RB,9,19,106,52,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Brooks ' AND Anio = 2023),"2),"
(' Derius Davis ',18,WR,17,14,101,51,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Derius Davis ' AND Anio = 2023),"2),"
(' Gardner Minshew ',14,QB,17,34,100,23,3,(SELECT Player_ID FROM Player_season WHERE Name = 'Gardner Minshew ' AND Anio = 2023),"2),"
(' Mac Jones ',22,QB,11,26,96,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mac Jones ' AND Anio = 2023),"2),"
(' Isaiah Spiller ',18,RB,9,37,96,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Isaiah Spiller ' AND Anio = 2023),"2),"
(' Tony Jones ',23,RB,7,26,95,19,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Tony Jones ' AND Anio = 2023),"2),"
(' Damien Harris ',4,RB,6,23,94,11,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Damien Harris ' AND Anio = 2023),"2),"
(' Ameer Abdullah ',17,RB,17,15,89,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ameer Abdullah ' AND Anio = 2023),"2),"
(' Puka Nacua ',19,WR,17,12,89,31,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Puka Nacua ' AND Anio = 2023),"2),"
(' Joe Burrow ',7,QB,10,31,88,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Joe Burrow ' AND Anio = 2023),"2),"
(' Tyler Goodson ',14,RB,6,13,87,31,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Goodson ' AND Anio = 2023),"2),"
(' Wan'Dale Robinson ',24,WR,15,9,87,32,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Wan'Dale Robinson ' AND Anio = 2023),"2),"
(' Boston Scott ',26,RB,15,20,86,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Boston Scott ' AND Anio = 2023),"2),"
(' Emanuel Wilson ',12,RB,7,14,85,31,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Emanuel Wilson ' AND Anio = 2023),"2),"
(' Bailey Zappe ',22,QB,10,17,83,18,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Bailey Zappe ' AND Anio = 2023),"2),"
(' Melvin Gordon III',3,RB,4,26,81,22,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Melvin Gordon III' AND Anio = 2023),"2),"
(' La'Mical Perine ',16,RB,5,22,77,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'La'Mical Perine ' AND Anio = 2023),"2),"
(' Tre Tucker ',17,WR,16,10,77,34,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tre Tucker ' AND Anio = 2023),"2),"
(' Kalif Raymond ',11,WR,17,7,75,40,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kalif Raymond ' AND Anio = 2023),"2),"
(' Ryan Tannehill ',31,QB,10,17,74,23,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Tannehill ' AND Anio = 2023),"2),"
(' Ihmir Smith-Marsette ',5,WR,17,8,74,20,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Ihmir Smith-Marsette ' AND Anio = 2023),"2),"
(' Tua Tagovailoa ',20,QB,17,35,74,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tua Tagovailoa ' AND Anio = 2023),"2),"
(' Keaontay Ingram ',1,RB,8,35,74,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Keaontay Ingram ' AND Anio = 2023),"2),"
(' Israel Abanikanda ',25,RB,6,22,70,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Israel Abanikanda ' AND Anio = 2023),"2),"
(' Trayveon Williams ',7,RB,17,15,69,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trayveon Williams ' AND Anio = 2023),"2),"
(' Xavier Gipson ',25,WR,17,8,68,18,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Xavier Gipson ' AND Anio = 2023),"2),"
(' Matthew Stafford ',19,QB,15,21,65,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Matthew Stafford ' AND Anio = 2023),"2),"
(' Dorian Thompson-Robinson ',8,QB,8,14,65,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dorian Thompson-Robinson ' AND Anio = 2023),"2),"
(' Kevin Harris ',22,RB,4,16,65,18,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kevin Harris ' AND Anio = 2023),"2),"
(' Salvon Ahmed ',20,RB,8,22,61,10,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Salvon Ahmed ' AND Anio = 2023),"2),"
(' Jerick McKinnon ',16,RB,12,21,60,10,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jerick McKinnon ' AND Anio = 2023),"2),"
(' Calvin Austin III',27,WR,17,11,57,12,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Calvin Austin III' AND Anio = 2023),"2),"
(' Will Levis ',31,QB,9,25,57,11,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Will Levis ' AND Anio = 2023),"2),"
(' Carson Wentz ',19,QB,2,17,56,12,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Carson Wentz ' AND Anio = 2023),"2),"
(' Deven Thompkins ',30,WR,17,8,56,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Deven Thompkins ' AND Anio = 2023),"2),"
(' Zay Flowers ',3,WR,16,8,56,37,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Zay Flowers ' AND Anio = 2023),"2),"
(' Tyler Huntley ',3,QB,5,15,55,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Huntley ' AND Anio = 2023),"2),"
(' Laviska Shenault Jr.',5,WR,8,12,55,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Laviska Shenault Jr.' AND Anio = 2023),"2),"
(' Mitchell Trubisky ',27,QB,5,16,54,15,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Mitchell Trubisky ' AND Anio = 2023),"2),"
(' Kenny Pickett ',27,QB,12,42,54,11,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenny Pickett ' AND Anio = 2023),"2),"
(' Marcus Mariota ',26,QB,3,8,52,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marcus Mariota ' AND Anio = 2023),"2),"
(' Velus Jones Jr.',6,WR,14,8,51,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Velus Jones Jr.' AND Anio = 2023),"2),"
(' Tyquan Thornton ',22,WR,9,3,51,39,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyquan Thornton ' AND Anio = 2023),"2),"
(' Tank Dell ',13,WR,11,11,51,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tank Dell ' AND Anio = 2023),"2),"
(' Xavier Hutchinson ',13,WR,16,5,49,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Xavier Hutchinson ' AND Anio = 2023),"2),"
(' Eric Gray ',24,RB,13,17,48,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Eric Gray ' AND Anio = 2023),"2),"
(' Raheem Blackshear ',5,RB,12,14,46,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Raheem Blackshear ' AND Anio = 2023),"2),"
(' Blaine Gabbert ',16,QB,2,7,45,25,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Blaine Gabbert ' AND Anio = 2023),"2),"
(' Damien Williams ',1,RB,3,11,43,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Damien Williams ' AND Anio = 2023),"2),"
(' Ke'Shawn Vaughn ',30,RB,6,24,42,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ke'Shawn Vaughn ' AND Anio = 2023),"2),"
(' DeMario Douglas ',22,WR,14,8,41,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DeMario Douglas ' AND Anio = 2023),"2),"
(' Tyler Scott ',6,WR,17,7,41,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Scott ' AND Anio = 2023),"2),"
(' Derek Carr ',23,QB,17,32,40,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Derek Carr ' AND Anio = 2023),"2),"
(' Trevor Siemian ',25,QB,5,11,40,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trevor Siemian ' AND Anio = 2023),"2),"
(' Leonard Fournette ',4,RB,2,12,40,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Leonard Fournette ' AND Anio = 2023),"2),"
(' Deuce Vaughn ',9,RB,7,23,40,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Deuce Vaughn ' AND Anio = 2023),"2),"
(' Jimmy Garoppolo ',17,QB,7,20,39,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jimmy Garoppolo ' AND Anio = 2023),"2),"
(' Chris Moore ',31,WR,17,2,39,38,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Moore ' AND Anio = 2023),"2),"
(' Curtis Samuel ',32,WR,16,7,39,15,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Curtis Samuel ' AND Anio = 2023),"2),"
(' Chris Godwin ',30,WR,17,4,38,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Godwin ' AND Anio = 2023),"2),"
(' Rashid Shaheed ',23,WR,15,7,37,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Rashid Shaheed ' AND Anio = 2023),"2),"
(' DeeJay Dallas ',29,RB,17,10,36,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DeeJay Dallas ' AND Anio = 2023),"2),"
(' Brandin Cooks ',9,WR,16,5,35,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandin Cooks ' AND Anio = 2023),"2),"
(' C.J. Beathard ',15,QB,7,8,35,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Beathard ' AND Anio = 2023),"2),"
(' Dare Ogunbowale ',13,RB,12,8,35,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dare Ogunbowale ' AND Anio = 2023),"2),"
(' Marquise Goodwin ',8,WR,12,4,33,20,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marquise Goodwin ' AND Anio = 2023),"2),"
(' Jeff Driskel ',8,QB,1,7,33,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jeff Driskel ' AND Anio = 2023),"2),"
(' Rashaad Penny ',26,RB,3,11,33,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Rashaad Penny ' AND Anio = 2023),"2),"
(' Lynn Bowden Jr.',23,WR,15,5,32,29,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Lynn Bowden Jr.' AND Anio = 2023),"2),"
(' Brandon Bolden ',17,RB,17,4,31,26,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Bolden ' AND Anio = 2023),"2),"
(' Kadarius Toney ',16,WR,13,11,31,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kadarius Toney ' AND Anio = 2023),"2),"
(' Tutu Atwell ',19,WR,16,5,31,22,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tutu Atwell ' AND Anio = 2023),"2),"
(' PJ Walker ',8,QB,6,13,30,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'PJ Walker ' AND Anio = 2023),"2),"
(' Ray-Ray McCloud III',28,WR,12,3,30,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ray-Ray McCloud III' AND Anio = 2023),"2),"
(' Clayton Tune ',1,QB,7,8,30,11,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Clayton Tune ' AND Anio = 2023),"2),"
(' Marvin Mims Jr.',10,WR,16,9,30,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marvin Mims Jr.' AND Anio = 2023),"2),"
(' Jameson Williams ',11,WR,12,3,29,19,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jameson Williams ' AND Anio = 2023),"2),"
(' Khari Blasingame ',6,FB,16,8,26,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Khari Blasingame ' AND Anio = 2023),"2),"
(' Derrick Gore ',32,RB,6,3,26,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Derrick Gore ' AND Anio = 2023),"2),"
(' Kirk Cousins ',21,QB,8,14,25,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kirk Cousins ' AND Anio = 2023),"2),"
(' Nick Mullens ',21,QB,5,10,25,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Mullens ' AND Anio = 2023),"2),"
(' Jakobi Meyers ',17,WR,16,4,24,17,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jakobi Meyers ' AND Anio = 2023),"2),"
(' Amon-Ra St. Brown',11,WR,16,4,24,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Amon-Ra St. Brown' AND Anio = 2023),"2),"
(' Demarcus Robinson ',19,WR,16,1,23,23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Demarcus Robinson ' AND Anio = 2023),"2),"
(' Mike Boone ',13,RB,9,5,23,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Boone ' AND Anio = 2023),"2),"
(' Calvin Ridley ',15,WR,17,9,23,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Calvin Ridley ' AND Anio = 2023),"2),"
(' Marquise Brown ',1,WR,14,2,23,29,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Marquise Brown ' AND Anio = 2023),"2),"
(' Skyy Moore ',16,WR,14,3,23,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Skyy Moore ' AND Anio = 2023),"2),"
(' Sean Tucker ',30,RB,11,15,23,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Sean Tucker ' AND Anio = 2023),"2),"
(' J.K. Dobbins ',3,RB,1,8,22,4,1,(SELECT Player_ID FROM Player_season WHERE Name = 'J.K. Dobbins ' AND Anio = 2023),"2),"
(' Erik Ezukanma ',20,WR,2,5,22,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Erik Ezukanma ' AND Anio = 2023),"2),"
(' Trey Palmer ',30,WR,17,3,22,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trey Palmer ' AND Anio = 2023),"2),"
(' Jared Goff ',11,QB,17,32,21,11,2,(SELECT Player_ID FROM Player_season WHERE Name = 'Jared Goff ' AND Anio = 2023),"2),"
(' DJ Moore ',6,WR,17,4,21,16,1,(SELECT Player_ID FROM Player_season WHERE Name = 'DJ Moore ' AND Anio = 2023),"2),"
(' Malik Willis ',31,QB,3,5,21,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Malik Willis ' AND Anio = 2023),"2),"
(' Bo Melton ',12,WR,5,3,21,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Bo Melton ' AND Anio = 2023),"2),"
(' Tyrion Davis-Price ',28,RB,1,6,21,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyrion Davis-Price ' AND Anio = 2023),"2),"
(' Jacoby Brissett ',32,QB,3,3,19,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jacoby Brissett ' AND Anio = 2023),"2),"
(' Brett Rypien ',19,QB,2,3,19,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brett Rypien ' AND Anio = 2023),"2),"
(' Gary Brightwell ',24,RB,7,9,19,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Gary Brightwell ' AND Anio = 2023),"2),"
(' Hunter Luepke ',9,RB,17,6,19,9,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Hunter Luepke ' AND Anio = 2023),"2),"
(' Zach Evans ',19,RB,10,9,19,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Zach Evans ' AND Anio = 2023),"2),"
(' DeAndre Carter ',17,WR,17,3,18,15,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DeAndre Carter ' AND Anio = 2023),"2),"
(' Rashod Bateman ',3,WR,16,1,18,18,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Rashod Bateman ' AND Anio = 2023),"2),"
(' George Pickens ',27,WR,17,3,18,16,0,(SELECT Player_ID FROM Player_season WHERE Name = 'George Pickens ' AND Anio = 2023),"2),"
(' Treylon Burks ',31,WR,11,5,18,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Treylon Burks ' AND Anio = 2023),"2),"
(' Brandon Powell ',21,WR,17,5,17,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brandon Powell ' AND Anio = 2023),"2),"
(' Jalen Reagor ',22,WR,11,1,17,17,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Reagor ' AND Anio = 2023),"2),"
(' Deon Jackson ',24,RB,4,14,16,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Deon Jackson ' AND Anio = 2023),"2),"
(' Tyreek Hill ',20,WR,16,6,15,14,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyreek Hill ' AND Anio = 2023),"2),"
(' Sam Darnold ',28,QB,10,21,15,9,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Sam Darnold ' AND Anio = 2023),"2),"
(' Devin Duvernay ',3,WR,13,4,15,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Devin Duvernay ' AND Anio = 2023),"2),"
(' Isaiah McKenzie ',14,WR,13,3,14,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Isaiah McKenzie ' AND Anio = 2023),"2),"
(' Drew Lock ',29,QB,4,5,14,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Drew Lock ' AND Anio = 2023),"2),"
(' Jaren Hall ',21,QB,3,6,14,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaren Hall ' AND Anio = 2023),"2),"
(' Kene Nwangwu ',21,RB,9,5,13,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kene Nwangwu ' AND Anio = 2023),"2),"
(' Charlie Jones ',7,WR,11,2,13,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Charlie Jones ' AND Anio = 2023),"2),"
(' Zonovan Knight ',11,RB,2,3,13,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Zonovan Knight ' AND Anio = 2023),"2),"
(' Andy Dalton ',5,QB,3,3,12,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Andy Dalton ' AND Anio = 2023),"2),"
(' Adam Prentice ',23,FB,13,2,12,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Adam Prentice ' AND Anio = 2023),"2),"
(' Chris Evans ',7,RB,8,2,12,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chris Evans ' AND Anio = 2023),"2),"
(' Jaylen Waddle ',20,WR,14,3,12,12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jaylen Waddle ' AND Anio = 2023),"2),"
(' Tyler Boyd ',7,WR,17,2,11,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Boyd ' AND Anio = 2023),"2),"
(' Braxton Berrios ',20,WR,16,1,11,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Braxton Berrios ' AND Anio = 2023),"2),"
(' Jonathan Ward ',31,RB,8,3,11,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonathan Ward ' AND Anio = 2023),"2),"
(' Christian Watson ',12,WR,9,4,11,13,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian Watson ' AND Anio = 2023),"2),"
(' Keisean Nixon ',12,CB,17,1,11,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Keisean Nixon ' AND Anio = 2023),"2),"
(' Aidan O'Connell ',17,QB,11,17,11,3,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Aidan O'Connell ' AND Anio = 2023),"2),"
(' Elijah Moore ',8,WR,17,9,11,19,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Elijah Moore ' AND Anio = 2023),"2),"
(' Gerald Everett ',18,TE,15,3,10,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Gerald Everett ' AND Anio = 2023),"2),"
(' Jake Funk ',14,RB,4,2,10,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jake Funk ' AND Anio = 2023),"2),"
(' Blake Gillikin ',1,P,13,1,10,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Blake Gillikin ' AND Anio = 2023),"2),"
(' Khalil Shakir ',4,WR,17,1,10,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Khalil Shakir ' AND Anio = 2023),"2),"
(' DeAndre Hopkins ',31,WR,17,2,9,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'DeAndre Hopkins ' AND Anio = 2023),"2),"
(' Michael Burton ',10,FB,17,7,9,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Michael Burton ' AND Anio = 2023),"2),"
(' Ty Montgomery II',22,WR,13,3,9,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ty Montgomery II' AND Anio = 2023),"2),"
(' Ben Skowronek ',19,WR,17,2,9,11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ben Skowronek ' AND Anio = 2023),"2),"
(' Davis Mills ',13,QB,6,2,9,9,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Davis Mills ' AND Anio = 2023),"2),"
(' Quentin Johnston ',18,WR,17,3,9,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Quentin Johnston ' AND Anio = 2023),"2),"
(' Mason Rudolph ',27,QB,4,10,8,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mason Rudolph ' AND Anio = 2023),"2),"
(' Jarrett Stidham ',10,QB,3,9,8,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jarrett Stidham ' AND Anio = 2023),"2),"
(' Harrison Bryant ',8,TE,17,5,8,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Harrison Bryant ' AND Anio = 2023),"2),"
(' Cedric Tillman ',8,WR,14,1,8,8,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cedric Tillman ' AND Anio = 2023),"2),"
(' Robert Woods ',13,WR,14,1,7,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Robert Woods ' AND Anio = 2023),"2),"
(' C.J. Ham ',21,FB,17,1,7,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'C.J. Ham ' AND Anio = 2023),"2),"
(' Nico Collins ',13,WR,15,1,7,7,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nico Collins ' AND Anio = 2023),"2),"
(' Keenan Allen ',18,WR,13,2,6,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Keenan Allen ' AND Anio = 2023),"2),"
(' Kyle Juszczyk ',28,FB,17,5,6,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Juszczyk ' AND Anio = 2023),"2),"
(' Adam Thielen ',5,WR,17,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Adam Thielen ' AND Anio = 2023),"2),"
(' Sterling Shepard ',24,WR,15,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Sterling Shepard ' AND Anio = 2023),"2),"
(' Logan Woodside ',2,QB,1,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Logan Woodside ' AND Anio = 2023),"2),"
(' Christian Kirk ',15,WR,12,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Christian Kirk ' AND Anio = 2023),"2),"
(' Joshua Palmer ',18,WR,11,1,6,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Joshua Palmer ' AND Anio = 2023),"2),"
(' Elijah Dotson ',18,RB,4,4,6,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Elijah Dotson ' AND Anio = 2023),"2),"
(' Chigoziem Okonkwo ',31,TE,17,2,6,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Chigoziem Okonkwo ' AND Anio = 2023),"2),"
(' Stefon Diggs ',4,WR,17,1,5,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Stefon Diggs ' AND Anio = 2023),"2),"
(' Tim Boyle ',25,QB,3,4,5,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tim Boyle ' AND Anio = 2023),"2),"
(' Devine Ozigbo ',11,RB,3,3,5,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Devine Ozigbo ' AND Anio = 2023),"2),"
(' Greg Dortch ',1,WR,16,1,5,5,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Greg Dortch ' AND Anio = 2023),"2),"
(' Darnell Mooney ',6,WR,15,2,5,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Darnell Mooney ' AND Anio = 2023),"2),"
(' Dee Eskridge ',29,WR,4,2,5,10,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dee Eskridge ' AND Anio = 2023),"2),"
(' Kendrick Bourne ',22,WR,8,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kendrick Bourne ' AND Anio = 2023),"2),"
(' Nick Bawden ',25,FB,16,2,4,3,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Bawden ' AND Anio = 2023),"2),"
(' Van Jefferson ',19,WR,17,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Van Jefferson ' AND Anio = 2023),"2),"
(' Sam LaPorta ',11,TE,17,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Sam LaPorta ' AND Anio = 2023),"2),"
(' John Metchie III',13,WR,16,1,4,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'John Metchie III' AND Anio = 2023),"2),"
(' Jalen Reeves-Maybin ',11,LB,17,2,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jalen Reeves-Maybin ' AND Anio = 2023),"2),"
(' Mike Williams ',18,WR,3,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike Williams ' AND Anio = 2023),"2),"
(' Andrew Beck ',13,FB,15,5,3,2,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Andrew Beck ' AND Anio = 2023),"2),"
(' Ashtyn Davis ',25,S,17,2,3,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ashtyn Davis ' AND Anio = 2023),"2),"
(' Mecole Hardman ',#N/D,WR,11,1,3,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mecole Hardman ' AND Anio = 2023),"2),"
(' Jake Bobo ',29,WR,17,1,3,3,1,(SELECT Player_ID FROM Player_season WHERE Name = 'Jake Bobo ' AND Anio = 2023),"2),"
(' Joe Flacco ',8,QB,5,9,2,3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Joe Flacco ' AND Anio = 2023),"2),"
(' Logan Thomas ',32,TE,16,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Logan Thomas ' AND Anio = 2023),"2),"
(' George Kittle ',28,TE,16,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'George Kittle ' AND Anio = 2023),"2),"
(' Ezekiel Turner ',1,LB,16,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ezekiel Turner ' AND Anio = 2023),"2),"
(' Amani Hooker ',31,S,13,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Amani Hooker ' AND Anio = 2023),"2),"
(' Kylen Granson ',14,TE,15,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kylen Granson ' AND Anio = 2023),"2),"
(' James Robinson ',12,RB,1,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'James Robinson ' AND Anio = 2023),"2),"
(' Cole Kmet ',6,TE,17,3,2,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cole Kmet ' AND Anio = 2023),"2),"
(' Jordan Addison ',21,WR,17,1,2,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jordan Addison ' AND Anio = 2023),"2),"
(' Case Keenum ',13,QB,2,2,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Case Keenum ' AND Anio = 2023),"2),"
(' Dallas Goedert ',26,TE,14,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dallas Goedert ' AND Anio = 2023),"2),"
(' Steven Sims ',13,WR,3,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Steven Sims ' AND Anio = 2023),"2),"
(' Noah Gray ',16,TE,17,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Noah Gray ' AND Anio = 2023),"2),"
(' Jashaun Corbin ',24,RB,6,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jashaun Corbin ' AND Anio = 2023),"2),"
(' Dontayvion Wicks ',12,WR,15,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dontayvion Wicks ' AND Anio = 2023),"2),"
(' Evan Hull ',14,RB,1,1,1,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Evan Hull ' AND Anio = 2023),"2),"
(' Tress Way ',32,P,17,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tress Way ' AND Anio = 2023),"2),"
(' Kenyan Drake ',12,RB,3,2,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kenyan Drake ' AND Anio = 2023),"2),"
(' KhaDarel Hodge ',2,WR,17,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'KhaDarel Hodge ' AND Anio = 2023),"2),"
(' Jonnu Smith ',2,TE,17,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonnu Smith ' AND Anio = 2023),"2),"
(' Jason Cabinda ',11,FB,4,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jason Cabinda ' AND Anio = 2023),"2),"
(' Mark Andrews ',3,TE,10,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mark Andrews ' AND Anio = 2023),"2),"
(' Tyler Conklin ',25,TE,17,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Tyler Conklin ' AND Anio = 2023),"2),"
(' Alec Ingold ',20,FB,17,2,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Alec Ingold ' AND Anio = 2023),"2),"
(' Nick Niemann ',18,LB,17,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nick Niemann ' AND Anio = 2023),"2),"
(' Connor Heyward ',27,TE,17,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Connor Heyward ' AND Anio = 2023),"2),"
(' Peyton Hendershot ',9,TE,8,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Peyton Hendershot ' AND Anio = 2023),"2),"
(' Dyami Brown ',32,WR,17,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Dyami Brown ' AND Anio = 2023),"2),"
(' Deonte Harty ',4,WR,16,4,0,4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Deonte Harty ' AND Anio = 2023),"2),"
(' Rakim Jarrett ',30,WR,10,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Rakim Jarrett ' AND Anio = 2023),"2),"
(' Ty Zentner ',31,P,9,1,0,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ty Zentner ' AND Anio = 2023),"2),"
(' Garrett Wilson ',25,WR,17,4,0,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Garrett Wilson ' AND Anio = 2023),"2),"
(' Noah Brown ',13,WR,10,1,-1,-1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Noah Brown ' AND Anio = 2023),"2),"
(' Kyle Trask ',30,QB,2,1,-1,-1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Trask ' AND Anio = 2023),"2),"
(' Teddy Bridgewater ',11,QB,1,2,-2,-1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Teddy Bridgewater ' AND Anio = 2023),"2),"
(' Jonathan Williams ',32,RB,1,1,-2,-2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jonathan Williams ' AND Anio = 2023),"2),"
(' Trent Taylor ',6,WR,17,1,-2,-2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Trent Taylor ' AND Anio = 2023),"2),"
(' Jamal Agnew ',15,WR,11,4,-2,1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jamal Agnew ' AND Anio = 2023),"2),"
(' Gabe Davis ',4,WR,17,1,-2,-2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Gabe Davis ' AND Anio = 2023),"2),"
(' Sean Clifford ',12,QB,2,3,-2,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Sean Clifford ' AND Anio = 2023),"2),"
(' Brian Hoyer ',17,QB,3,3,-3,-1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Brian Hoyer ' AND Anio = 2023),"2),"
(' Matt Barkley ',15,QB,1,3,-3,-1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Matt Barkley ' AND Anio = 2023),"2),"
(' Cooper Kupp ',19,WR,12,1,-3,-3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cooper Kupp ' AND Anio = 2023),"2),"
(' Rashee Rice ',16,WR,16,1,-3,-3,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Rashee Rice ' AND Anio = 2023),"2),"
(' Nathan Peterman ',6,QB,2,2,-4,-2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Nathan Peterman ' AND Anio = 2023),"2),"
(' Kyle Pitts ',2,TE,17,1,-4,-4,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Pitts ' AND Anio = 2023),"2),"
(' Cooper Rush ',9,QB,7,12,-5,6,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cooper Rush ' AND Anio = 2023),"2),"
(' Jameis Winston ',23,QB,7,5,-6,-1,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Jameis Winston ' AND Anio = 2023),"2),"
(' Ja'Marr Chase ',7,WR,16,3,-6,2,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ja'Marr Chase ' AND Anio = 2023),"2),"
(' Mike White ',20,QB,6,8,-9,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Mike White ' AND Anio = 2023),"2),"
(' Johnny Hekker ',5,P,17,1,-11,-11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Johnny Hekker ' AND Anio = 2023),"2),"
(' Ryan Stonehouse ',31,P,12,1,-11,-11,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Ryan Stonehouse ' AND Anio = 2023),"2),"
(' Justin Jefferson ',21,WR,10,1,-12,-12,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Justin Jefferson ' AND Anio = 2023),"2),"
(' Kyle Allen ',4,QB,7,13,-13,0,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Kyle Allen ' AND Anio = 2023),"2),"
(' Cameron Johnston ',13,P,13,1,-23,-23,0,(SELECT Player_ID FROM Player_season WHERE Name = 'Cameron Johnston ' AND Anio = 2023),"2),"

]

# Incertar datos de las estadísticas
for data in datos_a_insertar:
    cursor.execute('''
    INSERT INTO Statistics (Name, Team_ID, Position, Games_played, ATT, Yards, Long_Play, Touchdowns, Player_ID, Type_ID)
    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''')

# Confirmar los cambios
conn.commit()

# Cerrar la conexión
conn.close()

print("Datos insertados correctamente.")