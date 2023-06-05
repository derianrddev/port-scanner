## Network Port Scanner

This is a Python program that allows you to scan ports on a specific device or a network of devices. It utilizes socket connections and supports TCP and UDP transport protocols.

### Key Features

- Allows the user to choose between scanning a specific device or a network of devices.
- Provides an option to scan the first 1024 ports on a device or a custom range of ports.
- Uses socket connections to perform port scanning.
- Verifies the availability of IP addresses by sending ping packets before scanning the ports.
- Displays open ports on each discovered IP address.

### Usage Instructions

1. Clone the repository or download the files to your local machine.
2. Run the `port_scanner.py` file from the command line.
3. Follow the on-screen instructions to select the scan type and provide the IP address or network in CIDR format.
4. Select the transport protocol (TCP or UDP).
5. Enter the range of ports you want to scan.
6. The program will display the open ports on each discovered IP address.