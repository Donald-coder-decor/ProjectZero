from flask import Flask, jsonify
from controller import first_page_controller as fc


app = Flask(__name__)

fc.route(app)

if __name__ == '__main__':
    app.run(debug=True)
