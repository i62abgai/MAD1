import pandas as pd
import sys
import csv
import math
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np


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


def main():
    df = pd.read_csv(sys.argv[1], delimiter=';', decimal=',')
    shape = df.shape
    freqAttr = []
    means = []
    stds = []
    for column in df:
        freqVals = getFreq(column, df, shape)
        tlist = list(zip(*freqVals))
        mean = getMean(tlist[1])
        means.append(mean)
        std = getStd(tlist[1], mean)
        stds.append(std)
        freqAttr.append(freqVals)
        print("\n", column, "\n")
        for values in freqVals:
            print("Value: ", values[0], " Frequency: ", values[1],
                  " Relative Freq: ", values[2], " Cumulative Freq: ", values[3])

    for i, column in enumerate(df):
        x = np.linspace(means[i] - 3*stds[i], means[i] + 3*stds[i], 100)
        line, = plt.plot(x, stats.norm.pdf(x, means[i], stds[i]))
        line.set_label(column)
        print(column, " Mean: ", means[i], " Std: ", stds[i])
    
    """# Normal Distribution
    x = np.linspace(0 - 3*1, 0 + 3*1, 100)
    line, = plt.plot(x, stats.norm.pdf(x, 0, 1))
    line.set_label("Normal distribution")"""
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
