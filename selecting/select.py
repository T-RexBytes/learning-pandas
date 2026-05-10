import pandas as pd

df = pd.read_csv("pokemon.csv", index_col = "Name")

#selecting data by column :

# print(df["Name"])
# print(df["Weight"])
# print(df["Height"])   
# print(df[["Name", "Weight", "Height"]])

#selecting data by row

# print(df.loc[0])
# print(df.loc["Pikachu", ["Height", "Weight"]])
# print(df.loc["Pikachu" : "Moltres", ["Height", "Weight"]])
# print(df.iloc[0:11:3])
print(df.iloc[0:11:3, 0:3])