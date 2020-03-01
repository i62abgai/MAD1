import numpy as np
import matplotlib.pyplot as plt
import random
import operator
import pandas as pd
import sys
import statistics

def readInstance(fileName):
    data = pd.read_csv(fileName, header=None, delimiter=";")
    lol = data.values.tolist()

    nodes = []
    for i in lol:
        if not i[0] in nodes:
            nodes.append(i[0])
        if not i[1] in nodes:
            nodes.append(i[1])
    nodes = sorted(nodes)
    nNodes = len(nodes)

    adjacencyMatrix = np.zeros((nNodes, nNodes))

    for i in lol:
        adjacencyMatrix[i[0]-1][i[1]-1] = 1
        adjacencyMatrix[i[1]-1][i[0]-1] = 1

    return adjacencyMatrix


def plotResults(x, y):
    bar_width = 0.8
    opacity = 0.8
    plt.bar(y,x, bar_width,
            alpha=opacity,
            color='g',
            label='Degrees')
    plt.xlim(0, 18)
    plt.xlabel("Degrees")
    plt.ylabel("N of connections")
    plt.show()


def getDegrees(adjacencyMatrix):
    nNodes = len(adjacencyMatrix)
    nd = np.zeros(nNodes)
    for i, val in enumerate(adjacencyMatrix):
        count = 0
        for j in val:
            if j != 0:
                count += 1
        nd[i] = count
    return list(nd)


def main():
    if len(sys.argv) != 2:
        print("Incorrect number of parameters: \n" +
              "\t main.py \"instance file\"")
        return -1

    adjacencyMatrix = readInstance(sys.argv[1])
    nd = getDegrees(adjacencyMatrix)
    countDegrees = [[x,nd.count(x)] for x in set(nd)]
    tlist = list(zip(*countDegrees))
    y = tlist[0]
    x = tlist[1]
    print(adjacencyMatrix)
    plotResults(x, y)


if __name__ == "__main__":
    main()
