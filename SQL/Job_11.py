# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 13:41:04 2021

@author: Alexandre
"""

import mysql.connector


mdp = input("Entrez votre mot de passe MySql:")

# Demande a l'utilisateur de choisir un student id
student_id = input("Entrez un id de student:")


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password=mdp,
    database='laplateforme')

mycursor = mydb.cursor()

request = "SELECT student_fk, unit_fk, name FROM unit_viewer \
           INNER JOIN unit ON unit_viewer.unit_fk = unit.id \
           WHERE student_fk = %s"

adr = (student_id, )
mycursor.execute(request, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print("Student_id:", x[0], "|    Unit_id:", x[1], "|     Unit_name:", x[2])
  
 
mydb.close()
mycursor.close()


