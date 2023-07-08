class Pet:
    def __init__(self, name, age):
       self.name = name
       self.age = age

    def show(self):
       print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what i say")

class Cat(Pet):
    def speak(self):
        print("Meow")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p = Pet("tim",19)
p.show()
c = Cat("bill",34)
c.show()
c.speak()
d = Dog("jill",25)
d.show()
d.speak()
f = Fish("bubbles", 10)
f.speak()