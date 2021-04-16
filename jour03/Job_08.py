# -*- coding: utf-8 -*-

import re

"""
Fonction qui ouvre le fichier et calcule le nombre de mots pour chaque longueur
de mot

Parameters
----------
         
Returns
-------
words_len : dict
            dictionnaire ayant pour clé la longueur et valeur le nombre de mots
            correspondant à cette longueur
        
"""
def longeur_mots():
    # Ouverture du fichier
    f = open("data.txt", "r")
    data = f.read()
    f.close()

    # On split chaque lettre
    all_words = re.findall(r'\w+', data)

    # Puis on compte
    nb_letters = [len(x) for x in all_words]
    words_len = dict((x,nb_letters.count(x)) for x in set(nb_letters))
    
    return words_len



# Tests

def main():
    
    words_len = longeur_mots()
    
    # Matplotlib
    import matplotlib.pyplot as plt

    plt.figure()
    plt.bar(words_len.keys(), words_len.values(), 1, color='g')
    plt.title("Histogramme de la taille des mots")
    plt.xlabel("Taille mot")
    plt.show()




if __name__ == "__main__":
    main()
    
    
    
    
    
    