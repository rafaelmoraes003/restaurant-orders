class TrackOrders:
    def __init__(self):
        self.orders = []
        self.days = {}

    def __len__(self):
        return len(self.orders)

    def get_orders_by_customer(self, customer):
        customer_orders = {}

        for order in self.orders:
            if order["customer"] == customer:
                if order["order"] not in customer_orders:
                    customer_orders[order["order"]] = 1
                else:
                    customer_orders[order["order"]] += 1

        return customer_orders

    def add_new_order(self, customer, order, day):
        self.orders.append({
            "customer": customer,
            "order": order,
            "day": day
        })

        if day not in self.days:
            self.days[day] = 1
        else:
            self.days[day] += 1

    def get_most_ordered_dish_per_customer(self, customer):
        pass

    def get_never_ordered_per_customer(self, customer):
        pass

    def get_days_never_visited_per_customer(self, customer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
