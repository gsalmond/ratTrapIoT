# install FLASK if not installed
# $pip install Flask

# to run
# FLASK_APP=receiver.py flask run

from flask import Flask
app = Flask(__name__)

@app.route("/wait")
def wait():
    return "Trap is set and waiting for rat"

@app.route("/caught")
def caught():
    return "The trap has gone off and has caught a rat"

@app.route("/missed")
def missed():
    return "The trap has gone off, the rat has been decapitated or escaped"