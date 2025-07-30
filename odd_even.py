#Still testing my if and conditional statement
# if can use % as reminder,/,+,-,==,!=,<,>,<=,>=
print('Welcome, This is my even or odd play')
ask = int(input('Enter a number:'))
if ask % 2 == 0:
    print(f"The number {ask} is Even")
else:
    print(f"The number {ask} is Odd")
if ask % 4 == 0:
    print(f'{ask} is a multiple of 4')
num = int(input('Enter a number again:'))
check = int(input('enter another number:'))

if num % check == 0:
    print(f'{check} divides {num} evenly')
else:
    print(f'{check} does not divide {num} evenly')