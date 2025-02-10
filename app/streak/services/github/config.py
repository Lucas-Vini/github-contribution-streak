import os

class GithubConfig:
    def __init__(self):
        self.github_url = os.getenv("GH_URL")
        self.gh_token = os.getenv("GH_TOKEN")