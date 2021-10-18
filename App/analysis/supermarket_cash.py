import pandas as pd

df= pd.read_csv("./new_supermarket_dummy_data.csv")


#total=df[df['Cash']>0].Cash.count()
total_cash=df[df.Cash>=1]
cash_total=int(total_cash.Total.mean())
print(f"The average total price for using Cash is ${cash_total}")

total_ewallet=df[df.Ewallet>= 1]
ewallet_total=int(total_ewallet.Total.mean())
print(f"The average total price for using Ewallet is ${ewallet_total}")

total_cc=df[df.credit_card>= 1]
cc_total=int(total_cc.Total.mean())
print(f"The average total price for using Ewallet is ${cc_total}") 


#new_file= total_cash.to_csv("new_supermarket_cash.csv")
