#%%
def main():
    histories = [[int(n) for n in line.strip().split()] for line in open("in.txt", "rt").readlines()]

    for history in histories:
        print(history)