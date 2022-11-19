# Import Libraries
from flask import Flask, render_template, redirect, url_for
import requests
import json
import datetime
import pandas as pd
from FBData_API import *

app = Flask(__name__)

 # Home page content
@app.route("/", methods=("POST", "GET"))
def home(): 
    df = extract_data() # fetchs data from facebook graph API.
    return render_template('index.html',  column_names=df.columns.values, row_data=list(df.values.tolist()),
                           link_column="Media_URL", zip=zip) # Displays in html format in Web
    

if __name__ == "__main__":
    app.run()



