title = 'Electric Machine Fundamentals'
print(title.split())
# The split() method separates a string into parts wherever it finds a space
# and stores all the parts of the string in a list
filename = 'Python/Files and Exceptions/electric_machine_fundamentals.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file '{filename}' doesn't exist.")
else:
    # Count the approximate number of words in the file
    words = contents.split()
    num_words = len(words)
    print(f"The file '{filename}' has about {num_words} words.")
