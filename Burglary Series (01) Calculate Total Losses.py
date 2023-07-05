def calculate_losses(stolen_items):
    if not stolen_items:
        return "Lucky you!"
    else:
        total_loss = sum(stolen_items.values())
        return total_loss

print(calculate_losses({
  "painting" : 20000,
})) # 20000