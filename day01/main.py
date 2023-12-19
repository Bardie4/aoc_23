import re

# Read file as lines, remove newlines
with open('in.txt') as file:
    file = file.read().splitlines()

##################
##### Silver #####
##################
# Remove all characters that are not 0-9
bag = []
for line in file:
    line = re.sub(r'\D', '', line)
    bag.append(str(line)[0] + str(line)[-1])

for index, item in enumerate(bag):
    bag[index] = int(item)

print("silver:", sum(bag))

##################
###### Gold ######
##################
num_str = ['###', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# Sliding window
def sliding_window(array, window_size):
    for i in range(len(array) - window_size + 1):
        yield array[i:i + window_size]

def find_first(line, reverse = False):
    window_size = 5
    if len(line) < window_size:
        window_size = len(line)

    for window in list(sliding_window(line, window_size)):

        if reverse:
            window = window[::-1]
        # Check for integer value in window
        digit = re.search(r'\d', window if not reverse else window[::-1])
        digit_str = re.search(r'one|two|three|four|five|six|seven|eight|nine', window)

        if digit:
            digit_index = window.index(digit.group())

        if digit_str:
            digit_str_index = window.index(digit_str.group())

        # Add the integer value that has the lowest index
        if digit and digit_str:
            if not reverse:
                if digit_index < digit_str_index:
                    return digit.group()
                else:
                    return num_str.index(digit_str.group())
            else:
                if digit_index > digit_str_index:
                    return digit.group()
                else:
                    return num_str.index(digit_str.group())
        elif digit:
            return digit.group()
        elif digit_str:
            return num_str.index(digit_str.group())

bag = []
for line in file:
    first = find_first(line)
    last = find_first(line[::-1], reverse=True)
    res = int(str(first) + str(last))
    bag.append(res)

print("gold: ", sum(bag))