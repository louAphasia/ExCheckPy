import sqlite3

conn=sqlite3.connect('SQLTest.db')

cursor=conn.cursor()

try:
    cursor.execute('''
        CREATE TABLE users(
        id INTEGER NOT NULL PRIMARY KEY,
        name TEXT NOT NULL
        )
        ''')
    conn.commit()
except sqlite3.OperationalError:
    None



try:
    cursor.execute('''
        CREATE TABLE cars(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        brand TEXT NOT NULL,
        model TEXT NOT NULL,
        owner INTEGER NOT NULL,
        FOREIGN KEY(owner)REFERENCES user(id)ON DELETE CASCADE 
        )
            ''')
    conn.commit()
except sqlite3.OperationalError:
    None

cursor.execute('INSERT INTO users VALUES(NULL,'
               '"john smith")')

cursor.execute('INSERT INTO cars VALUES(NULL,"Volvo", "xmp", 1)')

cursor.execute('INSERT INTO cars VALUES(NULL,"bmw", "xmp", 1)')

cursor.execute('INSERT INTO cars VALUES(NULL,"yakuza", "xmp", 1)')

rows=list(cursor.execute('SELECT * FROM cars'))
print(len(rows))