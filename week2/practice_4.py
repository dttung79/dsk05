# constant
PI = 3.14   # convention: constant name should be in all caps, ex: PI, TAX_RATE

radius = float(input('Enter the radius of the circle: '))
area = PI * (radius ** 2)

print('Area of the circle is:', area)

# print with formatting
print(f'Area of the circle is: {area}')
print(f'Area of the circle is: {area:.2f}')  # 2 decimal places

# align output
print(f'Area of the circle is: +{area:<10}+')  # left align
print(f'Area of the circle is: +{area:>10}+')  # right align
print(f'Area of the circle is: +{area:^10}+')  # center align


