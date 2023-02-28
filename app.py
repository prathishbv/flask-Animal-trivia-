from flask import Flask, render_template, abort
from models import db
app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("home.html", message="Message from flask file")

@app.route("/questions/<int:index>")
def questions_view(index):
    try:
        questions_db = db[index]
        return render_template("quiz.html", question=questions_db)
    except:
        abort(404)
    
if __name__ == "__main__":
    app.run(debug=True)