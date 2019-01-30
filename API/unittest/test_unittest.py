import pprint as p

from .. import API


class TestClass:
    def test_get(self):
        api = API()
        get = api.get
        get.url = "http://integration-customer-owner-internal.golabs.io/internal/customers/280523"
        get.header = {
            "client-id": "go-shop-integration",
            "pass-key": "o3B3AgnyjD8zmlorYdrtxKRHFxxTwwZGQpQIAnA+ue0=",
            "Content-Type": "application/json",
            "Cache-Control": "no-cache",
            "Postman-Token": "4a8ea09e-cd6d-57ab-04b6-047c3c9323e2"
        }
        get.body = {}
        get.params = {}
        get.timeout = 1

        get.execute()
        print(type(get.response))
        p.pprint(get.response.json())
        assert 200 == get.response.status_code
