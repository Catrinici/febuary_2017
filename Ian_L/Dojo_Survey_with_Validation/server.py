from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "key"

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def results():
    invalid = False
    if len(request.form["name"]) == 0:
        flash("Name can't be empty!")
        invalid = True
    if len(request.form["comment"]) == 0:
        flash("Comment can't be empty!")
        invalid = True
    if len(request.form["comment"]) > 120:
        flash("Comment must be under 120 characters!")
        invalid = True
    if invalid:
        return redirect('/')
    else:
        return render_template("results.html", name = request.form["name"], location = request.form["location"], language = request.form["language"], comment = request.form["comment"])

app.run(debug=True)
