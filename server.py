import argparse
from backend import api


class Server(object):
    def __init__(self):
        self.api = api.API()
        self.host = self.api.host
        self.port = self.api.port
        self.debug = self.api.debug

    def run_server(self, **kwargs):
        self.api.server(host=kwargs['host'], port=kwargs['port'], debug=kwargs['debug'])


if __name__ == "__main__":
    args = {}
    server = Server()
    parser = argparse.ArgumentParser(description='Small API wrapper for Mobi.e API, based on Flask.')
    parser.add_argument('--host', '-hn', action='store', dest='host', help='Server hostname', default=server.host)
    parser.add_argument('--port', '-p', action='store', dest='port', help='Server port number', type=int, default=server.port)
    parser.add_argument('--debug', '-d', action='store_true', dest='debug', help='Run server in debug mode', default=server.debug)
    r = parser.parse_args()

    args['host'] = r.host if r.host is not None else server.host
    args['port'] = r.port if r.port is not None else server.port
    args['debug'] = r.debug if r.debug is not None else server.debug

    server.run_server(**args)
