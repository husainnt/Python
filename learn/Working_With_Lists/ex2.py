mill=list((range(1,1000000)))
print(sum(mill))
print(min(mill))
print(max(mill))
#printing odd numbers from 1-20
for o in range(1,20,2):
    print(o)
#list comprehension to generate cubes of numbers from 1-10
cbs=[c**3 for c in range(1,9)]
print(cbs)