from flask import Flask
from config import Config
from api.api import blueprint_api
from logger import create_logger
from main.views import main_blueprint


def create_app(name):
    app = Flask(name)
    app.config.from_object(Config)
    return app


app = create_app(__name__)
api_logger = create_logger()

#app = Flask(__name__)
#app.config["JSON_AS_ASCII"] = False


@app.errorhandler(404)
def page_not_found(e):
    return "Страница не найдена"


@app.errorhandler(500)
def server_error(e):
    return "Ошибка сервера"


app.register_blueprint(main_blueprint)
app.register_blueprint(blueprint_api)

if __name__ == "__main__":
    app.run(debug=True)
