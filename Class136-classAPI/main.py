import json
from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

@app.route("/")
def homepage():
    return jsonify({
        "data": data,
        "message": "sucess"
    }),200

@app.route("/planet")
def planet_name():
    name = request.args.get("name")
    pdata = next(item for item in data if item["name"] == name)
    return jsonify({
        "data": pdata,
        "message": "found"
    }),200


if __name__ == "__main__":
    app.run(debug=True)

