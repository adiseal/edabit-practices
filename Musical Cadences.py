def find_cadence(chord_progression):
    last_chords = chord_progression[-2:]  
    last_chord1, last_chord2 = last_chords

    if last_chord1 == "V" and last_chord2 == "I":
        return "perfect"
    elif last_chord1 == "IV" and last_chord2 == "I":
        return "plagal"
    elif last_chord1 == "V" and last_chord2 != "I":
        return "interrupted"
    elif last_chord1 != "I" and last_chord2 == "V":
        return "imperfect"
    else:
        return "no cadence"