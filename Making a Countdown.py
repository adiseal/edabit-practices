def countdown(n, txt):
    countdown_numbers = [str(i) for i in range(n, 0, -1)]    
    countdown_string = '. '.join(countdown_numbers) + '. '
    countdown_string += txt.upper() + '!'
    return countdown_string
