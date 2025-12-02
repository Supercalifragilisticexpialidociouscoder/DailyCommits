class mother:
    def mother_qualities(self):
        print("Caring and Loving")
class father:
    def father_qualities(self):
        print("Protective and Responsible")
class child(mother, father):
    def child_qualities(self):
        print("Playful and Curious")
c = child()
c.mother_qualities()
c.father_qualities()
c.child_qualities()

class animal:
    def sound(self):
        print("Animal makes a sound")
class dog(animal):
    def sound(self):
        print("Dog barks")
class baby_dog(dog):
    def sound(self):
        print("Baby dog yaps")
b = baby_dog()
b.sound()

class father:
    def property(self):
        print("House and Car")
class child1(father):
    def job(self):
        print("child1 is a doctor")
class child2(father):
    def buisness(self):
        print("child2 owns a buisness")
c1 = child1()
c1.property()
c1.job()
c2 = child2()
c2.property()
c2.buisness()   