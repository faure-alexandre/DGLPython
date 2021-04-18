# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 09:11:15 2021

@author: Alexandre
"""

import mysql.connector

mdp = input("Entrez votre mot de passe MySql:")

connexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password=mdp,
    database='Runtrack1')

# Insertion des valeurs dans les tables
request1 = "INSERT INTO Auteur (nom, prenom) \
            VALUES (%s, %s)"
request2 = "INSERT INTO Livre (titre, auteur_id) \
            VALUES (%s, %s)"

auteur_val = [('Kafka', 'Franz'), ('Orwell', 'George'), ('Hugo', 'Victor'), 
              ('Zola', 'Emile'), ('Tostoi', 'Leon')]
livre_val = [('Les miserables', '3'), ('Guerre et paix', '5'), ('Le proces', '1'), 
             ('1984', '2'), ('La ferme des animaux', '2'), ('L\'assomoir', '4')]

curseur = connexion.cursor()
curseur.executemany(request1, auteur_val)
curseur.executemany(request2, livre_val)
connexion.commit()


# Affichage des tables
request3 = "SELECT * FROM Auteur"
request4 = "SELECT * FROM Livre"

curseur.execute(request3)

auteurs = curseur.fetchall()

print("\n\n----------------------------------------------------")
print("----------------------Auteurs----------------------------")
for auteur in auteurs:
    print(auteur)



curseur.execute(request4)

livres = curseur.fetchall()

print("\n\n----------------------------------------------------")
print("----------------------Livres----------------------------")
for livre in livres:
    print(livre)

connexion.close()
curseur.close()





