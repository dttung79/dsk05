a = int(input("Enter a: "))
b = int(input("Enter b: "))

c = a
a = b
b = c

print(f'a: {a}, b: {b}')

a = a + b
b = a - b
a = a - b

print(f'a: {a}, b: {b}')

a, b = b, a
print(f'a: {a}, b: {b}')