from dataclasses import dataclass
import re


@dataclass
class Throw:
    red: int
    green: int
    blue: int

    def __init__(self, throw):
        try:
            self.red = int(re.search(r"(\d+)red", throw).group(1))
        except:
            self.red = 0

        try:
            self.green = int(re.search(r"(\d+)green", throw).group(1))
        except:
            self.green = 0

        try:
            self.blue = int(re.search(r"(\d+)blue", throw).group(1))
        except:
            self.blue = 0

@dataclass
class Game:
    throws: list[Throw]


def parse(input: str) -> list[Game]:
    # Read input, remove \n, remove spaces
    with open(input, 'r') as f:
        lines = f.read().splitlines()
        lines = [line.split(":")[1].replace(" ", "").split(";") for line in lines]

    games: list[Game] = []
    for line in lines:
        game = Game([])
        for throw in line:
            game.throws.append(Throw(throw))
        games.append(game)

    return games

##################
##### Silver #####
##################
# Determine which games would have been possible if the bag had been 
# loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes.

def throws_possible(throws: list[Throw]) -> bool:
    max_red = 12
    max_green = 13
    max_blue = 14

    for throw in throws:
        if  throw.red > max_red or throw.green > max_green or throw.blue > max_blue:
            return False
    
    return True


games = parse("in.txt")

silver = 0
for i, game in enumerate(games):
    if throws_possible(game.throws):
        print(f"{i+1} ✅", end=" ")
        silver += i+1

print(f"\nSilver: {silver}")

##################
###### Gold ######
##################

# Gold
# Determine which the minimum number of cubes that would have to be added
# to the bag to make each game possible.

def minimum_cubes(throws: list[Throw]) -> bool:
    min_red = 0
    min_green = 0
    min_blue = 0

    for throw in throws:
        if throw.red > min_red:
            min_red = throw.red
        if throw.green > min_green:
            min_green = throw.green
        if throw.blue > min_blue:
            min_blue = throw.blue

    return min_red * min_green * min_blue

games = parse("in.txt")

gold = 0
for i, game in enumerate(games):
    gold += minimum_cubes(game.throws)

print(f"Gold: {gold}")
