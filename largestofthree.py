a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
largest = max(a,b,c)

''''largest = a

if b > largest:
    largest = b
if c > largest:
    largest = c
'''
'''if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
'''
print("Largest number is:", largest)