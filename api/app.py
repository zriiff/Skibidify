from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/skibidify", methods=["GET"])
def skibidify():
    name = request.args.get("name", "World")
    return jsonify({'message': f"Hello {name}"})

if __name__ == '__main__':
    app.run(port=5000, debug=True)