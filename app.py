from flask import Flask, jsonify

app = Flask(__name__)

from products import products

#Testing route
@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"message": "Pong!"})

#Getting data
@app.route("/products", methods=["GET"])
def getProduct():
    return jsonify({"products": products, "message":"Products List"})


if __name__ == '__main__':
    app.run(debug=True, port=4000)