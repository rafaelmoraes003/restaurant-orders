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
            ingredient: 0
            for ingredient
            in self.MINIMUM_INVENTORY.keys()
        }

    def add_new_order(self, customer, order, day):
        # É garantido que os pedidos da semana
        # não irão zerar nenhum dos estoques.

        for ingredient in self.INGREDIENTS[order]:
            self.inventory[ingredient] += 1

        self.track_orders.add_new_order(customer, order, day)

    def get_quantities_to_buy(self):
        return self.inventory
