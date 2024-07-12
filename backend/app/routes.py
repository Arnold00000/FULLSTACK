# backend/app/routes.py
from flask import Blueprint, request, jsonify
from app.models import User
from app import db
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return jsonify({"message": "Welcome to the Flask API!"})


@main.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    new_user = User(
        username=data["username"], password=data["password"]
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully!"})


@main.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()
    if (
        user and user.password == data["password"]
    ):  # Passwords should be hashed and checked securely
        access_token = create_access_token(identity={"username": user.username})
        return jsonify(access_token=access_token)
    return jsonify({"message": "Invalid credentials!"}), 401


@main.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
