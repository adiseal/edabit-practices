def common_elements(list1, list2):
    i, j = 0, 0
    common = []
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            if not common or common[-1] != list1[i]:  
                common.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return common
