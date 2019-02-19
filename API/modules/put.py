import requests

from .baseApi import BaseApi


class Put(BaseApi):
    def __init__(self):
        super().__init__()
        self._method_name = "PUT"

    def execute(self):
        self.logger_request()
        self._response = requests.put(url=self.url,
                                      params=self.params, data=self.data, headers=self.headers, cookies=self.cookies,
                                      files=self.files, auth=self.auth,
                                      timeout=30 if self.timeout is None else self.timeout,
                                      allow_redirects=self.allow_redirects, proxies=self.proxies,
                                      hooks=self.hooks, stream=self.stream, verify=self.verify, cert=self.cert,
                                      json=self.json)
        self.logger_response()
        if self._response:
            self._json_object = "#NoBody on PUT response"
