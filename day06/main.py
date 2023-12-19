import numpy as np

times=[46,85,75,82]
distances = [208, 1412, 1257, 1410]

################
#### Silver ####
################
outcomes = []
for time in times:

    outcomes_for_time = []
    for t in range(time + 1):
        outcome = t * (time - t)
        outcomes_for_time.append(outcome)

    outcomes.append(outcomes_for_time)


wins = []
for game, distance in zip(outcomes, distances):
    wins_for_game = []
    for outcome in game:
        if outcome > distance:
            wins_for_game.append(outcome)
    wins.append(wins_for_game)

print(wins)

bag = []
for win in wins:
    bag.append(len(win))

print("silver: ", np.prod(bag))

################
#### Gold ######
################
time = 46857582
distance = 208141212571410

times = range(0, time + 1)

def f(t):
    return t * (time - t)

def find_first_win(range1):
    for i, t in enumerate(range1):
        if f(t) > distance:
            return i
        
min = find_first_win(times)
max = time - find_first_win(reversed(times))

print("gold: ", max - min + 1)
