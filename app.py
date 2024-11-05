from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Route to display guestbook entries
@app.route('/')
def index():
    conn = sqlite3.connect("guestbook.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM guestbook")
    entries = cursor.fetchall()
    conn.close()
    return render_template('index.html', entries=entries)

# Route to add a new entry
@app.route('/add', methods=['POST'])
def add_entry():
    name = request.form['name']
    message = request.form['message']
    conn = sqlite3.connect("guestbook.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO guestbook (name, message) VALUES (?, ?)", (name, message))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
