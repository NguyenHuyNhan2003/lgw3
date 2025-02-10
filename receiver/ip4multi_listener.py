import socket
import struct

MULTICAST_GROUP = '224.0.0.1'  
PORT = 5002
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', PORT))

mreq = struct.pack("4sl", socket.inet_aton(MULTICAST_GROUP), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
print(f"Listening for Multicast messages on {MULTICAST_GROUP}:{PORT}...")
while True:
    data, addr = sock.recvfrom(1024)
    print(f"Received multicast from {addr}: {data.decode()}")
