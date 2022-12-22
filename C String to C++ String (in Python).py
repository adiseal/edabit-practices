def cpp_txt(lst):
    lst = lst[:-1]
    return ''.join(lst)


assert cpp_txt(["H", "i", "!", "\0"]) == "Hi!"

assert cpp_txt(["H", "e", "l", "l", "o", "!", "\0"]) == "Hello!"

assert cpp_txt(["J", "A", "V", "a", "\0"]) == "JAVa"