import pandas as pd
from main import simple_stats 

print("\n-------------Welcome to salesQ interface3-------------\n") # I just gave the interface a quick name, we can change this...

sales_df = pd.read_csv("./supermarket_sales.csv")
choice_list = [{1: "View sample analytics"}, {2: "Run Analysis"}]

# def getData():
#     print('...getting dataframe')
#     sales_df = pd.read_csv("./supermarket_sales.csv")
#     return sales_df

def getSampleAnalysis(df, option):
    print("\nrunning sample analysis....")
    simple_stats(df, option)
    print("\n-------------DONE-------------\n")

def runAnalysis():
    print('...runing analysis')
    print("\n-------------DONE-------------\n")
    

def choiceLoop():
    key_slection = list()
    choice_selection =list()
    for i in choice_list:
        key_slection.append(i)
        for key, value in i.items():
            print(key, "---", value)
    c = input("\nWhat would you like to do?:\n")
    for i in key_slection:
        for key in i:
            choice_selection.append(key)
    if c.isdigit():
        c = int(c)
        if c not in choice_selection:
            print("\nInvalid choice, please type a number from the options list:")
            choiceLoop()
        elif c == 1:
            getSampleAnalysis(sales_df, 'all')
        elif c == 2:
            runAnalysis()
        else:
            print("exception")
    else:
        print("\INVALID choice. Input must be numeric.")
        choiceLoop()


choiceLoop()