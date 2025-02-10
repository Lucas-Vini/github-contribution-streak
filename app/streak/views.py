from flask import Blueprint, request
from app.streak.handler.streak import StreakHandler

streak = Blueprint("streak", __name__)

@streak.route("/streak")
def main():
	'''Streak endpoint, used to know how many day streaks user has'''
	username = request.args.get("username")
	data = StreakHandler(username).get_streaks()
	return data