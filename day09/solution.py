#%%

def extrapolate(line, p2 = False):
    next_seq = []

    for i in range(len(line) - 1):
        next_seq.append(line[i + 1] - line[i])

    if not any(next_seq):
        return line[-1] + next_seq[-1]

    value = extrapolate(next_seq, p2)

    if p2:
        return line[0] - value

    return line[-1] + value    


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        data = f.read().splitlines()
        data = [list(map(int, x.split(' '))) for x in data]

    extrapolated = sum([extrapolate(line) for line in data])
    extrapolated_p2 = sum([extrapolate(line, True) for line in data])

    print(extrapolated)
    print(extrapolated_p2)
