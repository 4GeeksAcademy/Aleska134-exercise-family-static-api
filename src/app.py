"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")
jackson_family.add_member({
    "first_name": "John",
    "age": 33,
    "lucky_numbers": [7,13,22]
})
jackson_family.add_member({
    "first_name": "Jane",
    "age": 35,
    "lucky_numbers": [10,14,3]
})
jackson_family.add_member({
    "first_name": "Jimmy",
    "age": 5,
    "lucky_numbers": [1]
})

@app.route('/')
def sitemap():
    return generate_sitemap(app)


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)

@app.route("/members", methods= ["GET"])
def handle_hello():
    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route("/member/<int:member_id>", methods=["GET"])
def get_one_member(member_id):
    request = jackson_family.get_member(member_id)
    if request is None:
        return jsonify({"message": "User doesn't exist"}),400
    return jsonify(request),200
    

@app.route("/member", methods=["POST"])
def add_family_member():
    body = request.get_json()
    jackson_family.add_member(body)
    return jsonify({}), 200


@app.route("/member/<int:member_id>",methods=['DELETE'])
def delete_one_member(member_id):
    request = jackson_family.delete_member(member_id)
    if request is False:
        return jsonify({"message": "User doesn't exist"}),400
    return jsonify({"message": "deleted succesfully"})
    


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)