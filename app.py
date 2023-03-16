import random
from datetime import datetime

from flask import Flask, request, Response
from satellite_czml import satellite_czml, satellite
import xmltodict

app = Flask(__name__)


@app.post("/converter/tle2czml/<start_date>/<end_date>/json")
def convert_test(start_date, end_date):
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

    multiple_sats = []
    for tle in multiple_tle:
        sat = satellite(tle,
                        description=tle[0],
                        color=[random.randrange(256) for x in range(3)],
                        marker_scale=12,
                        use_default_image=False,
                        start_time=datetime.strptime(request.view_args['start_date'], '%Y-%m-%dT%H:%M:%S%z'),
                        end_time=datetime.strptime(request.view_args['end_date'], '%Y-%m-%dT%H:%M:%S%z'),
                        show_label=True,
                        show_path=True,
                        )
        multiple_sats.append(sat)

    return Response(satellite_czml(satellite_list=multiple_sats).get_czml(), status=200, mimetype="application/json")


@app.post("/converter/tle2czml/xml")
def convert_xml():
    tle = [[xmltodict.parse(request.data)["tle"]["line0"],
            xmltodict.parse(request.data)["tle"]["line1"],
            xmltodict.parse(request.data)["tle"]["line2"]
            ]]

    return Response(satellite_czml(tle_list=tle).get_czml(), status=200, mimetype="application/json")


@app.get("/converter/tle2czml/help")
def help():
    return Response("In order to convert from TLE to CZML you need to attack the endpoint: \n"
                    "/converter/tle2czml/<start_date>/<end_date>/json \n"
                    "Sample: http://localhost:5000/converter/tle2czml/2022-01-02T14:34:27+0200/2022-01-02T14"
                    ":34:27+0200/json", status=200, mimetype="text/text")
