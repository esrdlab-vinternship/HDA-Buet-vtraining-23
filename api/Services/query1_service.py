from flask import jsonify
from flask.views import MethodView
from Controller.query1 import Query1

class Query1Service(MethodView):
    def get(self):
        return jsonify(Query1().execute())