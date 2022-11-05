"""
"""


from flask import Flask
from flask import render_template

application = Flask(__name__)


@application.route('/')
def index():
    return 'aloxa and timoxa'


@application.route('/square/<int:x>')
def kvadrat(x):
    return f'Result {str(x)}^2 = {str(x*x)}'


@application.route('/about')
def about():
    return render_template('index.html')


if __name__ == "__main__":
    application.debug = True
    application.env = "ankiav troodeetsa"
    application.run()
