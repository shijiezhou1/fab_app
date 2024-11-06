from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi
from .models import Food, ShoppingMall
# from . import appbuilder, db

"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""

class FoodModelView(ModelView):
    datamodel = SQLAInterface(Food)
    list_columns = ['name', 'cuisine', 'price', 'shopping_mall']
    add_columns = ['name', 'cuisine', 'price', 'shopping_mall']
    edit_columns = ['name', 'cuisine', 'price', 'shopping_mall']

class ShoppingMallModelView(ModelView):
    datamodel = SQLAInterface(ShoppingMall)
    related_views = [FoodModelView]
    list_columns = ['name', 'location', 'num_stores']
    add_columns = ['name', 'location', 'num_stores']
    edit_columns = ['name', 'location', 'num_stores']


# @appbuilder.app.errorhandler(404)
# def page_not_found(e):
#     return (
#         render_template(
#             "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
#         ),
#         404,
#     )


# db.create_all()
