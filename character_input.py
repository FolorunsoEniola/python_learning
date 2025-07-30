#I am using this to do basic python that calculates age and the year you'll turn 100
name = input('what is your name:')
current = input('what is your age:')
remain = 100 - int(current)
year = int(input("what is the current year:"))
age = year + int(remain)

mesg = (f'Hello {name}, you\'re {current} years old and will be 100 in {age} \n')
print(mesg)
times = int(input("how many times should i print:"))
out = mesg * times
print(out)


