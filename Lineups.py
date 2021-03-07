from App import PlayerDB, TeamDB, PlayerStatsDB
import random

teams = [1, 2, 3, 4]
teams_playing = []
home_team = (random.choice(teams))
if home_team in teams:
    teams.remove(home_team)
    teams_playing.append(home_team)
away_team = (random.choice(teams))
if away_team in teams:
    teams.remove(away_team)
    teams_playing.append(away_team)

connection = PlayerDB.connect()

home = TeamDB.get_teams_by_tid(connection, home_team)
away = TeamDB.get_teams_by_tid(connection, away_team)

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

home_players_on_court = [home_point_guard, home_shooting_guard, home_small_forward, home_power_forward, home_center]
away_players_on_court = [away_point_guard, away_shooting_guard, away_small_forward, away_power_forward, away_center]

