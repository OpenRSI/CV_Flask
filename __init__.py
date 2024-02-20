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

@app.route('/consultation/<int:post_id>')
def Readfiche(post_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM messages WHERE id = ?', (post_id,))
    data = cursor.fetchall()
    conn.close()
    
    # Rendre le template HTML et transmettre les données
    return render_template('read_data.html', data=data)

@app.route('/messages/', methods=['GET', 'POST'])
def ajouter_client():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        prenom = request.form['email']
        adresse = request.form['message']

        # Insérer les données dans la base de données (ici, je suppose que tu as une table 'clients')
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        if conn is not None:
            cursor.execute('INSERT INTO messages (email, message) VALUES (?, ?)', (email, message))
            conn.commit()
            conn.close()
        else:
            return 'Erreur de connexion à la base de données'

        # Rediriger vers la page de consultation des clients après l'ajout
        return redirect(url_for('/'))

    # Si la méthode est GET, simplement rendre le template du formulaire
    return render_template('messages.html')


if(__name__ == "__main__"):
    app.run()