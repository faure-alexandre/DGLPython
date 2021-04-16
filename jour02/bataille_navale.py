# -*- coding: utf-8 -*-


"""
Classe qui represente chacun des 2 joueurs

Attributes
----------
nom : str
      the name of the player
         
board: Board
       the game board of each player
       
"""
class Joueur:
    
    def __init__(self, nom):
        self.nom = nom
        self.board = Board()
        

"""
Classe qui represente une case vide par défaut et dont
les autres cases vont hériter (suivant les différents types de bateaux (cf. wikipedia))

Attributes
----------
toucher : bool
          return True if the square has been touched by the opponent
       
"""
class Case:
    
    def __init__(self):
        self.toucher = -1
    
        
    def action(self):
        print("Case vide")
        self.toucher = True
        
    def affichage(self):
        return "VIDE"


class PorteAvion(Case):
    
    def __init__(self):
        Case.__init__(self)
        self.toucher = False
        
    def action(self):
        print("Porte avion touché !")
        self.toucher = True
        
    def affichage(self):
        if self.toucher == True:
            return "(PA)"
        else:
            return " PA "
        
class Croiseur(Case):
    
    def __init__(self):
        Case.__init__(self)
        self.toucher = False
        
    def action(self):
        print("Croiseur touché !")
        self.toucher = True
        
    def affichage(self):
        if self.toucher == True:
            return " (C)"
        else:
            return "  C "
        
class Torpilleur(Case):
    
    def __init__(self):
        Case.__init__(self)
        self.toucher = False
        
    def action(self):
        print("Torpilleur touché !")
        self.toucher = True
        
    def affichage(self):
        if self.toucher == True:
            return " (T)"
        else:
            return "  T "
        
class ContreTorpilleur(Case):
    
    def __init__(self):
        Case.__init__(self)
        self.toucher = False

    def action(self):
        print("Contre Torpilleur touché !")
        self.toucher = True
        
    def affichage(self):
        if self.toucher == True:
            return "(CT)"
        else:
            return " CT "
        
class SousMarin(Case):
    
    def __init__(self):
        Case.__init__(self)
        self.toucher = False
        
    def action(self):
        print("Sous Marin touché !")
        self.toucher = True
        
    def affichage(self):
        if self.toucher == True:
            return "(SM)"
        else:
            return " SM "
        
        
