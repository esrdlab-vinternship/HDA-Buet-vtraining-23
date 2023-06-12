from flask import jsonify
from flask.views import MethodView

from QueryController.query9 import Query9


class Query9API(MethodView):
    def __init__(self):
        self.q9 = Query9()

    def get(self):
        result = self.q9.execute()
        return jsonify(result)
