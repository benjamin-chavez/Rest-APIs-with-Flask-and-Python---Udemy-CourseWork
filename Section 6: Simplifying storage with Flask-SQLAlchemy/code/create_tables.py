# CREATE TABLES SCRIPT:
import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# To autoincrement user id you must use "INTEGER PRIMARY KEY" instead of just 'int'
# creat_table = "CREATE TABLE IF NOT EXISTS users (id int, username text, password text")
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

# "real" is just a number with a decimal
# create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)"
create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(create_table)

# cursor.execute("INSERT INTO items VALUES ('test', 10.99)")

connection.commit()

connection.close()
