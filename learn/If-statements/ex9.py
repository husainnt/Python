# Create a new list from the original that only includes unique elements (no duplicates)
nums = [2, 5, 2, 7, 9, 5, 7, 10]
new_list = []

for n in nums:
    if n not in new_list:
        new_list.append(n)

print(new_list)


