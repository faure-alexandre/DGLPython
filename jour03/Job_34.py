# -*- coding: utf-8 -*-

from random import choices
from Job_08 import longeur_mots
from Job_13 import first_letter
import json

        
# Recuperation de toutes les statistiques precedemment calculées  

words_len_stats = longeur_mots() 
first_letters_stats = first_letter()
    
with open('job_21.txt', 'r') as file:
    letters_relations_stats = json.load(file)      
        


"""
Fonction qui genere un mot en fonction des différentes
fréquences d'apparition de notre texte

Parameters
----------
words_len : dict
            dictionnaire ayant pour clé la longueur et valeur le nombre de mots
            correspondant à cette longueur (Job_08)

first_letters : dict
                dictionnaire contenant en clé chaque lettreet en valeur le nombre 
                d'occurence de cette lettre en debut de mot (Job_13)
                
d : dict(dict)
    dictionnaire contenant en clé chaque lettre et en valeur un dictionnaire
    ayant pour clé les lettres qui suivent la première clé et en valeur le nombre d'occurences
    (Job_21)
         
Returns
-------
word : str
        un mot généré suivant les stats calculées dans notre texte
        
"""
def genere_mot(words_len, first_letters, d):
    # Calcul de la taille du mot
    taille_mot = choices(list(words_len.keys()), weights=list(words_len.values()), k=1)[0]
    
    #Choix de la premiere lettre
    first_letter = choices(list(first_letters.keys()), weights=list(first_letters.values()), k=1)[0]
    
    #initialisation du mot
    word = first_letter

    for i in range(1, taille_mot):
        letter = choices(list(d[word[i-1]].keys()), weights=list(d[word[i-1]].values()), k=1)[0]
        word += letter

    return word


# Tests
print(genere_mot(words_len_stats, first_letters_stats, letters_relations_stats))
print(genere_mot(words_len_stats, first_letters_stats, letters_relations_stats))
print(genere_mot(words_len_stats, first_letters_stats, letters_relations_stats))
print(genere_mot(words_len_stats, first_letters_stats, letters_relations_stats))
























