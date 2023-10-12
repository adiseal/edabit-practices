def transform_upvotes(upvotes):
    upvotes_list = upvotes.split()
    for i in range(len(upvotes_list)):
        if 'k' in upvotes_list[i]:
            upvotes_list[i] = float(upvotes_list[i].replace('k', '')) * 1000
        else:
            upvotes_list[i] = int(upvotes_list[i])
    return upvotes_list
