'''Make a list called sandwich_orders and fill it with the names of various
sandwiches. Then make an empty list called finished_sandwiches. Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list
of finished sandwiches. After all the sandwiches have been made, print a
message listing each sandwich that was made.'''

sandwich_orders=['cheese steak','cuban','reuben','corque']
finished_sandwiches=[]
counter=0
while counter<len(sandwich_orders):
    print(f"\nI made your {sandwich_orders[counter]}!")
    finished_sandwiches.append(sandwich_orders[counter])
    counter+=1
print("\n")
for s in finished_sandwiches:
    print(f"The following sandwich: {s} has been made!")