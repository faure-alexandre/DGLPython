# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:48:23 2021

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

mycursor.execute("SELECT count(*), promotion_fk FROM student GROUP BY promotion_fk")

myresult = mycursor.fetchall()

for x in myresult:
  print("promotion", x[1], ":", x[0])
  
  
mydb.close()
mycursor.close()