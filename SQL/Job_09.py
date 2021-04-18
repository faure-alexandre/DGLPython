# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 18:46:31 2021

@author: Alexandre
"""

import mysql.connector


mdp = input("Entrez votre mot de passe MySql:")

# Demande a l'utilisateur de choisir un id de job
job_id = input("Entrez un job id:")


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password=mdp,
    database='laplateforme')

mycursor = mydb.cursor()

request = "SELECT job.id, job.name AS job_name, unit.name AS unit_name \
            FROM job \
            INNER JOIN unit ON job.unit_fk = unit.id \
            WHERE job.id = %s"

adr = (job_id, )
mycursor.execute(request, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print("Job_id:", x[0], "|  Job name:", x[1], "|  Unit name:", x[2])
  

mydb.close()
mycursor.close()




