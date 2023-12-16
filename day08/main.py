# Input looks like this:
# RL
# 
# AAA = (BBB, CCC)
# BBB = (DDD, EEE)
# CCC = (ZZZ, GGG)
# DDD = (DDD, DDD)
# EEE = (EEE, EEE)
# GGG = (GGG, GGG)
# ZZZ = (ZZZ, ZZZ)
from itertools import cycle
from math import lcm
import re
from time import sleep


def input_to_list(file):
    with open(file) as f:
        data = f.read().splitlines()

    commands = data[0]
    mappings = []
    for line in data[2:]:
        # regex match three characters in a row
        x, y, z = re.findall(r'\w{3}', line)
        mappings.append([x, y, z])

    return commands, mappings
    
def list_to_graph(mappings):
    graph = {}
    for x, y, z in mappings:
        graph[x] = (y, z)
    return graph

def traverse(graph, commands, key, target):
    node = graph[key]
    steps  = 0
    while True:
        for command in commands:
            print(f"Current node: {key}: {node}")
            steps += 1
            if command == "L":
                key, node = node[0], graph[node[0]]
            else:
                key, node = node[1], graph[node[1]]

            if key == target:
                return steps

def traverse_multi(graph: dict, commands):
    # filter the graph to only contain keys that end with A
    nodes = {k: v for k, v in graph.items() if k.endswith("A")}
    bag = [0] * len(nodes)

    for i, node in enumerate(nodes):
        print(i, node)
        c = cycle(commands)
        pos = node
        while not pos.endswith("Z"):
            bag[i] += 1
            command = 0 if next(c) == "L" else 1
            pos = graph[pos][command]
            # pos = nodes[pos][next(c)]

    return bag
            
commands, mappings = input_to_list("in.txt")
graph = list_to_graph(mappings)

key = "AAA"
target = "ZZZ"

totals = traverse_multi(graph, commands)
print(lcm(*totals))
            
