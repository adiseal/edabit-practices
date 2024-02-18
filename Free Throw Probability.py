def free_throws(success_rate, num_throws):
    success_rate_decimal = int(success_rate.strip('%')) / 100
    probability = (success_rate_decimal ** num_throws) * 100
    rounded_probability = str(round(probability)) + '%'
    return rounded_probability