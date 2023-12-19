#%%
import argparse
import matplotlib.pyplot as plt
import networkx as nx


# parse input into a 2d array
def parse_input(input: str):
    with open(input, "r") as f:
        data = f.read().splitlines()
        data = [list(x) for x in data]

    return data


def create_graph(data: list):
    # Parsing the input text to create edges
    edges = []
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == ".":
                continue
            if char == "S":
                start = (x, y)

            # left
            if x > 0 and data[y][x - 1] in ["-", "L", "F"]:
                edges.append(((x, y), (x - 1, y)))
            # right
            if x < len(data[y]) - 1 and data[y][x + 1] in ["-", "J", "7"]:
                edges.append(((x, y), (x + 1, y)))
            # up
            if y > 0 and data[y - 1][x] in ["|", "F", "7"]:
                edges.append(((x, y), (x, y - 1)))
            # down
            if y < len(data) - 1 and data[y + 1][x] in ["|", "L", "J"]:
                edges.append(((x, y), (x, y + 1)))

    return edges, start


if __name__ == "__main__":
    data = parse_input("in.txt")

    edges, start = create_graph(data)

    # Creating the graph
    G = nx.Graph()
    G.add_edges_from(edges)

    # Drawing the graph
    plt.figure(figsize=(5, 5))
    nx.draw(G, with_labels=True, node_size=700, node_color="skyblue", font_size=15)
    plt.title("Graph from Text Input")
    plt.show()
