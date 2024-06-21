def intersection(dict1, dict2):
    common_keys = set(dict1.keys()).intersection(dict2.keys())
    
    dict1_filtered = {key: dict1[key] for key in common_keys}
    dict2_filtered = {key: dict2[key] for key in common_keys}
    
    return [dict1_filtered, dict2_filtered]