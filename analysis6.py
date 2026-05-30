import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/SampleSuperstore.csv")

region_sales = df.groupby('Region')['Sales'].sum()

region_sales.plot(kind='bar')

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.show()