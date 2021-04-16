# -*- coding: utf-8 -*-


numbers = []

#Creation des inputs
print("Veuillez entrer 5 nombres entiers:")
numbers.append(int(input("Nombre entier 1: ")))
numbers.append(int(input("Nombre entier 2: ")))
numbers.append(int(input("Nombre entier 3: ")))
numbers.append(int(input("Nombre entier 4: ")))
numbers.append(int(input("Nombre entier 5: ")))

#Tri par ordre croissant
numbers.sort(reverse=False)

#Affichage
print("\nListe triée:", numbers)



