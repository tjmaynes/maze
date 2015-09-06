# File: maze.py
# Author: TJ Maynes
import sys
import networkx as nx
import matplotlib.pyplot as plt

"""
Each of the lines has n bit strings, where each bit string has 5 characters
(characters are either 1/0). The first character of the bit string indicates
whether or not the square is yellow (1 indicates yellow and 0 indicates white).
The second character of the bit string indicates whether or not there is a wall
to the north (1 indicates there is a wall, 0 indicates there is no wall).
The third character of the bit string indicates whether or not there is a wall
to the south. The fourth character of the bit string indicates whether or not
there is a wall to the east. The final (fifth) character of the bit string
indicates whether or not there is a wall to the west.
"""

def maze(instance):
    G = nx.Graph()
    for i in range(instance):
        G.clear()
        blank = f.readline()
        specs = f.readline()
        second = specs.split(" ")
        level, width, height = int(second[0]), int(second[1]), int(second[2])

        starting = f.readline()
        third = starting.split(" ")
        enterLevel, enterX, enterY = int(third[0]), int(third[1]), int(third[2])
        enter_maze = (enterLevel, enterX, enterY)

        ending = f.readline()
        fourth = ending.split()
        endLevel, endX, endY = int(fourth[0]), int(fourth[1]), int(fourth[2])
        exit_maze = (endLevel, endX, endY)

        for k in range(1, level+1):
            for n in range(1, width+1):
                for m in range(1, height+1):
                    color, north, south, east, west, new_line = f.read(1),
                    f.read(1), f.read(1), f.read(1), f.read(1), f.read(1)

                    if G.has_node((k, n, m)) is True:
                        G.node[(k, n, m)]['color'] = color
                        G.node[(k, n, m)]['north'] = north
                        G.node[(k, n, m)]['south'] = south
                        G.node[(k, n, m)]['east'] = east
                        G.node[(k, n, m)]['west'] = west
                    else:
                        G.add_node((k, n, m), {'color': color, 'north': north,
                                               'south': south, 'east': east,
                                               'west': west})

                    if G.node[(k, n, m)]['color'] == '0' and k < level:
                        G.add_edge((k, n, m), (k+1, n, m))
                    if G.node[(k, n, m)]['south'] == '0' and n < width:
                        G.add_edge((k, n, m), (k, n+1, m))
                    if G.node[(k, n, m)]['east'] == '0' and m < height:
                        G.add_edge((k, n, m), (k, n, m+1))

        dijkstra = nx.dijkstra_path(G, enter_maze, exit_maze)

        path = []
        o = open('maynes.txt', 'a')

        for i in range(len(dijkstra)-1):
            if dijkstra[i][2] < dijkstra[i+1][2]:
                path.append("E")
                o.write("E ")
            if dijkstra[i][2] > dijkstra[i+1][2]:
                path.append("W")
                o.write("W ")
            if dijkstra[i][1] > dijkstra[i+1][1]:
                path.append("N")
                o.write("N ")
            if dijkstra[i][1] < dijkstra[i+1][1]:
                path.append("S")
                o.write("S ")
            if dijkstra[i][0] > dijkstra[i+1][0]:
                path.append("U")
                o.write("U ")
            if dijkstra[i][0] < dijkstra[i+1][0]:
                path.append("D")
                o.write("D ")

        o.write("\n\n")
        o.close()
        print ' '.join(path) + '\n'

def drawGraph(instance, G):
        nx.draw(G)
        helper = str(instance)
        plt.savefig("graph_drawing_" + helper + ".png")
        plt.show()

if __name__ == '__main__':
    output_file = open('maynes.txt', 'w')
    output_file.write("")
    output_file.close()

    f = open('input.txt', 'r')
    instances = f.readline()
    firstLine = int(instances)

    maze(firstLine)

    f.close()
