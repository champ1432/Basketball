#import sqlite3
#
#conn = sqlite3.connect("OLD")
#c = conn.cursor()
#
#
#def show_mavs():
#    c.execute("SELECT Players.name, Players.position FROM Players WHERE team_id = 1")
#    return c.fetchall()
#
#
#def show_heat():
#    c.execute("SELECT Players.name, Players.position FROM Players WHERE team_id = 2")
#    return c.fetchall()
#
#
## c.execute("CREATE TABLE Teams (team_id INTEGER, city TEXT, team_name TEXT, record TEXT)")
## conn.commit()
#
## c.execute("CREATE TABLE Players (player_id INTEGER, team_id INTEGER, name TEXT)")
## conn.commit()
#
## c.execute("CREATE TABLE PlayerStats (player_id INTEGER, points INTEGER, rebounds INTEGER, assists INTEGER)")
## conn.commit()
#
## c.execute("CREATE TABLE TeamStats (team_id INTEGER, tpoints INTEGER, trebounds INTEGER, tassists INTEGER)")
## conn.commit()
#
## c.execute("ALTER TABLE Players ADD COLUMN position TEXT")
## conn.commit()
#
## c.execute("INSERT INTO Teams VALUES (2, 'Miami', 'Heat', '0-0')")
## conn.commit()
#
## c.execute("INSERT INTO Players VALUES (10, 2, 'Bam Adebayo')")
## conn.commit()
#
## c.execute("UPDATE Players SET position = 'PG' WHERE player_id = 6")
## conn.commit()
#
## Mavs = [(2, 1, 'Tim Hardaway Jr.'), (3, 1, 'Dorian Finney-Smith'), (4, 1, 'Kristaps Porzingis')]
## c.executemany("INSERT INTO Players VALUES (?, ?, ?)", Mavs)
## conn.commit()
#
## c.execute("SELECT Players.name, Teams.team_name FROM Players LEFT JOIN Teams ON Players.team_id = Teams.team_id")
## items = c.fetchall()
## for item in items:
##   print(item)
#
## c.execute("SELECT * FROM Players")
## items = c.fetchall()
## for item in items:
##   print(item)
#
## c.execute("DELETE from Teams WHERE rowid = 82")
#
## conn.commit()
#
## conn.close()
#