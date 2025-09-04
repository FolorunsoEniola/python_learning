with open ("show_ip_int_brief.txt", "r") as file:
    content = file.read()
for i in content.splitlines():
    if "10.220" in i:
        field = i.split() 
        print("-" * 70)
        print(f"{field[0]} is with ip addr {field[1]} and the interface is {field[2]} and {field[3]}")
        print("-" * 70)
    else:
        print("line not found")