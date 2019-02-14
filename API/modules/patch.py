import requests

from API.modules.json.pyJson import PyJSON
from .baseApi import BaseApi


class Patch(BaseApi):
    def __init__(self):
        super().__init__()

    def execute(self):
        self._method_name = "PATCH"
        self.logger_request()
        self._response = requests.patch(url=self.url,
                                        params=self.params, data=self.data, headers=self.headers, cookies=self.cookies,
                                        files=self.files, auth=self.auth, timeout=self.timeout,
                                        allow_redirects=self.allow_redirects, proxies=self.proxies,
                                        hooks=self.hooks, stream=self.stream, verify=self.verify, cert=self.cert,
                                        json=self.json)
        self.logger_response()
        if self._response:
            self._json_object = PyJSON(self._response.json())
