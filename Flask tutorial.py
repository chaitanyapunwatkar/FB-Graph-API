# Import Libraries
from flask import Flask, render_template, redirect, url_for
import requests
import json
import datetime
import pandas as pd
from FBData_API import *

app = Flask(__name__)
 
@app.route("/", methods=("POST", "GET"))
def home():
    #return "Hello! This is the main page <h1>Welcome to Flask<h1>"
    df = extract_data()
    return render_template('index.html',  column_names=df.columns.values, row_data=list(df.values.tolist()),
                           link_column="Media_URL", zip=zip)
    
@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin!"))

if __name__ == "__main__":
    app.run()



