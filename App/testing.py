import pandas as pd
import numpy as np
from statistics import *
from library import Library as lib
from library import CleanDF as cdf

def filterQuery(df):
    df_ref = df[["Customer type", "Product line", "Unit price", "Quantity", "Total", "Date", "Time", "Payment", "gross income", "Rating"]]
    categorical_list = ["Customer type", "Product line", "Payment"]
    datetime_list = ["Date", "Time"]
    listed = lib.createListDict(df_ref)
    c = lib.printArrayDict(listed)
    idx = c[2]-1
    selection = c[2]
   
    if selection == 0:
        return 0
    field = c[1][int(idx)]
    series = df[field]
    print(f"\nGathering info to filter {field}\n")
    new_df = cdf.cleanNames(df)
    new_df = cdf.cleanTypes(new_df)
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
                filterQuery(df_ref)
        print(f"\nFor {field}:\nMinimum Value: {f_min}\nMaximum Value: {f_max}")
        new_idx = df.columns.get_loc(field)
        new_df = cdf.cleanNames(df)
        filtered_df = lib.validateMinMax(new_df, new_df.columns[new_idx])
    return filtered_df

#TEMPORARY TEST DATA
# df = pd.read_csv('./supermarket_sales.csv')
# filterQuery(df)
# print("----------------------")
