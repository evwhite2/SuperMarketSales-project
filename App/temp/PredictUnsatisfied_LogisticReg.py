import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

model_df = pd.read_csv("new_supermarket_dummy_data.csv")

model_y = model_df[["Unsatisfied"]]

print("Descriptive Statistics for entire dataset: ")
print(model_y.describe(),"\n")

model_x = model_df[["fashion_accessories", "food_bev", "electronic_accessories", "sports_travel", "home_lifesyle", "health_beauty"]]

#Divide data into testing and training datasets
x_train, x_test, y_train, y_test = train_test_split(model_x,
                     model_y, test_size=0.25, random_state = 7)

print("Descriptive Statistics for training dataset: ")
print(y_train.describe(),"\n")
print("Number training cases unsatisfied:",sum(y_train.Unsatisfied),"\n")

print("Descriptive Statistics for testing dataset:")
print(y_test.describe(),"\n")
print("Number test cases unsatisfied:",sum(y_test.Unsatisfied),"\n")

#convert dataframe to one-dimensional array
y_train = np.ravel(y_train)

#construct logistic regression classifier
log_reg_classifier = LogisticRegression(solver='lbfgs').fit(x_train, y_train)

print("training score of logistic regression model: ")
print(round(log_reg_classifier.score(x_train, y_train),4),"\n")

#construct list of predictions
unsatisfied_predict=log_reg_classifier.predict(x_test)
print("Predictions based on test data:")
print(unsatisfied_predict)
print("Number predicted to be unsatisfied:", sum(unsatisfied_predict))

