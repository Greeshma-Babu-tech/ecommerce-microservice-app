from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # <- Enable CORS for all domains

@app.route('/product', methods=['GET'])
def get_product():
    return jsonify({'id': 101, 'name': 'Laptop', 'price': 1200})

if __name__ == '__main__':
    app.run(port=5002)
