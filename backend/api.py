from flask import Flask, jsonify
from backend import mobie, geojson


mobie_api = mobie.Mobie()
app = Flask(__name__)


class API(object):
    def __init__(self):
        self.host = 'localhost'
        self.port = 8080
        self.debug = True

    @staticmethod
    def server(host, port, debug):
        app.run(host, port, debug)

    @staticmethod
    @app.route('/api/station/<string:station_id>', methods=['GET'])
    def station_info(station_id):
        try:
            data = mobie_api.get_station_info(station_id)
            # TODO: Refactor the raw response from Mobi.e
            return jsonify(data)
        except TypeError:
            return 'error parsing response'

    @staticmethod
    @app.route('/api/stations', methods=['GET'])
    def stations_list():
        try:
            data = mobie_api.get_station_list()
            return jsonify(data)
        except TypeError:
            return 'error parsing response'

    @staticmethod
    @app.route('/api/stations/geo', methods=['GET'])
    def geo_stations():
        try:
            data = mobie_api.get_station_list()
            stations = geojson.Json2GeoJson.converter(data)
            return stations
        except TypeError:
            return 'error parsing response'