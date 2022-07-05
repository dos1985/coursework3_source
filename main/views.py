import logging
from flask import Blueprint, render_template, request, jsonify
import utills

main_blueprint = Blueprint('main_blueprint', __name__)

api_logger = logging.getLogger("api_logger")


@main_blueprint.route("/")
def page_index():
    posts = utills.load_posts()
    api_logger.debug(f"Загрузка постов")
    return render_template('index.html', posts=posts)


@main_blueprint.route("/post/<int:id>")
def view_posts(id):
    post = utills.get_post(id)
    api_logger.info(f"Запрос /api/posts/'{id}'")
    comments = utills.get_comments(id)
    return render_template('post.html', post=post, comments=comments)


@main_blueprint.route("/post_by_name/<string:name>")
def view_posts_by_name(name):
    posts = utills.load_posts_by_name(name)
    api_logger.info(f"Запрос /api/post_by_name/'{name}'")
    return render_template('index.html', posts=posts)


@main_blueprint.route("/search/")
def page_post_search():
    text = request.values.get("s", "")
    text = str(text)
    if text == "":
        posts = []
    else:
        posts = utills.load_posts_by_text(text)
        api_logger.info(f"Выполняется поиск '{text}'")
    return render_template('search.html',
                           posts=posts,
                           text=text,
                           posts_len=len(posts)
                           )
