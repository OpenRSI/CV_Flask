from flask import Flask, render_template_string, render_template, jsonify
from flask import Flask, render_template, request, redirect
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("cv.html")

@app.route('/read')
def read():
    return render_template("read_data.html")

@app.route('/messages')
def messages():
    return render_template("messages.html")

@app.route('/ajouter_client/', methods=['GET', 'POST'])
def ajouter_client():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        email = request.form['email']
        message = request.form['message']
        

        # Insérer les données dans la base de données (ici, je suppose que tu as une table 'clients')
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        if conn is not None:
            cursor.execute('INSERT INTO clients (nom, prenom, adresse) VALUES (?, ?, ?)', (nom, prenom, adresse))
            conn.commit()
            conn.close()
        else:
            return 'Erreur de connexion à la base de données'

        # Rediriger vers la page de consultation des clients après l'ajout
        return redirect(url_for('/'))

    # Si la méthode est GET, simplement rendre le template du formulaire
    return render_template('messages.html')

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # Clé secrète pour les sessions (à cacher par la suite)

# Fonction pour créer une entrée "authentifie" dans la session de l'utilisateur
def est_authentifie():
    return session.get('authentifie')


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
