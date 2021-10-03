
from flask import Blueprint, render_template, request, jsonify
views = Blueprint(__name__, "views")
@views.route("/")
def home():
    return render_template("index.html", name="Nikos") 
@views.route("/profile")
def profile():
    args = request.args
    name = args.get('name')
    return render_template("index.html", name=name)
@views.route("/json")
def get_json():
    return jsonify({"name": "Danny", "skillset": "complete"})
@views.route("/data")
def get_data():
    ##data = incoming json file
    data = request.json
    return jsonify(data)
