from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# I could have stubbed out the "parent" budget blueprint and added
# the budget item as a child.

from blueprints.budget_item import routes as budget_item
app.register_blueprint(budget_item.budget_item_bp, url_prefix="/budget")
