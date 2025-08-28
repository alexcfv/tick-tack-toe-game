from flask import request, Blueprint, jsonify
from flask_login import login_required

#пока что не знаю как реализовать логику взаимодействия игры с сервером, нужен fast_api

game_blueprint = Blueprint("game", __name__)

@game_blueprint.route("/game", methods=["POST"])
@login_required
async def game():
    return jsonify(""), 200