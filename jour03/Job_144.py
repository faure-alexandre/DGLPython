# -*- coding: utf-8 -*-


"""
Fonction qui teste si la position d'une nouvelle dame est possible
compte tenu de la position des dames déjà placées

Parameters
----------
N : int
    la taille de notre échiquier

choix : list
        une liste dont les index sont les colonnes des dames déjà placées
        et les valeurs sont les lignes des dames déjà placées

row : int
      la ligne ou l'on veut placer la nouvelle dame
      
col : int
      la colonne ou l'on veut placer la nouvelle dame'

Returns
-------
booléen : True si la position est valide et False sinon
        
"""
def is_possible (N, choix, row, col):
    
    #Gestion des erreurs
    if row < 1 or row > N:
        raise Warning("Problem on row dimensions")
    
    if col < 1 or col > N:
        raise Warning("Problem on col dimensions")
        
    # Si on est sur la premiere colonne alors on peut forcement placer une dame
    if col == 1: 
        return True
    
    else:
        for i in range(len(choix)):
            #On teste horizontalement
            if row == choix[i]:
                return False
            #On teste verticalement
            elif col == i+1:
                return False
            #On teste les diagonales:
            for j in range(N):
                if choix[i]+j == row and i+1+j == col:
                    return False
            for j in range(N):
                if choix[i]-j == row and i+1-j == col:
                    return False
            for j in range(N):
                if choix[i]+j == row and i+1-j == col:
                    return False
            for j in range(N):
                if choix[i]-j == row and i+1+j == col:
                    return False
                
        return True
    
    
"""
# Tests
choix = [2, 4]
print(possible(4, choix, 1, 3))
"""


"""
Fonction qui résout le problème des N dames

Parameters
----------
         
Returns
-------
queens_number : int
                nombre de dames correctement placées
        
"""
def dames(N, choix=[], queens_number=0):
    
    if len(choix) == N:
        return queens_number
    
    for i in range(N):
        if queens_number < N and is_possible(N, choix, row=i+1, col=len(choix)+1 ):
            queens_number += 1
            choix.append(i+1)
            queens_number = dames(N, choix, queens_number)
    
    if queens_number == N:
        return queens_number
    
    choix.pop()
    queens_number -= 1

    return queens_number


"""
Fonction qui affiche dans le terminal la solution

Parameters
----------
         
Returns
-------
        
"""
def print_dames(N, choix):
    
    print("\n\n\n--------------------------------------------------")
    print("    ---------------Affichage-----------------")
    for i in range(N, 0, -1):
        index = choix.index(i) + 1
        row_str = "              |"
        
        for j in range(1,N+1,1):
            if j==index:
                row_str += "X|"
            else:
                row_str += "O|"
        
        print(row_str)
        
    print("--------------------------------------------------")
    
    
    
    
   
# Tests

choix = []
N = 8
dames(N, choix)
print_dames(N, choix)
















