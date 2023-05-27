from flask import jsonify
from flask.views import MethodView

from QueryController.query2_2 import Query2_2


class Query2_2API(MethodView):
    def __init__(self):
        self.q2_2 = Query2_2()

    def get(self):
        result = self.q2_2.execute()
        return jsonify(result)
