# Write a program that takes a list of integers and counts how many are even and how many are odd.
numbers = []
count_even = 0
count_odd = 0
for n in range(1, 11):
    n = int(input(f"Enter the {n} number: "))  # Convert input to int
    numbers.append(n)
for i in numbers:
    if i % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print(f"Count of even numbers is: {count_even}")
print(f"Count of odd numbers is: {count_odd}")
