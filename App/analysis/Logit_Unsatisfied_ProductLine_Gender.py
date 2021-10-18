import statsmodels.formula.api as smf
import pandas as pd

model_df = pd.read_csv("new_supermarket_dummy_data.csv")

model = smf.logit(formula="Unsatisfied ~ fashion_accessories + food_bev + electronic_accessories + sports_travel + home_lifestyle + health_beauty + Gender_Male1", data = model_df).fit()

print(model.summary())
