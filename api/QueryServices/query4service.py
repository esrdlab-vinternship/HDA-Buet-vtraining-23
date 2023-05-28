from flask import jsonify
from flask.views import MethodView

from QueryController.query4 import Query4


class Query4API(MethodView):
    def __init__(self):
        self.q4 = Query4()

    def get(self):
        result = self.q4.execute()
        return jsonify(result)
