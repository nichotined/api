# API

This package is used for REST API classbased, author used it for API flow testing.  
JSON body response will be converted to python data type. Made it easier for you to use.  
> This package is extending python requests library https://github.com/requests/requests/  

How to install 
```
$ pip3 install api-nichotined
```

How to distribute to pypi
```
$ python3 setup.py sdist bdist_wheel
$ python3 -m twine upload dist/*
```

Usage example
```python3
from API import Get, Post

from import_file import host

post_body = {
    "name": "Nicholas Frederick"
}

class GetRequest(Get):
    def __init__(self, latitude: str, longitude: str):
        super().__init__()
        self.url = "{0}/dummy?latitude={1}&longitude={2}".format(host["serviceHost"], latitude, longitude)
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "TOKEN"
        }
        self.execute()
        
class PostRequest(Post):
    def __init__(self, body: Data):
        super().__init__()
        self.url = "{0}/dummy".format(host['serviceHost'])
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "TOKEN"
        }
        self.json = body
        self.execute()

        
if __name__ == "__main__":
    get_data = GetRequest('106', '80')
    post_data = PostRequest(post_body)
    assert get_data.address_name == "somewhere"
    assert post_data.status_code == 200
```
