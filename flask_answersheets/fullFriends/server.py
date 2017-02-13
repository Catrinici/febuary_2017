from flask import Flask, render_template, redirect, request

from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'fullFriends')

# ----------------------------- Show all friends ------------------------------
@app.route('/')
def index():
    all_friends = mysql.query_db('SELECT id, first_name, last_name, email, DATE_FORMAT( created_at, "%b %d, %Y @ %h:%i") as created_at FROM friends')
    return render_template('index.html', friends = all_friends)

# --------------------------- Create a new friend -----------------------------
@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
    values = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    mysql.query_db(query, values)
    return redirect('/')

# --------------------------- Show friend edit page ----------------------------
@app.route('/friends/<id>/edit')
def edit(id):
    friend = mysql.query_db('SELECT * FROM friends WHERE id = {}'.format(id))
    return render_template('show.html', friend = friend)

# ------------------------------ Update a friend -------------------------------
@app.route('/friends/<id>', methods=['POST'])
def update(id):
    query = 'UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email, updated_at = NOW() WHERE id = :id'
    values = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'id': id,
    }
    mysql.query_db(query, values)
    return redirect('/')

# ------------------------------ Delete a friend -------------------------------
@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    query = 'DELETE FROM friends where id = :id'
    values = {
        'id':id,
    }
    mysql.query_db(query, values)
    return redirect('/')

app.run(debug=True)
