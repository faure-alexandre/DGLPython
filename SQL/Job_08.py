# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:44:30 2021

@author: Alexandre
"""

import mysql.connector

mdp = input("Entrez votre mot de passe MySql:")

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password=mdp,
    database='laplateforme')

mycursor = mydb.cursor()

mycursor.execute("SELECT DISTINCT name FROM unit \
                 WHERE name LIKE '%Pool%'")

myresult = mycursor.fetchall()

for x in myresult:
  print(x[0])
  
  
mydb.close()
mycursor.close()