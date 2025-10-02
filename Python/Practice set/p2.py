# Take a string input (a sentence), split it into words, and use a dictionary to count the frequency of each word.
#Example:
#"the cat and the dog" → { "the": 2, "cat": 1, "and": 1, "dog": 1 }
user_inp = input("Enter a sentence: ")
output = {}   
words = user_inp.split()   # split the sentence into words
for s in words:
    if s in output:
        output[s] += 1 #updating a existing keys value 
    else:
        output[s] = 1 #adding a new key to the dictionary     
print(output)

        

