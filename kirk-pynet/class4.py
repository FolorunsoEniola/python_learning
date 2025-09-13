mydict = {'rtr1': '10.100.1.1', 'rtr2': '10.100.2.1', 'rtr3': '10.100.100.1'
          , 'rtr4': '10.99.1.1'}
print(mydict)
print(type(mydict))
for k in mydict:
    print(k)
for v in mydict.values(): # this returns only values
    print(v)
for k, v in mydict.items(): # this returns both key and value
    print(f'the key {k} has {v} as value')
retval = mydict.pop('rtr4') # this removes the key and returns the value
print(f'removed {retval}')
print(mydict)
