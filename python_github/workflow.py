from python_github.github_object import GithubObject

class Workflow(GithubObject):
    def __init__(self, token) -> None:
        super().__init__(token)
    def execute(self, args) -> None:
        return