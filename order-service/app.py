from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # <- Enable CORS for all domains

@app.route('/order', methods=['GET'])
def get_order():
    return jsonify({'order_id': 500, 'user_id': 1, 'product_id': 101, 'quantity': 2})

if __name__ == '__main__':
    app.run(port=5003)
