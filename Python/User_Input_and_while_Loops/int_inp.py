# When you use the input() function, Python interprets everything the user enters as a string
age=input("Enter your age\n")
''' print(age>18), When you try to use the input to do a numerical comparison u, Python
produces an error because it can’t compare a string to an integer: the string
'21' that’s assigned to age can’t be compared to the numerical value 18 v.
We can resolve this issue by using the int() function, which tells
Python to treat the input as a numerical value. The int() function converts
a string representation of a number to a numerical representation.'''
age=int(age)
print(age>18)
hieght=input("How tall are you(in inches)?\n")
hieght=int(hieght)
if (hieght>62):
    print("You are tall enough to ride")
else:
    print("You'll be able to ride once you are a bit more taller!")
