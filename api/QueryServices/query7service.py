from flask import jsonify, request
from flask.views import MethodView
from QueryController.query7 import Query7


class Query7API(MethodView):

    def get(self):
        return jsonify({"success": True})

    def post(self):
        d = request.json['days']
        self.q7 = Query7(days=d)
        result = self.q7.execute()
        return jsonify(result)
