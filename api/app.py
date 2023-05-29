from flask import jsonify, request, Flask
from flask_cors import CORS
from router import query_api
from router import decision_api


app = Flask(__name__)
CORS(app)


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello Interns!'})


@app.route('/postdata', methods=['POST'])
def hellopost():
    data = {}
    data['name'] = request.json['name']
    data['age'] = request.json['age']
    return jsonify({
        'Name': data['name'],
        'age': data['age']
    })


app.register_blueprint(query_api, url_prefix='/api/')
app.register_blueprint(decision_api, url_prefix='/dec_api/')

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
