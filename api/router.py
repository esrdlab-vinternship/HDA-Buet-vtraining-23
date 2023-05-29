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

from DecisionServices.decision1aservice import Decision1aAPI
from DecisionServices.decision1bservice import Decision1bAPI
from DecisionServices.decision2aservice import Decision2aAPI
from DecisionServices.decision2bservice import Decision2bAPI
from DecisionServices.decision3aservice import Decision3aAPI
from DecisionServices.decision3bservice import Decision3bAPI
from DecisionServices.decision4aservice import Decision4aAPI
from DecisionServices.decision4bservice import Decision4bAPI
from DecisionServices.decision5aservice import Decision5aAPI
from DecisionServices.decision5bservice import Decision5bAPI

from flask import Blueprint

query_api = Blueprint('queryapi', __name__)
decision_api = Blueprint('decisionapi', __name__)


query_api.add_url_rule('/query1', view_func=Query1API.as_view("Get Division-wise Sales"))
query_api.add_url_rule('/query2', view_func=Query2API.as_view("Get Bank-wise Total Sales"))
query_api.add_url_rule('/query3', view_func=Query3API.as_view("Get Barisal Division Sales"))
query_api.add_url_rule('/query4', view_func=Query4API.as_view("Get Year 2015 Sales"))
query_api.add_url_rule('/query5', view_func=Query5API.as_view("Get Barisal Division 2015 Sales"))
query_api.add_url_rule('/query6', view_func=Query6API.as_view("Get Top 3 Sold Products of Each Store"))
query_api.add_url_rule('/query7', view_func=Query7API.as_view("Get Total Sales within Last X Days"))
query_api.add_url_rule('/query8', view_func=Query8API.as_view("Get Worst Quarter For Each Product Sales"))
query_api.add_url_rule('/query9', view_func=Query9API.as_view("Get Division-wise Sales For Each Product"))
query_api.add_url_rule('/query10', view_func=Query10API.as_view("Get Monthly Average Sales For Each Store"))


decision_api.add_url_rule('/decision1a', view_func=Decision1aAPI.as_view("Get Stores with Least Sales"))
decision_api.add_url_rule('/decision1b', view_func=Decision1bAPI.as_view("Get Most Profitable Districts Per Division"))
decision_api.add_url_rule('/decision2a', view_func=Decision2aAPI.as_view("Get Customers With Highest Purchases"))
decision_api.add_url_rule('/decision2b', view_func=Decision2bAPI.as_view("Get Customers With Highest Days Ordered"))
decision_api.add_url_rule('/decision3a', view_func=Decision3aAPI.as_view("Get Most Popular Soda Beverage"))
decision_api.add_url_rule('/decision3b', view_func=Decision3bAPI.as_view("Get Most Popular Product and Supplier"))
decision_api.add_url_rule('/decision4a', view_func=Decision4aAPI.as_view("Get Highest Quantity Products Sold"))
decision_api.add_url_rule('/decision4b', view_func=Decision4bAPI.as_view("Get Highest Sales in Cartons Unit"))
decision_api.add_url_rule('/decision5a', view_func=Decision5aAPI.as_view("Get Max and Min Medicine Sales"))
decision_api.add_url_rule('/decision5b', view_func=Decision5bAPI.as_view("Get Most In-demand Food"))
