from pathlib import Path
import os
# Create a new directory
try:
    os.mkdir('/home/captainboye/python_learning/new_directory')
except FileExistsError:
    print("Directory already exists.")

# Create a Path object for the new directory
p = Path('/home/captainboye/python_learning')
print(p.exists())  # Check if the directory exists
print(p.is_dir())  # Check if it is a directory
p.glob('*.py')  # List all Python files in the directory
print(p.glob('*.py'))  # List all Python files in the directory
print(list(p.glob('*.py')))  # Convert the generator to a list
for namee in Path('/home/captainboye/python_learning').iterdir():  # Iterate through items in the directory
    print(namee)  # Print each item in the directory

#check if flash drive is attached
flash_drive = Path('/media/captainboye/FLASH_DRIVE')
d_drive = Path('D:/')
if flash_drive.exists() and d_drive.exists():
    print("Flash drives are attached.")
elif flash_drive.exists():
    print("Flash drive is attached")
elif d_drive.exists():
    print("D drive is attached.")
else:
    print("ooops no Flash drive is attached.")