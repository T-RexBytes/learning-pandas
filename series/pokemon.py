import pandas as pd

pokedex = {"firetype" : ["Charmender", "Charmelion", "Charizard"], 
           "watertype" : ["Squirtle", "Wartortle", "Blastoise"], 
           "grasstype" : ["Bulbasaur", "Ivysaur", "Venusaur"], 
           "electrictype" : ["Pichu", "Pikachu", "Raichu"] }

pokemon = pd.Series(pokedex)



print(pokemon.loc["electrictype"][1])

