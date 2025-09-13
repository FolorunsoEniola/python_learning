test = ("my very energetic monster just scarfed nachos")
newtest = test.split()
length = len(newtest)
print("the length of test words is " + str(length))#concatenate str + int converted to str
print("lets test this out " + "will it print correctly?")# concatenate two strings


# Another test
print("Welcome to the program!")
print(' what is your age?')
myage = input('>')
print(' your were ' + str(int(myage) - 1) + " " + 'last year')# concatenate strings by also converting integre to string
print('you are ' + myage + ' years old now')# concatenate strings plus output of input whic is also a string
print(' your will be ' + str(int(myage) + 1) + " " + 'next year')