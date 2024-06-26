from flask import Flask, request, jsonify

# Initialise the flask app
app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the Flask API"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
