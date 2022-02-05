from flask import Flask, render_template
import sqlite3
conn = sqlite3.connect('kid.db')
c = conn.cursor()
app = Flask(__name__)

@app.route('/')
def posts(methods=['POST', 'GET']):
    conn = sqlite3.connect('kid.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT * FROM user_message")
    return render_template('posts.html', rows = c.fetchall())


if __name__ == '__main__':
    app.run(debug=True)