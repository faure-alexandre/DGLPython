# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 18:16:23 2021

@author: Alexandre
"""

import mysql.connector


mdp = input("Entrez votre mot de passe MySql:")

# Demande a l'utilisateur de choisir un skill id
skill_id = input("Entrez un skill id:")


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password=mdp,
    database='laplateforme')

mycursor = mydb.cursor()

request = "SELECT student_fk, sum(earned) \
            FROM acquiered_skill \
            INNER JOIN job_skill ON acquiered_skill.job_skill_fk = job_skill.id \
            WHERE skill_fk = %s \
            GROUP BY student_fk"

adr = (skill_id, )
mycursor.execute(request, adr)

myresult = mycursor.fetchall()

max_earned = 0
student_id = 0

for x in myresult:
    if max_earned < int(x[1]):
        max_earned = int(x[1])
        student_id = x[0]
        
print("Max_student_id:", student_id, "|  Max_earned_cumul:", max_earned)


mydb.close()
mycursor.close()


