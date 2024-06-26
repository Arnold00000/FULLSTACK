from flask import Flask, request, jsonify

# Initialise the flask app
app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the Flask API"


@app.route("/predict", methods=["POST"])
def predict():
    # Replace with actual model logic
    data = request.json
    tac = data.get("tac")
    prediction = {"tac": tac, "prediction": "This is a dummy prediction"}
    return jsonify(prediction)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
