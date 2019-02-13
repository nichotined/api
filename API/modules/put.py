from pprint import pprint

import curlify
import requests

from .baseApi import BaseApi


class Put(BaseApi):
    def __init__(self):
        super().__init__()

    def execute(self):
        self.logger()
        self._response = requests.put(url=self.url,
                                      params=self.params, data=self.data, headers=self.headers, cookies=self.cookies,
                                      files=self.files, auth=self.auth, timeout=self.timeout,
                                      allow_redirects=self.allow_redirects, proxies=self.proxies,
                                      hooks=self.hooks, stream=self.stream, verify=self.verify, cert=self.cert,
                                      json=self.json)
        print(' Response '.center(80, '*'))
        pprint(self._response.text)
        print(' CURL '.center(80, '*'))
        pprint(curlify.to_curl(self._response.request))
