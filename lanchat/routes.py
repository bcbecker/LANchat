from flask import Blueprint, render_template, url_for, redirect, request, session, jsonify, flash, escape
from .database import DataBase

main = Blueprint("main", __name__)


NAME_KEY = 'name'
MSG_LIMIT = 100

# routes
@main.route("/login", methods=["POST", "GET"])
def login():
    """
    displays main login page and handles saving name in session
    :exception POST
    :return: None
    """
    if request.method == "POST":
        name = escape(request.form["name"])
        if len(name) >= 2:
            session[NAME_KEY] = name
            flash(' You were successfully logged in as ' + name, category='success')
            return redirect(url_for("main.home"))
        else:
            flash(' Name must be longer than 1 character', category='error')

    return render_template("login.html", **{"session": session})


@main.route("/logout")
def logout():
    """
    logs the user out by popping name from session
    :return: None
    """
    session.pop(NAME_KEY, None)
    flash(' You were logged out', category='success')
    return redirect(url_for("main.login"))


@main.route("/")
@main.route("/home")
def home():
    """
    displays home page if logged in
    :return: None
    """
    if NAME_KEY not in session:
        flash(' Please login before chatting', category='error')
        return redirect(url_for("main.login"))

    return render_template("index.html", **{"session": session})


@main.route("/history")
def history():
    if NAME_KEY not in session:
        flash(' Please login before viewing message history', category='error')
        return redirect(url_for("main.login"))

    json_messages = get_history(session[NAME_KEY])
    print(json_messages)
    return render_template("history.html", **{"history": json_messages})


@main.route("/get_name")
def get_name():
    """
    :return: a json object storing name of logged in user
    """
    data = {"name": ""}
    if NAME_KEY in session:
        data = {"name": session[NAME_KEY]}
    return jsonify(data)


@main.route("/get_messages")
def get_messages():
    """
    :return: all messages stored in database
    """
    db = DataBase()
    msgs = db.get_all_messages(MSG_LIMIT)
    messages = remove_seconds_from_messages(msgs)

    return jsonify(messages)


@main.route("/get_history")
def get_history(name):
    """
    :param name: str
    :return: all messages by name of user
    """
    db = DataBase()
    msgs = db.get_messages_by_name(name)
    messages = remove_seconds_from_messages(msgs)

    return messages


# Utility functions 
def remove_seconds_from_messages(msgs):
    """
    removes the seconds from all messages
    :param msgs: list
    :return: list
    """
    messages = []
    for msg in msgs:
        message = msg
        message["time"] = remove_seconds(message["time"])
        messages.append(message)

    return messages


def remove_seconds(msg):
    """
    :return: string with seconds trimmed off
    """
    return msg.split(".")[0][:-3]
    