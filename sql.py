from flask import Flask, request, render_template, redirect
import sqlite3
import datetime

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    password TEXT
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT,
                    password TEXT,
                    user_agent TEXT,
                    ip TEXT,
                    result TEXT,
                    time TEXT
                )''')
    c.execute("SELECT * FROM users WHERE username='admin'")
    if not c.fetchone():
        c.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']
        ip = request.remote_addr
        user_agent = request.headers.get('User-Agent')
        time = str(datetime.datetime.now())

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        # ❗❗❗ SQL Injection zaif joy
        query = f"SELECT * FROM users WHERE username = '{uname}' AND password = '{pwd}'"
        print("Query:", query)
        try:
            c.execute(query)
            result = c.fetchone()
        except Exception as e:
            result = None

        # Log yozish
        login_result = 'Success' if result else 'Failed'
        c.execute("INSERT INTO logs (username, password, user_agent, ip, result, time) VALUES (?, ?, ?, ?, ?, ?)",
                  (uname, pwd, user_agent, ip, login_result, time))
        conn.commit()
        conn.close()

        if result:
            return render_template('admin.html', user=uname)
        else:
            return "<h3>Login failed</h3>"

    return render_template('login.html')

@app.route('/logs')
def show_logs():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT username, password, user_agent, ip, result, time FROM logs ORDER BY id DESC")
    data = c.fetchall()
    conn.close()
    return render_template('logs.html', logs=data)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)

