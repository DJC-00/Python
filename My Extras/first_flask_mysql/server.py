from flask_app import app
from flask_app.controllers import friendController
from flask_app.controllers import factionController

if __name__ == "__main__":
    app.run(debug=True)