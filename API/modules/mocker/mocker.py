from mitmproxy import http


class MockResponse:
    def __init__(self, url: str, status_code: int, body: str, content_type: str):
        self.url = url
        self.status_code = status_code
        self.body = body
        self.content_type = {"Content-Type": content_type}


class Events:
    def __init__(self, mock_data: MockResponse):
        self.mock_data = mock_data

    def request(self, flow: http.HTTPRequest) -> None:
        if self.mock_data.url in flow.request.url:
            flow.response = http.HTTPResponse.make(
                status_code=self.mock_data.status_code,
                content=self.mock_data.body,
                headers=self.mock_data.content_type
            )

# j = """
# {
# "key":"value"
# }
# """
#
# mr = MockResponse("https://google.com", 200, j, "application/json")
#
# addons = [
#     Events(mr)
# ]
