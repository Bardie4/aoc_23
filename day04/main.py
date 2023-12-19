###############
### Silver ###
###############
with open('in.txt') as f:
    lines = f.read().splitlines()

# line looks like this: Card x: 10 11 12 13 14 | 22 24 27 29 40
points = 0
for line in lines:
    # parse numbers before |
    card, nums = line.split(':')
    nums = nums.split('|')[0].strip().replace("  ", " ").split(' ')
    nums = [int(n) for n in nums]
    # parse numbers after |
    nums2 = line.split('|')[1].strip().replace("  ", " ").split(' ')
    nums2 = [int(n) for n in nums2]
    # check if there are any numbers in common
    common = [n for n in nums if n in nums2]

    _points = 0
    for _ in common:
        if _points == 0:
            _points = 1
        else:
            _points *= 2

    points += _points

print("silver: ", points)

###############
### Gold #####
###############
with open('in.txt') as f:
    lines = f.read().splitlines()

# line looks like this: Card x: 10 11 12 13 14 | 22 24 27 29 40
cards = [1] * len(lines)

for index, line in enumerate(lines):
    # parse numbers before |
    card, nums = line.split(':')
    nums = nums.split('|')[0].strip().replace("  ", " ").split(' ')
    nums = [int(n) for n in nums]

    # parse numbers after |
    nums2 = line.split('|')[1].strip().replace("  ", " ").split(' ')
    nums2 = [int(n) for n in nums2]

    # check if there are any numbers in common
    wins = [n for n in nums if n in nums2]
    draw_current = cards[index]

    for card_i, win in enumerate(wins, start=index + 1):
        cards[card_i] += draw_current

res = sum(cards)
print("gold: ", res)
