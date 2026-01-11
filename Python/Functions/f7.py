# Soring functions
'''By using descriptive names for your functions, your
main program will be much easier to follow. You can go a step further by
storing your functions in a separate file called a module and then importing
that module into your main program. An import statement tells Python to
make the code in a module available in the currently running program file.'''
# importing an entire module
# to import a module creating a file pizza.
# importing our module and calling function
import pizza
pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# importing specific functions
# from module_name import function_name
# importing several functions
# from module_name import function_0, function_1, function_2

# Using 'as' to Give a Function an Alias
'''If the name of a function you’re importing might conflict with an existing
name in your program or if the function name is long, you can use a
short, unique alias—an alternate name similar to a nickname for the function.'''
# from module_name import function_name as fn
from pizza import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using as to Give a Module an Alias
'''You can also provide an alias for a module name'''
import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Importing All Functions in a Module
'''You can tell Python to import every function in a module by using the asterisk (*) operator'''
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')