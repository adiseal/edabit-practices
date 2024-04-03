class Person:
    def __init__(self, name, likes, hates):
        self.name = name
        self.likes = likes
        self.hates = hates

    def taste(self, food):
        if food in self.likes:
            return "%s eats the %s and loves it!" % (self.name, food)
        elif food in self.hates:
            return "%s eats the %s and hates it!" % (self.name, food)
        else:
            return "%s eats the %s!" % (self.name, food)