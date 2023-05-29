from flask import jsonify, request
from flask.views import MethodView
from DecisionController.decision1b import Decision1b


class Decision1bAPI(MethodView):

    def get(self):
        return jsonify({"success": True})

    def post(self):
        y = request.json['year']
        m = request.json['month']
        a = request.json['days_start']
        b = request.json['days_end']
        self.decision1b = Decision1b(year=y, month=m, days_start=a, days_end=b)
        result = self.decision1b.execute()
        return jsonify(result)
