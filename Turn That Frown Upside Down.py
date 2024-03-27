def make_happy(sentence):
    sad_faces = [":(", "8(", "x(", ";("]
    happy_faces = [":)", "8)", "x)", ";)"]    
    for sad, happy in zip(sad_faces, happy_faces):
        sentence = sentence.replace(sad, happy)        
    return sentence