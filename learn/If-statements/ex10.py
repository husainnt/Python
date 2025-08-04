# From the list, print all prime numbers
nums = [2, 4, 5, 6, 9, 11, 13, 15, 17]

for n in nums:
    if n < 2:
        continue  # 0 and 1 are not prime
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n)
