from flask import Flask, session, render_template, redirect

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def general():
    session["score"] = 0
    return render_template('main.html')


@app.route("/scene1")
def scene1():
    return render_template('scene1.html', score=session["score"])


@app.route("/scene1/<score>")
def addScore(score):
    if 'score' not in session:
        return redirect("/")

    session["score"] += int(score)
    return redirect("/end")


@app.route("/end")
def end():
    if 'score' not in session:
        return redirect("/")
        
    return render_template('end.html', score=session["score"])