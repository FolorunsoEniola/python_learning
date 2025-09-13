userlist = []
passlist = []
username = input("Enter username: ")
password = input("Enter password: ")
userlist.append(username)
passlist.append(password)
if username in userlist and password in passlist:
    print("hello " + username + " login successful")
else:
    print("login failed")
    userlist.remove(username)


 