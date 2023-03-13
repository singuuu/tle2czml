from flask import Flask, request
from satellite_czml import satellite_czml

app = Flask(__name__)

@app.post("/tle2czml")
def convert():
    request_data = request.get_json()

    tle = [[request_data["line0"], request_data["line1"], request_data["line2"]]]

    return satellite_czml(tle_list=tle).get_czml(), 200

