from rich import print

interfaces = {}

with open("show_ip_int_brief.txt") as f:
    for line in f:
        # Skip header line
        if line.startswith("Interface") or line.strip() == "":
            continue
        
        parts = line.split()
        intf = parts[0]
        ip_addr = parts[1]
        
        if ip_addr != "unassigned":  # Skip unassigned IPs
            interfaces[intf] = ip_addr

print(interfaces)
