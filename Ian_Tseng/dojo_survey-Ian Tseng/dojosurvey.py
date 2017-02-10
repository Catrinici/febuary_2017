from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/result", methods=["POST"])
def create_user():

    if len(request.form["name"]) > 1 and len(request.form["comment"]) > 1 and len(request.form["comment"]) <= 120:
        # flash("Success, your name is {}".format(request.form["name"]))
        return render_template("result.html", name = request.form["name"],
        location = request.form["location"],language = request.form["language"],comment = request.form["comment"])
    else:
        flash("** Name / Comment cannot be empty **")
        return redirect("/")

app.run(debug=True) # run our server
