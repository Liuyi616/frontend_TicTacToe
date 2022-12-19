# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.
import os
from logic import *
import numpy as np
from pandas import * 
import pandas as pd
from getStats import *

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    num = 1
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = num
            num += 1
    valid = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    turn = 'X'
    # player,player1,player2 = '','',''
    print('Select game mode:')
    print('1.vs AI')
    print('2.vs Friend')
    mode = input('Please input your choice:')
    while mode not in ['1', '2']:
        mode = input('Wrong selection! Please select again:')
    if mode == '1':
        player = input('Please input your name:')
    if mode == '2':
        player1 = input("Please input the first palyer's name:")
        player2 = input("Please input the second palyer's name:")
    while not winner:
        print("This is %s's turn!" % turn)
        print_board(board)
        pos = input('Please select the chess position:')
        while pos not in valid:
            pos = input('This location is invalid, please select again:')
        valid.remove(pos)
        pos = int(pos)
        row = (pos - 1) // 3
        col = (pos - 1) % 3
        board[row][col] = turn
        winner = get_winner(board)
        if mode == '1' and not winner:
            winner = ai_move(valid, board)
        else:
            turn = other_move(turn)
    print_board(board)
    if winner == 'Tie'and mode == '1':
        winner_name = player+"(Tie)"
        loser_name = "Computer(Tie)"
        player1,player2 = player, "Computer"
        print('It ends in a draw!')
    if winner == 'Tie'and mode == '2':
        winner_name = player1+"(Tie)"
        loser_name = player2+"(Tie)"
        player1,player2 = player1, player2
        print('It ends in a draw!')
    if winner == 'O' and mode == '1':
        winner_name = "Computer"
        loser_name = player  
        player1,player2 = player, "Computer"
        print('Game over! The winner is %s!' % winner_name)
    if winner == 'X' and mode == '1':
        winner_name = player
        loser_name = "Computer"
        player1,player2 = player, "Computer"
        print('Game over! The winner is %s!' % winner_name)
    if winner == 'X' and mode == '2':
        winner_name = player1
        loser_name = player2
        player1,player2 = player1, player2
        print('Game over! The winner is %s!' % winner_name)
    if winner == 'O' and mode == '2':
        winner_name = player2
        loser_name = player1
        player1,player2 = player1, player2
        print('Game over! The winner is %s!' % winner_name)
   

    gameData = {
        'Game Mode': [mode],
        'Winner':[winner_name], 
        'Loser': [loser_name], 
        'Steps of Winner' :[stepsCounter()],  
        'Steps of Loser' :[stepsCounter(board,other_move(winner))] 
    }

    df2 = pd.DataFrame(gameData)
    if os.path.exists("./data/gameData.csv"):  
        df2.to_csv('./data/gameData.csv', mode='a',index=False, header=False)
        df3 = pd.read_csv('./data/gameData.csv')
        playersData = getStanding(df3,player1,player2)
    else:
        df2.to_csv('./data/gameData.csv', mode='a',index=False)
        df3 = pd.read_csv('./data/gameData.csv')
        playersData = getStanding(df3,player1,player2)

    
    df4 = pd.DataFrame(playersData)
    print("\n"+"********** Statistics to the players ********** "+"\n")
    print(df4)

    # Q2: Display any relevant statistics to the players 
    

