from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # <- Enable CORS for all domains

@app.route('/user', methods=['GET'])
def get_user():
    return jsonify({'id': 1, 'name': 'Greeshma Babu', 'email': 'greeshma@example.com'})

if __name__ == '__main__':
    app.run(port=5001)
