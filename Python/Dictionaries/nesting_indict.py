#nesting can be done inside dictionaries...
'''In the earlier
example of favorite programming languages, if we were to store each
person’s responses in a list, people could choose more than one favorite
language. When we loop through the dictionary, the value associated with
each person would be a list of languages rather than a single language.
Inside the dictionary’s for loop, we use another for loop to run through
the list of languages associated with each person:'''
favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")