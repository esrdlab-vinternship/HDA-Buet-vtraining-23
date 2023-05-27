from flask import jsonify, request
from flask.views import MethodView
from Controller.query7 import Query7

class Query7Service(MethodView):
    def post(self):
        d = request.json['days']
        return jsonify(Query7(days=d).execute())