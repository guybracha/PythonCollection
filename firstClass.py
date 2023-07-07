#define class
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def add_one(self, x):
        return x + 2.5

    def bark(self):
        print("woof")

# d variable
d1 = Dog("Guy", 25)
d1.bark()
print(d1.name)
print(d1.age)
print(d1.add_one(7.5))
print(type(d1))