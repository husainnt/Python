# default values in function
# we can define a fixed default value for a functions parameter so that the user needs to input parameter for the undefined parameter
def animal_func(pet_name,animal_type='dog'):
    print(f"I have a animal:{animal_type}")
    print(f"My {animal_type}s name is: {pet_name}")
# calling the funciton
animal_func(pet_name='Jack')
'''8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.'''
#using positional arg
def make_shirt(size,text_on_shirt):
    print(f"the shirt size:{size} says the following:{text_on_shirt}")
make_shirt('Large','Kaggle')
#using keyword arg
def make_shirt(size,text_on_shirt):
    print(f"the shirt size:{size} says the following:{text_on_shirt}")
make_shirt(size='Large',text_on_shirt='Kaggle')
'''Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country.'''
def describe_city(city,country='Iceland'):
    print(f"{city} is in {country}")
describe_city(city='Reykjavík')
describe_city(city='Kópavogur')
describe_city(city='London')

