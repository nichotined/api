import json

import requests

from API.modules.json.pyJson import PyJSON
from .baseApi import BaseApi


class Post(BaseApi):
    def __init__(self):
        super().__init__()
        self._method_name = "POST"

    def execute(self):
        self.logger_request()
        self._response = requests.post(url=self.url,
                                       params=self.params, data=self.data, headers=self.headers, cookies=self.cookies,
                                       files=self.files, auth=self.auth, timeout=30 if self.timeout is None else self.timeout,
                                       allow_redirects=self.allow_redirects, proxies=self.proxies,
                                       hooks=self.hooks, stream=self.stream, verify=self.verify, cert=self.cert,
                                       json=self.json)
        self.logger_response()
        try:
            self._json_object = PyJSON(self._response.json())
        except json.decoder.JSONDecodeError:
            self._json_object = "#NoBody on this POST response"
