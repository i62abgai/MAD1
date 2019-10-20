import pandas as pd
import numpy as np
import sys


def getCosine(data, shape):
    cosine_angle = [[0 for x in range(shape[0])] for y in range(shape[0])]
    # Get the cosine angle for each pair of points
    for i in range(0, shape[0]):
        val_1 = data.iloc[i]
        val_1 = val_1[['Sepal_Length','Sepal_Width', 'Petal_Length', 'Petal_Width']]
        for j in range(i,shape[0]):
            val_2 = data.iloc[i]
            val_2 = val_2[['Sepal_Length','Sepal_Width', 'Petal_Length', 'Petal_Width']]
            product = np.dot(val_1, val_2)
            norm_1 = np.linalg.norm(val_1)
            norm_2 = np.linalg.norm(val_2)
            result = product/(norm_1*norm_2)
            cosine_angle[i][j] = (result)
    return cosine_angle

def main():
    data = pd.read_csv(sys.argv[1], delimiter=';', decimal=',')
     
    shape = data.shape
    
    eu_distance = []
    # Get the euclidean distance for each pair of points
    for i in range(0, shape[0]):
        val_1 = data.iloc[i]
        x = (data[['Sepal_Length','Sepal_Width', 'Petal_Length', 'Petal_Width']]-val_1[['Sepal_Length','Sepal_Width', 'Petal_Length', 'Petal_Width']]).pow(2).sum(1).pow(0.5)
        eu_distance.append(x)        
    
    cosine_angle = getCosine(data, shape)
    print(cosine_angle)
    print(eu_distance)
    # Get the mean, median, var, and standard deviation from the dataframe
    # means = list(data.mean())
    # median = list(data.median())
    # vars = list(data.var())
    # std = list(data.std())
    
    means = []
    vars = []
    stds = []
    medians = []
    for i in range(0,4):
        mean = np.sum(data.iloc[:,i])/len(data)
        means.append(mean)
        
        var = (data.iloc[:,i] - mean).pow(2)
        var = np.sum(var)/len(data)
        vars.append(var)
        
        std = np.power(var, 0.5)
        stds.append(std)
        
        data_i = list(data.iloc[:,i])
        sorted_data = sorted(data_i)
        median = sorted_data[int(len(data)/2)]  
        medians.append(median)
            
    print(means,"\n", medians,"\n", vars,"\n", stds)
    

if __name__ == "__main__":
    main()
