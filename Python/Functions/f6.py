# passing an arbitrary number of arguments
'''The asterisk in the parameter name *toppings tells Python to make an
empty tuple called toppings and pack whatever values it receives into this
tuple.'''
def make_pizza(*toppings): # now here i can multiple arguments
    for t in toppings:
        print(t)
make_pizza('arabic ranch','bbq','fajita')
# a fixed argument and arbitrary no of args
def pizza(size,*toppings):
    for t in toppings:
        print(f"Your {size} {t} pizza is ready!")
pizza('Large','Ranch','BBQ')

