#!/usr/bin/env python3
import socket

def fetch_ip_address():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

def get_ip_address():
    ip_address = '';
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address

if __name__ == "__main__":
    print(f"IP Address [{fetch_ip_address()}] vs [{get_ip_address()}]")
