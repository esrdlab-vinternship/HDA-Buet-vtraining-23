from flask import jsonify
from flask.views import MethodView
from Controller.query10 import Query10

class Query10Service(MethodView):
    def get(self):
        return jsonify(Query10().execute())