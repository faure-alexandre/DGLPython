# -*- coding: utf-8 -*-

"""
Fonction qui calcule la plus proche permutation
d'un mot suivante par rapport à l'ordre alphabétique

Parameters
----------
word : string
      a word
         
Returns
-------
final_word : string
            the word wich is a permutation of the string "word"
       
"""
def next_word(word):
    
    len_word = len(word)
    
    #Gestion des erreurs
    if len_word < 1 or not isinstance(word, str):
        raise Warning("word argument must be a string sup or equal to 1")
        
    word_split = [char for char in word]
    remainings_letters = []
    remainings_letters.append(word_split[len_word-1])
    del word_split[len_word-1]
    
    for i in range(len_word-2, -1, -1):
        if word_split[i] < remainings_letters[0]:
            remainings_letters.insert(1, word_split[i])
            del word_split[i]
            
            break
            
        else:
            remainings_letters.append(word_split[i])
            remainings_letters.sort()
            del word_split[i]
    
    # Cas ou toutes les lettres du mot sont dans l'ordre décroissant
    if i == 0:
        return "Pas de mot plus éloigné dans l'ordre alphabétique'"
    
    else:
        final_word_split = word_split + remainings_letters
        
        # Reconstruction du mot à partir des lettres splitées
        final_word = ""
    
        for i in range(len_word):
            final_word += final_word_split[i]
            
    return final_word
    

# Tests

word_exemple = "abababjh"
word_exemple_sorted = next_word(word_exemple)
print(word_exemple_sorted)            
        
word_exemple = "edcba"
word_exemple_sorted = next_word(word_exemple)
print(word_exemple_sorted)  
        
