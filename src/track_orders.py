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
        customer_orders = self.get_orders_by_customer(customer)

        most_ordered = None
        most_ordered_times = 0

        for order in customer_orders:
            if customer_orders[order] > most_ordered_times:
                most_ordered_times = customer_orders[order]
                most_ordered = order

        return most_ordered

    def get_never_ordered_per_customer(self, customer):
        all_orders, customer_orders = set(), set()

        for order in self.orders:
            if order["customer"] == customer:
                customer_orders.add(order["order"])
            all_orders.add(order["order"])

        return all_orders.difference(customer_orders)

    def get_days_never_visited_per_customer(self, customer):
        all_days, customer_days = set(), set()

        for order in self.orders:
            if order["customer"] == customer:
                customer_days.add(order["day"])
            all_days.add(order["day"])

        return all_days.difference(customer_days)

    def get_busiest_day(self):
        busiest_day = None
        busiest_day_times = 0

        for day in self.days:
            if self.days[day] > busiest_day_times:
                busiest_day_times = self.days[day]
                busiest_day = day

        return busiest_day

    def get_least_busy_day(self):
        least_busy_day = None
        least_busy_day_times = 0

        for day in self.days:
            least_busy_day_times = self.days[day]
            break

        for day in self.days:
            if self.days[day] <= least_busy_day_times:
                least_busy_day_times = self.days[day]
                least_busy_day = day

        return least_busy_day


if __name__ == "__main__":

    csv_parsed = [
        ["maria", "pizza", "ter??a-feira"],
        ["maria", "hamburguer", "ter??a-feira"],
        ["joao", "hamburguer", "ter??a-feira"],
        ["maria", "coxinha", "segunda-feira"],
        ["arnaldo", "misto-quente", "ter??a-feira"],
        ["jose", "hamburguer", "sabado"],
        ["maria", "hamburguer", "ter??a-feira"],
        ["maria", "hamburguer", "ter??a-feira"],
        ["joao", "hamburguer", "ter??a-feira"],
    ]

    track_orders = TrackOrders()

    for name, food, day in csv_parsed:
        track_orders.add_new_order(name, food, day)

    print(track_orders.get_most_ordered_dish_per_customer("maria"))
    print(track_orders.get_never_ordered_per_customer("arnaldo"))
    print(track_orders.get_days_never_visited_per_customer("joao"))
    print(track_orders.get_busiest_day())
    print(track_orders.get_least_busy_day())
