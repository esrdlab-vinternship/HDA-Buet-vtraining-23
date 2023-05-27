from flask import jsonify
from flask.views import MethodView
from Controller.query3 import Query3

class Query3Service(MethodView):
    def get(self):
        return jsonify(Query3().execute())