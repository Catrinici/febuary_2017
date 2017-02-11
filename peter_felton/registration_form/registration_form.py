from flask import Flask, render_template, request, redirect, session, flash
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'


# our index route will handle rendering our form
@app.route('/')
def index():
    if not 'email' in session:
        session['email'] = ""
    if not 'first_name' in session:
        session['first_name'] = ""
    if not 'last_name' in session:
        session['last_name'] = ""
    if not 'password' in session:
        session['password'] = ""
    if not 'confirm_password' in session:
        session['confirm_password'] = ""
    if not 'returner' in session:
        session['returner'] = False
    return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/result', methods=['POST'])
def process():
   # do some validations here.
   session['returner'] = False # Use this so you add multiple flash messages at once.
   if len(request.form['email']) < 1:
       flash("You must type in an email address.")
       session['returner'] = True
   elif not EMAIL_REGEX.match(request.form['email']):
       flash("You must type in a valid email address.")
       session['returner'] = True
   if len(request.form['first_name']) < 1:
       flash("You must type in your first name.")
       session['returner'] = True
   elif not str.isalpha(str(request.form['first_name'])):
       flash("Your name cannot contain numbers or symbols. Sorry, we're biased like that.")
       session['returner'] = True
   if len(request.form['last_name']) < 1:
       flash("You must type in your last name.")
       session['returner'] = True
   elif not str.isalpha(str(request.form['last_name'])): # Done twice in rare case of last name not written but first name written correctly.
       flash("Your name cannot contain numbers or symbols. Sorry, we're biased like that.")
       session['returner'] = True
   if len(request.form['password']) < 1:
       flash("You have to have a password.")
       session['returner'] = True
   elif len(request.form['password']) < 8:
       flash("Your password must be greater than 8 characters.")
       session['returner'] = True
   elif request.form['password_confirmation'] != request.form['password']:
       flash("Your password and password confirmation must match.")
       session['returner'] = True

   # Set session variables.
   session['email'] = request.form['email']
   session['first_name'] = request.form['first_name']
   session['last_name'] = request.form['last_name']
   session['password'] = request.form['password']
   session['password_confirmation'] = request.form['password_confirmation']

   # redirect if you passed validation!
   if session['returner'] == False:
       flash("Thanks for submitting your information.")
       return redirect('/')

   # If you got this far, you didn't pass validation. Aw.
   return redirect('/')



if __name__ == "__main__":
    app.run(debug=True) # run our server
