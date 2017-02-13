from flask import Flask, render_template, session, request, redirect, flash
app = Flask(__name__)
app.secret_key = 'password'

@app.route('/')
def index():
    return render_template("dojo_Survey_index.html")

@app.route('/process', methods=['POST'])
def process():
    errors = False
    if len(request.form['name']) < 1:
        errors = True
        flash("Name can't be blank")
    if len(request.form['comment']) < 1:
        errors = True
        flash("Comment can't be blank")
    if len(request.form['comment']) > 128:
        errors = True
        flash("Comment shouldn't be longer than 120 characters")
    if errors:
        return redirect('/')

    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/success')

@app.route('/success')
def success():
    return render_template('results.index.html')

@app.route('/return', methods=['POST'])
def return1():
    return redirect('/')


app.run(debug=True)
