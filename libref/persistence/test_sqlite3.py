
import os
import sqlite3
db_file = 'example.db'



def test_overview():
    os.remove(db_file)
    con = sqlite3.connect(db_file)

    cur = con.cursor()
    cur.execute(''' CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')
    cur.execute(''' INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'RHAT', 100, 35.14) ''')

    con.commit()
    con.close()

def test_query_select():
    con = sqlite3.connect(db_file)
    cur = con.cursor()

    for row in cur.execute(' SELECT * FROM stocks ORDER BY price '):
        print(row)

    con.close()
    assert False




