#Looping Through an Entire List
#using a for loop to print entries in a list
magicians=['alice', 'david', 'carolina']
for m in magicians:
    print(m)
#More things can also be printed using for loops
for m in magicians:
    print(f"{m.title()},that was a great trick")
    print(f"i cant wait to see your next trick, {m.title()}")
print("\nThankyou everyone, that was a great show!")