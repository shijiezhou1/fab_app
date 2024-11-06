import logging

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA
from .views import FoodModelView, ShoppingMallModelView
from .rest import add_api_views

"""
 Logging configuration
"""

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object("config")
db = SQLA(app)
appbuilder = AppBuilder(app, db.session)

appbuilder.add_view(FoodModelView, "Foods", icon="fa-cutlery", category="Dining")
appbuilder.add_view(ShoppingMallModelView, "Shopping Malls", icon="fa-shopping-bag", category="Shopping")

add_api_views(appbuilder)


"""
from sqlalchemy.engine import Engine
from sqlalchemy import event

#Only include this for SQLLite constraints
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # Will force sqllite contraint foreign keys
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""

from . import views
