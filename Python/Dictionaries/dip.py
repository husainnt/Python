#looping through a dictionary
'''user_0={
    'username':'husainn_t',
    'first_name':'Hussain',
    'last_name':'Tahir',
}
for key,value in user_0.items():
    print(f"Key: {key}")
    print(f"Value: {value}\n")
'''
fav_languages={
    'raza':'python',
    'hussain':'c',
    'jennifer':'ruby',
    'edward':'haskell'
}
for n,l in fav_languages.items():
    print(f"The person with the following username:{n} has {l} as his favourite programming language\n")