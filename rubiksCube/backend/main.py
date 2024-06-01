from flask import Flask
from controllers import controllers
from endpoints import endpoints
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.register_blueprint(endpoints)
app.register_blueprint(controllers)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
