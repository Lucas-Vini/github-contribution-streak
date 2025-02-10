import requests
from app.streak.services.github.config import GithubConfig

class GithubClient(GithubConfig):
    def __init__(self):
        self.headers = {
            "Authorization": f"bearer {self.gh_token}"
        }

    def get_user_contributions(self, username):
        data = user_contributions_query()
        requests.post(url=self.github_url, data=data, headers=self.headers)