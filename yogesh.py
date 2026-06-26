#File created by Yogesh -- 26-06-2026

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "No common language"

    @staticmethod
    def category():
        return "Living Being"


class Dog(Animal):
    def speak(self):        
        return f"{self.name} barks..."


a = Animal("Common")
d = Dog("Moti")

print(a.speak())                  
print(d.speak())         