#strings behave same way as lists, they have indexes

ask = input('what do you want to check:')
msg = (len(ask)) #5
a = []
b = []
#This iterates through the ask string from start to end
for c in ask[0:msg]:
    a.append(c)
#This iterates through the ask string from the end to the start
for d in ask[msg::-1]:#[msg-1::-1] is also okay
    b.append(d)       #[msg:0:-1] will iterate from back but won't add index 0 
if a == b:
    print(f'{ask} is a palindrome')
else:
    print('try this again')
print(a)
print(b)




