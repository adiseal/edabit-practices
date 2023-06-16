def is_potential_friend(set1, set2):
    common_interests = set1.intersection(set2)
    if len(common_interests) >= 2 or common_interests == set1 == set2:
        return True
    return False
    
print(is_potential_friend(
  {"sports", "music", "chess"},
  {"coding", "music", "netflix", "chess"}
)) # True