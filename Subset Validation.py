def validate_subsets(subsets, main_set):
    main_set = set(main_set)
    for subset in subsets:
        if not set(subset).issubset(main_set):
            return False
    return True
