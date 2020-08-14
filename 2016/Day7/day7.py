from IP import IPAddresses

ip_addresses = IPAddresses("input.txt")
print(f'IPs Supporting TLS = {ip_addresses.supports_tls()}')
print(f'IPs Supporting SSL = {ip_addresses.supports_ssl()}')