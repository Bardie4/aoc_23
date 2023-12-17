# Silver
with open('in.txt') as f:
    lines = f.read().splitlines()

dirs = [(-1, +1), (0, +1), (+1, +1),
        (-1,  0),          (+1,  0),
        (-1, -1), (0, -1), (+1, -1)]

def has_adjacent_symbol(x, y):
    for dx, dy in dirs:
        try:
            cursor = lines[y + dy][x + dx]
            if not cursor.isnumeric() and not cursor == ".":
                return True
        except IndexError:
            continue
    return False

bag = []
for y, line in enumerate(lines):
    cursor = ""
    adj_symbol = False
    for x, char in enumerate(line):
        if char.isnumeric():
            cursor += char

            if adj_symbol or has_adjacent_symbol(x, y):
                adj_symbol = True
            
            last_char = x == len(line) - 1 or not line[x + 1].isnumeric()
            if last_char and adj_symbol:
                bag.append(int(cursor))
                cursor = ""
                adj_symbol = False
        else:
            cursor = ""
            adj_symbol = False

        
print(sum(bag))