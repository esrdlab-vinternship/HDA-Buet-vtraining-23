from flask import jsonify
from flask.views import MethodView
from Controller.query5 import Query5

class Query5Service(MethodView):
    def get(self):
        return jsonify(Query5().execute())