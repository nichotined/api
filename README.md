# API

This package is used for REST API classbased that's easy to be implemented and called especially for API flow testing.
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
from API import Get

from import_file import host


class RegionByLatLong(Get):
    def __init__(self, latitude: str, longitude: str):
        super().__init__()
        self.url = "{0}/regions?latitude={1}&longitude={2}".format(host["serviceHost"], latitude, longitude)
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "TOKEN"
        }
        self.execute()
        
response = RegionByLatLong('106', '80')
print(response)
```
