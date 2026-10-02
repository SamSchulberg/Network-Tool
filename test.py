import ipaddress

x = ipaddress.ip_network("192.168.10.0", strict=False)
print(x)
print(type(x))