m = int(input("enter maths marks:"))
s = int(input("enter science marks:"))
e = int(input("enter english marks:"))
Averagemarks = (m+s+e)/3
print(f"Total marks:{m+s+e}\nAverage marks:{(m+s+e)/3}")
#percentage = ((m+s+e)/300)*100
if Averagemarks > 90:
    print("Grade:A")
elif Averagemarks > 80:
    print("Grade:B")
elif Averagemarks > 70:
    print("Grade:C")
elif Averagemarks > 60:
    print("Grade:D")
else:
    print("Grade:F")
