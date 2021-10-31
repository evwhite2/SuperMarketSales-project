import pandas as pd
from simple_stats import simpleStats as ss
from plotting import histogram_loop, getBranchRatings, generateFacetGrid
from library import Library as lib

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
            print("MACHINE LEARNING JUNK")
        elif c == 3:
            getBranchRatings(sales_df)
        elif c== 4:
            generateFacetGrid(sales_df)
        elif c == 0:
            break
        lib.printRedirectMessage("ANALYTICS MENU")
        analysisMenuLoop()  
    mainMenuLoop()
        

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