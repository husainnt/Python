#copying a list
#list_name[:]->indicates that we mean a complete list, from start to end
my_foods=['pizza', 'falafel', 'carrot cake']
friend_foods=my_foods[:]
#now to cpy this list we will use list_name[:]->copies the list asking for a slice without specifying the index
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
#to prove both lists are separate, we'll add items to them
my_foods.append('pasta')
friend_foods.append('steak')
print(my_foods)
print(friend_foods)