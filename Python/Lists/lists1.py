#like arrays in c++, pyhton has lists
cars=['honda', 'toyota', 'nissan']
print(cars) #prints the all elements in the list 'cars'
#accessing individual elements
print(cars[0])
#to capitalise a elements inital add.title()
print(cars[1].title())
# to access the last element just give the index -1, 2nd last index -2 etc
print(cars[-1])
#inserting elements into a list,listname.insert(pos,data)
cars.insert(0,"mercedes")
print(cars)
#deleting a element from a list using del
del cars[2] #toyota gets deleted
print(cars)
#deleting by pop method
del_item=cars.pop(1)
print(cars)