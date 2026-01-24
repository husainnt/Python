# to read from a file: with open('using full path file_name.extension') as file_object:
#                        var=file_object.read()
#print(var)

# reading data from 'pi_digits.txt'
with open('Python/Files and Exceptions/pi_digits.txt') as f:
    contents = f.read()
print(contents)

print('\n')
# reading line by line
'''filename='Python/Files and Exceptions/pi_digits.txt'
with open(filename) as f:
    for line in f:
        print(line)'''

# to eliminate extra blank lines we use .rstrip()
filename='Python/Files and Exceptions/pi_digits.txt'
with open(filename) as f:
    for line in f:
        print(line.rstrip())

print('\n')
#printing a list of lines from a file
with open(filename) as f:
    lines=f.readlines()
for l in lines:
    print(line.rstrip())