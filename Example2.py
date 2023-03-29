class Dog: 
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name 
        self.age = age

buddy = Dog("Buddy", 9)
miles = Dog("Miles", 4)

print (buddy.name, miles.name, buddy.age) 

buddy.age = 10 
print (buddy.age)

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"

miles = Dog("Miles", 4)
print(miles)
        