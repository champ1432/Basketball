import sqlite3

CREATE_PLAYER_STATS_TABLE = "CREATE TABLE IF NOT EXISTS Player_Stats (pid INTEGER, points INTEGER, rebounds INTEGER, assists INTEGER); "
INSERT_PLAYER_STATS = "INSERT INTO Player_Stats (player_id, points, rebounds, assists) VALUES (?, ?, ?, ?);"

INSERT_STATS = "INSERT INTO Player_Stats (points) VALUES (?) WHERE pid = ?;"

# connection = sqlite3.connect("data.db")


def connect():
    return sqlite3.connect("data.db")


def insert_stats(connection, points, pid):
    with connection:
        connection.execute(INSERT_STATS, (points, pid))


def create_player_stats_table(connection):
    with connection:
        connection.execute(CREATE_PLAYER_STATS_TABLE)


def add_player_stats(connection, player_id, points, rebounds, assists):
    with connection:
        connection.execute(INSERT_PLAYER_STATS, (player_id, points, rebounds, assists))
