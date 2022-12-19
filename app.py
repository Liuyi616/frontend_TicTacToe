__author__ = 'Zhao'

from flask import Flask, render_template, session, redirect, url_for,request
from lib import logic, getStats
from flask_session import Session
from tempfile import mkdtemp
import pandas as pd
import os





app = Flask(__name__)


app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/')
def index():
    if request.method == 'POST':
        player1 = request.form.get('p1')
        player2 = request.form.get('p2')
        return redirect(url_for('friend_game',player1=player1,player2=player2))
    return render_template('index.html')


@app.route('/friend_game')
def gameboard2():
    player = request.args.get('player', None)
    player1 = request.args.get('p1', None)
    player2 = request.args.get('p2', None)
    if "board" not in session:
        session["board"] = [[None, None, None], [None, None, None], [None, None, None]]
        session["turn"] = "X"
        session["winner"] = None
        session['loser'] = None
        session['tie1'] = None
        session['tie2'] = None
        session['player1'] = player1
        session['player2'] = player2
        session['winnerSteps'] = None
        session['loserSteps'] = None
       
    else:
        board = session["board"]   
        p1 = session['player1'] 
        p2 = session['player2'] 
        session["winner"] = logic.get_winner(board)
        session['winnerSteps'] = logic.stepsCounter(board,session["winner"])
        session['loserSteps'] = logic.stepsCounter(board,logic.other_move(session["winner"]))
        if session["winner"] == 'Tie':
            session['tie1'] = p1
            session['tie2'] = p2
        if session["winner"] == 'X' :
            session["winner"]= p1
            session['loser'] = p2
        if session["winner"] == 'O' :
            session["winner"] = p2
            session['loser'] = p1
        if request.method == 'POST':
            return redirect(url_for('leaderboard'))
    return render_template("play.html", 
                            game=session["board"], turn=session["turn"], 
                            winner=session["winner"], loser = session['loser'], 
                            winnerSteps = session['winnerSteps'], loserSteps = session['loserSteps'],
                            player1=session['player1'],player2=session['player2'])

@app.route("/play/<int:row>/<int:col>")
def play(row, col):
        session["board"][row][col] = session["turn"]
        session["turn"] = logic.other_move(session["turn"])
        return redirect("/friend_game")

@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")

@app.route("/leaderboard")
def leaderboard():
    winner = session.get("winner", None)
    loser = session.get("loser", None)
    tie1 = session.get("tie1", None)
    tie2 = session.get("tie2", None)
    gameData = {
        'Winner':[winner], 
        'Loser': [loser], 
        'Tie1' :[tie1],  
        'Tie2' :[tie2] 
    }
    
    df1 = pd.DataFrame(gameData)
    
    if os.path.exists("data/gameData.csv"):  
        df1.to_csv('data/gameData.csv', mode='a',index=False, header=False)
        df2 = pd.read_csv('./data/gameData.csv')
        playersData = getStats.getStanding(df2,winner,loser)
        
    else:
        df1.to_csv('data/gameData.csv', mode='a',index=False)
        df2 = pd.read_csv('./data/gameData.csv')
        playersData = getStats.getStanding(df2,winner,loser)
        
    df3 = pd.DataFrame(playersData)
    return render_template('stats.html',playersData=df3)






if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000)