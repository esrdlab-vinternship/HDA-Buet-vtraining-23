from flask import jsonify
from flask.views import MethodView
from Controller.query6 import Query6

class Query6Service(MethodView):
    def get(self):
        return jsonify(Query6().execute())