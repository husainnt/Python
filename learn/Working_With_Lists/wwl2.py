#list of numbers
#range(a,b) allows to genreate numbers from a to b in range, excluding b
for n in range(1,10):
    print(n) #prints numbers from 1-9

#list of numbers, var=list(range(a,b)) creates a list of number
nl=list(range(1,5))
print(nl)

#3rd argumnet in range(a,b,c), the argument 'c' acts as a step size for each iteration between a and b
even_numbers=list(range(2,11,2)) #generates a list of even numbers from 2-11, with step size 2
print(even_numbers)
# in python, '**' represent exponent
#creating a list with squares of numbers from 1-10
squares=[]
for s in range(1,11):
    squares.append(s**2)
print(squares)

#max,min and sum function
digits=list(range(1,9))
print(sum(digits))
print(min(digits))
print(max(digits))

#list comprehension,combines for loop and creation of new elements into one line,var=[logic for var_name in range(a,b)]
#using list comprehension to generate squares
sqrs=[s**2 for s in range(1,11)] #list comprehension
print(sqrs)