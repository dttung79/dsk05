# Each type has its own set of operations.
# int, float: +, -, *, /, //, %, **

a = 10
b = 3

print(a + b)  # addition
print(a - b)  # subtraction
print(a * b)  # multiplication
print(a / b)  # division 
print(a // b) # floor division
print(a % b)  # modulo (get the remainder)
print(a ** b) # power

# use power to calculate square root
print(4 ** 0.5)  # square root of 4

# string: +, *, in, not in
s1 = 'Hello'
s2 = 'World'
print(s1 + s2)  # concatenation

print(s1 * 3)  # repeat 'Hello' 3 times

print('Hell' in s1)  # check if 'Hello' is in s1
print('hell' not in s1)  # check if 'hello' is in s1

# boolean: and, or, not
a = True
b = False
print(a and b)  # logical AND
print(a or b)   # logical OR
print(not a)    # logical NOT