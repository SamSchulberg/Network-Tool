import ipaddress

def get_ip():
    while True:
        ip_input = input("\nEnter an IP address: ")
        try:
            ip = ipaddress.ip_address(ip_input)
            return ip
        except ValueError:
            print(ip_input, "is not valid")

def get_network():
    while True:
        network_input = input("\nEnter a network: ")
        try:
            network = ipaddress.ip_network(network_input, strict=False)
            return network
        except ValueError:
            print("Network is not valid")

def compare_networks(network_one, network_two):
    if network_one == network_two:
        return "\nThese networks are identical"
    elif network_one.subnet_of(network_two):
        return f"\n{network_one} is a subnet of {network_two}\n"
    elif network_one.supernet_of(network_two):
        return f"\n{network_two} is a subnet of {network_one}\n"
    else:
        return "\nThese networks are unrelated"

def ip_in_network(ip, network):
    return ip in network    

class IPInfo:
    def __init__(self, ip):
        self.ip = ip
        self.kind = "Private" if ip.is_private else "Public"
        self.version = f"ipv{ip.version}"

    def display_ip_info(self):
        return f"\n{self.ip}\nType: {self.kind}\nVersion: {self.version}\n"

class NetworkInfo:
    def __init__(self, network):
        self.network = network
        self.network_address = network.network_address
        self.broadcast_address = network.broadcast_address if self.network.version == 4 else "N/A"
        if self.network.version == 4:
            self.total_addresses = network.num_addresses
            if self.total_addresses > 2:
                self.usable_addresses = self.total_addresses - 2
            elif self.total_addresses == 2:
                self.usable_addresses = 2
            else:
                self.usable_addresses = 1
        else: 
            self.total_addresses = network.num_addresses
            self.usable_addresses = "N/A"

    def display_network_info(self):
        return (
            f"\nnetwork: {self.network}\n"
            f"network address: {self.network_address}\n"
            f"broadcast address: {self.broadcast_address}\n"
            f"total addresses: {self.total_addresses}\n"
            f"usable addresses: {self.usable_addresses}\n"
        )

def main():
    while True:
        menu_input = input("Network Tool 1.0\n\nIP Info[1]\nNetwork Info[2]\nIs IP In Network[3]\nCompare Networks[4]\nExit[5]\n")

        if menu_input == "1":
            ip = IPInfo(get_ip())
            print(ip.display_ip_info())
        elif menu_input == "2":
            network = NetworkInfo(get_network())
            print(network.display_network_info())
        elif menu_input == "3":
            if ip_in_network(get_ip(), get_network()):
                print("\nIP is in the network\n")
            else:
                print("\nIP is not in the network\n")
        elif menu_input == "4":
            print(compare_networks(get_network(), get_network()))
        elif menu_input == "5":
            exit()
        else:
            print("invalid\n")
            continue

if __name__ == "__main__":
    main()