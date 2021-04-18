# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:11:58 2021

@author: Alexandre
"""

import mysql.connector

# Inputs
mdp = input("Entrez votre mot de passe MySql:")
auteur = input("Veuillez donner un nom d'auteur:")


connexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password=mdp,
    database='Runtrack1')

curseur = connexion.cursor()

# Recuperation de l'auteur_id
request1 = "SELECT id FROM Auteur \
            WHERE nom = %s"
            
adr = (auteur, )
curseur.execute(request1, adr)

myresult = curseur.fetchall()

auteur_id = myresult[0][0]


# Recuperation des livres
request = "SELECT titre FROM Livre \
           WHERE auteur_id = %s"
           
adr = (auteur_id, )
curseur.execute(request, adr)

myresult = curseur.fetchall()

for x in myresult:
  print(x[0])
  
connexion.close()
curseur.close()



