import subprocess
import argparse

def run_vboxmanage_command(command):
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        print(e.stdout)
        print(e.stderr)

def create_nat_network(network_name, network):
    command = [
        "VBoxManage", "natnetwork", "add",
        "--netname", network_name,
        "--network", network,
        "--enable"
    ]
    run_vboxmanage_command(command)

def configure_dhcp(network_name, ip, netmask, lowerip, upperip):
    command = [
        "VBoxManage", "dhcpserver", "add",
        "--netname", network_name,
        "--ip", ip,
        "--netmask", netmask,
        "--lowerip", lowerip,
        "--upperip", upperip,
        "--enable"
    ]
    run_vboxmanage_command(command)

def main():
    parser = argparse.ArgumentParser(description="Script to configure a DHCP server in VirtualBox using VBoxManage.")
    
    parser.add_argument('--network-name', required=True, help="Name of the internal or NAT network.")
    parser.add_argument('--network', required=True, help="Network address in CIDR format (e.g., 10.0.0.0/8).")
    parser.add_argument('--ip', required=True, help="IP of the DHCP server.")
    parser.add_argument('--netmask', required=True, help="Subnet mask (e.g., 255.0.0.0).")
    parser.add_argument('--lowerip', required=True, help="Lower IP address for the DHCP pool.")
    parser.add_argument('--upperip', required=True, help="Upper IP address for the DHCP pool.")

    args = parser.parse_args()

    create_nat_network(args.network_name, args.network)
    configure_dhcp(args.network_name, args.ip, args.netmask, args.lowerip, args.upperip)

if __name__ == '__main__':
    main()
