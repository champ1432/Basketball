from App import PlayerDB
import random
import time

connection = PlayerDB.connect()

quarter_clock = 100
qc = 12 * 60
home_score = 0
away_score = 0
x = True
i = 0
pos = 0

home = PlayerDB.connect_players_teams(connection, 5, 1)
away = PlayerDB.connect_players_teams(connection, 5, 2)

home_point_guard = PlayerDB.get_players_by_position(connection, 1, 1)
away_point_guard = PlayerDB.get_players_by_position(connection, 1, 2)

home_shooting_guard = PlayerDB.get_players_by_position(connection, 2, 1)
away_shooting_guard = PlayerDB.get_players_by_position(connection, 2, 2)

home_small_forward = PlayerDB.get_players_by_position(connection, 3, 1)
away_small_forward = PlayerDB.get_players_by_position(connection, 3, 2)

home_power_forward = PlayerDB.get_players_by_position(connection, 4, 1)
away_power_forward = PlayerDB.get_players_by_position(connection, 4, 2)

home_center = PlayerDB.get_players_by_position(connection, 5, 1)
away_center = PlayerDB.get_players_by_position(connection, 5, 2)


def jump_ball():
    global pos
    if pos == 0:
        print(
            f"{home_center[0][0]} {home_center[0][1]} and {away_center[0][0]} {away_center[0][1]} will square off for the jump!")
        outcome = random.randint(0, 1)
        if outcome == 0:
            print(f"{home_center[0][1]} wins the jump. The {home[0][2]} will start the game with the ball.")
            pos = int(f"{home_center[0][2]}")
        else:
            print(f"{away_center[0][1]} wins the jump. The {away[0][2]} will start the game with the ball.")
            pos = int(f"{away_center[0][2]}")


