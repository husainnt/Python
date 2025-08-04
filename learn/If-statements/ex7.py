# Print all numbers that are multiples of 3 from the list
nums = [3, 5, 9, 12, 17, 21, 25]
mult_of_3=[]
for n in nums:
    if n%3==0:
        mult_of_3.append(n)
print(mult_of_3)
