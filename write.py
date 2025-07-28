bacon_file = open("bacon.txt", "w")
bacon_file.write("Hello world!\n")
bacon_file.close()
bacon_shop = open("bacon.txt", "a")
bacon_shop.write("Bacon is not a vegetable.\n")
bacon_shop.close()
bacon_shop = open("bacon.txt", "r")
content = bacon_shop.read()
bacon_shop.close()
print(content)

#alternatively using same variable to call all commands
bacon_file = open("bacon.txt", "w")
bacon_file.write("Hello world!\n")
bacon_file.close()
bacon_file = open("bacon.txt", "a")
bacon_file.write("Bacon is not a vegetable.\n")
bacon_file.close()
bacon_file = open("bacon.txt", "r")
content = bacon_file.read()
bacon_file.close()
print(content)

# another alternative using with statement
# this is the preferred way to handle files in Python as it automatically closes the file
with open("bacon.txt", "w") as bacon_file:
    bacon_file.write("Hello world!\n")
with open("bacon.txt", "a") as bacon_file:
    bacon_file.write("Bacon is not a vegetable.\n")
with open("bacon.txt", "r") as bacon_file:
    content = bacon_file.read()
print(content)

from pathlib import Path
h = Path.home() # this opens the home directory
g = h / 'python_learning' # this opens the home/python_learning directory
with open(g / 'toomuch.txt', 'w') as f: # open g as file in w mode
    f.write('i want to write to this file\n and this is the second line ')
     # write with .write method
    


