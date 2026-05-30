import pandas as pd

df = pd.read_csv("data/SampleSuperstore.csv")

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned data
df.to_csv("data/cleaned_superstore.csv", index=False)

print("Cleaned dataset exported successfully!")