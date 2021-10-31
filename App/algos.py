import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from scipy.stats import chi2_contingency
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from library import CleanDF as cdf

def createDummies(rawDF):
    dummy_df= cdf.cleanDummies(rawDF)
    return dummy_df

def runChi2_Gender_Vs_Satisfaction(df):
    #create new dataframe of just two columns: gender, unsatisfied (categorical variables)
    contingency_df = df[['Gender','Unsatisfied']]
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


def runLogit_Unsatisfied_Vs_ProductLine_Vs_Gender(df):
    model = smf.logit(formula="Unsatisfied ~ fashion_accessories + food_bev + electronic_accessories + sports_travel + home_lifestyle + health_beauty + Gender_Male1", data = df).fit()
    print(model.summary())


def runLogisticRegresstion_Unsatisfied_Vs_ProductLine(df):
    model_y = df[['Unsatisfied']]
    model_x = df[['fashion_accessories', 'food_bev', 'electronic_accessories', 'sports_travel', 'home_lifestyle', 'health_beauty']]
    x_train, x_test, y_train, y_test = train_test_split(model_x, model_y, test_size=0.25, random_state=7)
    print("----------> number unsatisfied:  ",sum(y_test.Unsatisfied), "\n")
    y_train = np.ravel(y_train) #not a required step, but will produce a warning message with the Logistic Regression function if not included
    log_reg_classifier = LogisticRegression(solver='lbfgs').fit(x_train, y_train)
    print("resting score of logistic regression model:  ")
    print(round(log_reg_classifier.score(x_test, y_test), 4), "\n")
    unsatisfied_predict = log_reg_classifier.predict(x_test)
    print("Predictions based on test data: ")
    print(unsatisfied_predict)
    print("Number predicted to be unsatisfied:  ", sum(unsatisfied_predict))


def runLogisticRegresstion_PredictUnsatisfied(df):
    model_y = df[["Unsatisfied"]]
    print("Descriptive Statistics for entire dataset: ")
    print(model_y.describe(),"\n")
    model_x = df[["Mandalay"]]
    #Divide data into testing and training datasets
    x_train, x_test, y_train, y_test = train_test_split(model_x,
                        model_y, test_size=0.10, random_state = 7)
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
    #print out classification report
    print(classification_report(y_test,unsatisfied_predict))


def runCrossTabulation(df):
    customer_gender= pd.crosstab(df['customer_type'], df['Gender'], margins=True, margins_name= "Total")
    payment_gender= pd.crosstab(df['Payment'], df['Gender'], margins=True, margins_name= "Total")
    city_gender= pd.crosstab(df['City'], df['Gender'], margins=True, margins_name= "Total")
    payment_city= pd.crosstab(df['Payment'], df['City'], margins=True, margins_name= "Total")
    product_gender= pd.crosstab(df['product_line'], df['Gender'], margins=True, margins_name= "Total")
    customer_product= pd.crosstab(df['product_line'], df['customer_type'], margins=True, margins_name= "Total")
    product_gender= pd.crosstab(df['product_line'], df['Gender'], margins=True, margins_name= "Total")
    member_city= pd.crosstab(df['customer_type'], df['City'], margins=True, margins_name= "Total")
    print(customer_gender, "\n")
    print(payment_gender, "\n")
    print(city_gender, "\n")
    print(payment_city, "\n")
    print(product_gender, "\n")
    print(customer_product, "\n")
    print(member_city)


def runCash(df):
    total_cash=df[df.Cash>=1]
    cash_total=int(total_cash.Total.mean())
    print(f"The average total price for using Cash is ${cash_total}")
    total_ewallet=df[df.Ewallet>= 1]
    ewallet_total=int(total_ewallet.Total.mean())
    print(f"The average total price for using Ewallet is ${ewallet_total}")
    total_cc=df[df.credit_card>= 1]
    cc_total=int(total_cc.Total.mean())
    print(f"The average total price for using Ewallet is ${cc_total}") 
