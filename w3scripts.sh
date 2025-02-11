ip addr add 10.12.1.11/24 dev eth0 #set IP
route add -net 224.0.0.0 netmask 240.0.0.0 dev eth0 # add device 2 to multicast 224.0.0.0
sysctl net.ipv4.icmp_echo_ignore_broadcasts=0 #enable echo reply
# systemctl restart NetworkManager