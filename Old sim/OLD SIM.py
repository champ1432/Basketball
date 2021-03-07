# from Rosters import Mavs, Heat
# import random
# import DB
#
# print(random.randint(0, 1))
# DB.c.execute("SELECT Players.name, Players.position FROM Players WHERE team_id = 1 OR team_id = 2")
# x = DB.c.fetchall()
#
# DB.c.execute("SELECT Players.name From Players WHERE position = 'C' AND team_id =1")
# centers = DB.c.fetchall()
# DB.c.execute("SELECT Players.name From Players WHERE position = 'C' AND team_id = 2")
# center = DB.c.fetchall()
#
#
# def commentary():
#     print(
#         "Welcome to tonight's game where the visiting Miami Heat square off against the Dallas Mavericks at the "
#         "American Airlines Center. \nThe starting Lineups:")
#     print("{}: {}".format(Mavs, Heat))
#
# commentary()