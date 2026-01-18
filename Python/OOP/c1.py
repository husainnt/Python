# Generating and using a class
class Dog:
    '''A attmept to model a dog'''
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sit(self):
        print(f"{self.name} is now sitting")
    
    def roll_over(self):
        print(f"{self.name} rolled over!")
'''The __init__() Method
A function that’s part of a class is a method. Everything you learned about
functions applies to methods as well; the only practical difference for now is
the way we’ll call methods.'''
# Making an Instance from a Class
my_dog=Dog('Willie',6)
print(f"My Dogs name is {my_dog.name}")
print(f"My Dogs age is {my_dog.age}")
# Calling methods
my_dog.sit()
my_dog.roll_over()
# Creating multiple instances
your_dog=Dog('Lucy',3)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()