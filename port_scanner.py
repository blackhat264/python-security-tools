#!/usr/bin/env python3
"""Simple multi-threaded TCP port scanner"""

import socket
import sys
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"[+] Port {port} is open")
    except Exception:
        pass

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <IP>")
        sys.exit(1)

    target = sys.argv[1]
    print(f"Scanning {target}...")

    common_ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 3389, 8080]

    with ThreadPoolExecutor(max_workers=50) as executor:
        for port in common_ports:
            executor.submit(scan_port, target, port)

if __name__ == "__main__":
    main()
