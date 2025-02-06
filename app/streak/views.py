from flask import Blueprint

streak = Blueprint("streak", __name__)

@streak.route("/streak")
def main():
	'''Streak endpoint, used to know how many day streaks user has'''
	return "No data about day streaks yet"