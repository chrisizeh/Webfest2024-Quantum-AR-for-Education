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
    return render_template('scene1.html')


@app.route("/scene1/<score>")
def scene1Score(score):
    if 'score' not in session:
        return redirect("/")

    session["score"] += int(score)
    return redirect("/end")


@app.route("/scene2")
def scene2():
    return render_template('cat.html', score=session["score"])


@app.route("/scene2/<prob>")
def scene2Score(prob):
    if 'score' not in session:
        return redirect("/")

    if(prob < 0.5):
        session["score"] += 10
    else:
        session["score"] -= 3

    return render_template('cat.html', score=session["score"], prob=prob)


@app.route("/end")
def end():
    if 'score' not in session:
        return redirect("/")

    return render_template('end.html', score=session["score"])