    # from flask import Flask
    # app = Flask(__name__)

    # @app.route("/")
    # def hello():
    #     return "Hello World!"

    # if __name__ == "__main__":
    #     app.run(host='0.0.0.0')


import logging
from flask import Flask
from flask import json
from werkzeug.wrappers import response
app = Flask(__name__)

@app.route('/status')
def status():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
    app.logger.info("Status request was successful")

    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )
    app.logger.info("Metrics request was successful")
    return response
    
@app.route("/")
def hello():
    app.logger.info("Home request was successful")
    return "Hello World!"

if __name__ == "__main__":
    #stream all log to a file
    logging.basicConfig(filename="app.log",level=logging.DEBUG)
    app.run(host='0.0.0.0')
