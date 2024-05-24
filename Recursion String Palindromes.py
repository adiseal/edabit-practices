def is_palindrome(text):
  if len(text) <= 1:
    return True
  return text[0] == text[-1] and is_palindrome(text[1:-1])