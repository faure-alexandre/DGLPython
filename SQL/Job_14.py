# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 17:29:44 2021

@author: Alexandre
"""

import mysql.connector


mdp = input("Entrez votre mot de passe MySql:")

# Demande a l'utilisateur de choisir un student id
student_id = input("Entrez un student id:")


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password=mdp,
    database='laplateforme')

mycursor = mydb.cursor()

request = "SELECT skill_fk, sum(earned) \
            FROM acquiered_skill \
            INNER JOIN job_skill ON acquiered_skill.job_skill_fk = job_skill.id \
            WHERE student_fk = %s \
            GROUP BY skill_fk"

adr = (student_id, )
mycursor.execute(request, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print("Skill_id:", x[0], "|  Earned_cumul:", x[1])
  

mydb.close()
mycursor.close()



