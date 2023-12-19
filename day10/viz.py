# parse input into a 2d array
def parse_input(input: str):
    with open(input, 'r') as f:
        data = f.read().splitlines()
        data = [list(x) for x in data]

    return data

def replace_with_pipes(data: list):
    for y, row in enumerate(data):
        for x, col in enumerate(row):
            if col == '.':
                data[y][x] = ' '
            elif col == '|':
                data[y][x] = '║'
            elif col == '-':
                data[y][x] = '═'
            elif col == 'L':
                data[y][x] = '╚'
            elif col == 'J':
                data[y][x] = '╝'
            elif col == '7':
                data[y][x] = '╗'
            elif col == 'F':
                data[y][x] = '╔'

    return data

def vizualise(data: list):
    for row in data:
        print(''.join(row))

def traverse(data: list, start: tuple):
    n_traversed = 0
    x, y = start
    move = None
    while True:
        

        n_traversed += 1
        print(data[y][x])



data = parse_input('in.txt')
data = replace_with_pipes(data)

vizualise(data)