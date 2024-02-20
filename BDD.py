import sqlite3

# Connectez-vous à la base de données SQLite (ou créez-la si elle n'existe pas)
conn = sqlite3.connect('messages.db')

# Créez un curseur
c = conn.cursor()

# Créez une table
c.execute('''
    CREATE TABLE messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        message TEXT NOT NULL
    )
''')

# Fermez la connexion
conn.close()
