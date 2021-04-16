# -*- coding: utf-8 -*-

"""
Fonction qui trace un triangle

Parameters
----------
height : int
         height of the triangle
         
Returns
-------
draw the triangle in the prompt
       
"""
def draw_triangle(height):
    
    #Gestion des erreurs
    if height < 1 or not isinstance(height, int):
        raise Warning("height must be sup or equal to 1 and int type")
        
        
    #Creation de la base
    base_str = "_"
    
    for i in range(2*height - 3):
        base_str += "_"
        
    for i in range(height-1):
        space_str = ""
        left_space_str = ""
        
        for j in range(i):
            space_str +=  "  "
        for j in range(height-i-1):
            left_space_str += " "
            
        print(left_space_str, "/", space_str, "\ ", sep="")
    
    print("/", base_str, "\ ", sep="")
    
    return
              

# Tests
draw_triangle(5)

draw_triangle(10)

draw_triangle(1)

