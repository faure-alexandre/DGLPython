# -*- coding: utf-8 -*-

"""
Classe qui represente une personne

Attributes
----------
nom : str
      the name of the person
         
prenom : str
        the first name of the person
       
"""
class Personne:
    
    def __init__(self, nom, prenom):
        self.__nom = nom
        self.__prenom = prenom
        
    @property
    def nom(self):
        return self.__nom
    
    @property
    def prenom(self):
        return self.__prenom
    
    @nom.setter
    def nom(self, val):
        self.__nom = val
        
    @prenom.setter
    def prenom(self, val):
        self.__prenom = val
    

    def se_presenter(self):
        print("Je m'appelle", self.nom, self.prenom)
        
        
# Tests

def main():
    personne1 = Personne("Carlsen", "Magnus")
    personne2 = Personne("Stallman", "Richard")
    
    personne1.se_presenter()
    personne2.se_presenter()
    
if __name__ == "__main__":
    main()
    
    
    
    