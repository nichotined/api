# API

This python package for API testing.
Extending python requests library
https://github.com/requests/requests/

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
        
response = RegionByLatLong()
print(response)
```
