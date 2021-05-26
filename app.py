from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/home1')
def home1():
    return render_template("home1.html")


@app.route('/calculate')
def calculate():
    return render_template("calculate.html")


@app.route('/pic1')
def pic1():
    return render_template("pic1.html")


@app.route('/pic2')
def pic2():
    return render_template("pic2.html")


@app.route('/page')
def page():
    return render_template("page.html")


if __name__ == "__main__":
    app.run(debug=True)