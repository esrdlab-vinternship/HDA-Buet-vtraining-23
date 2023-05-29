from flask import jsonify
from flask.views import MethodView
from DecisionController.decision2b import Decision2b


class Decision2bAPI(MethodView):
    def __init__(self):
        self.decision2b = Decision2b()

    def get(self):
        result = self.decision2b.execute() ## Dataframe
        # print(jsonify(result))
        return jsonify(result)
