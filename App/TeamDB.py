import sqlite3


CREATE_TEAM_TABLE = "CREATE TABLE IF NOT EXISTS Teams (team_id INTEGER PRIMARY KEY, city TEXT, team_name TEXT, wins INTEGER, loss INTEGER); "

INSERT_TEAM = "INSERT INTO Teams (city, team_name, wins, loss) VALUES (?, ?, ?, ?);"

GET_TEAM_BY_TID = "SELECT * FROM Teams WHERE team_id = ?;"
GET_ALL_TEAMS = "SELECT * FROM Teams"


def connect():
    return sqlite3.connect("data.db")


def create_team_table(connection):
    with connection:
        connection.execute(CREATE_TEAM_TABLE)


def add_team(connection, city, team_name, wins, loss):
    with connection:
        connection.execute(INSERT_TEAM, (city, team_name, wins, loss))


def get_teams_by_tid(connection, team_id):
    with connection:
        return connection.execute(GET_TEAM_BY_TID, (team_id,)).fetchall()


def get_all_teams(connection):
    with connection:
        return connection.execute(GET_ALL_TEAMS).fetchall()
