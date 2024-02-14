def get_drink_ID(flavor, capacity):
    words = flavor.split()
    id_parts = [word[:3].upper() for word in words]
    id_parts.append(capacity[:-2])  
    return "".join(id_parts)
