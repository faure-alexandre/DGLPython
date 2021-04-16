# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 09:21:47 2021

@author: sanyd
"""

def add(num1, num2):
    return num1 + num2

def substract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print("Choose an operator")
print("1. add \n2. sub \n3. mul \n4. div")

select = int(input("select operator: "))
number1 = int(input("select number 1: "))
number2 = int(input("select number 2: "))

if select == 1:
    print(number1, "+", number2, "=", add(number1, number2))

elif select == 2:
    print(number1, "-", number2, "=", substract(number1, number2))

elif select == 3:
    print(number1, "*", number2, "=", multiply(number1, number2))

elif select == 4:
    print(number1, "/", number2, "=", divide(number1, number2))

else:
    print("Invalid input")





