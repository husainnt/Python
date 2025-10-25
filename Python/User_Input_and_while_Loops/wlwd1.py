# using while loop with dictionaries
# Filling a dictionary with user inputs
responses={}
# Set a Flag to indicate that polling is active
polling_active=True
while polling_active:
    # Prompt for the persons name and response
    name=input("\nWhat is your name?")
    repsonse=input("Which mountain would you like to climb someday?")
    # Store the response in the dictionary
    responses[name]=repsonse
    # Find out if anybody else is going to take the poll
    repeat=input("Would you like to let another person respond? (yes/no)")
    if repeat=='no':
        polling_active=False

# Polling is complete show the result
print("\n---Poll Results---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}")

