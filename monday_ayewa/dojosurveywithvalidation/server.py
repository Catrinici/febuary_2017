from flask import Flask, render_template, request  # Import Flask and  more to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file
                         # directly, or importing it as a module.
@app.route('/')          # The "@" symbol designates a "decorator" which attaches the following
                         # function to the '/' route. This means that whenever we send a request to
                         # localhost:5000/ we will run the following "hello_world" function.
def index():
  return render_template('index.html')  # Return main page.

@app.route('/result', methods=['POST'])

def survey_result():
    print request.form 
    return render_template("result.html", user_name=request.form['user_name'],
    location=request.form['dojo_location'],
    lang=request.form['fav_lang'],
    comment=request.form['comment'])   


app.run(debug=True)      # Run the app in debug mode.