import click
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random
import ntpath
from kneed import KneeLocator

sseV = {}
reportFile = []


@click.command()
@click.option('--instance', "-i", default=None, required=True,
              help=u'File with the instance.')
@click.option('--clusters', "-k", default=3, required=False,
              help=u'Number of clusters.')
@click.option('--iterations', "-it", default=10, required=False,
              help=u'Max number of iterations.')
@click.option('--delim', "-del", default=";", required=False,
              help=u'Delimiter to read CSV')
@click.option('--decim', "-dec", default=",", required=False,
              help=u'Decimal')
@click.option('--tag', "-t", default="yes", required=False,
              help=u'The csv has class or not')
def main(instance, clusters, iterations, delim, decim, tag):
    global reportFile, sseV
    reportFile = open("kMeansReport.txt", "w+")
    # Write title of report
    reportFile.write(
        "Report from KMEANS algorithm on the dataset \""+ntpath.basename(instance)+"\"\n\n")
    df = pd.read_csv(instance, delimiter=delim, decimal=decim)
    if(df.isnull().values.any()):
        reportFile.write("There are missing values.\nNumber of missing values: "+str(df.isnull().sum().sum())+"\n\n")
    reportFile.write("Has class tag: "+tag)
    # Drop columns with more than 40% of missing values
    for i in df.loc[:, df.isna().any()]:
        if df[i].isnull().sum()/df.shape[0] >= 0.4:
            df = df.drop(columns=i)
            
    # Drop tag
    dataNC = ""
    if tag == "yes":
        reportFile.write(", class tag is: "+df.columns[-1]+"\n\n")
        dataNC = df.drop(columns=df.columns[-1])
    else:
        dataNC = df
        reportFile.write("\n\n")

    for i in dataNC:
        if dataNC[i].dtype == "object":
            dataNC[i] = dataNC[i].astype('category')
            dataNC[i] = dataNC[i].cat.codes
        if dataNC[i].dtype == "bool":
            dataNC[i] = dataNC[i].astype(int)
    # Replace missing values with mean
    dataNC = dataNC.fillna(dataNC.mean())
    # Get summary of attributes        
    lol = dataNC.values.tolist()
    reportFile.write("Summary of attributes:\n")
    for i, o in enumerate(dataNC):
        mean = getMean(lol[i])
        std = getStd(lol[i], mean)
        freq = getFreq(o, dataNC, dataNC.shape)
        reportFile.write("\t"+o+": \n\t\tMean: "+str(mean) +
                         "\n\t\tStandard Deviation: "+str(std)+"\n\n")
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
    reportFile.write("KMEANS algorithm run\n\n")
    for i in range(2, clusters+1):
        k = kMeans(i, iterations)
        k.run(lol, df)
    x = list_keys = [ k for k in sseV ]
    y = list_values = [ v for v in sseV.values() ]
    # Get elbow best K value    
    kn = KneeLocator(x, y, curve='convex', direction='decreasing')
    reportFile.write("\n\nThe best value of K based on the SSE is: " + str(kn.knee))
    reportFile.close()


def getMean(lista):
    mean = 0
    n = len(lista)
    for i in range(n):
        mean += lista[i]
    return mean/n


def getStd(lista, mean):
    n = len(lista)
    var = 0
    for i in range(n):
        var += (lista[i] - mean)**2
    var = var/n
    std = math.sqrt(var)
    return std


def getFreq(column, df, shape):
    col = list(df[column])
    freq = [[x, col.count(x)] for x in set(col)]
    freq = [x + [freq[index][1]/shape[0]] for index, x in enumerate(freq)]
    freq = [x + [0] for index, x in enumerate(freq)]
    for it in range(len(freq)):
        if it == 0:
            freq[it][3] = freq[it][2]
        else:
            freq[it][3] = freq[it][2]+freq[it-1][3]
    return freq


def getEuclidean(feat_one, feat_two):
    squared_distance = 0
    for i in range(len(feat_one)):
        squared_distance += (feat_one[i] - feat_two[i])**2
    ed = math.sqrt(squared_distance)
    return ed


class kMeans:
    def __init__(self, clusters, iterations):
        # Number of clusters
        self.k = clusters
        # Number of iterations
        self.iter = iterations
        # Selected/Calculated centroids
        self.centroids = []
        # Instances classified
        self.cl = {}

    def run(self, data, df):
        global sseV, reportFile
        self.centroids = random.sample(data, self.k)
        plt.figure()
        if self.k == 1:
            self.cl = {}
            for j in data:
                self.cl[0].append(j)
        else:
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
                    self.centroids[classes] = np.average(
                        self.cl[classes], axis=0)
        # Calculate SSE
        sse = 0
        for x in self.cl:
            for y in self.cl[x]:
                sse += sum((y - self.centroids[x])**2)
        sseV[self.k]=sse
        reportFile.write("\nNumber of clusters: "+str(self.k) +
                             "\t\tSSE: "+str(sse)+"\n")
        for i, o in enumerate(self.centroids):
            reportFile.write("\n\tCluster "+str(i)+": \n\t\tCentroid Value: "+str(o)+"\n" +
                             "\t\tThere are "+ str(len(self.cl[i])) + " instances in this cluster \n")


if __name__ == "__main__":
    main()
