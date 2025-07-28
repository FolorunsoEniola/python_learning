import zipfile
with open('bacon.txt', 'w') as files:
    files.write('Hello' * 1000,)
    # note the zipfile and ZipFile
    # the zipfile is the name of the module
    # the ZipFile is the name of the function
with zipfile.ZipFile('bacon.zip', 'w') as myzip:
    myzip.write('bacon.txt', compress_type=zipfile.ZIP_DEFLATED)
