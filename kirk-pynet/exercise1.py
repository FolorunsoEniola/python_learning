#begin exercise1.pyReference code for these exercises is posted on GitHub at:
#from line line 3 to line 25 is a the exercise description
"""  
   https://github.com/twin-bridges/learning_python/tree/main/lesson3/exercises


1. This exercise expands on the subnet calculations from lesson2, exercise1.

Create a base address variable and set it to "192.168.254.". Prompt a user to enter a subnet prefix length that ranges between 25 to 30 (i.e. the netmask length of the subnets). Save this input as an integer.

From the entered subnet prefix length, calculate the size of the subnet (the number of total IP addresses in the subnet). Once we know the subnet size, we can calculate the number of hosts allowed in the subnet (subtract off the network number and the broadcast address).

Use a loop to print out all of the subnet network numbers. For example, if your prefix length is 26, then your program should print out the following:
​Subnets:
 Number of subnets: 4
 Subnet Number: 192.168.254.0
 Subnet Number: 192.168.254.64
 Subnet Number: 192.168.254.128
 Subnet Number: 192.168.254.192

Your program should print out the following:
The number of hosts in the subnet.
The total number of subnets and the network number for each of the subnets
The first and last host address in just the first subnet.
"""

base_address = "192.168.254."
prefix_length = input("(Enter the prefix length between 25-30):")
prefix_length = int(prefix_length)
if prefix_length < 25 or prefix_length > 30:
    print("Invalid prefix length. Please enter a value between 25 and 30.")
    exit()
def calculate_subnet_mask(prefix_length):
    mask = [0, 0, 0, 0]
    for i in range(prefix_length):
        mask[i // 8] += 1 << (7 - (i % 8))
    return ".".join(map(str, mask))
subnet_mask = calculate_subnet_mask(prefix_length)
number_of_subnets = 2 ** (prefix_length - 24)
hosts_per_subnet = 2 ** (32 - prefix_length) - 2
totalip_addresses = 2 ** (32 - prefix_length)
subnetipaddresses = []
for i in range(number_of_subnets):
    subnetipaddresses.append(f"{base_address}{i * (256 // number_of_subnets)}")
print("Subnets:")
print(f"Number of Subnets: There are {number_of_subnets} subnets")
for ip in subnetipaddresses:
    print(ip)
print(f"IP Addresses per subnet: {totalip_addresses}")
print(f"Subnet Mask: {subnet_mask}")
print(f"Available Hosts per Subnet: {hosts_per_subnet}")

first_subnet = subnetipaddresses[0]
firsthost = f"{base_address}1"
lasthost = f"{base_address}{totalip_addresses - 2}"
print(f"First Subnet: {first_subnet}")
print(f"First Host: {firsthost}")
print(f"Last Host: {lasthost}")
#end exercise1.py