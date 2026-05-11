import pandas as pd

df = pd.read_csv("pokemon.csv")

#filtering = keeping the rows that matches a condition

# tall_pokemon = df[df["Height"] >= 2] 
# water_pokemon= df[(df["Type1"] == "Water") | (df["Type2"] == "Water")]
fire_pokemon = df[(df["Type1"] == "Fire") & (df["Type2"] == "Flying")]
# legenday_pokemon = df[df["Legendary"] == True]

print(fire_pokemon) 