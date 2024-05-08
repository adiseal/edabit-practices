def get_birthday_cake(name, age):
    char = "#" if age % 2 == 0 else "*"
    message = str(age) + " Happy Birthday " + name + "! " + str(age)
    cake = [char * (len(message) + 4),  
            char + " " + message + " " + char, 
            char * (len(message) + 4)]  
    return cake
