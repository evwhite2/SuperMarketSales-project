'''  ALGORTIHMS LIBRARY  - Last Modified Nov 1, 2021
This file is holds all the algorithmics functionality available to users via the control file. 
It also calls on the CleanDF class in the library file to produce and retrieve a csv and DataFrame of the categorical field dummy variables

Noted per Presentation - We did not have the KMean analysis working properly at the time, but it's been updated and works to product two different plots
'''

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from scipy.stats import chi2_contingency
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.cluster import KMeans
from matplotlib.lines import Line2D
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from library import CleanDF as cdf


class algorithmsLibrary:

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
    

    def runLogit_Unsatisfied_Vs_AllIndependentVariables(df):
        model = smf.logit(formula="Unsatisfied ~ fashion_accessories + food_bev + electronic_accessories + home_lifestyle + health_beauty + Gender_Male1 + member_1 + Naypyitaw + Mandalay + Cash + credit_card + Quantity + unit_price", data = df).fit()
        print(model.summary())
        #test only Mandalay variable
        model_Mandalay = smf.logit(formula="Unsatisfied ~ Mandalay", data = df).fit()

        print(model_Mandalay.summary())

        #test only food_bev variable
        model_food_bev = smf.logit(formula="Unsatisfied ~ food_bev", data = df).fit()

        print(model_food_bev.summary())

        #test all store dummy variables
        model_stores = smf.logit(formula="Unsatisfied ~ Mandalay + Naypyitaw", data = df).fit()

        print(model_stores.summary())



    def runChi2_Mandalay_Vs_Satisfaction(df):
        #create new dataframe of just two columns: Mandalay (found significant in logit), unsatisfied (categorical variables)
        contingency_df = df[['Mandalay','Unsatisfied']]
        #create frequency table using crosstab function in pandas
        freq_tbl = pd.crosstab(contingency_df.Mandalay,contingency_df.Unsatisfied, margins=True)
        #print frequency table
        print(freq_tbl.head(5))

        #establish Critical Value variable for chi2 contingency table based on degrees of freedom and p value
        CriticalValue = 3.841
        #create array of observed values from frequency table
        observed = np.array([[350, 318], [151, 181]])
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
            print("accept null hypothesis; dissatisfaction independent of Mandalay")
        else:
            print("reject null hypothesis; significant association between dissatisfaction and Mandalay")


    def runLogisticRegression_PredictUnsatisfied(df):
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
        print("testing score of logistic regression model: ")
        print(round(log_reg_classifier.score(x_test, y_test),4),"\n")
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


    def runCashStats(df):
        total_cash=df[df.Cash>=1]
        cash_total=int(total_cash.Total.mean())
        print(f"The average total price for using Cash is ${cash_total}")
        total_ewallet=df[df.Ewallet>= 1]
        ewallet_total=int(total_ewallet.Total.mean())
        print(f"The average total price for using Ewallet is ${ewallet_total}")
        total_cc=df[df.credit_card>= 1]
        cc_total=int(total_cc.Total.mean())
        print(f"The average total price for using Ewallet is ${cc_total}") 


    def runKMeansAnalysis(df): 
        print("\n\nRunning Cluster Analysis on fields with relevant information related specifically to customer. \n Number of Clusters = 5")
        x_vars = df[['Yangon', 'Naypyitaw', 'Mandalay', 'member_1', 'Gender_Male1', 'fashion_accessories','food_bev', 'electronic_accessories','sports_travel','home_lifestyle','health_beauty', 'Total', "Ewallet", "Cash", "credit_card", "Quantity"]].values
        data_transformed = MinMaxScaler().fit(x_vars).transform(x_vars)
        kmeans_model = KMeans(n_clusters = 5, random_state=1).fit(data_transformed)
        centroids = kmeans_model.cluster_centers_
        df['cluster'] = kmeans_model.labels_
        colors = ['#DF2020', '#81DF20', '#2095DF', '#884EA0', '#F4D03F']
        df['color'] = df.cluster
        for i in df.color:
            i = colors[i]
        #configuring the legend
        legend_elements = [Line2D([0], [0], marker='o', color='w', label='Cluster {}'.format(i+1), markerfacecolor=mcolor, markersize=5) for i, mcolor in enumerate(colors)]
        #plotting cluster analysis Price v Quantity
        fig, ax = plt.subplots(1, figsize=(8,8))
        ax.scatter(df.Quantity, df.Total, c=df.color, alpha=.5, s=25)
        plt.xlabel('price of purchased item')
        plt.ylabel('quantity')
        plt.legend(handles=legend_elements, loc='upper right')
        plt.title('Price vs Quantity, number clusters = 5\n', loc='left', fontsize=16)
        #plotting cluster analysis City v Product line
        fig, ax = plt.subplots(1, figsize=(8,8))
        ax.scatter(df.City, df.product_line, c=df.color, alpha=.5, s=100)
        plt.xlabel('Branch City')
        plt.ylabel('Product Line')
        plt.title('Product purchases by Branch City, number clusters = 5\n', loc='left', fontsize=16)
        #plotting cluster analysis City v Product line
        fig, ax = plt.subplots(1, figsize=(8,8))
        ax.scatter(df.product_line, df.Total, c=df.color, alpha=.5, s=50)
        plt.xlabel('Product Line')
        plt.ylabel('Price Total')
        plt.title('Product Line vs price Total, number clusters = 5\n', loc='left', fontsize=16)
        plt.show()


export: algorithmsLibrary