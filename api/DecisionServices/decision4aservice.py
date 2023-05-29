from flask import jsonify
from flask.views import MethodView
from DecisionController.decision4a import Decision4a


class Decision4aAPI(MethodView):
    def __init__(self):
        self.decision4a = Decision4a()

    def get(self):
        result = self.decision4a.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)
