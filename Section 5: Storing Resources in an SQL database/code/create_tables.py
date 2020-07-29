# CREATE TABLES SCRIPT:
import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# To autoincrement user id you must use "INTEGER PRIMARY KEY" instead of just 'int'
# creat_table = "CREATE TABLE IF NOT EXISTS users (id int, username text, password text")
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

connection.commit()

connection.close()
