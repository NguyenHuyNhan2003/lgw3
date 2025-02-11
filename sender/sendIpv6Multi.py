import socket

MULTICAST_GROUP = 'ff02::1'
PORT = 6001
MESSAGE = "Hello IPv6 Multicast!"
sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_HOPS, 2)

sock.sendto(MESSAGE.encode(), (MULTICAST_GROUP, PORT))
print(f"Sent multicast message to {MULTICAST_GROUP}:{PORT}")