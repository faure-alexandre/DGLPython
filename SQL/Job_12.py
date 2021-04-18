# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 16:52:56 2021

@author: Alexandre
"""

import mysql.connector


mdp = input("Entrez votre mot de passe MySql:")

# Demande a l'utilisateur de choisir un group id
group_id = input("Entrez un group id:")


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password=mdp,
    database='laplateforme')

mycursor = mydb.cursor()

request = "SELECT DISTINCT job_fk FROM registration WHERE group_id = %s"
adr = (group_id, )
mycursor.execute(request, adr)

myresult = mycursor.fetchall()

job_id = myresult[0][0]

request = "SELECT job.id , job.name , unit.name FROM job \
           INNER JOIN unit ON unit_fk = unit.id \
           WHERE job.id = %s"
           
adr = (job_id, )
mycursor.execute(request, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print("Group_id:", group_id, "|  Job name:", x[1], "|  Unit_name:", x[2])
  
  
mydb.close()
mycursor.close()
  
  
  