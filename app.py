from flask import Flask, request, jsonify
from flask_cors import CORS
from controllers.main_controller import MainController

CONTROLLER = MainController()


app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    copito_miau = "Edgar's API Test backend"
    return "<H1>" + copito_miau + "</H1>"


@app.route("/search", methods=['POST'])
def search():
    if request.method == 'POST':
        data = request.json
        res = CONTROLLER.search(data)
        return res


if __name__ == "__main__":
    app.run(threaded=True, port=5000, debug=True)
