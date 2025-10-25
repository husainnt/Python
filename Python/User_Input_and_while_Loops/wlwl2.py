# Removing All Instances of Specific Values from a List
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
# remove the value 'cat' from everywhere in the list
while 'cat' in pets:
    pets.remove('cat')
print(pets)