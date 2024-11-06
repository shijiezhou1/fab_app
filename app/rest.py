from flask_appbuilder.api import ModelRestApi, expose
from flask_appbuilder import AppBuilder
from .models import ShoppingMall, Food
from flask_appbuilder.models.sqla.interface import SQLAInterface


class ShoppingMallModelApi(ModelRestApi):
    resource_name = 'shopping_mall'
    datamodel = SQLAInterface(ShoppingMall)
    allow_browser_login = True
    
    # Define the columns you want to include in the response
    list_columns = ['id', 'name', 'location', 'num_stores']
    show_columns = ['id', 'name', 'location', 'num_stores']
    
    @expose('/<pk>')
    def get(self, pk):
        shopping_mall = self.datamodel.get(pk)
        
        if shopping_mall:
            # Convert the shopping_mall object to a dictionary
            result = dict(zip(self.show_columns, self.datamodel.get_values_item(shopping_mall, self.show_columns)))
        
            # Ensure pk is an integer
            pk = int(pk)
            
            food_items = self.datamodel.session.query(Food).filter(Food.shopping_mall_id == pk).all()
            
            # Create a list of food item dictionaries
            result['food_items'] = [
                {'id': food.id, 'name': food.name, 'price': food.price}
                for food in food_items
            ]

            
            # Add the food_items to the shopping mall's __dict__
            return self.response(200, result=result)
        else:
            return self.response_404()
    
        
    

class FoodModelApi(ModelRestApi):
    resource_name = 'food'
    datamodel = SQLAInterface(Food)
    allow_browser_login = True
    related_field = ShoppingMall

def add_api_views(appbuilder: AppBuilder):
    appbuilder.add_api(ShoppingMallModelApi)
    appbuilder.add_api(FoodModelApi)
    
