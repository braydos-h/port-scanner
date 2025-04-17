import socket
#ill add nmap later to this
def scan_ports(target, start_port, end_port):
    # Create a TCP socket
    print(f"Scanning {target} from port {start_port} to {end_port}...")
    # Loop through the specified port range
    for port in range(start_port, end_port + 1):
        # Create a new socket for each port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for the connection attempt
        sock.settimeout(0.5)  # short timeout
        result = sock.connect_ex((target, port))
        # Check if the port is open (result == 0 means open)
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        sock.close()
# Main function to run the port scanner

#this is this the most basic port scanner you can find on github 
# please do not use this for illegal purposes ☹️
# as thats not ethical
# and i do not condone that
# and i will not be responsible for any illegal activities you do with this code
# even if this code even works
target_host = input("Enter target IP or hostname: ")
start = int(input("Start port: "))
end = int(input("End port: "))
scan_ports(target_host, start, end)
