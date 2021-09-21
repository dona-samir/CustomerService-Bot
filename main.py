from flask import Flask, render_template, request, redirect,url_for
from flask.json import jsonify, load
import CS
import utillis

app = Flask(__name__)


@app.route("/")

def index():
    
    return render_template("login.html")

@app.route("/login")

def login():
    Email = request.args.get('Email')
    passw = request.args.get('password')
    global user
    user = utillis.getUser(Email)
    if user:
        print(user)
        if user['password'] == passw:
            return "1"
        else:
            return '0'
    else:
        return "0"

@app.route("/home")

def home():

    return render_template("home.html")


@app.route("/get")

def chat():
    while (True):
        user_response = request.args.get('msg')
        utillis.cuser=user
        response = CS.chat(user_response)
        return response



# @app.route("/test",methods=["Post"])
# def test():
#     return jsonify(utillis.problem('18888','1'))

if __name__ == "__main__":

    app.run()
