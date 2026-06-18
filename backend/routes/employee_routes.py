from flask import Blueprint, jsonify

employee_bp = Blueprint("employee", __name__)

@employee_bp.route("/employees")
def employees():
    return jsonify([
        {"id":1,"name":"John","department":"IT"}
    ])


