import pandas as pd

df = pd.read_csv("customers.csv")
print("Average age:", df["age"].mean())
print("\nAverage spending by city:")
print(df.groupby("city")["spending"].mean())
