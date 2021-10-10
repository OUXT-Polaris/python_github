from requests.api import request
from python_github.github_object import GithubObject

class PullRequest(GithubObject):
    def __init__(self, token) -> None:
        super().__init__(token)
    def get(self, repository, state="open") -> None:
        url = self.base_url + "/repos/" + repository + "/pulls"
        if state == "closed":
            url = url + "?&state=closed"
        if state == "open":
            url = url + "?&state=open"
        super().request(url)