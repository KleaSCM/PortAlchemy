#python banner_grabber.py

#HTTP Server:
#IP: scanme.nmap.org
#Port: 80
#FTP Server:

#IP: ftp.example.com (Replace with a valid FTP server IP)
#Port: 21
#SSH Server:
#IP: ssh.example.com (Replace with a valid SSH server IP)
#Port: 22


import socket

def grab_banner(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner.decode().strip()
    except Exception as e:
        return str(e)
    finally:
        s.close()

ip = "192.168.1.1"   #update with url
port = 80
print(grab_banner(ip, port))