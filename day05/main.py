from typing import List
from concurrent.futures import ThreadPoolExecutor

file = open("in.txt").read().strip().split("\n\n")

seeds = [int(x) for x in file[0].replace("seeds: ", "").split(" ")]
maps = [
    [[int(y) for y in x.split(" ")] for x in file[i].splitlines()[1::]]
    for i in range(1, 8)
]

print(maps)

###############
### Silver ####
###############
bag = []
for seed in seeds:
    cur = seed
    # print(f"Seed: {seed}")
    for conversion in maps:
        offset_mappings = []
        for dest, src, length in conversion:
            offset_mappings.append([(src, src + length), (dest, dest + length)])

        for src_range, dest_range in offset_mappings:
            src_min, src_max = src_range
            dest_min, dest_max = dest_range

            if src_min <= cur <= src_max:
                cur = dest_min + (cur - src_min)
                break

        # print("->", cur)

    # print(cur)
    bag.append(cur)

print("silver: ", min(bag))


###############
### Gold #####
###############
lowest = 99999999999999
for seed in seeds:
    for cmap in maps:
        from_map = []
        to_map = []
        for line in cmap:
            dest, src, length = line
            destination = list(range(dest, dest + length))
            source = list(range(src, src + length))

            for d, s in zip(destination, source):
                from_map.append(s)
                to_map.append(d)

        if seed in from_map:
            index = from_map.index(seed)
            seed = to_map[index]

    if seed < lowest:
        lowest = seed

print("gold: ", lowest)

