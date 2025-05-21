def is_prime(n):
    if n < 1:
        return False
    if n == 1 or n == 2:
        return True
    
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
        
    return True

def print_primes(n):
    for i in range(n):
        if is_prime(i):
            print(i, end=' ')
    print()
    
def print_mult_table(n):
    print(f'Multiplication of {n}')
    for i in range(1, 11):
        print(f'{i} x {n} = {i*n}')

def print_triangle(n):
    for i in range(1, n+1):
        print('* ' * i)

def print_menu():
    print('1. Print primes.')
    print('2. Print multiplecation table.')
    print('3. Print triangle of characters.')
    print('0. Exit.')

def main():
    running = True
    while running:
        # ask user to enter n
        n = int(input('Enter n: '))
        # print menu
        print_menu()
        # ask user to choose an option
        choice = int(input('Enter your choice: '))
        # do a task based on option
        if choice == 1:
            print_primes(n)
        elif choice == 2:
            print_mult_table(n)
        elif choice == 3:
            print_triangle(n)
        elif choice == 0:
            running = False
        else:
            print('Invalid choice')


####   MAIN PROGRAM ####   
main()