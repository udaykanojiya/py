import math
a = 3
b = 4.5
c = "Hello, World!"
d = True
e = None

print(type(a))

print(str(a) + " is of type " + str(type(a)))

# f = int(input("Enter a number: "))
# print(f"{f} is of type {type(f)}")

a = 34
b = 80
if(a>b):
    print(f"{a} is greater than {b}")
else:
    print(f"{a} is less than {b}")

print((a+b)/2)

print(math.pow(2, 4))