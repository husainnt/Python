# to append text to a file we need to pass the 'a' argument
filename='Python/Files and Exceptions/programming.txt'
with open (filename,'a') as f:
    f.write("I also love finding meaning in large datasets.\n")
    f.write("I love creating apps that can run in a browser.\n")