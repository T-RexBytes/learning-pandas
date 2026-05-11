import pandas as pd

df = pd.read_csv("pokemon.csv")

# Whole DataFrame
# print(df.mean(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.count())

#Single Columns
# print(df["Height"].mean())
# print(df["Weight"].min())
# print(df["Weight"].max())
# print(df["Legendary"].sum())
# print((df["Type2"] == "Poison").count())

#groupby

group = df.groupby("Type1")
# print(group["Height"].mean())
# print(group["Height"].min())
# print(group["Height"].max())
# print(group["Height"].sum())
print(group["Height"].count())