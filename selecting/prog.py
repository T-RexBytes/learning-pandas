import pandas as pd

df = pd.read_csv("pokemon.csv", index_col="Name")

pokemon = input("Enter Your Pokemon's Name : ")

try : 
    print(df.loc[pokemon.title()]) #we use .title() to make sure every given valid name of the pokemon works inspite of the 1st letter being small
except KeyError:
    print(f"{pokemon} not found!")
