def worm_length(worm):
    if not worm or any(c != '-' for c in worm):
        return "invalid"
    else:
        return "%d mm." % (len(worm) * 10)

print(worm_length("----------")) # "100 mm."
print(worm_length("")) # "invalid"
print(worm_length("---_-___---_")) # "invalid"