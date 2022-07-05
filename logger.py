import logging


def create_logger():
    api_logger = logging.getLogger("api_logger")
    api_logger.setLevel(logging.DEBUG)

    api_logger_hendler = logging.FileHandler("logs.log")
    api_logger_hendler.setLevel(logging.DEBUG)
    api_logger.addHandler(api_logger_hendler)
    formatter_basic = logging.Formatter(" %(asctime)s :%(levelname)s : %(message)s")
    api_logger_hendler.setFormatter(formatter_basic)

    #return api_logger_hendler
