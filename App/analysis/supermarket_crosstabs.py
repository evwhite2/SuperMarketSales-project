import pandas as pd

df= pd.read_csv("./new_supermarket_dummy_data.csv")

#renaming colums with spaces
df.rename(columns = {'Invoice ID':'invoice_ID', 'Customer type':'customer_type', 'Product line':'product_line', 'Unit price':'unit_price', 'Tax 5%':'tax_5%', 'gross margin percentage':'gross_margin_%', 'gross income':'gross_income'}, inplace = True)

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

