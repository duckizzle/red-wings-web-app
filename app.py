from flask import Flask
import get_game as getgame

app = Flask(__name__)

@app.route('/')
def home():
    oh_baby_a_triple = ''
    data = getgame.get_json("http://site.api.espn.com/apis/site/v2/sports/hockey/nhl/scoreboard")
    events = getgame.get_event_names(data)
    detroit = getgame.is_team_on(events, 'Detroit')

    if detroit == True:
        oh_baby_a_triple = 'YES BITCH WE ON'

    if detroit == False:
        oh_baby_a_triple = 'NAH YO DETROIT AINT ON'


    return oh_baby_a_triple

if __name__ == '__main__':
    app.run(debug=True)