def space_me_out(s):
    return s.replace("", " ")[1: -1]


assert space_me_out("space") == "s p a c e"

assert space_me_out("far out") == "f a r   o u t"

assert space_me_out("elongated musk") == "e l o n g a t e d   m u s k"	