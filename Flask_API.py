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
dbname= 'etl_db'

engine = create_engine(f"mysql://{dbuser}:{dbpassword}@{dbhost}:{dbport}/{dbname}")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table


# GasPrices = Base.classes.gasprices
# States = Base.classes.states
# VMT = Base.classes.vmt


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
    Consumption = engine.execute("SELECT * FROM cons").fetchall()
    
    return jsonify({'Consumption': [dict(row) for row in Consumption]})

@app.route("/api/v1.0/gasprices")
def gasprices():
    """Return all state gas price data"""
    # Query all gas price data by state
    Gasprices = engine.execute("SELECT * FROM gasprices").fetchall()
    
    return jsonify({'Gasprices': [dict(row) for row in Gasprices]})

@app.route("/api/v1.0/states")
def states():
    """Return all state abbreviation data"""
    # Query all abbreviations by state
    States = engine.execute("SELECT * FROM states").fetchall()
    
    return jsonify({'States': [dict(row) for row in States]})

@app.route("/api/v1.0/vmt")
def vmt():
    """Return all vehicle miles traveled data by state"""
    # Query all vmt data by state
    VMT = engine.execute("SELECT * FROM vmt").fetchall()
    
    return jsonify({'VMT': [dict(row) for row in VMT]})




if __name__ == '__main__':
    app.run(debug=True)
