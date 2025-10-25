'''Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.'''
pizza_toppings = []
while True:
    topping = input("Enter a pizza topping (or type 'quit' to stop): ")
    if topping.lower() == 'quit':
        break
    else:
        pizza_toppings.append(topping)
        print(f"I'll add {topping} to your pizza.")
print("\nYour pizza will have the following toppings:")
for item in pizza_toppings:
    print(f"- {item}")
