from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/api/items', methods=['GET'])
def get_items():
    items = [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]
    return jsonify(items)

@app.route('/api/items', methods=['POST'])
def add_item():
    item = request.get_json()
    return jsonify(item), 201

if __name__ == '__main__':
    app.run(debug=True)