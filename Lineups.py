from App import PlayerDB, TeamDB, PlayerStatsDB
import random

# teams list = number of teams in DB
teams = [1, 2, 3, 4]
teams_playing = []

# chooses random teams to play
home_team = (random.choice(teams))
if home_team in teams:
    teams.remove(home_team)
    teams_playing.append(home_team)
away_team = (random.choice(teams))
if away_team in teams:
    teams.remove(away_team)
    teams_playing.append(away_team)

# connect to DataBase
connection = PlayerDB.connect()

# define home and away teams by the corresponding variable from teams list above
home = TeamDB.get_teams_by_tid(connection, home_team)
away = TeamDB.get_teams_by_tid(connection, away_team)

# defines home and away players
home_point_guard = PlayerDB.get_players_by_position(connection, 1, home_team)
away_point_guard = PlayerDB.get_players_by_position(connection, 1, away_team)

home_shooting_guard = PlayerDB.get_players_by_position(connection, 2, home_team)
away_shooting_guard = PlayerDB.get_players_by_position(connection, 2, away_team)

home_small_forward = PlayerDB.get_players_by_position(connection, 3, home_team)
away_small_forward = PlayerDB.get_players_by_position(connection, 3, away_team)

home_power_forward = PlayerDB.get_players_by_position(connection, 4, home_team)
away_power_forward = PlayerDB.get_players_by_position(connection, 4, away_team)

home_center = PlayerDB.get_players_by_position(connection, 5, home_team)
away_center = PlayerDB.get_players_by_position(connection, 5, away_team)

# defines who is on the court at the moment
home_players_on_court = [home_point_guard, home_shooting_guard, home_small_forward, home_power_forward, home_center]
away_players_on_court = [away_point_guard, away_shooting_guard, away_small_forward, away_power_forward, away_center]


# adds game to players stat
def add_game():
    for player in home_players_on_court:
        PlayerStatsDB.add_player_games(connection, player[0][3])

    for player in away_players_on_court:
        PlayerStatsDB.add_player_games(connection, player[0][3])


# clears Player Stats DataBase
# PlayerStatsDB.clear_stats(connection)
