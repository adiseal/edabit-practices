def sort_drinks_by_price(drinks):
    return sorted(drinks, key=lambda x: x['price'])

drinks = [
  {"name": "lemonade", "price": 50},
  {"name": "lime", "price": 10}
]