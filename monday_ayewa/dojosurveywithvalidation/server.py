from flask import Flask, render_template, request ,redirect, flash # Import Flask and  more to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.                         
                         
@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
                         # function to the '/' route. This means that whenever we send a request to
                         # localhost:5000/ we will run the following "hello_world" function.
def index():
  return render_template('index.html')  # Return main page.

survey_form = {}
@app.route('/result', methods=['POST'])
def process_survey():
    errors = False 
    
    survey_form['user_name'] = request.form['user_name']
    survey_form['dojo_location'] = request.form['dojo_location']
    survey_form['fav_lang'] = request.form['fav_lang']
    survey_form['comment'] = request.form['comment']
    
    if len(survey_form['user_name']) < 1:
        errors = True
        flash("User name can't be blank")
    if len(survey_form['comment']) < 1:
        errors = True
        flash("Comment can't be blank")
    if len(survey_form['comment']) < 120:
        errors = True
        flash("Comment should be longer than 120 charaters")
    if errors :
       print "found error"
       return redirect('/')
       
    return redirect("/show")  
                            
@app.route('/show')
def show_result():
    print request.form 
    return render_template("result.html", user_name=survey_form['user_name'],
                            location=survey_form['dojo_location'],
                            lang=survey_form['fav_lang'],
                            comment=survey_form['comment'])   

app.secret_key = "password"
app.run(debug=True)      # Run the app in debug mode.