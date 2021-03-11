import sqlite3

# add stat individually
CREATE_PLAYER_STATS_TABLE = "CREATE TABLE IF NOT EXISTS Player_Stats (pid INTEGER, points INTEGER, rebounds INTEGER, assists INTEGER); "
ADD_COLUMNS = "ALTER TABLE Player_Stats ADD games INTEGER"

UPDATE_PLAYER_GAMES = "UPDATE Player_Stats SET games = games+1 WHERE player_id = ?;"
UPDATE_PLAYER_POINTS = "UPDATE Player_Stats SET points = points+2 WHERE player_id = ?;"
UPDATE_PLAYER_REBOUNDS = "UPDATE Player_Stats SET rebounds = rebounds+1 WHERE player_id = ?;"
UPDATE_PLAYER_ASSISTS = "UPDATE Player_Stats SET assists = assists+1 WHERE player_id = ?;"

INSERT_STATS = "INSERT INTO Player_Stats (points) VALUES (?) WHERE pid = ?;"
CLEAR_STATS = "UPDATE Player_Stats SET points = 0, rebounds = 0, assists = 0, season = 1000, games = 0"

GET_PLAYERS_POINTS = "SELECT * FROM Player_Stats WHERE player_id = ?;"


# connection = sqlite3.connect("data.db")


def connect():
    return sqlite3.connect("data.db")


def insert_stats(connection, points, pid):
    with connection:
        connection.execute(INSERT_STATS, (points, pid))


def create_player_stats_table(connection):
    with connection:
        connection.execute(CREATE_PLAYER_STATS_TABLE)


def add_player_points(connection, player_id):
    with connection:
        connection.execute(UPDATE_PLAYER_POINTS, (player_id,))


def add_player_rebounds(connection, player_id):
    with connection:
        connection.execute(UPDATE_PLAYER_REBOUNDS, (player_id,))


def add_player_assists(connection, player_id):
    with connection:
        connection.execute(UPDATE_PLAYER_ASSISTS, (player_id,))


def add_player_games(connection, player_id):
    with connection:
        connection.execute(UPDATE_PLAYER_GAMES, (player_id,))


def clear_stats(connection):
    with connection:
        connection.execute(CLEAR_STATS)


def add_columns(connection):
    with connection:
        connection.execute(ADD_COLUMNS)


def get_players_points(connection, player_id):
    with connection:
        return connection.execute(GET_PLAYERS_POINTS, (player_id,)).fetchall()
