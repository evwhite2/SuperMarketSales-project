import pandas as pd
import datetime
from main import simple_stats
from branch_histograms import histogram_loop

print("\n-------------Welcome to salesQ interface-------------\n") # I just gave the interface a quick name, we can change this...

choice_list = [{1: "View sample analytics"}, {2: "Run Analysis"}, {0: "Exit"}]
analytics_choice_list = [{1: "Sales Histograms over time", 2: "Machine Learning", 0: "Back to Main Menu"}]
raw_data_csv = './supermarket_sales.csv'

def getRawData(pathString):
    sales_df = pd.read_csv(pathString)
    return sales_df

def printRedirectMessage():
    now = datetime.datetime.now()
    timestamp = now.strftime("%H:%M:%S")
    print(f'-------------Operation complete at {timestamp}-------------\n\nMAIN MENU\n')

def printArrayDict(array):
    key_slection = list()
    choice_selection =list()
    for i in array:
        key_slection.append(i)
        for key, value in i.items():
            print(key, "---", value)
    return key_slection, choice_selection


def getSampleAnalysis(df):
    print("\nrunning sample analysis....")
    print(simple_stats(df))

def analysisMenuLoop():
    print('\nANALYTICS MENU\n')
    sel = printArrayDict(analytics_choice_list)
    key_selection = sel[0]
    choice_selection = sel[1]
    sales_df = getRawData(raw_data_csv)
    c = input("\nWhat would you like to do?:    ")
    for i in key_selection:
        for key in i:
            choice_selection.append(key)
    if c.isdigit():
        c = int(c)
        if c not in choice_selection:
            print("\nInvalid choice, please type a number from the options list:")
            analysisMenuLoop()
        elif c == 1:
            histogram_loop(sales_df)
        elif c == 2:
            print("MACHINE LEARNING JUNK")
        elif c == 0:
            print(".....exiting")
            exit()
        else:
            print("exception")
    else:
        try:
            if c.isalnum():
                print(ValueError("Input must be Numeric"))
                analysisMenuLoop()
        finally:
            print("Unknown Input. Exiting process...")
            exit()
    

def mainMenuLoop():
    sel = printArrayDict(choice_list)
    key_selection = sel[0]
    choice_selection = sel[1]
    sales_df = getRawData(raw_data_csv)
    c = input("\nWhat would you like to do?:    ")
    for i in key_selection:
        for key in i:
            choice_selection.append(key)
    if c.isdigit():
        c = int(c)
        if c not in choice_selection:
            print("\nInvalid choice, please type a number from the options list:")
            mainMenuLoop()
        elif c == 1:
            getSampleAnalysis(sales_df)
        elif c == 2:
            analysisMenuLoop()
        elif c == 0:
            print(".....exiting")
            exit()
        else:
            print("exception")
    else:
        try:
            if c.isalnum():
                print(ValueError("Input must be Numeric"))
                mainMenuLoop()
        finally:
            print("Unknown Input. Exiting process...")
            exit()
    printRedirectMessage()
    mainMenuLoop()


mainMenuLoop()