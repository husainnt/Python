# Create a dictionary with student names as keys and their grades as values. Ask the user for a student’s name and print their grade. If the name doesn’t exist, print "Student not found".
result={'Raza':'A', 'Xaviyar':'B', 'Hanzla':'C' }
question=input("Enter Name of the student")
for k,v in result.items():
    if(question==k):
        print(f"The grade of the student {k} is: {v}.")
    else:
        print("Student Not found")