"""
Classe qui represente un plateau de jeu

Attributes
----------
board : list[list[Case]]
        a list of list containing all the square of the board
       
"""   
class Board:
    
    def __init__(self):
        #initialisation du plateau avec des cases vides
        self.board = [0 for i in range(10)]
        for i in range(10):
            self.board[i] = []
            for j in range(10):
                case_vide = Case()
                self.board[i].append(case_vide)
                
    
    """
    Fonction qui demande à chaque joueur dans le terminal
    de placer les coordonnées de ses différents bateaux

    Parameters
    ----------
       
    """
    def genere_board(self):
        
        print("\nPorte-avion (5 cases): ")
        x = int(input("x: "))
        y = int(input("y: "))
        orientation = input("Orientation (h ou v): ")
        
        if orientation == "h":
            for i in range(5):
                case_pa = PorteAvion()
                self.board[x][y+i] = case_pa
        else:
            for j in range(5):
                case_pa = PorteAvion()
                self.board[x+j][y] = case_pa
                
        
        print("\nCroiseur (4 cases): ")
        x = int(input("x: "))
        y = int(input("y: "))
        orientation = input("Orientation (h ou v): ")
        
        if orientation == "h":
            for i in range(4):
                case_cr = Croiseur()
                self.board[x][y+i] = case_cr
        else:
            for j in range(4):
                case_cr = Croiseur()
                self.board[x+j][y] = case_cr
        
        
        print("\nTorpilleur (2 cases): ")
        x = int(input("x: "))
        y = int(input("y: "))
        orientation = input("Orientation (h ou v): ")
        
        if orientation == "h":
            for i in range(2):
                case_tr = Torpilleur()
                self.board[x][y+i] = case_tr
        else:
            for j in range(2):
                case_tr = Torpilleur()
                self.board[x+j][y] = case_tr
        
        
        print("\nContre-torpilleur (3 cases): ")
        x = int(input("x: "))
        y = int(input("y: "))
        orientation = input("Orientation (h ou v): ")
        
        if orientation == "h":
            for i in range(3):
                case_ct = ContreTorpilleur()
                self.board[x][y+i] = case_ct
        else:
            for j in range(3):
                case_ct = ContreTorpilleur()
                self.board[x+j][y] = case_ct
        
        
        print("\nSous-marin (3 cases): ")
        x = int(input("x: "))
        y = int(input("y: "))
        orientation = input("Orientation (h ou v): ")
        
        if orientation == "h":
            for i in range(3):
                case_sm = SousMarin()
                self.board[x][y+i] = case_sm
        else:
            for j in range(3):
                case_sm = SousMarin()
                self.board[x+j][y] = case_sm
        
        
        
    def is_game_over(self):
        for i in range(10):
            for j in range(10):
                if self.board[i][j].toucher == False:
                    return False
                
        return True
        
        
    """
    Fonction qui affiche le plateau sans cacher les bateaux non touchés

    Parameters
    ----------
       
    """
    def print_full_board(self):
        for i in range(10):
            ligne = "|"
            for j in range(10):
                ligne += self.board[i][j].affichage()
                ligne += "|"
            print(ligne)
            
    """
    Fonction qui affiche le plateau en cachant les bateaux non touchés

    Parameters
    ----------
       
    """   
    def print_partial_board(self):
        for i in range(10):
            ligne = "|"
            for j in range(10):
                if self.board[i][j].toucher == True:
                    ligne += self.board[i][j].affichage()
                    ligne += "|"
                else:
                    ligne += "  ? "
                    ligne += "|"
            print(ligne)
      

class Jeu:
    
    def __init__(self, joueur1, joueur2):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        
    
    def _jouer_partie(self):
        
        #Creation des grilles des joueurs
        
        print("---------------------------------------------")
        print("A", self.joueur1.nom, "de placer ses bateaux:")
        print("---------------------------------------------")
        self.joueur1.board.genere_board()
        
        #Affichage du plateau de joueur 1
        print("\nPlateau de", self.joueur1.nom, ":")
        self.joueur1.board.print_full_board()
        
        print("---------------------------------------------")
        print("A", self.joueur2.nom, "de placer ses bateaux:")
        print("---------------------------------------------")
        self.joueur2.board.genere_board()
        
        #Affichage du plateau de joueur 2
        print("\nPlateau de", self.joueur2.nom, ":")
        self.joueur2.board.print_full_board()
        
        
        while True:
            
            #Tour du joueur 1
                
            print("--------------------\n Au joueur {0:s} de jouer".format(self.joueur1.nom))
        
            x = int(input("x: "))
            y = int(input("y: "))
        
            self.joueur2.board.board[x][y].action()
            self.joueur2.board.print_partial_board()
            
            if self.joueur2.board.is_game_over():
                print("Joueur 1 a gagné")
                return 
        
            
            #Tour du joueur 2
                
            print("--------------------\n Au joueur {0:s} de jouer".format(self.joueur2.nom))
        
            x = int(input("x: "))
            y = int(input("y: "))
        
            self.joueur1.board.board[x][y].action()
            self.joueur1.board.print_partial_board()
            
            if self.joueur1.board.is_game_over():
                print("Joueur 2 a gagné")
                return 
        
        
        
# Tests

#Creation des joueurs
joueur1 = Joueur("Bob")
joueur2 = Joueur("Luc")

#On crée puis on lance une partie
jeu = Jeu(joueur1, joueur2)
jeu._jouer_partie()
    
"""
Exemple de placement pour une partie
PA: (0, 2, v)
C: (4, 6, h)
T: (6, 4, v)
CT: (8, 6, h)
SM: (0, 6, v)
"""
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    