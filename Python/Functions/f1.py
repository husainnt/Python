# sample greet fucniton
def greet():
    print("Hello")
greet()

# passing information to a function
def greet_user(username):
    print(f"Hello, {username.title()}!")
greet_user('amanda')

# Arguments and parameters in function
'''Write a function called favorite_book() that accepts one parameter, title.'''
def favorite_book(title):
    print(f"My favorite book is {title}")
favorite_book('Atomic habits')

# Multiple arguments in a funciton
def car(name,engine):
    print(f"My favorite car is {name}, it comes with a {engine}")
car('McLaren F1','6.1l V12 engine')
  
# key word type: used to define paramenter to avoid positional arguments errors
def Pet(animal_type,pet_name):
    print(f"I have a {animal_type}")
    print(f"I call my {animal_type} {pet_name} ")
Pet(animal_type='cat',pet_name='milo')
