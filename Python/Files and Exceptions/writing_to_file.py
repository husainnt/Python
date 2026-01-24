# To write text to a file, you need to call open() with a second argument telling Python that you want to write to the file.

# You can open a file in read mode ('r'), write mode ('w'), append mode ('a'), or a mode that allows you to read and write to the file ('r+'). If you omit the mode argument, Python opens the file in read-only mode by default.

# Writing Multiple Lines
# one needs to add '\n' so that text is added to a new line
filename='Python/Files and Exceptions/programming.txt'
with open(filename,'w') as f:
    f.write('I love programming\n')
    f.write('I love creating new games\n')
