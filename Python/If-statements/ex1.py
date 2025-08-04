## Given a list of numbers, print whether each number is even or odd.
numbers = [10, 15, 22, 33, 42]
for n in numbers:
    if n%2==0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")