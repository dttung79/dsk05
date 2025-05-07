P = float(input('Enter the original amount: '))
r = float(input('Enter the interest rate: '))
n = int(input('Enter number of interest periods: '))
t = int(input('Enter number of years: '))

A = P * (1 + r / n) ** (n * t)
print(f'The amount after {t} years is: {A:.2f}')