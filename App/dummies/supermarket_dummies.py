import pandas as pd
import datetime

file=pd.read_csv("./supermarket_sales.csv")


#renaming colums with spaces
file.rename(columns = {'Invoice ID':'invoice_ID', 'Customer type':'customer_type', 'Product line':'product_line', 'Unit price':'unit_price', 'Tax 5%':'tax_5%', 'gross margin percentage':'gross_margin_%', 'gross income':'gross_income'}, inplace = True)

#listing all of the types of of products in order to create dummie variables
print(file.head())
product=file['product_line']
print(product.value_counts())


#changing product_line names
file.product_line.replace(to_replace=['Fashion accessories'], value= ["fashion_accessories"], inplace=True)
file.product_line.replace(to_replace=['Food and beverages'], value= ["food_bev"], inplace=True)
file.product_line.replace(to_replace=['Electronic accessories'], value= ["electronic_accessories"], inplace=True)
file.product_line.replace(to_replace=['Sports and travel'], value= ["sports_travel"], inplace=True)
file.product_line.replace(to_replace=['Home and lifestyle'], value= ["home_lifestyle"], inplace=True)
file.product_line.replace(to_replace=['Health and beauty'], value= ["health_beauty"], inplace=True)

#product_line dummy variables
product_series=file.product_line
                     
product= pd.get_dummies(product_series, columns=['product_line'])

file['fashion_accessories']=product.fashion_accessories
file['food_bev']=product.food_bev
file['electronic_accessories']= product.electronic_accessories
file['sports_travel']= product.sports_travel
file['home_lifestyle']= product.home_lifestyle
file['health_beauty']= product.health_beauty


#creating dummmy vaiables for gender
gender_series=file.Gender

gender_dummies=pd.get_dummies(gender_series, columns=['Gender'])

file['Gender_Male1']= gender_dummies.Male


#payment dummy variables
file.Payment.replace(to_replace=['Credit card'], value= ["credit_card"], inplace=True)

payment_series=file.Payment
                     
payment= pd.get_dummies(payment_series, columns=['Payment'])

file['Ewallet']=payment.Ewallet
file['Cash']=payment.Cash
file['credit_card']= payment.credit_card





#customer_type dummy variables
customer_series=file.customer_type

members=pd.get_dummies(customer_series, columns=['customer_type'])

file['member_1']= members.Member


#city dummy variables
city_series=file.City

city=pd.get_dummies(city_series, columns=['City'])

file['Yangon']= city.Yangon
file['Naypyitaw']= city.Naypyitaw
file['Mandalay']= city.Mandalay


# #Rating column recoded
file.loc[file.Rating < 7, 'Rating'] = 1
file.loc[file.Rating >= 7, 'Rating'] = 0
file.rename(columns = {"Rating":"Unsatisfied"}, inplace = True)

# #changing the layout of the page
file=file[['invoice_ID', 'Branch', 'City','Yangon', 'Naypyitaw','Mandalay', 'customer_type','member_1', 'Gender','Gender_Male1', 'product_line','fashion_accessories','food_bev', 'electronic_accessories','sports_travel', 'home_lifestyle', 'health_beauty', 'unit_price', 'Quantity', 'tax_5%', 'Total', 'Date','Time', 'Payment','Ewallet', 'Cash', 'credit_card', 'cogs', 'gross_margin_%', 'gross_income','Unsatisfied']]

new_file= file.to_csv("./new_supermarket_dummy_data.csv")
