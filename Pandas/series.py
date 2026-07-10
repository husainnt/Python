import pandas as pd
'''# converting a integer type list into series
l1=[100,200,300,400,500]
#using the Series const->not a func
s=pd.Series(l1) #->list is passed as arg
print(s)'''

'''# converting a string type list into series
l2=['A','B','C']
sr=pd.Series(l2)
print(sr)'''

''' # we can also pass another arg to the Series const
s = pd.Series(l1, index=["a", "b", "c", "d", "e"]) #->idx change from numb to alphabets
print(s) 

# loc["a var"]->returns value at that label
# print(s.loc["a"])

# changing a value at a loc
s.loc["a"]=900
print(s)

# values can also be accessed use the integer loc->iloc
# iloc[0]->1st val
print(s.iloc[0])

# Filtering by val
print(s[s>=200])'''

# creating a dictionary
calories={
    "Day 1": 1750,
    "Day 2": 2100,
    "Day 3": 1700
}
s2=pd.Series(calories)
print(s2)
# print(s2.loc["Day 1"])
s2.loc["Day 3"]+=500
print(s2)
print(s2[s2>2000])
