# The json module allows you to dump simple Python data structures into a file and load the data from that file the next time the program runs. You can also use json to share data between different Python programs.

# The json.dump() function takes two arguments: a piece of data to store and a file object it can use to store the data.
import json
numbers=[2,3,5,7,11,13]
filename='Python/Files and Exceptions/numbers.json'
with open(filename,'w') as f:
    json.dump(numbers,f)

# Now we’ll write a program that uses json.load() to read the list back into memory
with open(filename) as f:
    numbrs=json.load(f)
    print(numbrs)