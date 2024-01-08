import socket
from termcolor import colored

def scan(targets, ports):
    print('\n' + '*** starting scan for' + str(target) + ' ***')
    for port in range(1, ports):
        scan_port(targets, port)

def get_banner(s):
    return s.recv(1024)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipaddress, port))
        try:
            banner= get_banner(sock)
            print('[+} open port ' + str(port) + ' :' + str(banner.decode().strip('\n')))
        except:
            print('[+] open port ' + str(port))
            sock.close()
    except:
        pass

targets = input('[+] enter target to scan: ')
ports = int(input('[+] enter how many ports you wantto scan: '))
if ',' in targets:
    print(colored(("\n[*] scanning multiple targets [*]\n"), 'blue'))
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '),ports)
else:
    scan(targets,ports)