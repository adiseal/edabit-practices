def profit(info):
    total_cost = info['cost_price'] * info['inventory']
    total_sales = info['sell_price'] * info['inventory']
    profit = total_sales - total_cost
    return round(profit)