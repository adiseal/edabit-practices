def chatroom_status(users):
    if len(users) == 0:
        return "no one online"
    elif len(users) == 1:
        return users[0] + " online"
    elif len(users) == 2:
        return users[0] + " and " + users[1] + " online"
    else:
        var = len(users) - 2
        var_2 = users[0] + ", " + users[1] + " and " + str(var) + " more online"
        # print(var_2)
        return var_2
