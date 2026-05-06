import pandas as pd 

pokedex = {"firetype" : ["Charmender", "Charmelion", "Charizard"], 
           "watertype" : ["Squirtle", "Wartortle", "Blastoise"], 
           "grasstype" : ["Bulbasaur", "Ivysaur", "Venusaur"], 
           "electrictype" : ["Pichu", "Pikachu", "Raichu"] }

pokemon = pd.DataFrame(pokedex, index = ["1st Evo", "2nd Evo", "3rd Evo"])

pokemon["flyingtype"] = ["Pidgy", "Pidgeotto", "Pidgeot"]


new_row = pd.DataFrame({
    "firetype": ["Tepig", "Pignite", "Emboar"],
    "watertype": ["Oshawott", "Dewott", "Samurott"],
    "grasstype": ["Snivy", "Servine", "Serperior"],
    "electrictype": ["Tynamo", "Eelektrik", "Eelektross"],
    "flyingtype": ["Pidove", "Tranquill", "Unfezant"]
}, index=["1st Evo", "2nd Evo", "3rd Evo"])
pokemon = pd.concat([pokemon, new_row])

print(pokemon)
