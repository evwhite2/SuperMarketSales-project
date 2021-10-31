
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import *
from library import Library as lib
from library import CleanDF as cdf


def filterQuery(df):
    df_ref = df[["Customer type", "Product line", "Unit price", "Quantity", "Total", "Date", "Time", "Payment", "gross income", "Rating"]]
    df = cdf.cleanTypes(df)
    categorical_list = ["Customer type", "Product line"]
    listed = lib.createListDict(df_ref)
    c = lib.printArrayDict(listed)
    selection = c[2]-1
    field = c[1][int(selection)]
    series = df[field]
    print(f"SELECTION: {selection}\nFIELD:  {field}")
    if field in categorical_list:
        query_items = lib.getCategories(df, field)
        df['flagged'] = series.isin(query_items)
        filtered_df = df.query('flagged == True')
        return filtered_df
    else:
        if type(series) == float:
            print("FLOAT TYPE", type(series[3])) #TEST INFO
            mn = min(series,key=lambda x:float(x))
            mx = max(series,key=lambda x:float(x))
            print(mn, mx)
        elif type(series) == pd._libs.tslibs.timestamps.Timestamp:
            print("DATE TYPE", type(series[3])) #TEST INFO
            print(max(df[field]). min(df[field]))
        else:
            print("UNKNOWN TYPE", type(series[3])) #TEST INFO
            print(series.head(2)) #TEST INFO
    print("\nMODIFIED DF:\n") #TEST INFO
    print(df.head()) #TEST INFO
    filterQuery(ref_df)


def histogram_loop(df):
    print("\nWhich branch would you like to model?\n")
    opt_list = [{1: "Branch A"}, {2: "Branch B"}, {3: "Branch C"}]
    c = lib.printArrayDict(opt_list)
    opt = c[2]
    filter_opt = input('Would you like to add a filter? type y/n:    ')
    if lib.validateYN(filter_opt):
        filterQuery(df)
    if opt==1: 
        getBranchSeries(df, 'A')
    elif opt==2:
        getBranchSeries(df, 'B')
    elif opt==3:
        getBranchSeries(df, 'C')
    elif opt==0:
        next()
    else:
        print('\nInvalid Entry.\n')
        histogram_loop(df)


def getBranchRatings(df):
     generateBoxPlot(df, "Branch", "Rating","Distribution of Ratings by Branch")
    

def getBranchSeries(df, opt):
    sales_df_BrB = df.loc[df.Branch==opt].copy()
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


#TEMPORARY TEST DATT
df = pd.read_csv('./supermarket_sales.csv')
filterQuery(df)