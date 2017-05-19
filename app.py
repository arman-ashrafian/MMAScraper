from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from flask_sqlalchemy import SQLAlchemy
import time
import schedule
from threading import Thread


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
db = SQLAlchemy(app)

app.secret_key = 'supersecretkey'


class Fight(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, unique=True)
    event = db.Column(db.String(1000))
    date = db.Column(db.String(50))
    fighterA = db.Column(db.String(100))
    oddA = db.Column(db.Integer)
    fighterB = db.Column(db.String(100))
    oddB = db.Column(db.Integer)
    fightNum = db.Column(db.Integer, unique=True)

    # Constructor
    def __init__(self, event, date, fighterA, oddA, fighterB, oddB, num):
        self.event = event
        self.date = date
        self.fighterA = fighterA
        self.oddA = oddA
        self.fighterB = fighterB
        self.oddB = oddB
        self.fightNum = num

    # print
    def __repr__(self):
        return self.event + " " + self.date
import scraper

@app.route("/")
def index():
    return "<h1>HELLOOOOO</h1>"


def update_database():
    fights = scraper.getFights()

    for fight in fights:
        try:
            db.session.add(fight)
            db.session.commit()
        except:
            print("NOT UNIQUE")

def run_schedule():
    while True:
        schedule.run_pending()


if __name__ == '__main__':
    # schedule.every(10).seconds.do(update_database)
    # t = Thread(target=run_schedule)
    # t.start()
    # print("Starting Server")

    app.run(debug=False, use_reloader=False)
