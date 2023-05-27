from flask import jsonify
from flask.views import MethodView

from QueryController.query2_1 import Query2_1


class Query2_1API(MethodView):
    def __init__(self):
        self.q2_1 = Query2_1()

    def get(self):
        result = self.q2_1.execute()
        return jsonify(result)
