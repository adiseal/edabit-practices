def percentage_changed(old, new):
    old_price = int(old.replace("$", ""))
    new_price = int(new.replace("$", ""))
    if new_price < old_price:
        decrease = ((old_price - new_price) / float(old_price)) * 100
        return "{}% decrease".format(round(decrease))
    else:
        increase = ((new_price - old_price) / float(old_price)) * 100
        return "{}% increase".format(round(increase))
