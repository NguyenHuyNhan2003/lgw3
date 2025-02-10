import socket
 
HOST = '0.0.0.0'  # listening to all ip
PORT = 5000
 
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Listening for Unicast messages on {HOST}:{PORT}...")
    while True:
        data, addr = s.recvfrom(1024)
        print(f"Received message from {addr}: {data.decode()}")