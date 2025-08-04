# Print the largest number in the list
nums = [12, 78, 3, 45, 89, 1]
largest =0
for n in nums:
    if n>largest:
        largest=n
    else:
        largest=largest
print(largest)