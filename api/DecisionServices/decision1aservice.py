from flask import jsonify, request
from flask.views import MethodView
from DecisionController.decision1a import Decision1a


class Decision1aAPI(MethodView):

    def get(self):
        return jsonify({"success": True})

    def post(self):
        y = request.json['year']
        m = request.json['month']
        a = request.json['days_start']
        b = request.json['days_end']
        self.decision1a = Decision1a(year=y, month=m, days_start=a, days_end=b)
        result = self.decision1a.execute()
        return jsonify(result)
