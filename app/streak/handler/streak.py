class StreakHandler():
    def __init__(self, username: str) -> dict: 
        self.username = username
        self.message = None
        
    def get_streaks(self):
        if not self._is_valid_username():
            return {"error": self.message}, 422
        
    def _is_valid_username(self):
        if not isinstance(self.username, str):
            self.message = "Username must be string"
            return False
        if len(self.username) > 39:
            self.message = "Username must have at most 39 characters"
            return False