def fifty_thirty_twenty(ati):
    needs = 0.5 * ati
    wants = 0.3 * ati
    savings = 0.2 * ati
    return {"Needs": needs, "Wants": wants, "Savings": savings}



assert fifty_thirty_twenty(10000) == { "Needs": 5000, "Wants": 3000, "Savings": 2000 }

assert fifty_thirty_twenty(50000) == { "Needs": 25000, "Wants": 15000, "Savings": 10000 }

assert fifty_thirty_twenty(13450) == { "Needs": 6725, "Wants": 4035, "Savings": 2690 }

print(fifty_thirty_twenty(10000)) # { "Needs": 5000, "Wants": 3000, "Savings": 2000 }