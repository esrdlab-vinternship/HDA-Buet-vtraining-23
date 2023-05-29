from flask import jsonify
from flask.views import MethodView
from DecisionController.decision3a import Decision3a


class Decision3aAPI(MethodView):
    def __init__(self):
        self.decision3a = Decision3a()

    def get(self):
        result = self.decision3a.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)
