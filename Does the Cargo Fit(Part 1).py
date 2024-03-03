def will_fit(holds, cargo):
    cargo_space = {"S": 50, "M": 100, "L": 200}    
    total_space = sum(cargo_space[hold] for hold in holds)    
    total_cargo = sum(cargo)    
    return total_cargo <= total_space