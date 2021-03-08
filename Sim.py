from Lineups import *
from time import sleep

# connect to DataBase
connection = PlayerDB.connect()

# basic Sim settings:
# scores, who has possession(0-1), time of game, amount of time run by shot clock, amount of time left, print timers
home_score = 0
away_score = 0
pos = 0
t = 12
quarter_clock = t * 60
time_runoff = random.randint(10, 24)
time_of_possession = quarter_clock - time_runoff
game_timer = .75
intro_timer = 1


# print commentary for live sim
def commentary():
    sleep(intro_timer)
    print("Welcome to {}, where the visiting {} {} will square off against the {}.".format(home[0][1], away[0][1],
                                                                                           away[0][2], home[0][2]))


# lineup variables
home_starting = f"Starting Lineups for the {home[0][2]}: \n {home_point_guard[0][0]} {home_point_guard[0][1]} \n {home_shooting_guard[0][0]} {home_shooting_guard[0][1]}  \n {home_small_forward[0][0]} {home_small_forward[0][1]} \n {home_power_forward[0][0]} {home_power_forward[0][1]} \n {home_center[0][0]} {home_center[0][1]} \n"
away_starting = f"Starting Lineups for the {away[0][2]}: \n {away_point_guard[0][0]} {away_point_guard[0][1]} \n {away_shooting_guard[0][0]} {away_shooting_guard[0][1]}  \n {away_small_forward[0][0]} {away_small_forward[0][1]} \n {away_power_forward[0][0]} {away_power_forward[0][1]} \n {away_center[0][0]} {away_center[0][1]} \n"


# print lineups for live sim
def starting_lineups():
    sleep(intro_timer)
    print(home_starting + '\n' + away_starting)


# live sim play-by-play for jump
def ljump_ball():
    global pos
    if pos == 0:
        sleep(intro_timer)
        print(
            f"{home_center[0][0]} {home_center[0][1]} and {away_center[0][0]} {away_center[0][1]} will square off for the jump!")
        outcome = random.randint(0, 1)
        if outcome == 0:
            sleep(intro_timer)
            print(f"{home_center[0][1]} wins the jump. The {home[0][2]} will start the game with the ball.")
            pos = int(f"{home[0][0]}")
        else:
            sleep(intro_timer)
            print(f"{away_center[0][1]} wins the jump. The {away[0][2]} will start the game with the ball.")
            pos = int(f"{away[0][0]}")


# jump ball for quick sim
def qjump_ball():
    global pos
    if pos == 0:
        sleep(intro_timer)
        outcome = random.randint(0, 1)
        if outcome == 0:
            sleep(intro_timer)
            pos = int(f"{home[0][0]}")
        else:
            sleep(intro_timer)
            pos = int(f"{away[0][0]}")


