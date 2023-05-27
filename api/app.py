from flask import jsonify, request, Flask
from flask_cors import CORS
from router import query_api

app = Flask(__name__)
CORS(app)

from router import query_api

app.register_blueprint(query_api, url_prefix='/api/')

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
