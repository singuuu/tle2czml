from flask import Flask, request, Response
from satellite_czml import satellite_czml
import xmltodict

app = Flask(__name__)


@app.post("/tle2czml/json")
def convert_test():
    multiple_tle = []

    data = request.get_json()

    i = 0

    for _ in data:
        tle = []
        element = [data[i]]

        for line in element:
            tle.append(line["line0"])
            tle.append(line["line1"])
            tle.append(line["line2"])

        multiple_tle.append(tle)
        i += 1

    return Response(satellite_czml(tle_list=multiple_tle).get_czml(), status=200, mimetype="application/json")


@app.post("/tle2czml/xml")
def convert_xml():
    tle = [[xmltodict.parse(request.data)["tle"]["line0"],
            xmltodict.parse(request.data)["tle"]["line1"],
            xmltodict.parse(request.data)["tle"]["line2"]
            ]]

    return Response(satellite_czml(tle_list=tle).get_czml(), status=200, mimetype="application/json")
