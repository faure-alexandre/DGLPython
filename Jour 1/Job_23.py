# -*- coding: utf-8 -*-

"""
Fonction qui trace un rectangle

Parameters
----------
width : int
        width of the rectangle
height : int
         height of the rectangle
         
Returns
-------
draw the rectangle in the prompt
        
"""
def draw_rectangle(width, height):
    
    sup_str = ""
    mid_str = ""
    
    #Gestion des erreurs
    if height < 2 or not isinstance(height, int):
        raise Warning("height must be sup or equal to 2")
        
    if width < 1 or not isinstance(width, int):
        raise Warning("width must be sup or equal to 1")
        
    for i in range(width):
        sup_str += "-"
        mid_str += " "
    
    #Affichage du bord supérieur
    print("|", sup_str, "|", sep="")
    
    #Affichage des bords gauche et droits
    for i in range(height-2):
        print("|", mid_str, "|", sep="")
        
    #Affichage du bord inférieur
    print("|", sup_str, "|", sep="")
    
    return
    

# Tests

# Affichage d'un rectange de largeur 10 et hauteur 3
draw_rectangle(10, 3)