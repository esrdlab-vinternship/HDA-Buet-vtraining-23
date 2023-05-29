from flask import jsonify
from flask.views import MethodView
from DecisionController.decision3b import Decision3b


class Decision3bAPI(MethodView):
    def __init__(self):
        self.decision3b = Decision3b()

    def get(self):
        result = self.decision3b.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)
