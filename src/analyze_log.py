from csv import reader


def get_maria_orders(maria_orders, order):
    if order not in maria_orders:
        maria_orders[order] = 1
    else:
        maria_orders[order] += 1


def get_joao_days_and_orders(order, joao_orders, day, joao_days):
    joao_orders.add(order)
    if day != "domingo":
        joao_days.add(day)


def format_data_from_csv(
    maria_orders,
    arnaldo_hamburguers,
    orders_joao_never_ordered,
    days_joao_never_was
):
    maria_most_ordered = None
    maria_most_ordered_times = 0

    for order in maria_orders:
        if maria_orders[order] > maria_most_ordered_times:
            maria_most_ordered = order
            maria_most_ordered_times = maria_orders[order]

    with open("data/mkt_campaign.txt", mode="w") as file:
        file.writelines(f"{maria_most_ordered}\n")
        file.writelines(f"{str(arnaldo_hamburguers)}\n")
        file.writelines(f"{str(orders_joao_never_ordered)}\n")
        file.writelines(f"{str(days_joao_never_was)}")
        file.close()


def get_data_from_csv_list(csv_list):
    maria_orders = {}
    arnaldo_hamburguers = 0
    orders, joao_orders, days, joao_days = set(), set(), set(), set()

    for customer, order, day in csv_list:
        if customer == "maria":
            get_maria_orders(maria_orders, order)

        if customer == "arnaldo" and order == "hamburguer":
            arnaldo_hamburguers += 1

        if customer == "joao":
            get_joao_days_and_orders(order, joao_orders, day, joao_days)

        days.add(day) if day != "domingo" else None
        orders.add(order)

    format_data_from_csv(
        maria_orders,
        arnaldo_hamburguers,
        orders.difference(joao_orders),
        days.difference(joao_days)
    )


def analyze_log(path_to_file):
    extension = path_to_file.split(".")[1]

    if extension != "csv":
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file, mode="r") as file:
            content = reader(file)
            content_list = list(content)
        get_data_from_csv_list(content_list)
        return
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


if __name__ == "__main__":
    analyze_log("data/orders_1.csv")

    with open("data/mkt_campaign.txt", mode="r") as file:
        content = file.read()
        print(content)