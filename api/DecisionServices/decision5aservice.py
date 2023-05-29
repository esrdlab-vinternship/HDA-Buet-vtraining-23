from flask import jsonify
from flask.views import MethodView
from DecisionController.decision5a import Decision5a


class Decision5aAPI(MethodView):
    def __init__(self):
        self.decision5a = Decision5a()

    def get(self):
        result = self.decision5a.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)
