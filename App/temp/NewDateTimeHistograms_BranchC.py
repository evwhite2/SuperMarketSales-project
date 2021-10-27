#use pandas and matplotlib packages
import pandas as pd
import matplotlib.pyplot as plt

#create dataframe from csv file
sales_df = pd.read_csv('supermarket_sales.csv')
#create copy of dataframe filtering results for Branch C only
sales_df_BrC = sales_df.loc[sales_df.Branch=='C'].copy()
#create dataframe columns based on Date column from dataset breaking date into its components
sales_df_BrC['Date'] = pd.to_datetime(sales_df_BrC['Date'])
sales_df_BrC['day'] = (sales_df_BrC['Date']).dt.day
sales_df_BrC['month'] = (sales_df_BrC['Date']).dt.month
sales_df_BrC['year'] = (sales_df_BrC['Date']).dt.year
#create dataframe columns based on Time column
sales_df_BrC['Time'] = pd.to_datetime(sales_df_BrC['Time'])
sales_df_BrC['Hour'] = (sales_df_BrC['Time']).dt.hour
#create series based on dataframe column, hore
timeseries = sales_df_BrC['Hour']

fig = plt.figure()
#create histogram based on timeseries
plt.hist(timeseries, bins = 11)

plt.title('Distribution of Time of Sales in Branch C')
plt.xlabel('Time')
plt.ylabel('Frequency')

plt.show()
#create series based on month column
monthseries = sales_df_BrC['month']

fig = plt.figure()
#create histogram based on monthseries
plt.hist(monthseries, bins = 3)

plt.title('Distribution of Month of Sales in Branch C')
plt.xlabel('Month')
plt.ylabel('Frequency')

plt.show()
#create series based on day column
dayseries = sales_df_BrC['day']

fig = plt.figure()
#create histogram based on dayseries
plt.hist(dayseries, bins = 7)

plt.title('Distribution of Day of Sales in Branch C')
plt.xlabel('Day')
plt.ylabel('Frequency')

plt.show()
