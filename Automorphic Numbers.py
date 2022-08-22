def is_automorphic(n):
    if str(n ** 2).endswith(str(n)):
        return True
    return False