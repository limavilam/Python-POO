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
    
miles = Dog("Miles", 4)

miles.description()
'Miles is 4 years old'

miles.speak("Woof Woof")
'Miles says Woof Woof'

miles.speak("Bow Wow")
'Miles says Bow Wow'