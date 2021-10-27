import pandas as pd

def simple_stats(sales_df):
    
    #QUESTION 1 - Avg purchase price for each city- does the size of a city affect the amount purchased?
    sales_Br_A = sales_df.query('Branch == "A"')
    avg_sales_A = round(sales_Br_A["cogs"].mean(),3)
    sales_Br_B = sales_df.query('Branch == "B"')
    avg_sales_B = round(sales_Br_B["cogs"].mean(),3)
    sales_Br_C = sales_df.query('Branch == "C"')
    avg_sales_C = round(sales_Br_C["cogs"].mean(),3)
    print("\nAvg Sales price per city:")
    print(f"Branch A - Yangon:    ${avg_sales_A}")
    print(f"Branch B - Mandalay:  ${avg_sales_B}")
    print(f"Brancg C - Naypyitaw: ${avg_sales_C}")
    
    #QUESTION 5 - Total cost of goods sold
    print(f"Total cost of goods sold:   ${sales_df['cogs'].sum()}")
    
    #QUESTION 2 - Payment method- do customers buy more when using cc, cash, etc.?
    print("\nPayment method- raw counts:\n")
    print(sales_df["Payment"].value_counts(sort = True))
    
    #QUESTION 3 - What is the most popular category?  Are people more likely to use a cc to buy electronics, for example.
    print("\nPurchases by Category - raw counts:")
    print(sales_df["Product line"].value_counts(sort = True))
    
    #QUESTION 4 - Avg. Product price in a particular category
    print("\nAvg product price by category:")
    sales_df.rename(columns = {"Product line" : "Product_line"}, inplace = True)
    cat_fashion = sales_df.query('Product_line == "Fashion accessories"')
    avg_price_fashion = round(cat_fashion['Unit price'].mean(),3)
    cat_food = sales_df.query('Product_line == "Food and beverages"')
    avg_price_food = round(cat_food['Unit price'].mean(),3)
    cat_electronics = sales_df.query('Product_line == "Electronic accessories"')
    avg_price_electronics = round(cat_electronics['Unit price'].mean(),3)
    cat_sports = sales_df.query('Product_line == "Sports and travel"')
    avg_price_sports = round(cat_sports['Unit price'].mean(),3)
    cat_home = sales_df.query('Product_line == "Home and lifestyle"')
    avg_price_home = round(cat_home['Unit price'].mean(),3)
    cat_health = sales_df.query('Product_line == "Health and beauty"')
    avg_price_health = round(cat_health['Unit price'].mean(),3)
    print(f" \nFashion: ${avg_price_fashion}")
    print(f" \nFood & beverages:    ${avg_price_food}")
    print(f" \nElectronics: ${avg_price_electronics}")
    print(f" \nSports & travel: ${avg_price_sports}")
    print(f" \nHome & lifestyle:    ${avg_price_home}")
    print(f" \nHealth and beauty:   ${avg_price_health}")
    
    #QUESTION 6 - Avg. Customer satisfaction as per rating (per store)
    avg_satisfaction_A = round(sales_Br_A["Rating"].mean(),3)
    avg_satisfaction_B = round(sales_Br_B["Rating"].mean(),3)
    avg_satisfaction_C = round(sales_Br_C["Rating"].mean(),3)

    print("\nAvg Customer satisfaction rating by store:")
    print(f"\nBranch A: {avg_satisfaction_A}")
    print(f"\nBranch B: {avg_satisfaction_B}")
    print(f"\nBranch C: {avg_satisfaction_C}")

    print ("\nOverall satisfaction (if avg rating > 7)")
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
    male_df = sales_df.query('Gender == "Male"')
    female_df = sales_df.query('Gender == "Female"')
    print("\nProduct categories by purchaser gender\n")
    print("Males\n", male_df["Product_line"].value_counts(sort = True), "\n")
    print("Females\n", female_df["Product_line"].value_counts(sort = True))

