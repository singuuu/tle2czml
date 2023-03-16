# tle2czml
API with Flask for convert TLE data to CZML

Sample endpoint:
```sh
http://<ip-addres>:<port>/converter/tle2czml/2022-01-02T14:34:27+0200/2022-01-02T14:34:27+0200/json
```

Sample body:
```json
[
    {
        "line0": "ISS (ZARYA)",
        "line1": "1 25544U 98067A   18343.59228877  .00002464  00000-0  44555-4 0  9990",
        "line2": "2 25544  51.6406 224.5995 0005136 127.6506 318.1257 15.54075846145790"
    }
]
```
