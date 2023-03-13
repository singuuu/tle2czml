from flask import Flask, request
from satellite_czml import satellite_czml

app = Flask(__name__)

@app.post("/tle2czml")
def create_store():
    request_data = request.get_json()
    tle0 = request_data["line0"]
    tle1 = request_data["line1"]
    tle2 = request_data["line2"]
    tle = [[tle0, tle1, tle2]]

    return satellite_czml(tle_list=tle).get_czml(), 200

