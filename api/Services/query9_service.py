from flask import jsonify
from flask.views import MethodView
from Controller.query9 import Query9

class Query9Service(MethodView):
    def get(self):
        return jsonify(Query9().execute())