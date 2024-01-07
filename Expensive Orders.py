def expensive_orders(orders, cost):
    return {key: value for key, value in orders.items() if value > cost}
