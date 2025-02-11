import socket

BROADCAST_IP = '255.255.255.255'
PORT = 5001
MESSAGE = "Hello Ipv4 Broadcast!"
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.sendto(MESSAGE.encode(), (BROADCAST_IP, PORT))
    print(f"Broadcast message sent to {BROADCAST_IP}:{PORT}")