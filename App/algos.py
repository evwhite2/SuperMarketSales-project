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
        #I think I need to make new dummy data with more than 1's and 0s to do a proper scatter plot
        x_vars = df[['Yangon', 'Naypyitaw', 'Mandalay', 'member_1', 'Gender_Male1', 'fashion_accessories','food_bev', 'electronic_accessories','sports_travel','home_lifestyle','health_beauty']].values
        data_transformed = MinMaxScaler().fit(x_vars).transform(x_vars)
        kmeans_model = KMeans(n_clusters = 5, random_state=1).fit(data_transformed)
        centroids = kmeans_model.cluster_centers_
        df['cluster'] = kmeans_model.labels_
        cen_x = [i[0] for i in centroids]
        cen_y = [i[1] for i in centroids]
        df['cen_x'] = df.cluster.map({0:cen_x[0], 1:cen_x[1], 2:cen_x[2], 3:cen_x[3], 4:cen_x[4]})
        df['cen_y'] = df.cluster.map({0:cen_y[0], 1:cen_y[1], 2:cen_y[2], 3:cen_y[3], 4:cen_y[4]})
        colors = ['#DF2020', '#81DF20', '#2095DF', '#884EA0', '#F4D03F']
        df['color'] = df.cluster.map({0:colors[0], 1:colors[1], 2:colors[2], 3:colors[3], 4:colors[4]})
        fig, ax = plt.subplots(1, figsize=(8,8))
        ax.scatter(df.cen_x, df.cen_y, c=df.color, alpha=1, s=10)
        plt.xlabel('center x')
        plt.ylabel('center y')
        plt.show()
        # c1 = df.query('cluster==0')
        # c2 = df.query('cluster==1')
        # c3 = df.query('cluster==2')
        # c4 = df.query('cluster==3')
        # c5 = df.query('cluster==4')
        # print(c1.head(10))


export: algorithmsLibrary