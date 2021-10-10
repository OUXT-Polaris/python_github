import requests

class GithubObject:
    token = ""
    def __init__(self, token) -> None:
        self.token = token