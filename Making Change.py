def make_change(amount):
    coins = {'q': 0, 'd': 0, 'n': 0, 'p': 0}
    
    coins['q'] = amount // 25
    amount %= 25
    
    coins['d'] = amount // 10
    amount %= 10
    
    coins['n'] = amount // 5
    amount %= 5
    
    coins['p'] = amount
    
    return coins