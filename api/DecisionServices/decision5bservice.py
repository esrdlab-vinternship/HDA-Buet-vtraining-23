from flask import jsonify
from flask.views import MethodView
from DecisionController.decision5b import Decision5b


class Decision5bAPI(MethodView):
    def __init__(self):
        self.decision5b = Decision5b()

    def get(self):
        result = self.decision5b.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)
