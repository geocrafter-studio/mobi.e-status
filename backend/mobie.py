import re
import requests
from time import time


class Mobie(object):

    def __init__(self):
        self.api_url = 'https://www.mobie.pt/public/asset/'
        self.timestamp = str(int(time()))
        self.params = {'version': self.timestamp, 'timestamp': self.timestamp}
        self.session_cookies = {'allowCookies': 'true'}
        self.request_headers = {'Accept': 'application/json, text/javascript, */*; q=0.01'}
        self.client = requests.session()
        # Initialize cookies for session
        self.get_cookie()

    def get_cookie(self):
        try:
            r = self.client.get(self.api_url)
            self.session_cookies.update({'laravel_session': r.cookies.get('laravel_session'),
                                         'XSRF-TOKEN': r.cookies.get('XSRF-TOKEN')})
            # Grab CRF token
            matcher = '<meta name="csrf-token" content="(.*)">'
            csrf = re.search(matcher, r.text)
            self.request_headers.update({'X-CSRF-TOKEN': csrf.group(1)})
        except r.status_code != 200:
            print r.text

    def get(self, url):
        return self.client.get(url=url, params=self.params, cookies=self.session_cookies, headers=self.request_headers)

    def get_station_info(self, station_id):
        try:
            url = self.api_url + station_id
            r = self.get(url)
            return r.json()
        except ValueError:
            self.get_cookie()
            r = self.get(url)
            return r.json()

    def get_station_list(self):
        try:
            url = self.api_url
            r = self.get(url)
            return r.json()
        except ValueError:
            self.get_cookie()
            r = self.get(url)
            return r.json()
