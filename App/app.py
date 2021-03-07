from App.app_functions import *

# Create Main Menu
MAIN_MENU = """-- BASKETBALL --
Choose an option:

A: Players
B: Teams 
C: Tables

Your selection:"""

# Create Player Menu
PLAYER_MENU = """-- PLAYERS --
Choose an option:

1) Add player
2) See all players
3) Find a player by name
4) Find a player by team
5) Find a player by player id
6) Delete a player
7) Add player by primary key
8) Add new column
9) Back
10) Exit

Your selection:"""

# Create Team Menu
TEAM_MENU = """-- TEAMS --
Choose an option:

1) Add team
2) See all teams
3) Back
10) Exit

Your selection:"""

# Create Player Stats Menu
PLAYER_STATS_MENU = """-- PLAYER STATS --
Choose an option:

1) Add player
2) 
3) Back
10) Exit

Your selection:"""


# Main Function That Runs Menus
def menu():
    connection = PlayerDB.connect()
    PlayerDB.create_player_table(connection)
    TeamDB.create_team_table(connection)
    PlayerStatsDB.create_player_stats_table(connection)
    main = input(MAIN_MENU).upper()
    if main == "A":
        while (user_input := input(PLAYER_MENU)) != "10":
            if user_input == "1":
                add_new_player(connection)
            elif user_input == "2":
                see_all_players(connection)
            elif user_input == "3":
                find_player_by_name(connection)
            elif user_input == "4":
                find_player_by_team(connection)
            elif user_input == "5":
                find_player_by_playerid(connection)
            elif user_input == '6':
                delete_player(connection)
            elif user_input == '7':
                add_primary_key(connection)
            elif user_input == '8':
                add_new_column(connection)
            elif user_input == '9':
                menu()
            else:
                print("Invalid input, please try again.")
    elif main == "B":
        while (user_input := input(TEAM_MENU)) != "10":
            if user_input == "1":
                add_team(connection)
            elif user_input == "2":
                see_all_teams(connection)
            elif user_input == "3":
                menu()
    elif main == "C":
        while (user_input := input(PLAYER_STATS_MENU)) != "10":
            if user_input == "1":
                add_new_player_stats(connection)
            elif user_input == "2":
                print("WORK IN PROGRESS")
            elif user_input == "3":
                menu()
    else:
        print("Invalid input, please try again.")
        menu()


# menu()
