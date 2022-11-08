# -------------------------------------------------------
# Program by Mikhail Katsar (ankiav)
#
# Version       Date            Info
# 0.0.1         07/11/2022      First flask app
# -------------------------------------------------------


from flask import Flask
from flask import render_template, url_for


app = Flask(__name__)


# start and homepage
@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


# TODO How to connect html and python?
# @app.route('/calculator')
# def square():
#     return f"calc field = {str(input().replace(' ', '').replace(',', '.').Calculator.calculate())}"


# /about page from old html5 project
@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.debug = True
    app.env = "ankiav working hard!"
    app.run()
