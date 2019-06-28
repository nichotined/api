import json

import requests

from API.modules.json.pyJson import PyJSON
from .baseApi import BaseApi


class Get(BaseApi):
    def __init__(self):
        super().__init__()
        self._method_name = "GET"

    def execute(self):
        self.logger_request()
        self._response = requests.get(url=self.url,
                                      params=self.params, data=self.data, headers=self.headers, cookies=self.cookies,
                                      files=self.files, auth=self.auth,
                                      timeout=30 if self.timeout is None else self.timeout,
                                      allow_redirects=self.allow_redirects, proxies=self.proxies,
                                      hooks=self.hooks, stream=self.stream, verify=self.verify, cert=self.cert,
                                      json=self.json)
        self.logger_response()
        try:
            response_text = str(self._response.text)
            if response_text[0:2] == "[{" and response_text[-2:] == "}]":
                response_text = '{ "data": [' + response_text[1:-1] + "]}"
                self._json_object = PyJSON(json.loads(response_text))
            else:
                self._json_object = PyJSON(self._response.json())
        except json.decoder.JSONDecodeError:
            self._json_object = "#Failed to parse json object in this GET response"
