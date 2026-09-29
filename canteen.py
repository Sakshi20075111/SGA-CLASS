from flask import flask, render_template ,jsonify, request
app = flask(__name__)
menu = {"poha":30, "tea":15, "sandwich":50}

@app.route("/menu")
def get_menu():
    return render_template('index.html')

@app.route("/order", methods=["POST"])
def place_order():
    order = request.get_json()
    item = order["item"]
    qty = order["quantity"]
    total = menu[item] * qty
    return jsonify({
        "order_id": 101,
        "total":total,
        "status": "order placed"
    })
app.run(host = "0.0.0.0", port=5001)