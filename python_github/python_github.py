"""Main module."""
from python_github.workflow import Workflow
from python_github.pull_request import PullRequest
import os


class Github():
    def __init__(self):
        token = os.environ["GITHUB_TOKEN"]
        self.workflow = Workflow(token)
        self.pull_request = PullRequest(token)