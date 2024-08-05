def make_plus_function(base_number):
    def add_to_base(new_number):
        return base_number + new_number
    return add_to_base