# Using function within a while loop
def person_name(first_name,last_name):
    full_name=f"{first_name},{last_name}"
    return full_name
while(True):
    print("Tell me your name")
    print("(Enter 'q' to quit.)")
    first=input("First name: ")
    if first=='q':
        break
    last=input("Last name: ")
    comp_name=person_name(first,last)
    print(f"Hello, {comp_name}")
    '''Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.'''
def make_album(singer,album):
    numb_1={'name': singer, 'alb': album}
    return numb_1
while True:
    print("Enter your favorite singer and their favorite album: ")
    print("(press 'q' to quit)")
    singerr=input("Singer Name: ")
    albumm=input("Album: ")
    if singerr=='q':
        break
    album_info = make_album(singerr, albumm)
    print(album_info)


