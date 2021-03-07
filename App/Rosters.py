from App.app import *
from App.PlayerDB import *

conn = PlayerDB.connect()
curs = conn.cursor()


def Mavs(connection):
    players = get_players_by_team(connection, 1)
    dm = []
    for player in players:
        dm.append(f"{player[2]} {player[3]}")
    print(dm)


def Heat(connection):
    players = get_players_by_team(connection, 2)
    mh = []
    for player in players:
        mh.append(f"{player[2]} {player[3]}")
    print(mh)

Mavs(conn)
Heat(conn)