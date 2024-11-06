from flask_appbuilder import Model
from sqlalchemy.orm import relationship

from sqlalchemy import Column, Integer, String, Float, ForeignKey

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""


class Food(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    cuisine = Column(String(50))
    price = Column(Float)
    shopping_mall_id = Column(Integer, ForeignKey('shopping_mall.id'))
    shopping_mall = relationship("ShoppingMall")

    def __repr__(self):
        return self.name

class ShoppingMall(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    location = Column(String(200))
    num_stores = Column(Integer)

    def __repr__(self):
        return self.name