from flask import Flask, redirect, render_template, request
from helper_functions import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/caller")
def caller():
    return render_template("caller.html")


@app.route("/call_records")
def call_records():
    call_records = get_call_records("S****252G")
    ended = []
    ongoing = {}
    for call in call_records:
        if call['call_status'] == 'Ended':
            ended.append(call)
        else:
            ongoing = call
    return render_template("callrecords.html", ended=ended, ongoing=ongoing)


@app.route("/callerlogin", methods=["POST"])
def caller_login():
    data = request.values
    email = data['email'].strip()
    if email == "":
        return render_template("caller.html", result="Please fill in your email")
    login_result = login_caller(email)

    if login_result:
        ongoing_call = ""
        if has_ongoing_call(email):
            ongoing_call = get_ongoing_call_details(email)
        print(ongoing_call)
        return render_template("callportal.html", email=email, ongoing_call=ongoing_call)

    return render_template("caller.html", result="Wrong email")


@app.route("/startcall", methods=["POST"])
def start_call():
    data = request.values
    email = data['email'].strip()
    nric = data['nric'].strip()
    if nric == "":
        return render_template("callportal.html", email=email, ongoing_call="")

    mark_call_as_ongoing(email, nric)
    ongoing_call = get_ongoing_call_details(email)
    return render_template("callportal.html", email=email, ongoing_call=ongoing_call)


@app.route("/endcall", methods=["POST"])
def end_call():
    data = request.values
    email = data['email'].strip()
    mark_call_as_ended(email)
    return render_template("callportal.html", email=email, ongoing_call="")
