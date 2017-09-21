import os
import re
from flask import Flask, jsonify, render_template, request, url_for
import requests
import csv, json

# configure application
app = Flask(__name__)


# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# configure CS50 Library to use SQLite database
# db = SQL("sqlite:///mashup.db")

@app.route("/")
def index():
    """Render map."""
    # if not os.environ.get("API_KEY"):
    #     raise RuntimeError("API_KEY not set")
    # return render_template("index.html", key=os.environ.get("API_KEY"))
    return render_template("testpage.html")

@app.route("/search")
def search():
    
    temp = []

    csv_from_link = requests.get('http://www.airnowapi.org/aq/forecast/zipCode/?format=text/csv&zipCode=06511&date=2016-12-07&distance=50&API_KEY=A21183C3-CD14-486B-A323-490DC1A37FE0')
    # csvfile = csv.reader(csv_from_link)
    with open('output.csv') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            temp.append(row)



    return jsonify(temp)

