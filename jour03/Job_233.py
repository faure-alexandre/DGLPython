# -*- coding: utf-8 -*-


# Extraction de la liste de pokemons
import csv
import re
 
pokemon_list = []


with open('pokemon.csv', encoding='utf8') as File:
    reader = csv.reader(File, delimiter=',')
    for line in reader:
        pokemon_list.append(line[1]) 
        
del pokemon_list[0]


# Recuperation data
f = open("data.txt", "r")
data = f.read()
f.close()


# On boucle sur tout les pokemons
for pokemon in pokemon_list:
    t = re.findall(pokemon, data)
    
    if len(t) > 0:
        print(t[0])
    
# On trouve le pokemon "Natu"




