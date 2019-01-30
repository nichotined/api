import requests


class Response(requests.models.Response):
    def __init__(self):
        super().__init__()


class Request(requests.models.Request):
    def __init__(self):
        super().__init__()


class BaseApi:
    _response: Response
    _request: Request

    def __init__(self):
        self._response = Response()
        self._request = Request()
        self._timeout = None
        self._allow_redirects = None
        self._cert = None
        self._proxies = None
        self._stream = None
        self._verify = None

    @property
    def url(self) -> str:
        return self._request.url

    @url.setter
    def url(self, value: str):
        self._request.url = value

    @property
    def headers(self) -> {}:
        return self._request.headers

    @headers.setter
    def headers(self, value: {}):
        self._request.headers = value

    @property
    def response(self) -> requests.models.Response:
        return self._response

    @response.setter
    def response(self, value: requests.models.Response):
        self._response = value

    @property
    def params(self) -> {}:
        return self._request.params

    @params.setter
    def params(self, value: {}):
        self._request.params = value

    @property
    def data(self) -> []:
        return self._request.data

    @data.setter
    def data(self, value: []):
        self._request.data = value

    @property
    def cookies(self):
        return self._request.cookies

    @cookies.setter
    def cookies(self, value):
        self._request.cookies = value

    @property
    def files(self) -> []:
        return self._request.files

    @files.setter
    def files(self, value: []):
        self._request.files = value

    @property
    def auth(self):
        return self._request.auth

    @auth.setter
    def auth(self, value):
        self._request.auth = value

    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, value):
        self._timeout = value

    @property
    def allow_redirects(self):
        return self._allow_redirects

    @allow_redirects.setter
    def allow_redirects(self, value):
        self._allow_redirects = value

    @property
    def proxies(self):
        return self._proxies

    @proxies.setter
    def proxies(self, value):
        self._proxies = value

    @property
    def hooks(self) -> {}:
        return self._request.hooks

    @hooks.setter
    def hooks(self, value: {}):
        self._request.hooks = value

    @property
    def stream(self):
        return self._stream

    @stream.setter
    def stream(self, value):
        self._stream = value

    @property
    def verify(self):
        return self._verify

    @verify.setter
    def verify(self, value):
        self._verify = value

    @property
    def cert(self):
        return self._cert

    @cert.setter
    def cert(self, value):
        self._cert = value

    @property
    def json(self):
        return self._request.json

    @json.setter
    def json(self, value):
        self._request.json = value
