'''  LIBRARY & CLEANDF  - Last Modified Oct 31, 2021
This file contains all the helper functions used to produce outputs to the user in all other App/ files. The library class is separate from the cleanDF class because of their speicific purposes.
'''

import datetime
from numpy import lib
import pandas as pd

class Library:
    choice_list = [
        {1: "View sample analytics"}, 
        {2: "Run Analysis"}]
    analytics_choice_list = [
        {1: "Sales Histograms by branch"}, 
        {2: "Machine Learning"}, 
        {3: "View box plot of Branch ratings"}, 
        {4: "View FacetGrid of all Sales by Branch"}]
    algo_choice_list = [
        {1:"runChi2_Gender_Vs_Satisfaction"},
        {2:"runLogit_Unsatisfied_Vs_AllIndependentVariables"}, 
        {3: "runChi2_Mandalay_Vs_Satisfaction"}, 
        {4:"runLogisticRegression_PredictUnsatisfied"}, 
        {5: "runCrossTabulation"},
        {6: "runKMeansAnalysis"}]
    filter_options_list = [
        {1: "Filter minimum value only"}, 
        {2: "Filter maximum value only"},
        {3: "Filter minimum & maximum values"}]

    raw_data_csv = './supermarket_sales.csv'

    def validateChoice(k, v, prompt):
        i = input(prompt)
        p = "Select choice from the list: "
        if i is None:
            raise ValueError("ERR1 - Please input selection.")
        while True:
            try:
                i = int(i)
                if i in k:
                    break
                elif i == 0:
                    print("...returning")
                    break
                else:
                    i = input("ERR2 - Input selection from list of options:   ")
            except ValueError:
                i = input("ERR3 - Input must be numeric:    ")
        return i
    
    def validateYN(ip):
        ip = ip.lower()
        options = ['n', 'y']
        while True:
            if ip not in options:
                ip = input("Please confirm 'y' or 'n")
            else:
                break
        return bool(options.index(ip))

    def validateMinMax(df, field):
        filter_type = Library.printArrayDict(Library.filter_options_list)
        filter_type = filter_type[2]
        while filter_type > 0:
            if filter_type == 1:
                n2 = input("Enter minimum value filter: ")
                df = df.query(f"{field} > {n2}")
                filter_type = filter_type-1
            if filter_type == 2:
                n1 = input("Enter maximum value filter: ")
                df = df.query(f"{field} < {n1}")
                filter_type = filter_type-2
            elif filter_type == 3:
                n1 = input("Enter maximum value filter: ")
                n2 = input("Enter minimum value filter: ")
                df = df.query(f"{field} < {n1}")
                df = df.query(f"{field} > {n2}")
                filter_type = filter_type-3
            else:
                print("exiting filters")
                break
        # print("\nMODIFIED DF:") #TEST INFO
        # print(df[field], df) #TEST INFO
        return(df)


    def printArrayDict(list_of_kv_pairs):
        k_list=list()
        v_list=list()
        for i in list_of_kv_pairs:
            for key, value in i.items():
                k_list.append(key)
                v_list.append(value)
                print(key, "---", value)
        print("0 --- Exit/Back")
        prompt = "Input numeric selection:   "
        choice = Library.validateChoice(k_list, v_list, prompt)
        return k_list, v_list, choice

    def printRedirectMessage(string):
        now = datetime.datetime.now()
        timestamp = now.strftime("%H:%M:%S")
        print(f'-------------Operation complete at {timestamp}-------------\n\n{string}\n')

    def createListDict(df_col):
        fields_list = df_col
        field_list_dict = []
        for i in fields_list:
            field_list_dict.append({fields_list.index(i)+1:i})
        return field_list_dict

    def getCategories(df, field):
        k_list=list()
        v_list=list()
        q_list = list()
        series = df[field]
        for i in series:
            val = i
            if val not in v_list:
                v_list.append(val)
                k_list.append(len(v_list))
                print(len(v_list), "---", val)
        while True:
            try:
                c = Library.validateChoice(k_list, v_list, 'Select from list to INCLUDE in query:    ')
                if c == 0:
                    print("Invalid input.")
                    continue
                q_list.append(v_list[c-1])
                if len(q_list)==len(v_list)-1:
                    break
                else:
                    next_prompt = input("Would you like to add another? (type y/n):   ")
                    if_next = Library.validateYN(next_prompt)
                    if if_next == False:
                        break
                    else:
                        continue
            except ValueError:
                print("Invalid input")
                break
        print(f"Filtering selection to include records where {field} in {q_list}")
        return q_list

    
