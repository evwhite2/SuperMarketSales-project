#use pandas and matplotlib packages
import pandas as pd
import matplotlib.pyplot as plt
from main import printArrayDict
from control import choiceLoop

def userLoop(df):
    opt_list = [{1: "Branch A"}, {2: "Branch B"}, {3: "Branch C"}]
    printArrayDict(opt_list)
    opt = int(input("Which Branch would you like to model?"))
    if opt==1:
        salesTimeSeries(df, 'A')
    elif opt==2:
        salesTimeSeries(df, 'B')
    elif opt==3:
        salesTimeSeries(df, 'C')
    else:
        print('not in range')
        userLoop()
    opt2 = input("What would you like to do?:")
    opt2_list = [{1: "Go back to main menu"}, {2:"Run mode on another branch"}, {3:"Exit program"}]
    if opt2 == 1:
        choiceLoop()
    elif opt2 ==2:
        userLoop()
    elif opt2==3:
        exit()
    else:
        Exception("Invalid entry")
        return opt2   


def salesTimeSeries(df, opt):
    sales_df_BrB = sales_df.loc[sales_df.Branch==opt].copy()
    #create dataframe columns based on Date column from dataset breaking date into its components
    sales_df_BrB['Date'] = pd.to_datetime(sales_df_BrB['Date'])
    sales_df_BrB['day'] = (sales_df_BrB['Date']).dt.day
    sales_df_BrB['month'] = (sales_df_BrB['Date']).dt.month
    sales_df_BrB['year'] = (sales_df_BrB['Date']).dt.year
    #create dataframe columns based on Time column
    sales_df_BrB['Time'] = pd.to_datetime(sales_df_BrB['Time'])
    sales_df_BrB['Hour'] = (sales_df_BrB['Time']).dt.hour
    #create series based on dataframe column, hour
    timeseries = sales_df_BrB['Hour']

    fig = plt.figure()
    #create histograme based on timeseries
    plt.hist(timeseries, bins = 11)

    plt.title('Distribution of Time of Sales in Branch B')
    plt.xlabel('Time')
    plt.ylabel('Frequency')

    plt.show()
    #create series based on month column
    monthseries = sales_df_BrB['month']

    fig = plt.figure()
    #create histograme based on monthseries
    plt.hist(monthseries, bins = 3)

    plt.title(f'Distribution of Month of Sales in Branch {opt}')
    plt.xlabel('Month')
    plt.ylabel('Frequency')

    plt.show()
    #create day series based on day column
    dayseries = sales_df_BrB['day']

    fig = plt.figure()
    #create histogram based on dayseries
    plt.hist(dayseries, bins = 7)

    plt.title(f'Distribution of Day of Sales in Branch {opt}')
    plt.xlabel('Day')
    plt.ylabel('Frequency')

    plt.show()

sales_df = pd.read_csv('supermarket_sales.csv')
userLoop(sales_df)