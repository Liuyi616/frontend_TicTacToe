
from pandas import * 
import pandas as pd


# df = pd.read_csv('./data/gameData.csv')



def getWins(player,df):
    counter = 0
    for i in df.loc[:,"Winner"].to_numpy():
        if i == player:
            counter+=1
    return counter

def getlosses(player,df):
    counter = 0
    for i in df.loc[:,"Loser"].to_numpy():
        if i == player:
            counter+=1
    return counter

def getDraws(player,df):
    counter = 0
    for i in df.loc[:,"Tie1"].to_numpy():
        if i == player:
            counter+=1
    for i in df.loc[:,"Tie2"].to_numpy():
        if i == player:
            counter+=1
    return counter

def getPoints(player,df):
    point = getDraws(player,df)+getWins(player,df)*3
    return point


def getStanding(df,player1,player2):
    playersData = {
        'Player':[player1, player2], 
        'Wins' :[getWins(player1,df),getWins(player2,df)],  
        'Losses' :[getlosses(player1,df),getlosses(player2,df)], 
        'Draws':[getDraws(player1,df), getDraws(player2,df)], 
        'Points': [getPoints(player1,df), getPoints(player2,df)] 
    }
    return playersData