def play14():
    global home_score, away_score, quarter_clock, pos, time_runoff
    screen_success = random.randint(0, 3)
    decision = random.randint(0, 2)
    shot_success = random.randint(0, 1)
    last_second = random.randint(0, 1)
    if pos == 1:
        print(
            f"\n{home_point_guard[0][0]} {home_point_guard[0][1]} is bringing the ball down the court for the {home[0][2]}.")
        print(
            f"{home_point_guard[0][0]} passes it to {home_shooting_guard[0][0]} {home_shooting_guard[0][1]}. He cuts to the basket off a {home_power_forward[0][0]} {home_power_forward[0][1]} screen. ")
        if screen_success == 0:
            print(f"{home_shooting_guard[0][1]} passes it to the cutting {home_point_guard[0][1]}.")
            if decision == 0:
                print(f"{home_point_guard[0][1]} lays it up...")
                if shot_success == 0:
                    print("MISSES!")
                    pos = 2
                    quarter_clock = quarter_clock - time_runoff
                    print(quarter_clock)
                elif shot_success == 1:
                    print("IT'S GOOD!")
                    home_score += 2
                    pos = 2
                    quarter_clock = quarter_clock - time_runoff
                    print(quarter_clock)
            elif decision == 1:
                print(f"{home_point_guard[0][1]} dribbles. Pulls Up...")
                if shot_success == 0:
                    print("MISSES!")
                    pos = 2
                    quarter_clock = quarter_clock - time_runoff
                    print(quarter_clock)
                elif shot_success == 1:
                    print("IT'S GOOD!")
                    home_score += 2
                    pos = 2
                    quarter_clock = quarter_clock - time_runoff
                    print(quarter_clock)
            elif decision == 2:
                print(
                    f"{home_point_guard[0][1]} can not find a shot. He passes it out to {home_small_forward[0][0]} {home_small_forward[0][1]}. {home_small_forward[0][1]} gives it to {home_shooting_guard[0][1]}. He cuts off of {home_center[0][0]} {home_center[0][1]}.")
                if screen_success == 0:
                    print(
                        f"{home_shooting_guard[0][1]} passes it to the cutting {home_small_forward[0][1]}.\n He takes the shot...")
                    if shot_success == 0:
                        print("MISSES!")
                        pos = 2
                        quarter_clock = quarter_clock - time_runoff
                        print(quarter_clock)
                    elif shot_success == 1:
                        print("IT'S GOOD!")
                        home_score += 2
                        pos = 2
                        quarter_clock = quarter_clock - time_runoff
                        print(quarter_clock)
                else:
                    print(f"{home_center[0][1]} sets a pick for {home_shooting_guard[0][1]}.")
                    if decision == 0:
                        print(
                            f"{home_shooting_guard[0][1]} gives a bounce pass to the cutting {home_center[0][1]}. He goes up for the shot...")
                        if shot_success == 0:
                            print("MISSES!")
                            pos = 2
                            quarter_clock = quarter_clock - time_runoff
                            print(quarter_clock)
                        elif shot_success == 1:
                            print("IT'S GOOD!")
                            home_score += 2
                            pos = 2
                            quarter_clock = quarter_clock - time_runoff
                            print(quarter_clock)
                    elif decision == 1:
                        print(f"{home_shooting_guard[0][1]} uses the screen. Steps back. Fires...")
                        if shot_success == 0:
                            print("MISSES!")
                            pos = 2
                            quarter_clock = quarter_clock - time_runoff
                            print(quarter_clock)
                        elif shot_success == 1:
                            print("IT'S GOOD!")
                            home_score += 3
                            pos = 2
                            quarter_clock = quarter_clock - time_runoff
                            print(quarter_clock)
                    elif decision == 2:
                        print(
                            f"{home_shooting_guard[0][1]} dribbles around the screen and kicks it to {home_point_guard[0][0]}.")
                        if last_second == 0:
                            print(f"{home_point_guard[0][1]} Fires...")
                            if shot_success == 0:
                                print("MISSES!")
                                pos = 2
                                quarter_clock = quarter_clock - time_runoff
                                print(quarter_clock)
                            elif shot_success == 1:
                                print("IT'S GOOD!")
                                home_score += 3
                                pos = 2
                                quarter_clock = quarter_clock - time_runoff
                                print(quarter_clock)
                        elif last_second == 1:
                            print(f"{home_point_guard[0][1]} kicks it to {home_power_forward[0][1]} for the mid-range.")
                            if shot_success == 0:
                                print("MISSES!")
                                pos = 2
                                quarter_clock = quarter_clock - time_runoff
                                print(quarter_clock)
                            elif shot_success == 1:
                                print("IT'S GOOD!")
                                home_score += 2
                                pos = 2
                                quarter_clock = quarter_clock - time_runoff
                                print(quarter_clock)
        else:
            print(f"{home_shooting_guard[0][1]} receives a screen from {home_power_forward[0][1]}.")
            if decision == 0:
                print(
                    f"{home_shooting_guard[0][1]} gives a bounce pass to the cutting {home_power_forward[0][1]}. He goes up for the shot...")
                if shot_success == 0:
                    print("MISSES!")
                    pos = 2
                    quarter_clock = quarter_clock - time_runoff
                    print(quarter_clock)
                elif shot_success == 1:
                    print("IT'S GOOD!")
                    home_score += 2
                    pos = 2
                    quarter_clock = quarter_clock - time_runoff
                    print(quarter_clock)
            elif decision == 1:
                print(f"{home_shooting_guard[0][1]} uses the screen. Steps back. Fires...")
                if shot_success == 0:
                    print("MISSES!")
                    pos = 2
                    quarter_clock = quarter_clock - time_runoff
                    print(quarter_clock)
                elif shot_success == 1:
                    print("IT'S GOOD!")
                    home_score += 3
                    pos = 2
                    quarter_clock = quarter_clock - time_runoff
                    print(quarter_clock)
            elif decision == 2:
                print(
                    f"{home_shooting_guard[0][1]} dribbles around the screen and kicks it to {home_small_forward[0][0]}. He dishes it over to {home_point_guard[0][1]}.")
                print(f"{home_small_forward[0][1]} cuts off a screen given by {home_center[0][1]}.")
                if decision == 0:
                    print(f"{home_small_forward[0][1]} receives the pass and goes up for the shot...")
                    if shot_success == 0:
                        print("MISSES!")
                        pos = 2
                        quarter_clock = quarter_clock - time_runoff
                        print(quarter_clock)
                    elif shot_success == 1:
                        print("IT'S GOOD!")
                        home_score += 2
                        pos = 2
                        quarter_clock = quarter_clock - time_runoff
                        print(quarter_clock)
                elif decision == 1:
                    print(
                        f'{home_center[0][1]} gives {home_point_guard[0][1]} a screen. He goes around it, {home_center[0][1]} goes up for the lob...')
                    if shot_success == 0:
                        print("MISSES!")
                        pos = 2
                        quarter_clock = quarter_clock - time_runoff
                        print(quarter_clock)
                    elif shot_success == 1:
                        print("IT'S GOOD!")
                        home_score += 3
                        pos = 2
                        quarter_clock = quarter_clock - time_runoff
                        print(quarter_clock)
                elif decision == 2:
                    print(f"{home_point_guard[0][1]} uses the screen. Steps back. Fires...")
                    if shot_success == 0:
                        print("MISSES!")
                        pos = 2
                        quarter_clock = quarter_clock - time_runoff
                        print(quarter_clock)
                    elif shot_success == 1:
                        print("IT'S GOOD!")
                        home_score += 3
                        pos = 2
                        quarter_clock = quarter_clock - time_runoff
                        print(quarter_clock)
    elif pos == 2:
        print(
            f"\n{away_point_guard[0][0]} {away_point_guard[0][1]} is bringing the ball down the court for the {away[0][2]}.")
        print(
            f"{away_point_guard[0][0]} passes it to {away_shooting_guard[0][0]} {away_shooting_guard[0][1]}. He cuts to the basket off a {away_power_forward[0][0]} {away_power_forward[0][1]} screen. ")
        if screen_success == 0:
            print(f"{away_shooting_guard[0][1]} passes it to the cutting {away_point_guard[0][1]}.")
            if decision == 0:
                print(f"{away_point_guard[0][1]} lays it up...")
                if shot_success == 0:
                    print("MISSES!")
                    pos = 1
                    quarter_clock = quarter_clock - time_runoff
                    print(quarter_clock)
                elif shot_success == 1:
                    print("IT'S GOOD!")
                    away_score += 2
                    pos = 1
                    quarter_clock = quarter_clock - time_runoff
                    print(quarter_clock)
            elif decision == 1:
                print(f"{away_point_guard[0][1]} dribbles. Pulls Up...")
                if shot_success == 0:
                    print("MISSES!")
                    pos = 1
                    quarter_clock = quarter_clock - time_runoff
                    print(quarter_clock)
                elif shot_success == 1:
                    print("IT'S GOOD!")
                    away_score += 2
                    pos = 1
                    quarter_clock = quarter_clock - time_runoff
                    print(quarter_clock)
            elif decision == 2:
                print(
                    f"{away_point_guard[0][1]} can not find a shot. He passes it out to {away_small_forward[0][0]} {away_small_forward[0][1]}. {away_small_forward[0][1]} gives it to {away_shooting_guard[0][1]}. He cuts off of {away_center[0][0]} {away_center[0][1]}.")
                if screen_success == 0:
                    print(
                        f"{away_shooting_guard[0][1]} passes it to the cutting {away_small_forward[0][1]}. \n He takes the shot...")
                    if shot_success == 0:
                        print("MISSES!")
                        pos = 1
                        quarter_clock = quarter_clock - time_runoff
                        print(quarter_clock)
                    elif shot_success == 1:
                        print("IT'S GOOD!")
                        away_score += 2
                        pos = 1
                        quarter_clock = quarter_clock - time_runoff
                        print(quarter_clock)
                else:
                    print(f"{away_center[0][1]} sets a pick for {away_shooting_guard[0][1]}.")
                    if decision == 0:
                        print(
                            f"{away_shooting_guard[0][1]} gives a bounce pass to the cutting {away_center[0][1]}. He goes up for the shot...")
                        if shot_success == 0:
                            print("MISSES!")
                            pos = 1
                            quarter_clock = quarter_clock - time_runoff
                            print(quarter_clock)
                        elif shot_success == 1:
                            print("IT'S GOOD!")
                            away_score += 2
                            pos = 1
                            quarter_clock = quarter_clock - time_runoff
                            print(quarter_clock)
                    elif decision == 1:
                        print(f"{away_shooting_guard[0][1]} uses the screen. Steps back. Fires...")
                        if shot_success == 0:
                            print("MISSES!")
                            pos = 1
                            quarter_clock = quarter_clock - time_runoff
                            print(quarter_clock)
                        elif shot_success == 1:
                            print("IT'S GOOD!")
                            away_score += 3
                            pos = 1
                            quarter_clock = quarter_clock - time_runoff
                            print(quarter_clock)
                    elif decision == 2:
                        print(
                            f"{away_shooting_guard[0][1]} dribbles around the screen and kicks it to {away_point_guard[0][0]}.")
                        if last_second == 0:
                            print(f"{away_point_guard[0][1]} Fires...")
                            if shot_success == 0:
                                print("MISSES!")
                                pos = 1
                                quarter_clock = quarter_clock - time_runoff
                                print(quarter_clock)
                            elif shot_success == 1:
                                print("IT'S GOOD!")
                                away_score += 3
                                pos = 1
                                quarter_clock = quarter_clock - time_runoff
                                print(quarter_clock)
                        elif last_second == 1:
                            print(f"{away_point_guard[0][1]} kicks it to {away_power_forward[0][1]} for the mid-range.")
                            if shot_success == 0:
                                print("MISSES!")
                                pos = 1
                                quarter_clock = quarter_clock - time_runoff
                                print(quarter_clock)
                            elif shot_success == 1:
                                print("IT'S GOOD!")
                                away_score += 2
                                pos = 1
                                quarter_clock = quarter_clock - time_runoff
                                print(quarter_clock)
        else:
            print(f"{away_shooting_guard[0][1]} receives a screen from {away_power_forward[0][1]}.")
            if decision == 0:
                print(
                    f"{away_shooting_guard[0][1]} gives a bounce pass to the cutting {away_power_forward[0][1]}. He goes up for the shot...")
                if shot_success == 0:
                    print("MISSES!")
                    pos = 1
                    quarter_clock = quarter_clock - time_runoff
                    print(quarter_clock)
                elif shot_success == 1:
                    print("IT'S GOOD!")
                    away_score += 2
                    pos = 1
                    quarter_clock = quarter_clock - time_runoff
                    print(quarter_clock)
            elif decision == 1:
                print(f"{away_shooting_guard[0][1]} uses the screen. Steps back. Fires...")
                if shot_success == 0:
                    print("MISSES!")
                    pos = 1
                    quarter_clock = quarter_clock - time_runoff
                    print(quarter_clock)
                elif shot_success == 1:
                    print("IT'S GOOD!")
                    away_score += 3
                    pos = 1
                    quarter_clock = quarter_clock - time_runoff
                    print(quarter_clock)
            elif decision == 2:
                print(
                    f"{away_shooting_guard[0][1]} dribbles around the screen and kicks it to {away_small_forward[0][0]}. He dishes it over to {away_point_guard[0][1]}.")
                print(f"{away_small_forward[0][1]} cuts off a screen given by {away_center[0][1]}.")
                if decision == 0:
                    print(f"{away_small_forward[0][1]} receives the pass and goes up for the shot...")
                    if shot_success == 0:
                        print("MISSES!")
                        pos = 1
                        quarter_clock = quarter_clock - time_runoff
                        print(quarter_clock)
                    elif shot_success == 1:
                        print("IT'S GOOD!")
                        away_score += 2
                        pos = 1
                        quarter_clock = quarter_clock - time_runoff
                        print(quarter_clock)
                elif decision == 1:
                    print(
                        f'{away_center[0][1]} gives {away_point_guard[0][1]} a screen. He goes around it, {away_center[0][1]} goes up for the lob...')
                    if shot_success == 0:
                        print("MISSES!")
                        pos = 1
                        quarter_clock = quarter_clock - time_runoff
                        print(quarter_clock)
                    elif shot_success == 1:
                        print("IT'S GOOD!")
                        away_score += 3
                        pos = 1
                        quarter_clock = quarter_clock - time_runoff
                        print(quarter_clock)
                elif decision == 2:
                    print(f"{away_point_guard[0][1]} uses the screen. Steps back. Fires...")
                    if shot_success == 0:
                        print("MISSES!")
                        pos = 1
                        quarter_clock = quarter_clock - time_runoff
                        print(quarter_clock)
                    elif shot_success == 1:
                        print("IT'S GOOD!")
                        away_score += 3
                        pos = 1
                        quarter_clock = quarter_clock - time_runoff
                        print(quarter_clock)


def score():
    print("{}: {}\n{}: {}".format(home[0][2], home_score, away[0][2], away_score))


def first_quarter():
    global quarter_clock, time_runoff
    jump_ball()
    while quarter_clock > 0:
        play14()
        score()
        if time_runoff > quarter_clock:
            time_runoff = quarter_clock
            if quarter_clock == 0:
                break
            quarter_clock = 100


def quarter_sim():
    global quarter_clock, time_runoff
    while quarter_clock > 0:
        play14()
        score()
        if time_runoff > quarter_clock:
            time_runoff = quarter_clock
            if quarter_clock == 0:
                break
            quarter_clock = 100


def game_sim():
    first_quarter()
    quarter_sim()
    quarter_sim()
    quarter_sim()


def wack():
    global qc
    while qc > 0:
        ty_res = time.gmtime(qc)
        print(time.strftime('%M:%S', ty_res))
        run = random.randrange(10, 24)
        qc = qc - run
    qc = 0
    ty_res = time.gmtime(qc)
    print(time.strftime("%M:%S", ty_res), "\nEnd of Quarter")


wack()
