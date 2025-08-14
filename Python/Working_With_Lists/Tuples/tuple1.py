#Tuples are the same as lists, except that they cant be modified such as Lists
#for defining tuples, we use ()
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
'''#let us try to modify the tuple
dimensions[0]=250
print(dimensions[0]) #->we get an error as tuple doesn't support assignment'''
for d in dimensions:
    print(d)
# we can assign new values to tuple unlike as we cant modify it
dimensions=(400,50)
print(dimensions)