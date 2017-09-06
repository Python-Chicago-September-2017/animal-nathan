class Animal(object):
    def __init__(self,name,health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print "Health: " + str(self.health)

bunny = Animal("Bunny",50)
print "Bunny:"
bunny.walk().walk().walk().run().run().display_health()

class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__("Dog",150)
    def pet(self):
        self.health += 5
        return self

dog = Dog()
print "Dog:"
dog.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
    def __init__(self):
        super(Dragon, self).__init__("Dragon",170)
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        super(Dragon, self).display_health()
        print "I am a Dragon"

dragon = Dragon()
print "Dragon:"
dragon.walk().run().fly().display_health()