import socket

HOST = '0.0.0.0'
PORT = 5001
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Listening for Broadcast messages on {PORT}...")
    while True:
        data, addr = s.recvfrom(1024)
        print(f"Received broadcast from {addr}: {data.decode()}")