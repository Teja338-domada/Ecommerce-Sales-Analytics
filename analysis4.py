import pandas as pd

df = pd.read_csv("data/SampleSuperstore.csv")

category_profit = df.groupby('Category')['Profit'].sum()

print(category_profit)