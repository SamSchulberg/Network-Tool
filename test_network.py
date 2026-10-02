import ipaddress
from main import ip_in_network, compare_networks, IPInfo, NetworkInfo

def test_ip_in_network():
    ip = ipaddress.ip_address("192.168.1.50")
    network = ipaddress.ip_network("192.168.1.0/24")

    assert ip_in_network(ip, network) is True

def test_compare_networks_identical():
    network_one = ipaddress.ip_network("192.168.1.0/24")
    network_two = ipaddress.ip_network("192.168.1.0/24")

    assert compare_networks(network_one, network_two) == "\nThese networks are identical"

def test_compare_networks_subnet():
    network_one = ipaddress.ip_network("192.168.1.0/25")
    network_two = ipaddress.ip_network("192.168.1.0/24")
    
    assert compare_networks(network_one, network_two) == f"\n{network_one} is a subnet of {network_two}\n"

def test_compare_networks_subnet_reverse():
    network_one = ipaddress.ip_network("192.168.1.0/24")
    network_two = ipaddress.ip_network("192.168.1.0/25")
    
    assert compare_networks(network_one, network_two) == f"\n{network_two} is a subnet of {network_one}\n"

def test_compare_networks_unrelated():
    network_one = ipaddress.ip_network("192.100.2.0/24")
    network_two = ipaddress.ip_network("190.168.0.0/22")
    
    assert compare_networks(network_one, network_two) == "\nThese networks are unrelated"

def test_ip_info_private():
    ip = ipaddress.ip_address("192.168.10.0")
    info = IPInfo(ip)

    assert info.kind == "Private"

def test_ip_info_public():
    ip = ipaddress.ip_address("8.8.8.8")
    info = IPInfo(ip)

    assert info.kind == "Public"

def test_ip_version_four():
    ip = ipaddress.ip_address("192.168.10.10")
    info = IPInfo(ip)

    assert info.version == "ipv4"

def test_ip_version_six():
    ip = ipaddress.ip_address("::4")
    info = IPInfo(ip)

    assert info.version == "ipv6"

def test_network_info_address():
    network = ipaddress.ip_network("192.168.10.22/24", strict=False)
    info = NetworkInfo(network)

    assert info.network_address == ipaddress.ip_address("192.168.10.0")

def test_network_info_broadcast():
    network = ipaddress.ip_network("192.168.10.22/24", strict=False)
    info = NetworkInfo(network)

    assert info.broadcast_address == ipaddress.ip_address("192.168.10.255")

def test_total_addresses():
    network = ipaddress.ip_network("192.168.10.22/24", strict=False)
    info = NetworkInfo(network)

    assert info.total_addresses == 256

def test_usable_addresses():
    network = ipaddress.ip_network("192.168.10.22/24", strict=False)
    info = NetworkInfo(network)

    assert info.usable_addresses == 254

def test_usable_addresses_32():
    network = ipaddress.ip_network("192.168.10.22/32", strict=False)
    info = NetworkInfo(network)

    assert info.usable_addresses == 1

def test_usable_addresses_31():
    network = ipaddress.ip_network("192.168.10.22/31", strict=False)
    info = NetworkInfo(network)

    assert info.usable_addresses == 2

def test_display_network_info():
    network = ipaddress.ip_network("192.168.10.22/24", strict=False)
    info = NetworkInfo(network)
    output = info.display_network_info()

    assert "network: 192.168.10.0/24" in output
    assert "network address: 192.168.10.0" in output
    assert "broadcast address: 192.168.10.255" in output
    assert "total addresses: 256" in output
    assert "usable addresses: 254" in output

def test_display_network_info_32():
    network = ipaddress.ip_network("192.168.10.22/32", strict=False)
    info = NetworkInfo(network)
    output = info.display_network_info()

    assert "network: 192.168.10.22/32" in output
    assert "network address: 192.168.10.22" in output
    assert "broadcast address: 192.168.10.22" in output
    assert "total addresses: 1" in output
    assert "usable addresses: 1" in output

def test_display_network_info_31():
    network = ipaddress.ip_network("192.168.10.22/31", strict=False)
    info = NetworkInfo(network)
    output = info.display_network_info()

    assert "network: 192.168.10.22/31" in output
    assert "network address: 192.168.10.22" in output
    assert "broadcast address: 192.168.10.23" in output
    assert "total addresses: 2" in output
    assert "usable addresses: 2" in output

def test_display_ip_info():
    ip = ipaddress.ip_address("192.168.10.10")
    info = IPInfo(ip)
    output = info.display_ip_info()

    assert "192.168.10.10" in output
    assert "Type: Private" in output
    assert "Version: ipv4" in output
