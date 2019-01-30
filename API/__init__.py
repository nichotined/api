name = "API"

from .modules import *


class API:
    def __init__(self):
        self.get = Get()
        self.post = Post()
