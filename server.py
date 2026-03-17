from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

balance = 100

@app.route("/spin", methods=["POST"])
def spin():
    global balance

    data = request.json
    bet = data["bet"]
    number = data["number"]

    result = random.randint(0, 36)

    if number == result:
        balance += bet * 35
        win = True
    else:
        balance -= bet
        win = False

    return jsonify({
        "result": result,
        "balance": balance,
        "win": win
    })

app.run(port=5000)