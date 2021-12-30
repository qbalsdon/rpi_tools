#!/usr/bin/env python3
import socket

def fetch_ip_address():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

if __name__ == "__main__":
    print(f"IP Address [{fetch_ip_address()}]")
