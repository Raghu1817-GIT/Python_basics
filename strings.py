# Positive and negative indexing
str = 'python'
#    p  y  t  h  o  n
#+   0  1  2  3  4  5
#-  -6 -5 -4 -3 -2 -1
# [start : stop]
# [start : stop : step]
# Square brackets can be used to access elements of the string.
print(str[5])
print(str[1])
print(str[-1])
print(str[1:3])
print(str[:3])
print(str[2:])
print(str[:-1])
print(str[::2])
print(str[1::2])
print(str[::-1])

