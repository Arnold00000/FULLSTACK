# backend/app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS

# Initialize the flask app
app = Flask(__name__)

app.config.from_object("app.config.Config")
CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# Import and register blueprints
from app.routes import main as main_blueprint

app.register_blueprint(main_blueprint)


@app.route("/")
def home():
    return "Welcome to the TAC Predictor API!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")


# from flask import Flask, request, jsonify


# from flask_sqlalchemy import SQLAlchemy
# from flask_jwt_extended import JWTManager, create_access_token, jwt_required
# from flask_migrate import Migrate
# from flask_cors import CORS
# import pandas as pd
# import joblib

# # Initialise the flask app
# app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://youruser:yourpassword@db/yourdb"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["JWT_SECRET_KEY"] = "your_jwt_secret_key"
# CORS(app)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)  # Ensure Migrate is initialized with app and db
# jwt = JWTManager(app)


# # Import the models here
# # from app.models import User

# # Load the trained model
# # model = joblib.load("tac_predictor_model.pkl")


# @app.route("/")
# def home():
#     return "Welcome to the TAC Predictor API!"


# # @app.route("/register", methods=["POST"])
# # def register():
# #     data = request.json
# #     new_user = User(username=data["username"], password=data["password"])
# #     db.session.add(new_user)
# #     db.session.commit()
# #     return jsonify(message="User registered"), 201


# # @app.route("/login", methods=["POST"])
# # def login():
# #     data = request.json
# #     user = User.query.filter_by(username=data["username"]).first()
# #     if user and user.password == data["password"]:
# #         access_token = create_access_token(identity={"username": user.username})
# #         return jsonify(access_token=access_token), 200
# #     return jsonify(message="Invalid credentials"), 401


# @app.route("/dashboard", methods=["GET"])
# @jwt_required()
# def dashboard():
#     # Example dashboard data
#     return jsonify(message="Welcome to the admin dashboard")


# # @app.route("/predict", methods=["POST"])
# # def predict():
# #     if request.method == "POST":
# #         data = request.get_json(force=True)
# #         tac = data["tac"]
# #         reportingBodyId = int(tac[:2])
# #         manufacturerModelId = int(tac[2:])
# #         features = pd.DataFrame(
# #             [[reportingBodyId, manufacturerModelId]],
# #             columns=["reportingBodyId", "manufacturerModelId"],
# #         )
# #         prediction = model.predict(features)
# #         return jsonify(prediction=prediction.tolist())
# #     return jsonify(error="Invalid request method"), 405


# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0")
