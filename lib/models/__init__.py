import sqlite3

CONN = sqlite3.connect('chore.db')
CURSOR = CONN.cursor()
