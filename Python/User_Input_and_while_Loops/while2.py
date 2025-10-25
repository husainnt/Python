prompt="\nTell me something and i will repeat it back to you:"
prompt+="\nEnter 'quit' to end the program"
active=True
while active:
    msg=input(prompt)
    if msg=='quit':
        active=False
    else:
        print(msg)    

'''We set the variable active to True u so the program starts in an active
state. Doing so makes the while statement simpler because no comparison is
made in the while statement itself; the logic is taken care of in other parts of
the program. As long as the active variable remains True, the loop will continue
running v.
In the if statement inside the while loop, we check the value of message
once the user enters their input. If the user enters 'quit' w, we set active
to False, and the while loop stops. If the user enters anything other than
'quit' x, we print their input as a message.'''
