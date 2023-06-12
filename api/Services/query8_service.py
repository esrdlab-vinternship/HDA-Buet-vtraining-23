from flask import jsonify
from flask.views import MethodView
from Controller.query8 import Query8

class Query8Service(MethodView):
    def get(self):
        return jsonify(Query8().execute())