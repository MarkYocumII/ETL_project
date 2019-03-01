import numpy as np
import datetime as dt
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask, jsonify

dbuser = 'root'
dbpassword = 'ro-Cha7t'
dbhost = 'localhost'
dbport = '3306'
dbname= 'ETL_db'

engine = create_engine(f"mysql://{dbuser}:{dbpassword}@{dbhost}:{dbport}/{dbname}")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Consumption = Base.classes.cons
GasPrices = Base.classes.gasprices
States = Base.classes.states
VMT = Base.classes.vmt


session=Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/consumption<br/>"
        f"/api/v1.0/gasprices<br/>"
        f"/api/v1.0/states<br/>"
        f"/api/v1.0/vmt<br/>"
    )

@app.route("/api/v1.0/consumption")
def consumption():
    """Return all state consumption data"""
    # Query all consumption data by state
    results = session.query(Consumption).all()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_cons = list(np.ravel(results))

    return jsonify(all_cons)

# @app.route("/api/v1.0/gasprices")
# def gasprices():
#    """Return all state vmt data"""
#     # Query all vmt data by state
#     results_gasprices = session.query(GasPrices).all()

#     # Create a dictionary from the row data and append to a list of all_passengers
#     all_vmt = list(np.ravel(results_gasprices))

#     return jsonify(all_vmt)