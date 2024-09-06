This script creates the NAT network and configures the DHCP server based on the arguments you provide.

1. Run the script with the necessary arguments. For example:

```bash
python3 vbox_dhcp_setup.py --network-name intnet --network 10.0.0.0/8 --ip 10.0.0.1 --netmask 255.0.0.0 --lowerip 10.0.0.2 --upperip 10.255.255.254
```
