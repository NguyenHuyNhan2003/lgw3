import socket
import struct

MULTICAST_GROUP = 'ff80::1'
PORT = 6001
sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', PORT))

group = socket.inet_pton(socket.AF_INET6, MULTICAST_GROUP)
mreq = group + struct.pack('@I', 0)
sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_JOIN_GROUP, mreq)
print(f"Listening for IPv6 Multicast messages on {MULTICAST_GROUP}:{PORT}...")
while True:
    data, addr = sock.recvfrom(1024)
    print(f"Received multicast from {addr}: {data.decode()}")