import sqlite3

CREATE_PLAYER_TABLE = "CREATE TABLE IF NOT EXISTS Players (player_id INTEGER PRIMARY KEY, tid INTEGER, first_name TEXT, last_name TEXT); "
DELETE_PLAYER_TABLE = "DROP TABLE Players"

INSERT_PLAYER = "INSERT INTO Players (tid, first_name, last_name, position) VALUES (?, ?, ?, ?);"
DELETE_PLAYER = "DELETE FROM Players WHERE player_id = ?;"
INSERT_PRIMARY_KEY = "INSERT INTO Players (player_id, tid, first_name, last_name, position) VALUES (?, ?, ?, ?, ?);"


GET_ALL_PLAYERS = "SELECT * FROM Players;"
GET_PLAYERS_BY_NAME = "SELECT * FROM Players WHERE last_name = ?;"
GET_PLAYERS_BY_TEAM = "SELECT * FROM Players WHERE tid = ?;"
GET_PLAYERS_BY_PLAYERID = "SELECT * FROM Players WHERE player_id = ?;"
GET_PLAYERS_BY_POSITION = "SELECT first_name, last_name, tid FROM Players WHERE position = ? AND tid = ?;"
GET_ALL_PLAYERS_TID_BY_POSITION_TEAM = "SELECT tid FROM Players WHERE position = ? AND tid = ?"

CONNECT_PLAYERS_TO_TEAMS = "SELECT first_name, last_name, team_name, position FROM Players INNER JOIN Teams ON Teams.team_id = Players.tid WHERE position = ? AND tid = ?"

ADD_COLUMN = "ALTER TABLE Players ADD COLUMN position INTEGER"

PG = "SELECT first_name, last_name FROM Players WHERE tid = ? AND position = ?"


def connect():
    return sqlite3.connect("data.db")


def create_player_table(connection):
    with connection:
        connection.execute(CREATE_PLAYER_TABLE)


def add_player(connection, tid, first_name, last_name, position):
    with connection:
        connection.execute(INSERT_PLAYER, (tid, first_name, last_name, position))


def get_all_players(connection):
    with connection:
        return connection.execute(GET_ALL_PLAYERS).fetchall()


def get_players_by_name(connection, last_name):
    with connection:
        return connection.execute(GET_PLAYERS_BY_NAME, (last_name,)).fetchall()


def get_players_by_team(connection, tid):
    with connection:
        return connection.execute(GET_PLAYERS_BY_TEAM, (tid,)).fetchall()


def delete_table(connection):
    with connection:
        connection.execute(DELETE_PLAYER_TABLE)


def delete_player(connection, player_id):
    with connection:
        connection.execute(DELETE_PLAYER, (player_id,))


def get_players_by_playerid(connection, player_id):
    with connection:
        return connection.execute(GET_PLAYERS_BY_PLAYERID, (player_id,)).fetchall()


def insert_primary_key(connection, player_id, tid, first_name, last_name, position):
    with connection:
        connection.execute(INSERT_PRIMARY_KEY, (player_id, tid, first_name, last_name, position))


def add_column(connection):
    with connection:
        connection.execute(ADD_COLUMN)


def get_players_by_position(connection, position, tid):
    with connection:
        return connection.execute(GET_PLAYERS_BY_POSITION, (position, tid)).fetchall()


def connect_players_teams(connection, position, tid):
    with connection:
        return connection.execute(CONNECT_PLAYERS_TO_TEAMS, (position, tid)).fetchall()


def get_players_tid_by_position(connection, position, tid):
    with connection:
        return connection.execute(GET_ALL_PLAYERS_TID_BY_POSITION_TEAM, (position, tid)).fetchall()
