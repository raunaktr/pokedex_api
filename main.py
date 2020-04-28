import os
import traceback
from flask import Flask, request, jsonify, json
from flask_cors import CORS, cross_origin
from app.models.ApiResponse import ApiResponse
from app.models.ErrorObject import ErrorObject
from service import connection
from app.utils.es_connection import es_verify
from app.pokemon.get_name_service import get_pokemon
from app.pokemon.get_evolution_service import evolution
from app.pokemon.get_weaknesses_service import get_weaknesses
from app.pokemon.get_type_service import get_types


app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})


@app.route("/")
def home():
    return "welcome to pokedex"


@app.route("/name", methods=["GET"])
def view_pokemon():
    try:
        request_data = request.get_json()
        data = get_pokemon(request_data["name"])
        if (data['error'] == "true"):
            status = ErrorObject("true", "200", data["msg"])
            data = ""
            api_response = ApiResponse(data, status)
        else:
            status = ErrorObject("false", "200", "working")
            api_response = ApiResponse(data["msg"], status)

        json_data = json.dumps(
            api_response.__dict__, default=lambda o: o.__dict__, indent=4
        )
        return json_data
    except Exception as e:
        traceback.print_exc()
        status = ErrorObject("true", "400", str(e))
        api_response = ApiResponse("", status)
        json_data = json.dumps(
            api_response.__dict__, default=lambda o: o.__dict__, indent=4
        )
        return json_data


@app.route("/evolutions", methods=["GET"])
def view_evolutions():
    try:
        request_data = request.get_json()
        data = evolution(request_data["name"])

        if data["error"] == "true":
            status = ErrorObject("true", "200", data["msg"])
            data = ""
            api_response = ApiResponse(data, status)
        else:
            status = ErrorObject("false", "200", "working")
            api_response = ApiResponse(data["msg"], status)
        json_data = json.dumps(
            api_response.__dict__, default=lambda o: o.__dict__, indent=4
        )
        return json_data
    except Exception as e:
        traceback.print_exc()
        status = ErrorObject("true", "400", str(e))
        api_response = ApiResponse("", status)
        json_data = json.dumps(
            api_response.__dict__, default=lambda o: o.__dict__, indent=4
        )
        return json_data


@app.route("/weaknesses")
def check_weaknesses():
    try:
        request_data = request.get_json()
        data = get_weaknesses(request_data["weaknesses"])

        if data["error"] == "true":
            status = ErrorObject("true", "200", data["msg"])
            data = ""
            api_response = ApiResponse(data, status)
        else:
            status = ErrorObject("false", "200", "working")
            api_response = ApiResponse(data["msg"], status)
        json_data = json.dumps(
            api_response.__dict__, default=lambda o: o.__dict__, indent=4
        )
        return json_data
    except Exception as e:
        traceback.print_exc()
        status = ErrorObject("true", "400", str(e))
        api_response = ApiResponse("", status)
        json_data = json.dumps(
            api_response.__dict__, default=lambda o: o.__dict__, indent=4
        )
        return json_data


@app.route("/types")
def view_types():
    try:
        request_data = request.get_json()
        data = get_types(request_data["type"])

        if data["error"] == "true":
            status = ErrorObject("true", "200", data["msg"])
            data = ""
            api_response = ApiResponse(data, status)
        else:
            status = ErrorObject("false", "200", "working")
            api_response = ApiResponse(data["msg"], status)
        json_data = json.dumps(
            api_response.__dict__, default=lambda o: o.__dict__, indent=4
        )
        return json_data
    except Exception as e:
        traceback.print_exc()
        status = ErrorObject("true", "400", str(e))
        api_response = ApiResponse("", status)
        json_data = json.dumps(
            api_response.__dict__, default=lambda o: o.__dict__, indent=4
        )
        return json_data


if __name__ == "__main__":
    app.run(debug=True)
