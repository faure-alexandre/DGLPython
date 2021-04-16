# -*- coding: utf-8 -*-

from Job_01 import Personne


"""
Classe qui represente un livre

Attributes
----------
titre : str
      the title of the book
       
"""
class Livre:
    
    def __init__(self, titre):
        self.titre = titre
        self.auteur = Auteur 
        
    def print_livre(self):
        print(self.titre)

        
"""
Classe qui represente un auteur

Attributes
----------
nom : str
      the name of the person
         
prenom : str
        the first name of the person
        
oeuvre : Livre[]
        the book collection of the autor
       
"""  
class Auteur(Personne):
    
    def __init__(self, nom, prenom):
        Personne.__init__(self, nom, prenom)
        self.oeuvre = []
        
    def listerOeuvre(self):
        print("Liste des oeuvres de l'auteur", self.nom, ":")
        for livre in self.oeuvre:
            livre.print_livre()
        
    def ecrireUnLivre(self, titre):
        livre = Livre(titre)
        self.oeuvre.append(livre)
   
    
# Tests

def main():
    auteur1 = Auteur("Camus", "Albert")
    auteur1.se_presenter()
    auteur1.ecrireUnLivre("L'etranger")
    auteur1.ecrireUnLivre("La peste")
    auteur1.listerOeuvre()

if __name__ == "__main__":
    main()
        
        
        
        
        
        
        
        
        
        
        

