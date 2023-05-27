from flask import Flask, request, jsonify
from flask_cors import CORS

from router import query_api

app = Flask(__name__)
CORS(app)

app.register_blueprint(query_api, url_prefix="/api/")


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)