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
        if column != "Species":
            freqVals = getFreq(column, df, shape)
            tlist = list(zip(*freqVals))
            colVals = list(df[column])
            mean = getMean(colVals)
            means.append(mean)
            std = getStd(colVals, mean)
            stds.append(std)
            freqAttr.append(freqVals)
            print("\n", column, "\n")
            """for values in freqVals:
                print("Value: ", values[0], " Frequency: ", values[1],
                      " Relative Freq: ", values[2], " Cumulative Freq: ", values[3])"""

    print("\n\n")

        
    # Theoretical distributions
    for i, column in enumerate(df):
        if column != "Species":      
            leftSigma = means[i]-stds[i]
            rightSigma = means[i]+stds[i]
            
            left2Sigma = means[i]-2*stds[i]
            right2Sigma = means[i]+2*stds[i]
            
            left3Sigma = means[i]-3*stds[i]
            right3Sigma = means[i]+3*stds[i]
            
            percentSigma = len(list(x for x in list(df[column]) if leftSigma <= x <= rightSigma))
            percent2Sigma = len(list(x for x in list(df[column]) if left2Sigma <= x <= right2Sigma))
            percent3Sigma = len(list(x for x in list(df[column]) if left3Sigma <= x <= right3Sigma))
            
            print(column, " Mean: ", means[i], " Std: ", stds[i],
                  " \n\tRange(1*sigma): ", means[i]-stds[i], ", ", means[i]+stds[i], " --> elements: ", percentSigma, " percent: ", percentSigma/150,
                  " \n\tRange(2*sigma): ", means[i]-2*stds[i], ", ", means[i]+2*stds[i], " --> elements: ", percent2Sigma, " percent: ", percent2Sigma/150,
                  " \n\tRange(3*sigma): ", means[i]-3*stds[i], ", ", means[i]+3*stds[i], " --> elements: ", percent3Sigma, " percent: ", percent3Sigma/150, "\n")

    fig1, ax1 = plt.subplots()
    # Empirical distributions
    for i, column in enumerate(df):
        if column != "Species":
            x = np.linspace(means[i] - 3*stds[i], means[i] + 3*stds[i], 100)
            line2, = ax1.plot(x, stats.norm.pdf(x, means[i], stds[i]))
            line2.set_label(column)
    ax1.grid(True)
    ax1.legend()

    plt.show()


if __name__ == "__main__":
    main()
