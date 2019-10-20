import pandas as pd
import numpy as np
import itertools
import sys

#Function that checks if two elements from the csv file are the same
def isEqual(row,check):
    x = True
    for i in range(len(row)-1):
        if row[i] != '' and row[i] != check[i]:
            x = False
    return x

#Function that checks if two elements from the csv included the class column are the samen
def isEqualConfidence(row,check):
    x = True
    for i in range(len(row)):
        if row[i] != '' and row[i] != check[i]:
            x = False
    return x   

def main():
    #Read the CSV file and stablish the delimiter
    data = pd.read_csv(sys.argv[1], delimiter=';')
    #Get the unique values for each column
    distinctValues = [data.Outlook.unique().tolist(), data.Temperature.unique().tolist(), data.Humidity.unique().tolist(), data.Windy.unique().tolist(), data.Play.unique().tolist()]
    #Append the empty element to get the correct number of association rules
    for x in range(len(distinctValues)-1):
        distinctValues[x].append("")
    #Transform the DataFrame into a list of lists
    dataList = data.values.tolist()
    #Get all the combinations (Association rules) that exist in the DataFrame
    associationRules = list(itertools.product(*distinctValues))
    print("Values \t Support \t Confidence \t Count")
    #Get the support and confidence value for each rule
    for row in associationRules:
        #Calculates the support and calculates the confidence
        count1 = count2 = 0
        for check in dataList:
            if bool(isEqual(row, check)):
                count1+=1
            if bool(isEqualConfidence(row, check)):
                count2+=1
        support = count1/len(dataList)

        #Checks is not a division by zero
        if count1 == 0:
            confidence = 0
        else:
            confidence = count2/count1
       
        print(str(row)+"\t"+str(support)+"\t"+str(confidence)+"\t"+str(count1))

if __name__ == "__main__":
    main()


