import requests
from app.streak.services.github.config import GithubConfig
from app.streak.services.github.helpers import user_contributions_query

class GithubClient(GithubConfig):
    def __init__(self):
        super().__init__()
        self.headers = {
            "Authorization": f"bearer {self.gh_token}"
        }

    def get_user_contributions(self, username):
        data = user_contributions_query(username)
        response = requests.post(url=self.github_url, data=data, headers=self.headers)
        return response