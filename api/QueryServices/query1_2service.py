from flask import jsonify
from flask.views import MethodView
from QueryController.query1_2 import Query1_2

class Query1_2API(MethodView):
    def __init__(self):
        self.q1_2 = Query1_2()

    def get(self):
        result = self.q1_2.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)
