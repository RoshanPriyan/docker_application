from flask import request, jsonify
from config import SessionLocal
from models import UserModel


def get_users():
    pass
    # db: Session = next(get_db())
    # # users = db.query(User).all()
    # return jsonify("successfully generated")
