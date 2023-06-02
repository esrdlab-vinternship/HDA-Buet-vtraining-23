from QueryServices.query1service import Query1API
from flask import Blueprint

from QueryServices.query2service import Query2API
from QueryServices.query7service import Query7API

query_api = Blueprint('queryapi', __name__)
query_api1 = Blueprint('queryapi1', __name__)

query_api.add_url_rule('/query1', view_func=Query1API.as_view("Get Division-wise Sales"))
query_api.add_url_rule('/query2', view_func=Query2API.as_view("Customer wise total_sale_price"))
query_api1.add_url_rule('/query7', view_func=Query7API.as_view("X days"))
