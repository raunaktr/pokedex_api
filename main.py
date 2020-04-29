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
from app.routes import routes  # routes

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})


@app.route("/")
def home():
    return "welcome to pokedex"


# add_url_rule imports routes from app>>routes>>routes.py
app.add_url_rule("/name", view_func=routes.view_pokemon)
app.add_url_rule("/evolutions", view_func=routes.view_evolutions)
app.add_url_rule("/weaknesses", view_func=routes.check_weaknesses)
app.add_url_rule("/types", view_func=routes.view_types)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
