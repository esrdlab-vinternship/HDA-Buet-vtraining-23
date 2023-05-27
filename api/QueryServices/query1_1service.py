from flask import jsonify
from flask.views import MethodView
from QueryController.query1_1 import Query1_1

class Query1_1API(MethodView):
    def __init__(self):
        self.q1_1 = Query1_1()

    def get(self):
        result = self.q1_1.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)
