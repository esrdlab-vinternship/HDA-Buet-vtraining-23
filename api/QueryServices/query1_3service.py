from flask import jsonify
from flask.views import MethodView
from QueryController.query1_3 import Query1_3

class Query1_3API(MethodView):
    def __init__(self):
        self.q1_3 = Query1_3()

    def get(self):
        result = self.q1_3.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)
