import pandas as pd
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
            algoLib.runLogit_Unsatisfied_Vs_ProductLine_Vs_Gender(dummyDF)
        elif c ==3:
            algoLib.runLogisticRegresstion_Unsatisfied_Vs_ProductLine(dummyDF)
        elif c ==4:
            algoLib.runLogisticRegresstion_PredictUnsatisfied(dummyDF)
        elif c ==5:
            algoLib.runCrossTabulation(dummyDF)
        elif c ==6:
            algoLib.runKMeansAnalysis(dummyDF) # MIGHT NEED TO SWTICH DUMMY DATA FOR THIS
        algoMenuLoop()
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