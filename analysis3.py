import pandas as pd

df = pd.read_csv("data/SampleSuperstore.csv")

region_sales = df.groupby('Region')['Sales'].sum()

print(region_sales)