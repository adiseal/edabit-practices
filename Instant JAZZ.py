def jazzify(chords):
    jazzified_chords = []
    for chord in chords:
        if not chord.endswith('7'):
            jazzified_chords.append(chord + '7')
        else:
            jazzified_chords.append(chord)
    return jazzified_chords

print(jazzify(["G", "F", "C"])) # ["G7", "F7", "C7"]