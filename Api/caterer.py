class Caterer(object):
    """docstring for Caterer"""
    caterer = [{'username' : 'admin', 'password' : 'admin', 'cater_id' : 1234, 'admin' : True}]
    meal_list = [{"meal_id":1, "meal_name": "Rice", "price":200, "category":"dinner", "day":"Monday"}]
    menu_list = [{"meal_id":1, "meal_name": "Rice", "price":200, "category":"dinner", "day":"Monday"}]
    order_list = [{"meal_id":1, "meal_name": "Rice", "price":200, "category":"dinner", "day":"Monday", "quantity":1, "username":"user"}]
    def __init__(self):
        self.output = {}

    def post_meal(self, meal_id, meal_name, price, category, day):
        if meal_id == '' or meal_name == '' or price == '' or category == '' or day == '':
            return 'Please enter all the details'

        #Should validate the input data types

        mea = [meal for meal in Caterer().meal_list if meal["meal_id"] == meal_id and meal['meal_name'] == meal_name]
        if mea:
            return 'Meal exists!'

        self.output['meal_id'] = meal_id
        self.output['meal_name'] = meal_name
        self.output['price'] = price
        self.output['category'] = category
        self.output['day'] = day
        self.output['menu'] = False
        Caterer.meal_list.append(self.output)
        return 'Meal successfully created'

    def get_meals(self):
        return Caterer().meal_list

    def modify_meal(self, meal_id, meal_name, price, category, day):
        mea = [meal for meal in Caterer().meal_list if meal["meal_id"] == meal_id]
        modify = mea[0]

        if not mea:
            return 'Meal unavailable!'

        modify['meal_name'] = meal_name
        modify['price'] = price
        modify['category'] = category
        modify['day'] = day
        return 'Meal modification successful'

    def delete_ml(self, meal_id):
        mea = [meal for meal in Caterer().meal_list if meal["meal_id"] == meal_id]

        if not mea:
            return 'Meal unavailable!'

        Caterer.meal_list.remove(mea[0])
        return 'Meal Deleted successfully'

    def post_menu(self, meal_id, meal_name, price, category, day):
        if meal_id == '' or meal_name == '' or price == '' or category == '' or day == '':
            return 'Please enter all the details'

        #Should validate the input data types
        menus = [menu for menu in Caterer().menu_list if menu["meal_id"] == meal_id and menu['meal_name'] == meal_name]
        if menus:
            return 'Meal exists in menu!'

        self.output['meal_id'] = meal_id
        self.output['meal_name'] = meal_name
        self.output['price'] = price
        self.output['category'] = category
        self.output['day'] = day
        Caterer.menu_list.append(self.output)
        return 'Meal successfully added to menu'

    def get_orders(self):
        return self.order_list