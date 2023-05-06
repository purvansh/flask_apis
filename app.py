from flask import Flask ,render_template,request,redirect
import json
from flask_mysqldb import MySQL
import MySQLdb.cursors
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'sql12.freemysqlhosting.net'
app.config['MYSQL_USER'] = 'sql12616339'
app.config['MYSQL_PASSWORD'] = '28ZLshkDpQ'
app.config['MYSQL_DB'] = 'sql12616339'

mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('register.html')

@app.route('/data')
def data():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM accounts')
    return render_template('index.html',listdata =cursor.fetchall  ())    


@app.route('/dataadd',methods=['POST','GET'])
def data_for_name():
    if request.method == 'POST':
        print(request)
        print(request.form)
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        email = request.form['email']
        password = request.form['password']
        cursor.execute("insert into accounts(email,password) values('"+email+"','"+password+"') ")
        mysql.connection.commit()
        return redirect('/data')
        
@app.route('/updatedata',methods=['POST','GET'])
def updatedata():
    return render_template('updatepassword.html')

if __name__ =="__main__":
    app.run(debug=True,host="0.0.0.0",port = 80)