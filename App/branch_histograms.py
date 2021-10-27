#use pandas and matplotlib packages
import pandas as pd
import matplotlib.pyplot as plt

#Circular import forced a copy & paste of this fucntion, it's not ideal but will have to work for now
def printArrayDict(array):
    key_slection = list()
    choice_selection =list()
    for i in array:
        key_slection.append(i)
        for key, value in i.items():
            print(key, "---", value)
    return key_slection, choice_selection

# Still need to add data validation here
def histogram_loop(df):
    opt_list = [{1: "Branch A"}, {2: "Branch B"}, {3: "Branch C"}]
    printArrayDict(opt_list)
    opt = int(input("\nWhich Branch would you like to model?: "))
    if opt==1:
        salesTimeSeries(df, 'A')
    elif opt==2:
        salesTimeSeries(df, 'B')
    elif opt==3:
        salesTimeSeries(df, 'C')
    else:
        print('\nInvalid Entry.\n')
        histogram_loop(df)

# Need to update the settings for the histograms
def salesTimeSeries(df, opt):
    sales_df_BrB = df.loc[df.Branch==opt].copy()
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

    plt.title(f'Distribution of Time of Sales in Branch {opt}')
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
