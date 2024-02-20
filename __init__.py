from cv import Flask, render_template, jsonify
import json
import sqlite3

app = Flask(__name__) #creating flask app name

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/resume_1')
def resume_1():
    return render_template("resume_1.html")

@app.route('/cv')
def resume_2():
    return render_template("cv.html")

@app.route('/resume_template')
def resume_template():
    return render_template("resume_template.html")

# Création d'une nouvelle route pour la lecture de la BDD
@app.route('/lecture/')
def ReadBDD():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM messages').fetchall()
    conn.close()

    # Convertit la liste de livre en un format JSON
    json_posts = [{'id': post['id'], 'email': post['email'], 'message': post['message']} for post in posts]

    # Renvoie la réponse JSON
    return jsonify(posts=json_posts)

if(__name__ == "__main__"):
    app.run()
