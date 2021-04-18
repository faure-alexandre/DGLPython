# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 19:14:56 2021

@author: Alexandre
"""

import mysql.connector

mdp = input("Entrez votre mot de passe MySql:")

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password=mdp,
)

mycursor = mydb.cursor()

request = "DROP DATABASE IF EXISTS `Runtrack1`;       \
CREATE DATABASE `Runtrack1`;                          \
USE `Runtrack1`;                                      \
CREATE TABLE `Auteur` (                               \
	`id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,     \
	`nom` varchar(100) NOT NULL,                      \
	`prenom` varchar(100) NOT NULL                    \
	);                                                \
	CREATE TABLE `Livre` (                            \
	`id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,     \
	`titre` varchar(100),                             \
	`auteur_id` int NOT NULL                          \
	);"



mycursor.execute(request)

mydb.close()
mycursor.close()


