import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")

@app.route("/", methods=["GET", "POST"])
def index():
    rows = db.execute("SELECT * FROM birthdays")
    if request.method == "POST":
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")
        rows = db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)


        # TODO: Add the user's entry into the database

        return redirect("/")

    else:
        rows = db.execute("SELECT * FROM birthdays")
        # TODO: Display the entries in the database on index.html

        return render_template("index.html", rows=rows)


