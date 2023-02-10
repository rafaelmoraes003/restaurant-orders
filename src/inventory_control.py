from src.track_orders import TrackOrders


class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.track_orders = TrackOrders()
        self.inventory = {
            ingredient: 0 for ingredient in self.MINIMUM_INVENTORY.keys()
        }
        self.available_dishes = set(self.INGREDIENTS.keys())

    def delete_dishes_that_contain_ingredient(self, ingredient):
        for dish in self.INGREDIENTS:
            if ingredient in self.INGREDIENTS[dish]:
                self.available_dishes.discard(dish)

    def add_new_order(self, customer, order, day):
        for ingredient in self.INGREDIENTS[order]:
            if self.inventory[ingredient] < self.MINIMUM_INVENTORY[ingredient]:
                self.inventory[ingredient] += 1
                if self.inventory[ingredient] >= self.MINIMUM_INVENTORY[
                    ingredient
                ]:
                    self.delete_dishes_that_contain_ingredient(ingredient)
            else:
                return False

        self.track_orders.add_new_order(customer, order, day)

    def get_quantities_to_buy(self):
        return self.inventory

    def get_available_dishes(self):
        return self.available_dishes
