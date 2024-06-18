class Animal:
    def speak():
        return "animal is speaking"
class Dog(Animal):
     def speak():
         return "dog is barking"
class Cat(Animal):
    def speak():
        return "meow meow"
animal=Animal
dog=Dog
cat=Cat
print(Animal.speak())
print(dog.speak())
print(cat.speak())
