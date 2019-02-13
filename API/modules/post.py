import requests

from .baseApi import BaseApi


class Post(BaseApi):
    def __init__(self):
        super().__init__()

    def execute(self):
        self.logger_request()
        self._response = requests.post(url=self.url,
                                       params=self.params, data=self.data, headers=self.headers, cookies=self.cookies,
                                       files=self.files, auth=self.auth, timeout=self.timeout,
                                       allow_redirects=self.allow_redirects, proxies=self.proxies,
                                       hooks=self.hooks, stream=self.stream, verify=self.verify, cert=self.cert,
                                       json=self.json)
        self.logger_response()
