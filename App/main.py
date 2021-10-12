
import pandas as pd
sales_df = pd.read_csv("./supermarket_sales.csv")     #read csv file using pandas
print("\n The columns in sales_df DataFrame are: \n", sales_df.columns)

#QUESTION 1 - Avg purchase price for each city- does the size of a city affect the amount purchased?
print(" \n 1. Avg purchase price for each city: \n")
sales_Br_A = sales_df.query('Branch == "A"')
avg_sales_A = round(sales_Br_A["cogs"].mean(),3)
print(f"\n The average sales in Branch A which is located in Yangon is {avg_sales_A} sales.")
sales_Br_B = sales_df.query('Branch == "B"')
avg_sales_B = round(sales_Br_B["cogs"].mean(),3)
print(f"\n The average sales in Branch B which is located in Mandalay is {avg_sales_B} sales.")
sales_Br_C = sales_df.query('Branch == "C"')
avg_sales_C = round(sales_Br_C["cogs"].mean(),3)
print(f"\n The average sales in Branch C which is located in Naypyitaw is {avg_sales_C} sales.")

#QUESTION 2 - Payment method- do customers buy more when using cc, cash, etc.?
print("\n 2. Payment method- do customers buy more when using cc, cash, etc.? ")
print("\n", sales_df["Payment"].value_counts(sort = True), "\n")

#QUESTION 3 - What is the most popular category?  Are people more likely to use a cc to buy electronics, for example.
print("\n 3. What is the most popular category?  ")
print("\n", sales_df["Product line"].value_counts(sort = True), "\n")

#QUESTION 4 - Avg. Product price in a particular category
print("\n 4. Avg. Product price in a particular category")
sales_df.rename(columns = {"Product line" : "Product_line"}, inplace = True)
cat_fashion = sales_df.query('Product_line == "Fashion accessories"')
avg_price_fashion = round(cat_fashion['Unit price'].mean(),3)
print(f" \n The average product price in the category Fashion accessories is ${avg_price_fashion}")
cat_food = sales_df.query('Product_line == "Food and beverages"')
avg_price_food = round(cat_food['Unit price'].mean(),3)
print(f" \n The average product price in the category Food and beverages is ${avg_price_food}")
cat_electronics = sales_df.query('Product_line == "Electronic accessories"')
avg_price_electronics = round(cat_electronics['Unit price'].mean(),3)
print(f" \n The average product price in the category Electronic accessories is ${avg_price_electronics}")
cat_sports = sales_df.query('Product_line == "Sports and travel"')
avg_price_sports = round(cat_sports['Unit price'].mean(),3)
print(f" \n The average product price in the category Sports and travel is ${avg_price_sports}")
cat_home = sales_df.query('Product_line == "Home and lifestyle"')
avg_price_home = round(cat_home['Unit price'].mean(),3)
print(f" \n The average product price in the category Home and lifestyle is ${avg_price_home}")
cat_health = sales_df.query('Product_line == "Health and beauty"')
avg_price_health = round(cat_health['Unit price'].mean(),3)
print(f" \n The average product price in the category Health and beauty is ${avg_price_health}")

#QUESTION 5 - Total cost of goods sold
print(" \n 5. Total cost of goods sold")
print (" \n The total cost of goods sold is: $", sales_df["cogs"].sum())

#QUESTION 6 - Avg. Customer satisfaction as per rating (per store)
print("\n 6. Avg. Customer satisfaction as per rating (per store)")
avg_satisfaction_A = round(sales_Br_A["Rating"].mean(),3)
print(f"\n The average Customer satisfaction as per rating in Branch A is {avg_satisfaction_A}.")
avg_satisfaction_B = round(sales_Br_B["Rating"].mean(),3)
print(f"\n The average Customer satisfaction as per rating in Branch B is {avg_satisfaction_B}.")
avg_satisfaction_C = round(sales_Br_C["Rating"].mean(),3)
print(f"\n The average Customer satisfaction as per rating in Branch C is {avg_satisfaction_C}.")

#QUESTION 7 - Time frame when the stores are most busy?

#QUESTION 8 - 	Are most of the customers satisfied overall?
print ("\n 8. Are most of the customers satisfied overall?")
if avg_satisfaction_A > 7:
    print("\nThe customers are pretty satisfied in Branch A")
else:
    print("\nThe custometrs are not too satisfied in Branch A")
    
if avg_satisfaction_B > 7:
    print("\nThe customers are pretty satisfied in Branch B")
else:
    print("\nThe custometrs are not too satisfied in Branch B")
if avg_satisfaction_C > 7:
    print("\nThe customers are pretty satisfied in Branch C")
else:
    print("\nThe custometrs are not too satisfied in Branch C")

#QUESTION 9 - If most customer are male or female and members or non-members?
print ("\n 9. If most customer are male or female and members or non-members?")
print("\n", sales_df["Gender"].value_counts(sort = True), "\n")
sales_df.rename(columns = {"Customer type" : "Customer_type"}, inplace = True)
sales_df.Customer_type.replace(to_replace = ["Normal"], value = ["Non_Member"], inplace = True)
print("\n", sales_df["Customer_type"].value_counts(sort = True), "\n")

#QUESTION 10 - Does customer gender influence what product categories the customer buys?
print("\n 10. Does customer gender influence what product categories the customer buys?")
print("\n Product categories the Male customer buys: ") 
male_df = sales_df.query('Gender == "Male"')
print("\n ", male_df["Product_line"].value_counts(sort = True), "\n")
print("\n Product categories the Female customer buys: ")
female_df = sales_df.query('Gender == "Female"')
print("\n ", female_df["Product_line"].value_counts(sort = True), "\n")

