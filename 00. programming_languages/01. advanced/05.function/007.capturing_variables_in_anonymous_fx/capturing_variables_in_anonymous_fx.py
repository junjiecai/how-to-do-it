x = 10
a = lambda y: x + y
print(a(10))

x = 20
b = lambda y: x + y
print(b(10))
print(a(10))

x = 10
a = lambda y, x=x: x + y
x = 20
b = lambda y, x=x: x + y

print(a(10))
print(b(10))