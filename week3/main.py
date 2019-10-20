import numpy as np
import matplotlib.pyplot as plt
import random
import operator
import pandas as pd
import sys


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


def plotResults(nd):
    nNodes = len(nd)
    index = np.arange(nNodes)
    bar_width = 0.70
    opacity = 0.8
    plt.bar(index, nd, bar_width,
            alpha=opacity,
            color='g',
            label='Degrees')
    plt.xticks(index + bar_width, index)
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
    return nd


def main():
    if len(sys.argv) != 2:
        print("Incorrect number of parameters: \n" +
              "\t main.py \"instance file\"")
        return -1

    adjacencyMatrix = readInstance(sys.argv[1])
    nd = getDegrees(adjacencyMatrix)
    plotResults(nd)


if __name__ == "__main__":
    main()
