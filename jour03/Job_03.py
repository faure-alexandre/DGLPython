# -*- coding: utf-8 -*-

import re

# Demande a l'utilisateur de renseigner un nombre
nb = int(input("Veuillez renseigner une taille de mot:"))

f = open("data.txt", "r")
data = f.read()
f.close()

regex = r'\w{' + str(nb) + '}'
all_nb_words = re.findall(regex, data)

print(len(all_nb_words))

