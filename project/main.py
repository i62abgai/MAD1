import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    dataset = pd.read_csv('train.csv', delimiter=",", decimal=".")
    
    dataset.hist()
    plt.show()
    
if __name__ == "__main__":
    main()
