import pprint as p

from .. import API


class TestClass:
    def test_get(self):
        api = API()
        get = api.get
        get.url = "https://google.com"
        get.header = {}
        get.body = {}
        get.params = {}
        get.timeout = 1

        get.execute()
        print(type(get.response))
        p.pprint(get.response.json())
        assert 200 == get.response.status_code
