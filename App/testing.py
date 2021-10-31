import pandas as pd
import numpy as np
from statistics import *
from library import Library as lib
from library import CleanDF as cdf

def filterQuery(df):
    df_ref = df[["Customer type", "Product line", "Unit price", "Quantity", "Total", "Date", "Time", "Payment", "gross income", "Rating"]]
    df = cdf.cleanTypes(df)
    categorical_list = ["Customer type", "Product line", "Payment"]
    datetime_list = ["Date", "Time"]
    listed = lib.createListDict(df_ref)
    c = lib.printArrayDict(listed)
    idx = c[2]-1
    selection = c[2]
    print(f"INDEX: {idx}\nSelection {c[2]}") #TEST INPUT
    
    if selection == 0:
        return 0
    field = c[1][int(idx)]
    series = df[field]
    print(series.head(3))
    print(f"\nGathering info to filter {field}\n")
    
    if field in categorical_list:
        query_items = lib.getCategories(df, field)
        df['flagged'] = series.isin(query_items)
        filtered_df = df.query('flagged == True')
        return filtered_df
    elif field in datetime_list:
        print("TIME STAMPS")
        f_min = min(series)
        f_max = max(series)
        print(f_min, f_max)
    else:
        sample = series[1]
        print('CHECKING......', sample, "\n") #TEST INPUT
        if sample.dtype == np.int64:
            print("INT TYPE", type(series[1])) #TEST INFO
            f_min = np.min(series)
            f_max = np.max(series)
        elif sample.dtype == np.float64:
            f_min = np.min(series)
            f_max = np.max(series)
        else:
            print("UNKNOWN TYPE", type(series[3])) #TEST INFO
            print(series.head(2)) #TEST INFO
    print("\nMODIFIED DF:\n") #TEST INFO
    print(df.head()) #TEST INFO
    filterQuery(df_ref)



#TEMPORARY TEST DATT
df = pd.read_csv('./supermarket_sales.csv')
filterQuery(df)
print("----------------------")
# print(np.typecodes.get("Float"))