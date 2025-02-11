import socket

TARGET_IP = '10.12.1.22'  
PORT = 5000
MESSAGE = "Hello Ipv4 Unicast!"
 
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(MESSAGE.encode(), (TARGET_IP, PORT))
    print(f"Sent message to {TARGET_IP}:{PORT}")