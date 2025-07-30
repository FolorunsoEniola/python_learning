# to check for common elements between two lists
# This will have duplicates
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for i in a:
    for j in b:
        if i == j:# it'll print every line that matches and even duplicates
            c.append(j)
print(c)

#To remove the duplicate
d = []
for p in a:
    for q in b:
        # compare p objects with q, where there's replicate that's already
        #in d[], it'll jump over it
        if p == q not in d:# if p == q and q not in d: will also work
            d.append(q)
print(d)
import random
y = []
z = []
o = []
for w in range(0,10):
    y.append(random.randint(0,20))
    z.append(random.randint(0,20))
for value in y:
    if value in z and value not in o:# The IN will check the values in a list
        o.append(value)
               #OR
for check in z:
    # The == will check if the values are the same
    if value == check and value not in o:
        o.append(value)
    
y.sort()
z.sort()
print(y)
print(z)
print(o)


