def number_to_words(n):
    # Dictionary to convert numbers to words
    num_words = {
        1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
        11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
        15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
        19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
        50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'
    }
    
    if n <= 20:
        return num_words[n]
    elif n < 100:
        return num_words[n // 10 * 10] + ('' if n % 10 == 0 else '-' + num_words[n % 10])
    else:
        return 'number too large'

def is_super_cool(s):
    if not s:
        return False
    
    def helper(n):
        word = number_to_words(n)
        if len(word) == n:
            return True
        return helper(len(word))
    
    return helper(len(s))

