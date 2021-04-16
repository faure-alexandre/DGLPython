# -*- coding: utf-8 -*-

import re


# Ouverture du fichier
f = open("data.txt", "r")
data = f.read()
f.close()

# On split chaque lettre
all_letters = re.findall(r'[a-zA-Z]', data)

# On transforme les majuscules en minuscules
all_letters_lower = [each_string.lower() for each_string in all_letters]

# Puis on compte
nb_letters = dict((x,all_letters_lower.count(x)) for x in set(all_letters_lower))


# Matplotlib
import matplotlib.pyplot as plt

plt.figure()
plt.bar(nb_letters.keys(), nb_letters.values(), 1, color='g')
plt.title("Histogramme d'apparition de chaque lettre")
plt.xlabel("Lettres")
plt.show()