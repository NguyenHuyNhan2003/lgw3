import socket

MULTICAST_GROUP = '224.0.0.1'
PORT = 5002
MESSAGE = "Hello Ipv4 Multicast!"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

sock.sendto(MESSAGE.encode(), (MULTICAST_GROUP, PORT))
print(f"Sent multicast message to {MULTICAST_GROUP}:{PORT}")