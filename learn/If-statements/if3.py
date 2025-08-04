#Numreical Comparisons
age=18
print(age==18) #returns true
ans=42
if ans!=41:
    print('That is not the correct answer!')
a1=18
print(a1<21) #->returns true
a2=32
print(a2>35) #->returns false
print((a1>21) and (a2<40)) #->returns false

#checking wether a value is in a list or not?
nums=['10','20','30','40','50']
val_chk='27' #->must be a string too!
if val_chk in nums:
    print(f"The value {val_chk} is present in nums!")
else:
    print(f"The value {val_chk} is not present in nums!")
