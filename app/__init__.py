from flask import Flask
from app.ping import ping
from app.streak import streak

ACTIVE_ENDPOINTS = (
	("/", ping),
	("/", streak)
	)

def create_app():
	app = Flask(__name__)
	
	# accepts both /endpoint and /endpoint/ as valid URLs
	app.url_map.strict_slashes = False

	for url, blueprint in ACTIVE_ENDPOINTS:
		app.register_blueprint(blueprint, url_prefix=url)

	return app