# -*- coding: utf-8 -*-


import re

"""
Fonction qui compte le nombre d'apparation de chaque lettre en debut de mot

Parameters
----------
         
Returns
-------
prem_lettre : dict
            dictionnaire contenant en clé chaque lettreet en valeur le nombre 
            d'occurence de cette lettre en debut de mot
        
"""
def first_letter():
    # Ouverture du fichier
    f = open("data.txt", "r")
    data = f.read()
    f.close()

    # On split chaque lettre
    all_letters = re.findall(r'\s[a-zA-Z]|^[a-zA-Z]', data)

    # On transforme les majuscules en minuscules
    all_letters_lower = [each_string.lower().lstrip() for each_string in all_letters]

    # Puis on compte
    prem_lettre = dict((x,all_letters_lower.count(x)) for x in set(all_letters_lower))
    
    return prem_lettre



# Tests 

def main():
    
    prem_lettre = first_letter()
    # Matplotlib

    import matplotlib.pyplot as plt

    plt.figure()
    plt.bar(prem_lettre.keys(), prem_lettre.values(), 1, color='g')
    plt.title("Histogramme d'apparition de chaque lettre en debut de mot")
    plt.xlabel("Lettres en debut de mot")
    plt.show()




if __name__ == "__main__":
    main()
    
    
    