def zip_it(women, men):
    if len(women) != len(men):
        return "sizes don't match"
    return list(tuple(zip(women, men)))


assert zip_it(["Elise", "Mary"], ["John", "Rick"]) == [("Elise", "John"), ("Mary", "Rick")]

assert zip_it(["Ana", "Amy", "Lisa"], ["Bob", "Josh"]) == "sizes don't match"

assert zip_it(["Ana", "Amy", "Lisa"], ["Bob", "Josh", "Tim"]) == [("Ana", "Bob"), ("Amy", "Josh"), ("Lisa", "Tim")]