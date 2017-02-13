import random
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key='ThisSecretKey'
@app.route('/')
def new():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities']=[]
    # if 'activities' not in session:
    #     session['activities'] =[]

    return render_template('index.html')
@app.route('/erase')
def Erase():
    session['gold'] = 0
    session['activities'] = []
    return redirect('/')
@app.route('/process',methods=['Post'])
def FunctionProcess():
    # NinjaGold = request.form['ninjacount']
    buildings={
        'farm':random.randint(5,10),
        'casino':random.randint(-50,50),
        'cave':random.randint(0,30),
        'house':random.randint(0,5)
    }
    if request.form['building'] in buildings:
        print request.form['building']
        result =  int(buildings[request.form['building']])

        session['gold'] += result
        result_dictionary ="you went to the {} and walked away with {}".format(request.form['building'],result)
        session['activities'].append(result_dictionary)
    #     result = int(buildings[request.form['building']])
    #     session['gold'] = session['gold'] + result
    return redirect('/')
app.run(debug=True)
