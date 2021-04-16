# -*- coding: utf-8 -*-

"""
Fonction qui arrondie les notes de plus de 40
si l'écart avec le multiple de 5 supérieur est
inférieur ou égal à 2

Parameters
----------
grades_list : list
              list containing all the grades
         
Returns
-------
grades_list_approx : list
                     A list containing the grades approximations
       
"""
def Arrondir_notes(grades_list):
    
    list_size = len(grades_list)
    grades_list_approx = grades_list.copy()
    
    for i in range(list_size):
        
        if grades_list[i] >= 40:
        
            reste_div = grades_list[i] % 5
            if reste_div > 2:
                grades_list_approx[i] += 5 - reste_div
        
    return grades_list_approx


# Tests

grades_list = [24, 58, 86, 72, 12, 41, 89, 43]

grades_list_arrondie = Arrondir_notes(grades_list)

print(grades_list)
print(grades_list_arrondie)
        