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
        line_protocol = parts[-1]
        line_status = " ".join(parts[4:-1])  # join in case of multi-word status

        interfaces[intf] = {
            "ip_addr": ip_addr,
            "line_status": line_status,
            "line_protocol": line_protocol,
        }

print(interfaces)
