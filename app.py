from flask import Flask, render_template, request, redirect, url_for, jsonify, session
from flask_sqlalchemy import SQLAlchemy
import scrape
import time
import schedule
from threading import Thread


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
db = SQLAlchemy(app)

app.secret_key = 'supersecretkey'


class Thing(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, unique=True)
    data = db.Column(db.String(1000), unique=True)

    # Constructor
    def __init__(self, data):
        self.data = data

    # print
    def __repr__(self):
        return self.data

@app.route("/")
def index():
    return "<h1>HELLOOOOO</h1>"


def update_database():
    eventTup = scrape.scrape()
    print('\n\n' + eventTup[1]+ '\n\n')
    event = Thing(eventTup[0])
    try:
        db.session.add(event)
        db.session.commit()
    except:
        print("NOT UNIQUE")

def run_schedule():
    while True:
        schedule.run_pending()


if __name__ == '__main__':
    schedule.every(10).seconds.do(update_database)
    t = Thread(target=run_schedule)
    t.start()
    print("Starting")
    app.run(debug=False, use_reloader=False)
