import json
from json import JSONDecodeError

file_name = 'data/data.json'


def load_date(file_name):
    """Загружает данные из файла"""
    try:
     with open(file=file_name, mode='r', encoding='utf-8') as file:
        data = json.load(file)
    except(FileNotFoundError, JSONDecodeError):
        raise BadDataSource("JSON поврежден")
    return data


def load_posts():
    """ Отдаем список постов"""
    posts = load_date('data/data.json')
    for post in posts:
        post['short'] = post['content'][0:10]
    return posts


def get_post(id):
    """Отдаем пост по id"""
    posts = load_posts()
    for post in posts:
        if post["pk"] == id:
            return post


def load_posts_by_name(name):
    """Отдаем пост по имени"""
    posts = load_posts()
    return [post for post in posts if post["poster_name"] == name]


def get_comments(id):
    """Отдаем комментарий к посту"""
    comments = load_date('data/comments.json')
    comments_post = []
    for comment in comments:
        if comment["post_id"] == id:
            comments_post.append(comment)
    return comments_post


def load_posts_by_text(text):
    """"Отдаем пост по слову в посте"""

    return [post for post in load_posts() if text.lower() in post["content"].lower()]

# pp(load_posts_by_text("еда"))
