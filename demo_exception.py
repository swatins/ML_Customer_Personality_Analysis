from flask import Flask
from src.logger.logs import logging
from src.exception.exception import AppException
import os, sys

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        raise Exception("We are testing our custom exception file")
    except Exception as e:
        customer = AppException(e, sys)
        logging.info(customer.error_message)
        logging.info("We are testing logging module")
        return "hello World"
    

try:
    pass
except Exception as e:
    raise AppException(e, sys)


if __name__=="__main__":
    app.run(debug=True)