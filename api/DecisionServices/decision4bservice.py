from flask import jsonify
from flask.views import MethodView
from DecisionController.decision4b import Decision4b


class Decision4bAPI(MethodView):
    def __init__(self):
        self.decision4b = Decision4b()

    def get(self):
        result = self.decision4b.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)
