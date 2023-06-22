def simple_encoder(str):
    encoded_str = ""
    str = str.lower()  # Convert the string to lowercase to treat upper and lowercase characters equally
    for char in str:
        if str.count(char) == 1:
            encoded_str += "["
        else:
            encoded_str += "]"
    return encoded_str
    
print(simple_encoder("Mubashir")) # "[[[[[[[["