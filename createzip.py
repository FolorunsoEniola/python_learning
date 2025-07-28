import zipfile
with open('bacon.txt', 'w') as files:
    files.write('Hello' * 1000,)
with zipfile.ZipFile('bacon.zip', 'w') as myzip:
    myzip.write('bacon.txt', compress_type=zipfile.ZIP_DEFLATED)
