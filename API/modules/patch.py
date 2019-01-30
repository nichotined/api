import requests

from .baseApi import BaseApi


class Patch(BaseApi):
    def __init__(self):
        super().__init__()

    def execute(self):
        self._response = requests.patch(url=self.url,
                                        params=self.params, data=self.data, headers=self.headers, cookies=self.cookies,
                                        files=self.files, auth=self.auth, timeout=self.timeout,
                                        allow_redirects=self.timeout, proxies=self.proxies,
                                        hooks=self.hooks, stream=self.stream, verify=self.verify, cert=self.cert,
                                        json=self.json)
