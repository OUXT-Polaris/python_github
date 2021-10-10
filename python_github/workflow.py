from python_github.github_object import GithubObject

class Workflow(GithubObject):
    def __init__(self, token) -> None:
        super().__init__(token)
    def get(self, repository) -> None:
        url = self.base_url + "/repos/" + repository + "/actions/workflows"
        return super().request(url)
    def get_id(self, repository, name) -> None:
        url = self.base_url + "/repos/" + repository + "/actions/workflows"
        response = super().request(url)
        for workflow in response["workflows"]:
            if workflow["name"] == name:
                return workflow['id']
        return None