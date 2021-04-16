# -*- coding: utf-8 -*-

#Imports
import numpy as np
import pygame as pg
import sys, math
from pygame.locals import *


"""
Fonction qui teste si un joueur a gagné

Parameters
----------
board : np.array((3,3))
        Array representing the board
piece : int
        a player
         
Returns
-------
bolean
True if the player win
"""
def is_winning_move(board, player):
    nb_rows, nb_columns = board.shape
    
	# Check horizontal locations for win
    for r in range(nb_rows):
        if board[r][0] == player and board[r][1] == player and board[r][2] == player:
            return True

	# Check vertical locations for win
    for c in range(nb_columns):
        if board[0][c] == player and board[1][c] == player and board[2][c] == player:
            return True

	# Check negatively sloped diagonal
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

	# Check positively sloped diagonal
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True


"""
Fonction qui crée un plateau de jeu vide

Parameters
----------
         
Returns
-------
board : np.array((3,3))
        the board with all squares initialize to 0
"""
def create_board():
	board = np.zeros((3,3))
	return board


"""
Fonction qui place le coup d'un joueur dans le plateau

Parameters
----------
board : np.array((3,3))
        Array representing the board
row : int
      the row to put the move
col : int
      the column to put the move
player : int
         a player
         
Returns
-------
the board updated with the move
"""
def play_move(board, row, col, player):
	board[row][col] = player
    

"""
Fonction qui teste si un coup est possible

Parameters
----------
board : np.array((3,3))
        Array representing the board
row : int
      the row to put the move
col : int
      the column to put the move
         
Returns
-------
True if the move is valid
"""
def is_valid_move(board, row, col):
	return board[row][col] == 0


"""
Fonction qui teste si une case du plateau est encore vide

Parameters
----------
board : np.array((3,3))
        Array representing the board
         
Returns
-------
True if the board is empty
"""
def is_board_is_full(board):
    nb_rows, nb_columns = board.shape
    
    for c in range(nb_columns):
        for r in range(nb_rows):
            if board[r][c] == 0 :
                return False
    return True


"""
Fonction qui dessine le plateau et les pieces des joueurs

Parameters
----------
board : np.array((3,3))
        Array representing the board
SQUARESIZE : int
             a number representing the size of a square
screen : the screen of the pygame

Returns
-------
draw the board with the moves of each players in a pygame windows
"""
def draw_board(board, SQUARESIZE, screen):
    BLUE = (0,0,255)
    RED = (255,0,0)
    YELLOW = (255,255,0)
    nb_rows, nb_columns = board.shape
    RADIUS = 50

    #Affichage des colonnes de la grille
    for c in range(nb_columns):
        pg.draw.line(screen, BLUE, (c*200,0), (c*200,600), 5)
        
    #Affichage des lignes de la grille
    for r in range(nb_rows):
        pg.draw.line(screen, BLUE, (0,r*200), (600,r*200), 5)

    #Affichage des pieces des joueurs
    for c in range(nb_columns):
        for r in range(nb_rows):		
            if board[r][c] == 1:
                pg.draw.circle(screen, RED, (int(c*200 + 100), int(r*200 + 100) ), RADIUS)
            elif board[r][c] == 2: 
                pg.draw.circle(screen, YELLOW, (int(c*200 + 100), int(r*200 + 100) ), RADIUS)
                
    pg.display.update()




# Initialisation d'une partie
BLUE = (0,0,255)
RED = (255,0,0)
WHITE = (255, 255, 255)
YELLOW = (255,255,0)

board = create_board()
player = 0
turn = 0
game_over = False


# Affichage du plateau vide
pg.init()

size = (600, 600)
screen = pg.display.set_mode(size)
pg.display.set_caption('TicTacToe1337')
police_texte = pg.font.SysFont("monospace", 50)
screen.fill(WHITE)
draw_board(board, 100, screen)

pg.display.update()


# Game loop
while not game_over:
  
    for event in pg.event.get():

        if event.type == pg.locals.QUIT:
            pg.quit()
            sys.exit()

        
        if event.type == pg.MOUSEBUTTONDOWN:
			
            # Si c'est au tour du joueur 1
            if player == 0:
                x, y = event.pos
                col = int(math.floor(x/200))
                row = int(math.floor(y/200))
				

                if is_valid_move(board, row, col):
                    play_move(board, row, col, 1)

                    if is_winning_move(board, 1):
                        game_over = True
                        screen.fill(WHITE)
                        image_texte = police_texte.render("Player 1 wins !!", 1, RED)
                        screen.blit(image_texte, (80,300))
                        pg.display.update()
                        
                        break


			# Si c'est au tour du joueur 2
            else:				
                x, y = event.pos
                col = int(math.floor(x/200))
                row = int(math.floor(y/200))

                if is_valid_move(board, row, col):
                    play_move(board, row, col, 2)

                    if is_winning_move(board, 2):
                        game_over = True
                        screen.fill(WHITE)
                        image_texte = police_texte.render("Player 2 wins !!", 1, YELLOW)
                        screen.blit(image_texte, (80,300))
                        pg.display.update()
                        
                        break
                        
            
            
            # Si le plateau est plein
            if is_board_is_full(board):
                game_over = True
                screen.fill(WHITE)
                image_texte = police_texte.render("Match Nul !!", 1, BLUE)
                screen.blit(image_texte, (120,300))
                pg.display.update()
                        
                break
              
                
            # Mise à jour de l'affichage
            screen.fill(WHITE)
            draw_board(board, 100, screen)
            turn += 1
            player += 1
            player = player % 2
            pg.display.update()


if game_over:
    pg.time.wait(2000)
    pg.display.quit()
    sys.exit()






