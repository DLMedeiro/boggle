from flask import Flask, render_template, session, request, redirect, flash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'BoggleFun'

# 1. Import boggle.py file
from boggle import Boggle

#2.  Set boggle class to variable
boggle_game = Boggle()
game_responses = []
# Generate boggle board on home page
@app.route('/')
def home():
    board = boggle_game.make_board()
    session['board'] = board
    session['score'] = 0
    return render_template('index.html', board = session['board'], game_responses = game_responses, score = session['score'])


@app.route('/game_play', methods = ['POST'])
def test_route():
    board = session['board']
    guess = request.form['guess']
    response = boggle_game.check_valid_word(board, guess)

    
    if (response == 'ok'):
        game_responses.append(guess)
        session['score'] += len(guess)
        return render_template ('index.html',board = board,game_responses = game_responses, score = session['score'])
    else:
        flash(response)
        return render_template ('index.html',board = board,game_responses = game_responses, score = session['score'])


# Issues:
    # reload page with generate a copy of the last entered value -> using redirect will reset the board each time / and score
    # submitting an empty form generates an error
    # Page doesn't always reset the responses [], or will reset after another word is logged on a new board