# Find the sum of all odd numbers in the list
nums = [5, 8, 11, 24, 33, 44]
odd=0
for o in nums:
    if o%2!=0:
        odd= o+odd
    else:
        odd=odd
print(odd)