from flask import Flask, render_template, abort, jsonify, redirect, request, url_for
from models import db, save_db

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("home.html", questions=db)

@app.route("/questions/<int:index>")
def questions_view(index):
    try:
        questions_db = db[index]
        return render_template('quiz.html',
                               question=questions_db,
                               index=index,
                               max_index=len(db) - 1)
    except:
        abort(404)    

@app.route('/add_new_questions', methods=['GET', 'POST'])
def add_question():
    if request.method == "POST":
        result = {
            "question" : request.form['question'],
            "answer" : request.form['answer']
        }
        db.append(result)
        save_db()
        return redirect(url_for("questions_view", index=len(db) - 1))
    else:
        return render_template('add_new_question.html')

@app.route("/remove_question/<int:index>", methods=['GET', 'POST'])
def remove_question(index):
    try:
        if request.method == "POST":
            del db[index]
            save_db()
            return redirect(url_for("welcome"))
        else:
            return render_template("remove_question.html", question=db[index])
    except IndexError:
        abort(404)
        
@app.route('/api/questions')
def api_questions_list():
    return jsonify(db)

@app.route("/api/questions/<int:index>")
def api_question_list(index):
    try:
        return db[index]
    except:
        abort(404)
if __name__ == "__main__":
    app.run(debug=True)