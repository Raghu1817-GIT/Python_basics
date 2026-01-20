
'''
a = int(input("enter a:"))
b = int(input("enter b:"))
temp = a
a = b
b = temp
print("value of a is:",a)
print("value of b is:",b)
'''
a = int(input("enter a:"))
b = int(input("enter b:"))
b = b+ a
a = b-a
b = b-a

print("value of a is:",a)
print("value of b is:",b)