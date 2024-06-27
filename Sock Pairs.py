from collections import Counter

def sock_pairs(socks):
  sock_counts = Counter(socks)  
  return sum(count // 2 for count in sock_counts.values())