def like_or_dislike(lst):
    if not lst:
        return "Nothing"
    state = "Nothing"
    for action in lst:
        if action != state:
            state = action
        else:
            state = "Nothing"
    return state
