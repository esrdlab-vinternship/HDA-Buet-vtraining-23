from flask import jsonify
from flask.views import MethodView
from Controller.query4 import Query4

class Query4Service(MethodView):
    def get(self):
        return jsonify(Query4().execute())