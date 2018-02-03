# import necessary libraries
import pandas as pd

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import (
    Flask,
    render_template,
    jsonify)

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///db/bigfoot.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to the table
Bigfoot = Base.classes.bigfoot

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# Query the database and send the jsonified results
@app.route("/data")
def data():

    # @TODO: Create a database query to fetch the results and send
    # the data to your plo
    sel = [func.strftime("%Y", Bigfoot.timestamp), func.count(Bigfoot.timestamp)]
    # years = session.query(sel[0]).group_by(sel[0])
    # sightings = session.query(sel[1].group_by(sel[0])).all()

    results = session.query(func.strftime("%Y", Bigfoot.timestamp), func.count(Bigfoot.timestamp)).\
        group_by(func.strftime("%Y", Bigfoot.timestamp)).all()
    # results = session.query(sel[0],sel[1]).group_by(sel[0]).all

    # @TODO: YOUR CODE HERE

    years = []
    sightings = []
    for result in results:
        years.append(result[0])
        sightings.append(result[1])
    trace = {
        "x":years,
        "y":sightings,
        "type":"scatter"
    }
    data = [trace]
    
    return jsonify(data)

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
