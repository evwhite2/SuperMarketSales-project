import pandas as pd
#Import the pyplot module from the matplotlib package
import matplotlib.pyplot as plt

sales_df = pd.read_csv('supermarket_sales.csv')

sales_df['Time'] = pd.to_datetime(sales_df['Time'], format='%H:%M').dt.hour

#create a series from the time column
timeseries = sales_df.Time
#construct a matplotlib figure
fig = plt.figure()

#create a histogram of the rating data
plt.hist(timeseries, bins = 11)

#modify title and axis labels
plt.title('Distribution of Time of Sales')
plt.xlabel('Time')
plt.ylabel('Frequency')

#display chart
plt.show()
