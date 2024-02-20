from flask import Flask, render_template_string, render_template, jsonify
from flask import Flask, render_template, request, redirect
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("cv.html")

@app.route('/messages')
def messages():
    return render_template("messages.html")

@app.route("/consultation/")
def ReadBDD():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM messages;')
    data = cursor.fetchall()
    conn.close()
    
    # Rendre le template HTML et transmettre les données
    return render_template('read_data.html', data=data)

if(__name__ == "__main__"):
    app.run()