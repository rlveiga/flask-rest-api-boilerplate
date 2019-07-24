from flask import jsonify
from . import main

@main.route('/')
def index():
	response = {
		'message': 'We are live!',
	}

	return jsonify(response)