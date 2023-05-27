from flask import jsonify
from flask.views import MethodView

from QueryController.query2_3 import Query2_3


class Query2_3API(MethodView):
    def __init__(self):
        self.q2_3 = Query2_3()

    def get(self):
        result = self.q2_3.execute()
        return jsonify(result)
