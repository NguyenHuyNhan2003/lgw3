import socket

def send_ipv4_unicast():
    TARGET_IP = '10.12.1.22'  
    PORT = 5000
    MESSAGE = "Hello Ipv4 Unicast!"
    
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(MESSAGE.encode(), (TARGET_IP, PORT))
        print(f"Sent message to {TARGET_IP}:{PORT}")
        
def send_ipv4_broadcast():
    BROADCAST_IP = '255.255.255.255'
    PORT = 5001
    MESSAGE = "Hello Ipv4 Broadcast!"
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.sendto(MESSAGE.encode(), (BROADCAST_IP, PORT))
        print(f"Broadcast message sent to {BROADCAST_IP}:{PORT}")
        
def send_ipv4_multicast():
    MULTICAST_GROUP = '224.0.0.1'
    PORT = 5002
    MESSAGE = "Hello Ipv4 Multicast!"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

    sock.sendto(MESSAGE.encode(), (MULTICAST_GROUP, PORT))
    print(f"Sent multicast message to {MULTICAST_GROUP}:{PORT}")

def send_ipv6_unicast():
    TARGET_IP = 'fe80::da3a:ddff:fee4:ec3a%eth0'  
    PORT = 6000
    MESSAGE = "Hello IPv6 Unicast!"

    with socket.socket(socket.AF_INET6, socket.SOCK_DGRAM) as s:
        s.sendto(MESSAGE.encode(), (TARGET_IP, PORT))
        print(f"Sent message to {TARGET_IP}:{PORT}")
          
def send_ipv6_multicast():
    MULTICAST_GROUP = 'ff02::1'
    PORT = 6001
    MESSAGE = "Hello IPv6 Multicast!"
    sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_HOPS, 2)

    sock.sendto(MESSAGE.encode(), (MULTICAST_GROUP, PORT))
    print(f"Sent multicast message to {MULTICAST_GROUP}:{PORT}")
    
def run_menu():
    option = 0
    print("Enter 1 for IPv4 Unicast\n"+
        "Enter 2 for IPv4 Broadcast\n"+
        "Enter 3 for IPv4 Multicast\n"+
        "Enter 4 for IPv6 Unicast\n"+
        "Enter 5 for IPv6 Multicast\n"+
        "Enter 0 to exit\n")
    while True:
        option = int(input("Pick your option:\n"))
        if option == 1:
            send_ipv4_unicast()
        if option == 2:
            send_ipv4_broadcast()
        if option == 3:
            send_ipv4_multicast()
        if option == 4:
            send_ipv6_unicast()
        if option == 5:
            send_ipv6_multicast()
        if option == 0:
            break
        else:
            continue

if __name__ == "__main__":
    run_menu()