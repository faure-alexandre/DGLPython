# -*- coding: utf-8 -*-

from Job_02 import Personne, Auteur


"""
Classe qui represente une bibliotheque

Attributes
----------
nom : str
      the name of the library
         
catalogue : dict{Livre:int}
            the catalogue of the library: keys are the books and values are the quantity
            of each book available
       
"""
class Bibliotheque:
    
    def __init__(self, nom):
        self.nom = nom
        self.catalogue = {}
        
    def acheterLivre(self, auteur, titre, quantite):
        
        #Test pour voir si le livre appartient a la collection de l'auteur
        for livre in auteur.oeuvre:
            if livre.titre == titre:
                
                #On regarde si le livre est deja disponible dans le catalogue
                if livre in self.catalogue.keys():
                    self.catalogue[livre] += quantite
                else:
                    self.catalogue[livre] = quantite
                
    def inventaire(self):
        print("-------------------------------------------")
        print("Titre des livres du catalogue de la bibliothéque", self.nom, ":")
        for livre, quantite in self.catalogue.items():
            print(livre.titre, ":", quantite)
            
        print("-------------------------------------------")
            
    def louer(self, client, titre):
        for livre, quantite in self.catalogue.items():
            if livre.titre == titre and quantite > 0:
                client.collection.append(livre)
                self.catalogue[livre] -= 1
                
    def rendreLivres(self, client):
        for livre in client.collection:
            self.catalogue[livre] += 1
            
        del client.collection[:]
                

"""
Classe qui represente un client

Attributes
----------
nom : str
      the name of the person
         
prenom : str
        the first name of the person
        
collection : Livre[]
            All the book borrowed by the client
       
"""
class Client(Personne):
    
    def __init__(self, nom, prenom):
        Personne.__init__(self, nom, prenom)
        self.collection = []
        
    def inventaire(self):
        print("----------------", self.nom, "-------------------")
        for livre in self.collection:
            print(livre.titre)
            
        print("---------------------------------------------")
        
    

# Tests

#Creation des Auteurs et des livres
auteur1 = Auteur("Camus", "Albert")
auteur1.ecrireUnLivre("L'etranger")
auteur1.ecrireUnLivre("La peste")

auteur2 = Auteur("Hugo", "Victor")
auteur2.ecrireUnLivre("Les miserables")
auteur2.ecrireUnLivre("L'assomoir")

auteur3 = Auteur("Orwell", "George")
auteur3.ecrireUnLivre("1984")
auteur3.ecrireUnLivre("La ferme des animaux")

auteur4 = Auteur("Dostoievski", "Fiodor")
auteur4.ecrireUnLivre("Crime et chatiment")
auteur4.ecrireUnLivre("Les demons")

#Creation des bibliotheques
bibliotheque_marseille = Bibliotheque("Marseille")
bibliotheque_marseille.acheterLivre(auteur1, "La peste", 1)
bibliotheque_marseille.acheterLivre(auteur3, "1984", 3)
bibliotheque_marseille.acheterLivre(auteur3, "1984", 1)

bibliotheque_paris = Bibliotheque("Paris")
bibliotheque_paris.acheterLivre(auteur1, "La peste", 2)
bibliotheque_paris.acheterLivre(auteur2, "Les miserables", 3)
bibliotheque_paris.acheterLivre(auteur4, "Crime et chatiment", 1)
bibliotheque_paris.acheterLivre(auteur2, "L'assomoir", 2)

bibliotheque_marseille.inventaire()
bibliotheque_paris.inventaire()

#Creation des clients
client1 = Client("Carlsen", "Magnus")
client2 = Client("Stallman", "Richard")


#Locations
bibliotheque_marseille.louer(client1, "La peste")
bibliotheque_paris.louer(client2, "La peste")
bibliotheque_paris.louer(client2, "Les miserables")

bibliotheque_marseille.inventaire()
bibliotheque_paris.inventaire()

client1.inventaire()
client2.inventaire()

#Rendus des livres
bibliotheque_marseille.rendreLivres(client1)
bibliotheque_marseille.inventaire()
client1.inventaire()

bibliotheque_paris.rendreLivres(client2)
bibliotheque_paris.inventaire()
client2.inventaire()


