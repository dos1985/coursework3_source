import logging
from flask import Flask

app = Flask(__name__)

# Create a logger object
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a handler to log messages to a file
handler = logging.FileHandler('app.log')
handler.setLevel(logging.DEBUG)

# Create a formatter for the log messages
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

# Example endpoint to demonstrate logging
@app.route("/")
def index():
    logger.debug("A debug message")
    logger.info("An info message")
    logger.warning("A warning message")
    logger.error("An error message")
    logger.critical("A critical message")
    return "Log messages have been created in the app.log file."
