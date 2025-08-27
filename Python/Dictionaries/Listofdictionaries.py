'''The alien dictionary contains a variety of information about one alien,
but it has no room to store information about a second alien, much less a
screen full of aliens. How can you manage a fleet of aliens?'''
#The following code builds a list of dictionaries.
'''alien_0={'color':'red','points':'5'}
alien_1={'color':'orange','points':'7'}
alien_2={'color':'yellow','points':'9'}
aliens=[alien_0,alien_1,alien_2]
for a in aliens:
    print(a)'''
# Make an empty list for storing aliens.
aliens=[]
# Make 30 green aliens.
for al in range(30):
    new_alien={'color':'green','points':'25'}
    aliens.append(new_alien)
# Show the first 5 aliens
for a in aliens[:5]:
    print(a)
print("...")
# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")
# To understand, read below:
'''At range() returns a series of numbers, which just tells
Python how many times we want the loop to repeat. Each time the loop
runs we create a new alien and then append each new alien to the list
aliens. We use a slice to print the first five aliens, and then we
print the length of the list to prove we’ve actually generated the full fleet of
30 aliens.'''