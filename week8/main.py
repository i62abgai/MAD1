import click
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random


@click.command()
@click.option('--instance', "-i", default=None, required=True,
              help=u'File with the instance.')
@click.option('--clusters', "-k", default=3, required=False,
              help=u'Number of clusters.')
@click.option('--iterations', "-it", default=10, required=False,
              help=u'Max number of iterations.')
@click.option('--attr1', "-at1", default=2, required=False,
              help=u'Attribute to represent (X axis).')
@click.option('--attr2', "-at2", default=3, required=False,
              help=u'Attribute to represent (Y axis).')
@click.option('--delim', "-del", default=";", required=False,
              help=u'Delimiter to read CSV')
@click.option('--decim', "-dec", default=",", required=False,
              help=u'Decimal')
def main(instance, clusters, iterations, attr1, attr2, delim, decim):
    df = pd.read_csv(instance, delimiter=delim, decimal=decim)
    dataNC = df.drop(columns=df.columns[-1])
    shape = df.shape
    # Normalize de data
    normalized_dataNC = (dataNC-dataNC.min())/(dataNC.max()-dataNC.min())
    # Create the adjacency matrix
    adjacencyMatrix = np.zeros((shape[0], shape[0]))
    lol = normalized_dataNC.values.tolist()

    for i, r in enumerate(adjacencyMatrix):
        feat_one = lol[i]
        for j, c in enumerate(r):
            feat_two = lol[j]
            adjacencyMatrix[i][j] = getEuclidean(feat_one, feat_two)

    # KMEANS
    for i in range(2, clusters+1):
        k = kMeans(i, iterations)
        k.run(lol, df, attr1, attr2)
    plt.show()


def getEuclidean(feat_one, feat_two):
    squared_distance = 0
    for i in range(len(feat_one)):
        squared_distance += (feat_one[i] - feat_two[i])**2
    ed = math.sqrt(squared_distance)
    return ed


class kMeans:
    def __init__(self, clusters, iterations):
        self.k = clusters
        self.iter = iterations
        self.t = 0.00001
        self.centroids = []
        self.cl = {}

    def run(self, data, df, attr1, attr2):
        print("\nNumber of clusters: ", self.k)
        self.centroids = random.sample(data, self.k)
        plt.figure()
        for i in range(self.iter):
            self.cl = {}
            for j in range(self.k):
                self.cl[j] = []
            for f in data:
                dist = []
                for c in range(len(self.centroids)):
                    eu = getEuclidean(f, self.centroids[c])
                    dist.append(eu)
                # Get the minimal distance to the centroid
                species = dist.index(min(dist))
                # Assign to that centroid the feature
                self.cl[species].append(f)
                
            for classes in self.cl:
                print(classes,": ",self.cl[classes])
                input()
                self.centroids[classes] = np.average(self.cl[classes], axis=0)
                
        colors = colors = cm.rainbow(np.linspace(0, 1, len(self.cl)))
        for centroid in self.centroids:
            plt.scatter(
                centroid[attr1], centroid[attr2], s=130, marker="x")
        for classes in self.cl:
            color = colors[classes]
            for f in self.cl[classes]:
                plt.scatter(f[attr1], f[attr2], color=color, s=30)
        for i, centroid in enumerate(self.centroids):
            plt.scatter(
                centroid[attr1], centroid[attr2], s=130, marker="x")
            txt = "c"+str(i)
            plt.text(centroid[attr1], centroid[attr2], txt)

        for classes in self.cl:
            print("\tThere are ",len(self.cl[classes])," instances in the class ",classes)
        plt.xlabel(df.columns[attr1])
        plt.ylabel(df.columns[attr2])


if __name__ == "__main__":
    main()
