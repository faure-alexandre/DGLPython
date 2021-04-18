# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:30:24 2021

@author: Alexandre
"""

import mysql.connector

mdp = input("Entrez votre mot de passe MySql:")

connexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password=mdp)

mycursor = connexion.cursor()

sql = open("laplateforme.sql").read()
mycursor.execute(sql)

connexion.close()
mycursor.close()