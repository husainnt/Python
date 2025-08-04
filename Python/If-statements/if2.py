# performing equality checks
cars = 'bmw'
print(cars == 'bmw')  # check, which returns True
car2 = 'audi'
print(car2 == 'bmw')  # returns False
# Testing for equality is case sensitive in Python. 
# For example, two values with different capitalization are not considered equal
car3 = 'pagani'
print(car3 == 'Pagani')  # returns False
# If case doesn’t matter and instead you just want to test the value of a variable, 
# you can convert the variable’s value to lowercase before doing the comparison 
car4 = 'Honda'
print(car4.lower() == 'honda')  # returns True
# != -> not equal
requested_topping='mushrooms'
if requested_topping!='olives':
    print('Hold the olives!')