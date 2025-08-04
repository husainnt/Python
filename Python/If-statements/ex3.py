# Given a list of marks, print grade:
# >=90: A, 80-89: B, 70-79: C, 60-69: D, <60: F
marks = [95, 82, 67, 45, 78]
for m in marks:
    if m >= 90:
        print("A")
    elif 80 <= m < 90:
        print("B")
    elif 70 <= m < 80:
        print("C")
    elif 60 <= m < 70:
        print("D")
    else:
        print("F")
