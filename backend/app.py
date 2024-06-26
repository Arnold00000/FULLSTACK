from flask import Flask, request, jsonify


from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

# Initialise the flask app
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://youruser:yourpassword@db/yourdb"
app.config["JWT_SECRET_KEY"] = "your_jwt_secret_key"


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


db = SQLAlchemy(app)
jwt = JWTManager(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)


@app.route("/register", methods=["POST"])
def register():
    data = request.json
    new_user = User(username=data["username"], password=data["password"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(message="User registered"), 201


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data["username"]).first()
    if user and user.password == data["password"]:
        access_token = create_access_token(identity={"username": user.username})
        return jsonify(access_token=access_token), 200
    return jsonify(message="Invalid credentials"), 401


@app.route("/dashboard", methods=["GET"])
@jwt_required()
def dashboard():
    # Example dashboard data
    return jsonify(message="Welcome to the admin dashboard")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
