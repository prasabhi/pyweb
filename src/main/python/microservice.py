# microservice.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data')
def get_data():
    data = {'message': 'This is data from the microservice!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
