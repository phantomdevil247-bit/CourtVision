from flask import Flask, render_template, request 
import api_handler

app = Flask(__name__)

@app.route('/')
def index():
    search = request.args.get('search', '')
    if search:
        players = api_handler.search_players(search)
    else:
         players = api_handler.get_players()
    return render_template('index.html', players=players, search=search)

@app.route('/standings')
def standings():
    standings = api_handler.get_standings()
    return render_template('index.html', standings=standings)

@app.route('/player/<int:player_id>')
def player_stats(player_id):
    games = api_handler.get_player_games(player_id)
    return render_template('player.html', games=games)

if __name__ == '__main__':
    app.run(debug=True)
    

