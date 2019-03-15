from datetime import date
import api.dates
import api.top
import api.number
from flask import Flask, jsonify

app = Flask(__name__)

def today_iso():
    return date.today().strftime('%Y%m%d')

@app.route('/dates/<action>/<project>')
@app.route('/dates/<action>/<project>/<startdate>')
@app.route('/dates/<action>/<project>/<startdate>/<enddate>')
def dates_router(action, project, startdate=today_iso(), enddate=today_iso()):
    return jsonify(getattr(api.dates, action)(project, startdate, enddate))

@app.route('/number/<action>/<project>')
def number_router(action, project):
    return jsonify(getattr(api.number, action)(project))

@app.route('/top/<action>/<project>')
@app.route('/top/<action>/<project>/<limit>')
@app.route('/top/<action>/<project>/<limit>/<offset>')
def top_router(action, project, limit=10, offset=0):
    return jsonify(getattr(api.top, action)(project, limit, offset))

@app.route('/endpoints')
def endpoints():
    return jsonify({
        'dates': [
            {
                'code': 'number_of_articles',
                'name': 'Počet článků'
            }
        ],
        'top': [
            {
                'code': 'top_articles',
                'name': 'Nejlepší články'
            }
        ],
        'number': [
            {
                'code': 'stub_articles',
                'name': 'Počet pahýlových článků'
            }
        ]
    })

if __name__ == "__main__":
    app.run(debug=True)