import socket

def get_ip_from_domain(domain):
    try:
        # Get the IP address for the domain
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return "Could not resolve domain name to IP"
    except Exception as e:
        return f"Error: {str(e)}"

# Specific IP to check
target_ip = "142.250.186.174"
domain = "google.com"

# Get the resolved IP
resolved_ip = get_ip_from_domain(domain)
print(f"Resolved IP for {domain}: {resolved_ip}")

# Note: We can't force it to return 142.250.186.174 specifically,
# but we can verify if that IP belongs to the domain
try:
    # Reverse lookup to verify the IP
    hostname = socket.gethostbyaddr(target_ip)[0]
    print(f"Domain for {target_ip}: {hostname}")
    if "google" in hostname.lower():
        print(f"{target_ip} is associated with Google")
    else:
        print(f"{target_ip} is not directly associated with Google")
except socket.herror:
    print(f"No domain information found for {target_ip}")



# The IP address returned for "google.com" can vary because Google uses multiple servers 
# and load balancing. The IP 142.250.186.174 might be one of Google's valid IPs, 
# but DNS resolution won't always return that specific address. However, 
# I can modify the code to show you how to work with IP resolution and 
# even check if that specific IP is associated with Google:


# When you run this:
# 1. It first resolves "google.com" to whatever IP your DNS returns
# 2. Then it checks if 142.250.186.174 resolves back to a Google-related domain

# Why you might not get 142.250.186.174:
# - DNS load balancing distributes traffic across many IPs
# - Your location affects which Google server you connect to
# - The resolved IP changes based on DNS servers and time

# Sample output might look like:
# Resolved IP for google.com: 142.250.190.78  # This will vary
# Domain for 142.250.186.174: fra16s50-in-f14.1e100.net
# 142.250.186.174 is associated with Google

# Note: "1e100.net" is a domain owned by Google, often used for their servers.

# If you specifically need to work with 142.250.186.174, you could hardcode it, 
# but the DNS lookup won't guarantee that exact IP for "google.com". 
# Let me know if you'd like to modify this further!