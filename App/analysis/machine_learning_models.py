import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

import datetime

ct = datetime.datetime.now()
print("\n---------------------------------------------\n", "run timestamp: ", ct, "\n---------------------------------------------")

df= pd.read_csv("./new_supermarket_dummy_data.csv")

#renaming colums with spaces
df.rename(columns = {'Invoice ID':'invoice_ID', 'Customer type':'customer_type', 'Product line':'product_line', 'Unit price':'unit_price', 'Tax 5%':'tax_5%', 'gross margin percentage':'gross_margin_%', 'gross income':'gross_income'}, inplace = True)

model_y = df[['Unsatisfied']]
# print(model_y.describe())

model_x = df[['fashion_accessories', 'food_bev', 'electronic_accessories', 'sports_travel', 'home_lifestyle', 'health_beauty']]

x_train, x_test, y_train, y_test = train_test_split(model_x, model_y, test_size=0.25, random_state=7)

# print("\n-------------describe training set-------------\n")
# print(y_train.describe(), "\n")

# print("\n-------------describe test set-------------\n")
# print(y_test.describe(), "\n")
print("----------> number unsatisfied:  ",sum(y_test.Unsatisfied), "\n")

y_train = np.ravel(y_train) #not a required step, but will produce a warning message with the Logistic Regression function if not included

log_reg_classifier = LogisticRegression(solver='lbfgs').fit(x_train, y_train)

print("resting score of logistic regression model:  ")
print(round(log_reg_classifier.score(x_test, y_test), 4), "\n")

unsatisfied_predict = log_reg_classifier.predict(x_test)
print("Predictions based on test data: ")
print(unsatisfied_predict)
print("Number predicted to be unsatisfied:  ", sum(unsatisfied_predict))
