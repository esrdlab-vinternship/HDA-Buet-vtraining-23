from flask import jsonify
from flask.views import MethodView
from QueryController.query1_4 import Query1_4


class Query1_4API(MethodView):
    def __init__(self):
        self.q1_4 = Query1_4()

    def get(self):
        result = self.q1_4.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)
