import logging
from flask import Blueprint, jsonify
import utills

blueprint_api = Blueprint("api", __name__, url_prefix='/api')

api_logger = logging.getLogger("api_logger")


@blueprint_api.route("/posts/")
def api_posts():
    posts = utills.load_posts()
    api_logger.info("Загрузка постов/api/post")
    return jsonify(posts)


@blueprint_api.route("/posts/<int:id>")
def api_post(id):
    post = utills.get_post(id)
    api_logger.info(f"Загрузка постов /api/post'{id}'")
    return jsonify(post)
