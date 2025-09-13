a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
def list(define):# defined the function to iterate through a list
    result = [] # store the variable in a list
    for num in define: # for num in the list 
          if num < 5:
               result.append(num) # add the ones that meet the condition into the list
    return result       # return the list that's been updated
print(list(a)) # this works well for other lists
# this only works for a, it's better to use the above def. that can be used for multiple lists
for num in a: #iterates through the list
     if num < 5:
          print(num)
#This checks the list and compare if the number is greater or less than input
def check_number(element):
    mylist = []
    check = int(input('let\'s check your number:'))
    for new in element:
        if check > new:
            mylist.append(new)
    return mylist
print(check_number(a))
        



