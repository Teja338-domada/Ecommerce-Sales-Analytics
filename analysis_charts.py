import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/SampleSuperstore.csv")

# Region Sales
region_sales = df.groupby('Region')['Sales'].sum()

plt.figure(figsize=(8,5))
region_sales.plot(kind='bar')

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("visuals/sales_by_region.png")

plt.show()

category_profit = df.groupby('Category')['Profit'].sum()

plt.figure(figsize=(8,5))
category_profit.plot(kind='bar')

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")

plt.tight_layout()

plt.savefig("visuals/profit_by_category.png")

plt.show()

top_products = (
    df.groupby('Sub-Category')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,5))
top_products.plot(kind='bar')

plt.title("Top Selling Sub-Categories")
plt.xlabel("Sub-Category")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("visuals/top_products.png")

plt.show()