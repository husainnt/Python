# passing a list to a function
def greetings(names):
    for n in names:
        print(f"Hello,{n.title()}")

usernames=['anna','james','henry','jason']
greetings(usernames)
# modifying a list in function
def print_models(unfinished_designs,finished_designs):
    while unfinished_designs:
        current=unfinished_designs.pop()
        finished_designs.append(current)

def completed_models_show(finished_designs):
    print("The printed models are: ")
    for f in finished_designs:
        print(f)

unfinished_designs=['phone case', 'robot pendant', 'dodecahedron']
finshed_designs=[]
print_models(unfinished_designs,finshed_designs)
completed_models_show(finshed_designs)
