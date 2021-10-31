
import statistics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import *
from library import Library as lib
from library import CleanDF as cdf


def filterQuery(df):
    # df_ref = df[["Customer type", "Product line", "Unit price", "Quantity", "Total", "Date", "Time", "Payment", "gross income", "Rating"]]
    df = cdf.cleanNames(df)
    df = cdf.cleanTypes(df)
    df_col = ['customer_type', 'product_line', 'unit_price', 'Quantity', 'Total', 'Payment', 'gross_income', 'Rating']
    categorical_list = ["customer_type", "product_line", "Payment"]
    datetime_list = ["Date", "Time"]
    listed = lib.createListDict(df_col)
    c = lib.printArrayDict(listed)
    idx = c[2]-1
    selection = c[2]
    if selection == 0:
        return 0
    field = c[1][int(idx)]
    series = df[field]
    print(f"\nGathering info to filter {field}\n")
    if field in categorical_list:
        query_items = lib.getCategories(df, field)
        df['flagged'] = series.isin(query_items)
        filtered_df = df.query('flagged == True')
        return filtered_df
    else:
        if field in datetime_list:
            f_min = min(series)
            f_max = max(series)
        else:
            sample = series[1]
            if sample.dtype in [ np.int64 , np.float64]:
                f_min = np.min(series)
                f_max = np.max(series)
            else:
                print("\nUNKNOWN TYPE!\n", sample, type(sample))
                print("retrying....")
                filterQuery(df)
        print(f"\nFor {field}:\nMinimum Value: {f_min}\nMaximum Value: {f_max}")
        filtered_df = lib.validateMinMax(df, field)
    return filtered_df


def histogram_loop(df):
    print("\nWhich branch would you like to model?\n")
    opt_list = [{1: "Branch A"}, {2: "Branch B"}, {3: "Branch C"}, {4: "All Branches"}]
    c = lib.printArrayDict(opt_list)
    opt = c[2]
    filter_opt = input('Would you like to add a filter? type y/n:    ')
    if lib.validateYN(filter_opt):
       df = filterQuery(df)
    if opt==1: 
        getBranchSeries(df, 'A')
    elif opt==2:
        getBranchSeries(df, 'B')
    elif opt==3:
        getBranchSeries(df, 'C')
    elif opt==4:
        getBranchSeries(df, 'X')
    elif opt==0:
        next()
    else:
        print('\nInvalid Entry.\n')
        histogram_loop(df)


def getBranchRatings(df):
     generateBoxPlot(df, "Branch", "Rating","Distribution of Ratings by Branch")


def getBranchSeries(df, opt):
    sales_df_BrB = df.copy()
    if opt in ['A', 'B', 'C']:
        sales_df_BrB = sales_df_BrB.loc[df.Branch==opt]
    sales_df_BrB['Date'] = pd.to_datetime(sales_df_BrB['Date']) #create dataframe columns based on Date column from dataset 
    sales_df_BrB['Time'] = pd.to_datetime(sales_df_BrB['Time'])#create dataframe columns based on Time column
    #create series based on dataframe column, hour
    time_series = (sales_df_BrB['Time']).dt.hour
    week_series = (sales_df_BrB['Date']).dt.month
    #generating charts using matpltlib-powered functions built below:
    hourplt = generateHistogram(time_series, 'Distribution sales over time of day - Branch', opt, 'Hour (24 hour)', 'Sales Frequency', 11)
    weekplt = generateBarChart(week_series, 'Distribution sales per week over 3 months - Branch', opt, 'Month', 'Sales Frequency')
    hourplt.show()
    weekplt.show()
  

def generateHistogram(series, title, branch, xaxis, yaxis, nbins):
    plt.figure()
    plt.hist(series, bins=nbins)
    plt.title(f'{title} {branch}')
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    return plt

def generateBarChart(series, title, branch, xaxis, yaxis):
    hist,bin_edges = np.histogram(series)
    plt.figure()
    plt.bar(bin_edges[:-1], hist, width = 0.5, color='#0504aa',alpha=0.7)
    plt.grid(axis='y', alpha=.75)
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.title(f'{title} {branch}')
    return plt

def generateBoxPlot(series, var1, var2, label):
    sns.boxplot(x=series[var1], y=series[var2], palette = "Blues").set(title=label)
    plt.show()


def generateFacetGrid(df):
    FacGr = sns.FacetGrid(df, col="Branch")
    ax = FacGr.map(sns.distplot, "Total")
    plt.show()

