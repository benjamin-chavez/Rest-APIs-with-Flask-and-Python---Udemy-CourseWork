import sqlite3

# Initialize DB connection
connection = sqlite3.connect('data.db')

cursor = connection.cursor()

# Defining the schema
create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

# Store some data in your database - Insert 1 user in the DB
user = (1, 'jose', 'go123')
insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user)

# Store some data in your database - Insert multiple users in the DB
users = [
    (2, 'Ben', 'abc'),
    (3, 'Lupe', 'lala'),
    (4, 'Donna', 'nono21')
]
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

# Whenever you insert data you have to tell the connection to save the
# changes into the disk (data.db file)
connection.commit()

connection.close()
