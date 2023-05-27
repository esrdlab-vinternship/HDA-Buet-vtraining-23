from flask import Blueprint

from QueryServices.query1_1service import Query1_1API
from QueryServices.query1_2service import Query1_2API
from QueryServices.query1_3service import Query1_3API
from QueryServices.query1_4service import Query1_4API

from QueryServices.query2_1service import Query2_1API
from QueryServices.query2_2service import Query2_2API
from QueryServices.query2_3service import Query2_3API

from QueryServices.query3service import Query3API
from QueryServices.query4service import Query4API
from QueryServices.query5service import Query5API
from QueryServices.query6service import Query6API
from QueryServices.query7service import Query7API
from QueryServices.query8service import Query8API
from QueryServices.query9service import Query9API
from QueryServices.query10service import Query10API

query_api = Blueprint('queryapi', __name__)

query_api.add_url_rule('/q1_1', view_func=Query1_1API.as_view("Division-wise Sales"))
query_api.add_url_rule('/q1_2', view_func=Query1_2API.as_view("District-wise Sales"))
query_api.add_url_rule('/q1_3', view_func=Query1_3API.as_view("Year-wise Sales"))
query_api.add_url_rule('/q1_4', view_func=Query1_4API.as_view("Month-wise Sales"))

query_api.add_url_rule('/q2_1', view_func=Query2_1API.as_view("Customer-wise Sales"))
query_api.add_url_rule('/q2_2', view_func=Query2_2API.as_view("Bank-wise Sales"))
query_api.add_url_rule('/q2_3', view_func=Query2_3API.as_view("Transaction-wise Sales"))

query_api.add_url_rule('/q3', view_func=Query3API.as_view("Total sales in Barisal"))
query_api.add_url_rule('/q4', view_func=Query4API.as_view("Total sales in 2015"))
query_api.add_url_rule('/q5', view_func=Query5API.as_view("Total sales of Barisal in 2015"))
query_api.add_url_rule('/q6', view_func=Query6API.as_view("Top three products"))
query_api.add_url_rule('/q7', view_func=Query7API.as_view("Sold through card or mobile since X days"))
query_api.add_url_rule('/q8', view_func=Query8API.as_view("Worst quarter"))
query_api.add_url_rule('/q9', view_func=Query9API.as_view("Total sales of items geographically"))
query_api.add_url_rule('/q10', view_func=Query10API.as_view("Average sales monthly per store"))
