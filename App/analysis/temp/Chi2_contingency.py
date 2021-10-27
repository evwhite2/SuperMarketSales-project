#use numpy, scipy and pandas packages
import numpy as np
from scipy.stats import chi2_contingency
import pandas as pd
#create dataframe from dummy variable file version
dummy_df= pd.read_csv("new_supermarket_dummy_data.csv")
#create new dataframe of just two columns: gender, unsatisfied (categorical variables)
contingency_df = dummy_df[['Gender','Unsatisfied']]
#create frequency table using crosstab function in pandas
freq_tbl = pd.crosstab(contingency_df.Gender,contingency_df.Unsatisfied, margins=True)
#print frequency table
print(freq_tbl.head(5))

#establish Critical Value variable for chi2 contingency table based on degrees of freedom and p value
CriticalValue = 3.841
#create array of observed values from frequency table
observed = np.array([[259, 242], [242, 257]])
#use scipy chi2_contingency to calculate chi2 results
results = chi2_contingency(observed)
print(results)
#convert results tuple to list
results = list(results)
#convert Test Statistic from results list to float
TestStatistic = float(results[0])
print(TestStatistic)
#if statement to test hypothesis
if TestStatistic < CriticalValue:
    print("accept null hypothesis; satisfaction independent of gender")
else:
    print("reject null hypothesis; satisfaction dependent of gender")
