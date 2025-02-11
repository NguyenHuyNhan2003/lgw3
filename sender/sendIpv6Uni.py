import socket

TARGET_IP = 'fe80::da3a:ddff:fee4:ec3a%eth0'  
PORT = 6000
MESSAGE = "Hello IPv6 Unicast!"

with socket.socket(socket.AF_INET6, socket.SOCK_DGRAM) as s:
    s.sendto(MESSAGE.encode(), (TARGET_IP, PORT))
    print(f"Sent message to {TARGET_IP}:{PORT}")
