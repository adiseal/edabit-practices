def count_smileys(lst):
    eyes = [":", ";"]
    noses = ["-", "~"]
    mouths = [")", "D"]
    
    count = 0
    
    for face in lst:
        if len(face) == 2:
            if face[0] in eyes and face[1] in mouths:
                count += 1
        elif len(face) == 3:
            if face[0] in eyes and face[1] in noses and face[2] in mouths:
                count += 1
    
    return count