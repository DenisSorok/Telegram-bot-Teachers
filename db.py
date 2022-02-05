import sqlite3


__connection = None


def get_connection():
    global __connection
    if __connection is None:
        __connection = sqlite3.connect('kid.db', check_same_thread=False)
    return __connection

def init_db(force: bool = False):
    conn = get_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS user_message 
    (name, how, lastname, day, list, here, ploho, covid, contact, another)''')
    conn.commit()
def add_message(name: str, how: int, lastname: str, day: str, list: int, here: int, ploho: int, covid: int, contact: int, another: int):
    conn = get_connection()
    c = conn.cursor()
    c.execute('INSERT INTO user_message (day, name, list, here, how, ploho, covid, contact, another, lastname) VALUES (?,?,?,?,?,?,?,?,?,?)', (day, name, list, here, how, ploho, covid, contact, another, lastname))
    conn.commit()
if __name__ == '___name___':
    init_db()
conn = get_connection()
c = conn.cursor()
c.execute("SELECT * FROM user_message")
rows = c.fetchall()
for row in rows:
    print(row)
def vivod():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM user_message")
    rows = c.fetchall()
    for row in rows:
        print(row)
