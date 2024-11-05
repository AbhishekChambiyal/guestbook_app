import sqlite3

# Connect to a database file (or create one if it doesn't exist)
connection = sqlite3.connect("guestbook.db")

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Create a table to store guestbook entries
cursor.execute('''
CREATE TABLE IF NOT EXISTS guestbook (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    message TEXT NOT NULL
)
''')

# Commit changes and close the connection
connection.commit()
connection.close()
