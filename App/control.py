'''  CONTROL  - Last Modified Oct 31, 2021
This is the root file of the App. Users should run the program from this file. It calls upon functions from all other App/ files and to produce outputs, and reads/creats DataFrames from the raw 'supermarket_sales.csv' file which are passed to the utlized functions outside this file.
'''

import pandas as pd
import os
from simple_stats import simpleStats as ss
from plotting import histogram_loop, getBranchRatings, generateFacetGrid
from library import Library as lib
from library import CleanDF as cdf
from algos import algorithmsLibrary as algoLib

rawdata = './supermarket_sales.csv'


print("\n-------------Welcome to salesQ interface-------------\n") 


def getRawData():
    sales_df = pd.read_csv(rawdata)
    return sales_df


def analysisMenuLoop():
    sales_df = getRawData().copy()
    c = lib.printArrayDict(lib.analytics_choice_list)
    c=c[2]
    while True:      
        if c == 1:
            histogram_loop(sales_df)
            lib.printRedirectMessage("")
            analysisMenuLoop()
        elif c == 2:
            print('\nALGORITHMS MENU\n')
            algoMenuLoop()
        elif c == 3:
            getBranchRatings(sales_df)
        elif c== 4:
            generateFacetGrid(sales_df)
        elif c == 0:
            break
        lib.printRedirectMessage("ANALYTICS MENU")
        analysisMenuLoop()  
    print("\n\nMAIN MENU\n")
    mainMenuLoop()


def algoMenuLoop():
    c = lib.printArrayDict(lib.algo_choice_list)
    c = c[2]
    df = getRawData().copy()
    dummyDF = cdf.cleanDummies(df)
    while True:
        if c == 1:
            algoLib.runChi2_Gender_Vs_Satisfaction(dummyDF)
        elif c ==2:
            algoLib.runLogit_Unsatisfied_Vs_AllIndependentVariables(dummyDF)
        elif c ==3:
            algoLib.runChi2_Mandalay_Vs_Satisfaction(dummyDF)
        elif c ==4:
            algoLib.runLogisticRegression_PredictUnsatisfied(dummyDF)
        elif c ==5:
            algoLib.runCrossTabulation(dummyDF)
        elif c ==6:
            algoLib.runKMeansAnalysis(dummyDF) # MIGHT NEED TO SWTICH DUMMY DATA FOR THIS
        elif c ==0:
            break
        lib.printRedirectMessage("ALGORITHMS MENU")
        algoMenuLoop()
    print("\n\nANALYTICS MENU\n")
    analysisMenuLoop()  

    

def mainMenuLoop():
    c = lib.printArrayDict(lib.choice_list)
    sales_df = getRawData()
    c=c[2]
    if c == 1:
        print("\nRunning sample statistics....")
        ss.printSimpleStats(sales_df)
        lib.printRedirectMessage("MAIN MENU")
    elif c == 2:
        print('\nANALYTICS MENU\n')
        analysisMenuLoop()
        lib.printRedirectMessage("MAIN MENU")
    elif c == 0:
        lib.printRedirectMessage("Good Bye!")
        exit()
    mainMenuLoop()


mainMenuLoop()