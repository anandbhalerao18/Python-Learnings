# single inheritance in python
class Animals:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("sound made by the animal")

class dog(Animals):
    def __init__(self, name, breed):
        Animals.__init__(self, name, species="dog")
        self.breed = breed
    def make_sound(self):
        print("bark")


d = dog("dog", "doggerman")
d.make_sound()

a = Animals("dog", "dog")
a.make_sound()