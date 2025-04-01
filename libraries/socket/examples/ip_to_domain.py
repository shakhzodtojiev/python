import socket

def get_domain_from_ip(ip_address):
    try:
        # Perform reverse DNS lookup
        domain_name = socket.gethostbyaddr(ip_address)[0]
        return domain_name
    except socket.herror:
        return "No domain name found for this IP"
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage
ip = input("Enter IP address: ")
result = get_domain_from_ip(ip)
print(f"Domain name: {result}")

# example
# Enter IP address: 8.8.8.8
# Domain name: dns.google