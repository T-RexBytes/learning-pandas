import pandas as pd

df = pd.read_csv("pokemon.csv")


# 1. drop() : dropping not needed columns
# df = df.drop(columns=["Legendary", "No"])


# 2. Handle missing Data
# df = df.dropna(subset=["Type2"])
# df = df.fillna({"Type2" : "None"})

# 3. Fix inconsistant values
# df["Type1"] = df["Type1"].replace({"Grass" : "GRASS"})
# df[["Type1", "Type2"]] = df[["Type1", "Type2"]].replace({"Grass": "GRASS", "Watre": "WATER"})

# 4. Standertize data
# df["Name"] = df["Name"].str.lower()

# 5. Fixing Data types
# df["Legendary"] = df["Legendary"].astype(bool)

#  6. Remove Duplicate Values 
df = df.drop_duplicates()


print(df.to_string())