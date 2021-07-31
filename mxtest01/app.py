from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)
app.secret_key = 'your secret key'

#DB information
# Server: sql10.freemysqlhosting.net
# Name: sql10428400
# Username: sql10428400
# Password: LNBGr9NwcH
# Port number: 3306

app.config['MYSQL_HOST'] = 'sql10.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql10428400'
app.config['MYSQL_PASSWORD'] = 'LNBGr9NwcH'
app.config['MYSQL_DB'] = 'sql10428400'
mysql = MySQL(app)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form['usuario']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            return 'Logged in successfully!'
        else:
            msg = 'Incorrect username/password!'
    return render_template('index.html', msg=msg)

        





if __name__ == '__main__':
    app.run(debug=True)