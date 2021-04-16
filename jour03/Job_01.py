# -*- coding: utf-8 -*-

#Demande a l'utilisateur de saisir une chaine de caracteres et l'enregistre
f = open("output.txt", "w")

text = input("Veuillez saisir un texte:\n")
f.write(text)
f.close()

#Lis le fichier output.txt
f = open("output.txt", "r")
print(f.read())
f.close()