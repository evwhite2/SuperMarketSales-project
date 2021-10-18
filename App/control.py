# This code currently is not connected to anything, but will serve as controller for user input to the 'main file' with most/all of analytical code. 
# I imagine we may make another code file for the Machine learningcode and yet another for the the MatLib code, depends how long it is.

import pandas as pd
print("\n-------------Welcome to salesQ interface3-------------\n") # I just gave the interface a quick name, we can change this...

choice_list = [{1: "Get Data"}, {2: "Run Analysis"}]


def getData():
    print('...getting dataframe')
    return "...."

def runAnalysis():
    print('...runing analysis')
    

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
            getData()
        elif c == 2:
            runAnalysis()
        else:
            print("exception")
    else:
        print("\INVALID choice. Input must be numeric.")
        choiceLoop()


choiceLoop()