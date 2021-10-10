from github_object import GithubObject

class Workflow(GithubObject):
    def __init__(self, token) -> None:
        super().__init__(token)