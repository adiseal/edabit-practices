def can_play(hand, face):
    face_color, face_number = face.split(' ')
    
    for card in hand:
        card_color, card_number = card.split(' ')
        
        if card_color == face_color or card_number == face_number:
            return True
    
    return False