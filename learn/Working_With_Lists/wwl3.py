#Slicing a list
#print(list_name[index_a:index_b]), prints the first three elements in a list, returning elements at indices 0,1,2
players=['Adam','James','Rodriguez','Mathew','Hammonds']
print("List slice from index 0-3: ",players[0:3])
print("List subset from index 1-4 : ",players[1:4])
#to slice a list from a specific index to the end of the list leave index_b empty print(list_name[index_a:])
print(players[2:])
#to print kth last list of elements, use a -ve index
#to print last 3 elements, we would use print(list_name[-3:])
print("Last 3 elements from the list: ", players[-3:])