from App import PlayerDB, PlayerStatsDB, TeamDB


# Player Functions
def add_new_player(connection):
    team_id = int(input("Enter team_id:"))
    first_name = input("Enter player's first name:").capitalize()
    last_name = input("Enter player's last name:").capitalize()
    position = int(input("Enter player's position:"))

    PlayerDB.add_player(connection, team_id, first_name, last_name, position)


def see_all_players(connection):
    players = PlayerDB.get_all_players(connection)

    for player in players:
        print(f"{player[2]} {player[3]}, Team: {player[1]}")


def find_player_by_name(connection):
    name = input("Enter player's last name to find:").capitalize()
    players = PlayerDB.get_players_by_name(connection, name)

    for player in players:
        print(f"{player[2]} {player[3]}, Team: {player[1]}")


def find_player_by_team(connection):
    team_id = int(input("Enter the team id corresponding to the team #:"))
    players = PlayerDB.get_players_by_team(connection, team_id)

    for player in players:
        print(f"{player[2]} {player[3]}")


def delete_player(connection):
    player_id = int(input("Enter player's player id to delete:"))

    PlayerDB.delete_player(connection, player_id)


def find_player_by_playerid(connection):
    player_id = int(input("Enter the player id corresponding to the player's #"))
    players = PlayerDB.get_players_by_playerid(connection, player_id)

    for player in players:
        print(f"{player[2]} {player[3]}")


def add_primary_key(connection):
    player_id = int(input("Enter player_id:"))
    team_id = int(input("Enter team_id:"))
    first_name = input("Enter player's first name:").capitalize()
    last_name = input("Enter player's last name:").capitalize()
    position = int(input("Enter player's position:"))

    PlayerDB.insert_primary_key(connection, player_id, team_id, first_name, last_name, position)


# Team Functions
def add_team(connection):
    city = input("Enter the name of the city:").capitalize()
    team_name = input("Enter the name of the team:").capitalize()
    wins = int(input("Enter the amount of wins:"))
    loss = int(input("Enter the amount of losses:"))

    TeamDB.add_team(connection, city, team_name, wins, loss)


def see_all_teams(connection):
    teams = TeamDB.get_all_teams(connection)

    for team in teams:
        print(f"{team[1]} {team[2]}, {team[3]}-{team[4]}")


def add_new_column(connection):
    PlayerDB.add_column(connection)


# Table Functions

def add_new_player_stats(connection):
    pid = int(input("Enter player_id:"))
    points = int(input("Enter player's points:"))
    rebounds = int(input("Enter player's rebounds:"))
    assists = int(input("Enter player's assists:"))

    PlayerStatsDB.add_player_stats(connection, pid, points, rebounds, assists)