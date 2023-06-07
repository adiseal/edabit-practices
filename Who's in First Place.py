def first_place(road):
    print(road)
    count = 1
    try:
        while road[-count] == "=":
            count += 1
        return road[-count]
    except:
        return None
        
print(first_place("====b===O===e===U=A==")) # "A"