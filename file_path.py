from pathlib import Path # import the path library
import os
my_files = ['accounts.txt', 'details.csv', 'invite.docx', 'report.pdf']
for filename in my_files:
    print(Path(r'C:/Users/Boye/HP/Documents/', filename))

print(Path.cwd())  # prints the current working directory
print(Path.home())  # prints the home directory


