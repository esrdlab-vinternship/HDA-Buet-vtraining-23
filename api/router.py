from QueryServices.query1service import Query1API
from flask import Blueprint

from QueryServices.query2service import Query2API
from QueryServices.query3service import Query3API
from QueryServices.query4service import Query4API
from QueryServices.query5service import Query5API
from QueryServices.query6service import Query6API
from QueryServices.query7service import Query7API
from QueryServices.query8service import Query8API

query_api = Blueprint('queryapi', __name__)
query_api1 = Blueprint('queryapi1', __name__)

query_api.add_url_rule('/q1', view_func=Query1API.as_view("Get Division-wise Sales"))
query_api.add_url_rule('/q2', view_func=Query2API.as_view("Customer wise total_sale_price"))
query_api.add_url_rule('/q3', view_func=Query3API.as_view("Barisal"))
query_api.add_url_rule('/q4', view_func=Query4API.as_view("2015"))
query_api.add_url_rule('/q5', view_func=Query5API.as_view("Barisal 2015"))
query_api.add_url_rule('/q6', view_func=Query6API.as_view("Top three products from each store"))
query_api.add_url_rule('/q7', view_func=Query7API.as_view("X days"))
query_api.add_url_rule('/q8', view_func=Query8API.as_view("Worst quarter"))
