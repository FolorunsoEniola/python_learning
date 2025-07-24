import csv #import to read a .csv file
from pprint import pprint     #import pprint for the output to be set and well arranged

with open('portfolio.csv', 'r') as f: # open a file and set the mode
    f_csv = csv.reader(f)             # read the file with csv.reader
    headers = next(f_csv)             # the next command will skip the header
    rows = list(f_csv)                # this command defines every list as a role
    pprint(rows)                      # will arrange the output better than just print
