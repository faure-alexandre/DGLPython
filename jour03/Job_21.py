# -*- coding: utf-8 -*-

import re
import json

# Ouverture du fichier
f = open("data.txt", "r")
data = f.read()
f.close()


all_group_letters = re.findall(r'[a-zA-Z][a-zA-Z]', data)

test = [(x[0].lower(),x[1].lower()) for x in all_group_letters]
test2 = [(test[i][1], test[i+1][0]) for i in range(len(test)-1)]

all_group_2letters = test + test2

d = {}

for x in set(all_group_2letters):
    nb = all_group_2letters.count(x)
    
    if x[0] in d.keys():
        d[x[0]][x[1]] = nb
    else:
        d[x[0]] = {}
        d[x[0]][x[1]] = nb
    

# Normalisation
for x in d.values():
    norm = 0
    for y in x.keys():
        norm += x[y]
    for z in x.keys():
        x[z] = (x[z]/norm)*100
        

#Enregistrement pour pas avoir à recalculer dans job_34...

# Enregistrer le dictionnaire dans un fichier :
with open('job_21.txt', 'w') as file:
    json.dump(d, file)
 
    
    
    