# live sim play-by-play
def lsim():
    global quarter_clock, home_score, away_score, pos, time_of_possession
    shot_success = random.randint(0, 1)
    last_second_shot = random.randint(0, 2)
    if pos == home_team:
        shooter = random.choice(home_players_on_court)
        if quarter_clock > 24:
            if shot_success == 0:
                sleep(game_timer)
                print("\n{} {} misses it.".format(shooter[0][0], shooter[0][1]))
                quarter_clock = quarter_clock - random.randint(10, 24)
                minutes, seconds = divmod(quarter_clock, 60)
                print(f"{home[0][2]}: {home_score} - {away[0][2]}: {away_score}    \n{minutes}:{seconds:02d} remaining")
                pos = away_team
            elif shot_success == 1:
                sleep(game_timer)
                print("\n{} {} makes it.".format(shooter[0][0], shooter[0][1]))
                home_score = home_score + 2
                quarter_clock = quarter_clock - random.randint(10, 24)
                minutes, seconds = divmod(quarter_clock, 60)
                print(f"{home[0][2]}: {home_score} - {away[0][2]}: {away_score}    \n{minutes}:{seconds:02d} remaining")
                pos = away_team
        else:
            if last_second_shot == 1:
                sleep(game_timer)
                print(f"\n{shooter[0][0]} {shooter[0][1]} MAKES IT AT THE BUZZER!")
                home_score = home_score + 2
                quarter_clock = 0
                print(f"{quarter_clock}:00 END OF QUARTER! \n{home[0][2]}: {home_score} - {away[0][2]}: {away_score}")
            else:
                sleep(game_timer)
                print(f"\n{shooter[0][0]} {shooter[0][1]} misses it at the buzzer.")
                quarter_clock = 0
                print(f"{quarter_clock}:00 END OF QUARTER! \n{home[0][2]}: {home_score} - {away[0][2]}: {away_score}")
    elif pos == away_team:
        shooter = random.choice(away_players_on_court)
        if quarter_clock > 24:
            if shot_success == 0:
                sleep(game_timer)
                print("\n{} {} misses it.".format(shooter[0][0], shooter[0][1]))
                quarter_clock = quarter_clock - random.randint(10, 24)
                minutes, seconds = divmod(quarter_clock, 60)
                print(f"{home[0][2]}: {home_score} - {away[0][2]}: {away_score}    \n{minutes}:{seconds:02d} remaining")
                pos = home_team
            elif shot_success == 1:
                sleep(game_timer)
                print("\n{} {} makes it.".format(shooter[0][0], shooter[0][1]))
                away_score = away_score + 2
                quarter_clock = quarter_clock - random.randint(10, 24)
                minutes, seconds = divmod(quarter_clock, 60)
                print(f"{home[0][2]}: {home_score} - {away[0][2]}: {away_score}    \n{minutes}:{seconds:02d} remaining")
                pos = home_team
        else:
            if last_second_shot == 1:
                sleep(game_timer)
                print(f"\n{shooter[0][0]} {shooter[0][1]} MAKES IT AT THE BUZZER!")
                away_score = away_score + 2
                quarter_clock = 0
                print(f"{quarter_clock}:00 END OF QUARTER! \n{home[0][2]}: {home_score} - {away[0][2]}: {away_score}")
            else:
                sleep(game_timer)
                print(f"\n{shooter[0][0]} {shooter[0][1]} misses it at the buzzer.")
                quarter_clock = 0
                print(f"{quarter_clock}:00 END OF QUARTER! \n{home[0][2]}: {home_score} - {away[0][2]}: {away_score}")


# quick sim
def qsim():
    global quarter_clock, home_score, away_score, pos, time_of_possession
    shot_success = random.randint(0, 1)
    last_second_shot = random.randint(0, 2)
    if pos == home_team:
        if quarter_clock > 24:
            if shot_success == 0:
                quarter_clock = quarter_clock - random.randint(10, 24)
                pos = away_team
            elif shot_success == 1:
                home_score = home_score + 2
                quarter_clock = quarter_clock - random.randint(10, 24)
                pos = away_team
        else:
            if last_second_shot == 1:
                home_score = home_score + 2
                quarter_clock = 0
            else:
                quarter_clock = 0
    elif pos == away_team:
        if quarter_clock > 24:
            if shot_success == 0:
                quarter_clock = quarter_clock - random.randint(10, 24)
                pos = home_team
            elif shot_success == 1:
                away_score = away_score + 2
                quarter_clock = quarter_clock - random.randint(10, 24)
                pos = home_team
        else:
            if last_second_shot == 1:
                away_score = away_score + 2
                quarter_clock = 0
            else:
                quarter_clock = 0


# live quarter sim
def lquarter_sim():
    global quarter_clock
    quarter_clock = t * 60
    while quarter_clock > 0:
        lsim()


# quick quarter sim
def qquarter_sim():
    global quarter_clock
    quarter_clock = t * 60
    while quarter_clock > 0:
        qsim()


# live sim = play-by-play
def live_sim():
    commentary()
    starting_lineups()
    ljump_ball()
    lquarter_sim()
    lquarter_sim()
    lquarter_sim()
    lquarter_sim()


# quick sim
def quick_sim():
    qjump_ball()
    qquarter_sim()
    qquarter_sim()
    qquarter_sim()
    qquarter_sim()
    print(f"Final Score \n{home[0][2]}: {home_score} - {away[0][2]}: {away_score}")

# runs function in this file
if __name__ == "__main__":
    quick_sim()
