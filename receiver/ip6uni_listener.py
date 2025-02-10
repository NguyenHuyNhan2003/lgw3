import socket

HOST = '::'
PORT = 6000
with socket.socket(socket.AF_INET6, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))    
    print(f"Listening for IPv6 Unicast messages on {HOST}:{PORT}...")
    while True:
        data, addr = s.recvfrom(1024)
        print(f"Received message from {addr}: {data.decode()}")