import argparse

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

# parse input into a 2d array
def parse_input(input: str):
    with open(input, 'r') as f:
        data = f.read().splitlines()
        data = [list(x) for x in data]

    return data

def find_start(data: list):
    # Find S
    y, row = next(((y, row) for y, row in enumerate(data) if 'S' in row))
    x = row.index('S')
    return (x, y)

# Get all neighboring nodes, that point to the current node
def get_neighbors(x, y):
    neighbors = []
    # left
    if x > 0 and data[y][x-1] in ["-", "L", "F"]:
        neighbors.append((x-1, y))
    # right
    if x < len(data[y]) - 1 and data[y][x+1] in ["-", "J", "7"]:
        neighbors.append((x+1, y))
    # up
    if y > 0 and data[y-1][x] in ["|", "F", "7"]:
        neighbors.append((x, y-1))
    # down
    if y < len(data) - 1 and data[y+1][x] in ["|", "L", "J"]:
        neighbors.append((x, y+1))
    return neighbors

def build_graph(data: list, start: tuple):
    graph = {}

    nodes = [start]
    while True:
        x, y = nodes.pop()

        neighbors = get_neighbors(x, y)
        
        graph[(x, y)] = neighbors
        nodes.extend(neighbors)

        if len(nodes) == 0:
            break

    return graph
        

        

if __name__ == '__main__':
    # accept one unnamed argument from the commandline
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    args = parser.parse_args()

    data = parse_input(args.input)
    print(data)

    start = find_start(data)

    graph = build_graph(data, start)
    print(graph)