class CleanDF:
    def cleanTypes(df):
        for i in df.Date:
            df.Date.replace(to_replace=[i], value=[pd.to_datetime(i).date()], inplace=True)
        for i in df.Time:
            df.Time.replace(to_replace=[i], value=[pd.to_datetime(i).strftime("%H:%M:%S")], inplace=True)
        return df

    def cleanNames(df):
        df.rename(columns = {'Invoice ID':'invoice_ID', 'Customer type':'customer_type', 'Product line':'product_line', 'Unit price':'unit_price', 'Tax 5%':'tax_5%', 'gross margin percentage':'gross_margin_%', 'gross income':'gross_income'}, inplace = True)
        return df


    def cleanDummies(df):
        df.rename(columns = {'Invoice ID':'invoice_ID', 'Customer type':'customer_type', 'Product line':'product_line', 'Unit price':'unit_price', 'Tax 5%':'tax_5%', 'gross margin percentage':'gross_margin_%', 'gross income':'gross_income'}, inplace = True)
        
        df.product_line.replace(to_replace=['Fashion accessories'], value= ["fashion_accessories"], inplace=True)
        df.product_line.replace(to_replace=['Food and beverages'], value= ["food_bev"], inplace=True)
        df.product_line.replace(to_replace=['Electronic accessories'], value= ["electronic_accessories"], inplace=True)
        df.product_line.replace(to_replace=['Sports and travel'], value= ["sports_travel"], inplace=True)
        df.product_line.replace(to_replace=['Home and lifestyle'], value= ["home_lifestyle"], inplace=True)
        df.product_line.replace(to_replace=['Health and beauty'], value= ["health_beauty"], inplace=True)
        product_series=df.product_line
        product= pd.get_dummies(product_series, columns=['product_line'])
        df['fashion_accessories']=product.fashion_accessories
        df['food_bev']=product.food_bev
        df['electronic_accessories']= product.electronic_accessories
        df['sports_travel']= product.sports_travel
        df['home_lifestyle']= product.home_lifestyle
        df['health_beauty']= product.health_beauty

        gender_series=df.Gender
        gender_dummies=pd.get_dummies(gender_series, columns=['Gender'])
        df['Gender_Male1']= gender_dummies.Male

        df.Payment.replace(to_replace=['Credit card'], value= ["credit_card"], inplace=True)

        payment_series=df.Payment    
        payment= pd.get_dummies(payment_series, columns=['Payment'])
        df['Ewallet']=payment.Ewallet
        df['Cash']=payment.Cash
        df['credit_card']= payment.credit_card

        customer_series=df.customer_type
        members=pd.get_dummies(customer_series, columns=['customer_type'])
        df['member_1']= members.Member

        #city dummy variables
        city_series=df.City
        city=pd.get_dummies(city_series, columns=['City'])
        df['Yangon']= city.Yangon
        df['Naypyitaw']= city.Naypyitaw
        df['Mandalay']= city.Mandalay
        
        df.loc[df.Rating < 7, 'Rating'] = 1
        df.loc[df.Rating >= 7, 'Rating'] = 0
        df.rename(columns = {"Rating":"Unsatisfied"}, inplace = True)

        # #changing the layout of the page
        df=df[['invoice_ID', 'Branch', 'City','Yangon', 'Naypyitaw','Mandalay', 'customer_type','member_1', 'Gender','Gender_Male1', 'product_line','fashion_accessories','food_bev', 'electronic_accessories','sports_travel', 'home_lifestyle', 'health_beauty', 'unit_price', 'Quantity', 'tax_5%', 'Total', 'Date','Time', 'Payment','Ewallet', 'Cash', 'credit_card', 'cogs', 'gross_margin_%', 'gross_income','Unsatisfied']]
        df.to_csv("./new_supermarket_dummy_data.csv")
        return df

           
export: Library 
export: CleanDF
