# port scanner 
# 127.0.0.1
# 202.4.28.10
# scanme.nmap.org


#import statements
import nmap
import os

def scan_ports(target):
    nm = nmap.PortScanner()
    nm.scan(target, '1-1024')  # Scans ports 1-1024 by default
    
    # Ensure logs directory exists
    logs_dir = r'C:\Users\Kliea\Documents\Development\Python\CybrSuit\PortAlchemy\PortAlchemy\logs'
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
    
    # Define the file path
    file_path = os.path.join(logs_dir, f'scan_results_{target.replace(":", "_")}.txt')

    # Write the scan results to the file
    with open(file_path, 'w') as file:
        for host in nm.all_hosts():
            file.write(f"Host: {host} ({nm[host].hostname()})\n")
            file.write(f"State: {nm[host].state()}\n")
            for proto in nm[host].all_protocols():
                file.write(f"Protocol: {proto}\n")
                lport = nm[host][proto].keys()
                for port in sorted(lport):
                    file.write(f"Port: {port}\tState: {nm[host][proto][port]['state']}\tService: {nm[host][proto][port]['name']}\n")
            file.write("\n")
    
    print(f"Scan results saved to {file_path}")

if __name__ == "__main__":
    target = input("Enter target IP address or range: ")
    scan_ports(target)



