from boggle import Boggle
from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"

boggle_game = Boggle()


@app.route('/')
def create_board():
    board = boggle_game.make_board()
    session['my_board'] = board
    session['guess'] = []
    return render_template('home-page.html', board=board)


@app.route('/boggle')
def game_begin():
    print(session.get('guess'))
    board = session.get('my_board')
    return render_template('boggle.html', board=board)


@ app.route('/submit', methods=['post'])
def submit():
    pick = request.form['guess']
    guess_list = session.get('guess')
    guess_list.append(pick)
    session['guess'] = guess_list
    return redirect('/boggle')
