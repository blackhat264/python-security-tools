#!/usr/bin/env python3
"""Simple TCP banner grabber"""

import socket
import sys

def grab_banner(ip, port, timeout=3):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((ip, port))
            banner = s.recv(1024).decode(errors="ignore").strip()
            if banner:
                print(f"[{ip}:{port}] {banner}")
            else:
                print(f"[{ip}:{port}] No banner received")
    except Exception as e:
        print(f"[{ip}:{port}] Error: {e}")

def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <IP> <PORT>")
        sys.exit(1)

    target = sys.argv[1]
    port = int(sys.argv[2])
    grab_banner(target, port)

if __name__ == "__main__":
    main()
