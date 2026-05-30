import pandas as pd

df = pd.read_csv("data/SampleSuperstore.csv")

print("Total Sales:")
print(df['Sales'].sum())

print("\nTotal Profit:")
print(df['Profit'].sum())

print("\nTotal Quantity Sold:")
print(df['Quantity'].sum())