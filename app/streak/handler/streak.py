from app.streak.services.github.github_client import GithubClient
from datetime import datetime, timedelta

class StreakHandler():
    def __init__(self, username: str) -> dict: 
        self.username = username
        self.message = None
        
    def get_streaks(self):
        if not self._is_valid_username():
            return {"error": self.message}, 422
        
        gh_client = GithubClient()
        user_contributions =  gh_client.get_user_contributions(self.username)
        streak_days = self._get_streak_days_from_user_contributions(user_contributions)
        return {"streak_days": streak_days}

        
    def _is_valid_username(self):
        if not isinstance(self.username, str):
            self.message = "Username must be string"
            return False
        if len(self.username) > 39:
            self.message = "Username must have at most 39 characters"
            return False
        if any(not char.isalnum() and char not in ['-', '_'] for char in self.username):
            self.message = "Username with invalid character"
            return False
        return True
    
    def _get_streak_days_from_user_contributions(self, user_contributions: dict) -> int:
        weeks = user_contributions["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
        date_of_first_contribution_available = weeks[0]['contributionDays'][0]['date']
        initial_streak_date = datetime.strptime(date_of_first_contribution_available, '%Y-%m-%d')
        streak_days = 0
        for weak in weeks:
            for contribution in weak['contributionDays']:
                date = datetime.strptime(contribution["date"], '%Y-%m-%d')
                diff = datetime.today() - date
                if contribution["contributionCount"] > 0:
                    streak_days += 1
                elif diff.days > 0:
                    streak_days = 0
            
        return streak_days