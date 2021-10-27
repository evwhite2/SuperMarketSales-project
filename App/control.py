import pandas as pd
import datetime
from main import  simple_stats

print("\n-------------Welcome to salesQ interface-------------\n") # I just gave the interface a quick name, we can change this...

choice_list = [{1: "View sample analytics"}, {2: "Run Analysis"}, {0: "Exit"}]
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


def runAnalysis():
    print('...runing analysis')
    

def choiceLoop():
    sel = printArrayDict(choice_list)
    key_selection = sel[0]
    choice_selection = sel[1]
    sales_df = getRawData(raw_data_csv)
    c = input("\nWhat would you like to do?:\n")
    for i in key_selection:
        for key in i:
            choice_selection.append(key)
    if c.isdigit():
        c = int(c)
        if c not in choice_selection:
            print("\nInvalid choice, please type a number from the options list:")
            choiceLoop()
        elif c == 1:
            getSampleAnalysis(sales_df)
        elif c == 2:
            runAnalysis()
        elif c == 0:
            print(".....exiting")
            exit()
        else:
            print("exception")
    else:
        print("\INVALID choice. Input must be numeric.")
        choiceLoop()
    printRedirectMessage()
    choiceLoop()


choiceLoop()