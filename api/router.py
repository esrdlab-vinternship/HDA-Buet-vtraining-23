from Services.query1_service import Query1Service
from Services.query2_service import Query2Service
from Services.query3_service import Query3Service
from Services.query4_service import Query4Service
from Services.query5_service import Query5Service
from Services.query6_service import Query6Service
from Services.query7_service import Query7Service
from Services.query8_service import Query8Service
from Services.query9_service import Query9Service
from Services.query10_service import Query10Service

from flask import Blueprint

query_api = Blueprint('query_api', __name__)

query_api.add_url_rule('/query1', view_func=Query1Service.as_view('Query 1 Service'))
query_api.add_url_rule('/query2', view_func=Query2Service.as_view('Query 2 Service'))
query_api.add_url_rule('/query3', view_func=Query3Service.as_view('Query 3 Service'))
query_api.add_url_rule('/query4', view_func=Query4Service.as_view('Query 4 Service'))
query_api.add_url_rule('/query5', view_func=Query5Service.as_view('Query 5 Service'))
query_api.add_url_rule('/query6', view_func=Query6Service.as_view('Query 6 Service'))
query_api.add_url_rule('/query7', view_func=Query7Service.as_view('Query 7 Service'))
query_api.add_url_rule('/query8', view_func=Query8Service.as_view('Query 8 Service'))
query_api.add_url_rule('/query9', view_func=Query9Service.as_view('Query 9 Service'))
query_api.add_url_rule('/query10', view_func=Query10Service.as_view('Query 10 Service'))