from flask import Flask, session, render_template

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def general():
    session["score"] = 0
    return render_template('main.html')


@app.route("/scene1")
def scene1():
    if 'score' not in session:
        session["score"] = 0

    session["score"] += 5

    return render_template('scene1.html', score=session["score"])


@app.route("/scene1/<score>")
def addScore(score):
    if 'score' not in session:
        session["score"] = 0

    session["score"] += int(score)

    return render_template('scene1.html', score=session["score"])


@app.route("/end")
def end():
    return render_template('end.html', score=session["score"])