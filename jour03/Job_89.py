# -*- coding: utf-8 -*-

"""
Fonction factorielle

Parameters
----------
n : int
    la factorielle à calculer
      
Returns
-------
n!
        
"""
def factorielle(n):
    if n == 0:
        return 1
    else:
        return n*factorielle(n-1)
    
# Tests

print("6! =", factorielle(6))
print("3! =", factorielle(3))

