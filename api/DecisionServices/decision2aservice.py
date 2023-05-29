from flask import jsonify
from flask.views import MethodView
from DecisionController.decision2a import Decision2a


class Decision2aAPI(MethodView):
    def __init__(self):
        self.decision2a = Decision2a()

    def get(self):
        result = self.decision2a.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)
