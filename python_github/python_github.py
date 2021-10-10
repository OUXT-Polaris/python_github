"""Main module."""
from workflow import Workflow

class Github():
    def __init__(self, token):
        self.workflow = Workflow(token)