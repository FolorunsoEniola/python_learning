 # see how dictionaries work
 # and also the while loop
# birthdays.py
import json
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4', 'Bunmi': 'Apr 27'}

# Load data from file if it exists
try:
    with open('birthdays.json', 'r') as f:
        birthdays = json.load(f)
except FileNotFoundError:
    pass 
    

# Your while loop here...
while True:
    print('Enter a name: (enter to quit)')
    name = input('name:')
    if name == '':
        break

    if name in birthdays:
       print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')

# Save updated data
with open('birthdays.json', 'w') as f:
    json.dump(birthdays, f)
