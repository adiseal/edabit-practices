def face_interval(lst):
    if not isinstance(lst, list):
        return ":/"
    else:
        interval = max(lst) - min(lst)
        if interval in lst:
            return ":)"
        else:
            return ":("