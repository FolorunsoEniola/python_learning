# This will make a list containing the range
num = []
def make_list():
    for i in range(0,10):
        num.append(i)
    return num
    
print(make_list())
#This finds all the divisors of a number
x = int(input('Enter your number:'))
y = []
for i in range(1, x+1):
    if x % i == 0:
        y.append(i)
print(y)