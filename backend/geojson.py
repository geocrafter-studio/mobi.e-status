
class Json2GeoJson(object):

    @staticmethod
    def converter(data):
        geojson = {
            "type": "FeatureCollection",
            "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},
            "features": [
                {
                    "type": "Feature",
                    "properties": d,
                    "geometry": {
                        "type": "Point",
                        "coordinates": [float(d["location"]["longitude"]), float(d["location"]["latitude"])],
                    },
                } for d in data['data']]
        }
        return geojson
