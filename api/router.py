
from flask import Blueprint

from QueryServices.query1service import Query1API
from QueryServices.query2service import Query2API
from QueryServices.query3service import Query3API
from QueryServices.query4service import Query4API
from QueryServices.query5service import Query5API

from QueryServices.query6service import Query6API
from QueryServices.query7service import Query7API
from QueryServices.query8service import Query8API
from QueryServices.query9service import Query9API
from QueryServices.query10service import Query10API





query_api = Blueprint('queryapi', __name__)

query_api.add_url_rule('/q1', view_func=Query1API.as_view("Get Division-wise Sales"))
query_api.add_url_rule('/q2', view_func=Query2API.as_view("Customer wise total_sale_price"))
query_api.add_url_rule('/q3', view_func=Query3API.as_view("Total sales in Barisal"))
query_api.add_url_rule('/q4', view_func=Query4API.as_view("Total sales in 2015"))
query_api.add_url_rule('/q5', view_func=Query5API.as_view("Total sales of Barisal in 2015"))

query_api.add_url_rule('/q6', view_func=Query6API.as_view("the top three products that are most often purchased "
                                                           "each store(or item supplier)"))
query_api.add_url_rule('/q7', view_func=Query7API.as_view("the products that have been sold since X days"))
query_api.add_url_rule('/q8', view_func=Query8API.as_view("the season(quarter)that is the worst for each product item"))
query_api.add_url_rule('/q9', view_func=Query9API.as_view("the total sales of items geographically (division-wise)"))
query_api.add_url_rule('/q10', view_func=Query10API.as_view("the average sales of products sales per store monthly"))


