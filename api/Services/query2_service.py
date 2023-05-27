from flask import jsonify
from flask.views import MethodView
from Controller.query2 import Query2

class Query2Service(MethodView):
    def get(self):
        return jsonify(Query2().execute())