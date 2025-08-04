# Store the locations in a list (not in alphabetical order)
places_to_visit = ['estonia', 'iceland', 'california', 'auckland', 'liverpool']

# Print the list in its original order
print("Original list:", places_to_visit)

# Print the list in alphabetical order without modifying the original list
print("Alphabetical order (temporary):", sorted(places_to_visit))

# Show that the original list is still in its original order
print("Original list after sorted():", places_to_visit)

# Print the list in reverse alphabetical order without modifying the original list
print("Reverse alphabetical order (temporary):", sorted(places_to_visit, reverse=True))

# Show that the original list is still in its original order
print("Original list after reverse sorted():", places_to_visit)

# Use reverse() to change the order of the list
places_to_visit.reverse()
print("List after reverse():", places_to_visit)

# Use reverse() again to get back to the original order
places_to_visit.reverse()
print("List after second reverse():", places_to_visit)

# Use sort() to change the list to alphabetical order
places_to_visit.sort()
print("List after sort() in alphabetical order:", places_to_visit)

# Use sort() to change the list to reverse alphabetical order
places_to_visit.sort(reverse=True)
print("List after sort() in reverse alphabetical order:", places_to_visit)
