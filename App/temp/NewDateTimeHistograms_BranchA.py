#use pandas and matplotlib packages
import pandas as pd
import matplotlib.pyplot as plt

#create dataframe from csv file
sales_df = pd.read_csv('supermarket_sales.csv')
#create copy of dataframe filtering results for Branch A only
sales_df_BrA = sales_df.loc[sales_df.Branch=='A'].copy()
#create dataframe columns based on Date column from dataset breaking date into its components
sales_df_BrA['Date'] = pd.to_datetime(sales_df_BrA['Date'])
sales_df_BrA['day'] = (sales_df_BrA['Date']).dt.day
sales_df_BrA['month'] = (sales_df_BrA['Date']).dt.month
sales_df_BrA['year'] = (sales_df_BrA['Date']).dt.year
#create dataframe columns based on Time column
sales_df_BrA['Time'] = pd.to_datetime(sales_df_BrA['Time'])
sales_df_BrA['Hour'] = (sales_df_BrA['Time']).dt.hour
#create series based on dataframe column, hour
timeseries = sales_df_BrA['Hour']

fig = plt.figure()
#create histogram based on timeseries
plt.hist(timeseries, bins = 11)

plt.title('Distribution of Time of Sales in Branch A')
plt.xlabel('Time')
plt.ylabel('Frequency')

plt.show()
#create series based on month column
monthseries = sales_df_BrA['month']

fig = plt.figure()
#create histogram based on monthseries
plt.hist(monthseries, bins = 3)

plt.title('Distribution of Month of Sales in Branch A')
plt.xlabel('Month')
plt.ylabel('Frequency')

plt.show()
#create series based on day column
dayseries = sales_df_BrA['day']

fig = plt.figure()
#create histograme based on dayseries
plt.hist(dayseries, bins = 7)

plt.title('Distribution of Day of Sales in Branch A')
plt.xlabel('Day')
plt.ylabel('Frequency')

plt.show()
