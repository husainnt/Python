content = 'Python/Files and Exceptions/sample.txt'
#Read entire file
with open(content) as f:
    data = f.read()
    print(data)
print('\n')
#Loop over the file object
with open(content) as f:
    for line in f:
        print(line)
print('\n')
#Store lines in a list and work with them later
with open(content) as f:
    lines = f.readlines()
for line in lines:
    print(line)
