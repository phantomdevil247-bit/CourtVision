from flask import Flask, render_template
import api_handler

app = Flask(__name__)

@app.route('/')
def index():
    players = api_handler.get_players()
    return render_template('index.html', players=players)

@app.route('/standings')
def standings():
    standings = api_handler.get_standings()
    return render_template('index.html', standings=standings)

if __name__ == '__main__':
    app.run(debug=True)
    

