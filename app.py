from flask import Flask, request, Response
from satellite_czml import satellite_czml
import xmltodict

app = Flask(__name__)


@app.post("/tle2czml/json")
def convert_json():

    request_data = request.get_json()

    tle = [[request_data["line0"],
            request_data["line1"],
            request_data["line2"]
            ]]

    return Response(satellite_czml(tle_list=tle).get_czml(), 200, mimetype="application/json")


@app.post("/tle2czml/xml")
def convert_xml():

    tle = [[xmltodict.parse(request.data)["tle"]["line0"],
            xmltodict.parse(request.data)["tle"]["line1"],
            xmltodict.parse(request.data)["tle"]["line2"]
            ]]

    return Response(satellite_czml(tle_list=tle).get_czml(), 200, mimetype="application/json")
