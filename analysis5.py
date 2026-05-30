import pandas as pd

df = pd.read_csv("data/SampleSuperstore.csv")

top_products = (
    df.groupby('Sub-Category')['Sales']
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print(top_products)