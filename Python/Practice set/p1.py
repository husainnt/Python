# Given a list of numbers, print the maximum and minimum number without using Python’s built-in max() and min() functions.
nl=list(range(1,11))
maxx=nl[0]
minn=nl[0]
for n in nl:
     if n>maxx:
        maxx=n
     elif n<minn:
        minn=n
print("Maximum: ",maxx)
print("Minimum: ",minn)

