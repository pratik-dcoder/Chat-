from flask import Flask, render_template, request, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secure_key_here'  # Change this!

# Database setup for challenges
def init_db():
    conn = sqlite3.connect('ctf.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS challenges (
            id INTEGER PRIMARY KEY,
            title TEXT,
            description TEXT,
            difficulty TEXT,
            solution TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/challenges')
def challenges():
    conn = sqlite3.connect('ctf.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM challenges')
    challenges = cursor.fetchall()
    conn.close()
    return render_template('challenges.html', challenges=challenges)

if __name__ == '__main__':
    init_db()
    app.run(debug=True, ssl_context='adhoc')  # HTTPS for security
