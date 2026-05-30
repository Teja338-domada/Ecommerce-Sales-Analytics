import pandas as pd

df = pd.read_csv("data/SampleSuperstore.csv")

print("Duplicate Rows:")
print(df.duplicated().sum())