import ipaddress

# Define a network (IP + subnet mask)
network = ipaddress.ip_network("192.168.1.0/32", strict=False)

# Print all IPs in the subnet
print("All IPs in the subnet:")
for ip in network.hosts():  # .hosts() skips network and broadcast IPs
    print(ip)

# Count usable IPs
usable_ips = sum(1 for _ in network.hosts())
print(f"Number of usable IPs: {usable_ips}")