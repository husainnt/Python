# Return values
# simple return values
def get_formatted_name(first_name,last_name):
    full_name=f"{first_name} {last_name}"
    return full_name.title()
musician=get_formatted_name('jimi','hendrix')
print(musician)

# optional arguments
# adding middle name as a optional argument
def formatted_name(first_name,middle_name=None,last_name=None):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician=formatted_name('jimi','hendrix')
print(musician)
musician=formatted_name('jimi','hooker','hendrix')
print(musician)
# returning a dictionary
def build_person(first_name, last_name):
    person={'first':first_name, 'last':last_name}
    return person
musician=build_person('jimi','hendrix')
print(musician)