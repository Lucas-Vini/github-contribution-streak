from flask import Flask
from app.ping import ping

ACTIVE_ENDPOINTS = (
	("/", ping),
	)

def create_app():
	app = Flask(__name__)
	
	# accepts both /endpoint and /endpoint/ as valid URLs
	app.url_map.strict_slashes = False

	for url, blueprint in ACTIVE_ENDPOINTS:
		app.register_blueprint(blueprint, url_prefix=url)

	return app