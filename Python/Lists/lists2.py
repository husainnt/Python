#sorting a list sot()
cars=['bmw','audi','toyota','subaru']
cars.sort() #sorts in alphabetical order
print(cars)
#to sort in reverse alphabetical order, use sort(reverse=True)
cars.sort(reverse=True)
print(cars)
#to temporarily sor the list use sorted(list name)
m1="Here is the original list: "
print(f"{m1}{cars}")
m2="Here is the list sorted: "
print(f"{m2}{sorted(cars)}")
m3="Here is the original list again: "
print(f"{m3}{cars}")