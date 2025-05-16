import socket
import argparse

# Common ports to scan
COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP"
}

def banner_grab(ip, port):
    try:
        with socket.create_connection((ip, port), timeout=2) as s:
            return s.recv(1024).decode().strip()
    except:
        return "No banner"

def port_scan(ip):
    print(f"[*] Scanning {ip} for open ports...\n")
    for port in COMMON_PORTS:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((ip, port))
                if result == 0:
                    banner = banner_grab(ip, port)
                    print(f"[+] Port {port} ({COMMON_PORTS[port]}) is OPEN - Banner: {banner}")
        except Exception as e:
            print(f"[-] Error scanning port {port}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Simple Python VAPT Tool")
    parser.add_argument("target", help="Target IP address to scan")
    args = parser.parse_args()

    print(f"\n--- PyVA Scanner ---")
    print(f"Target: {args.target}")
    port_scan(args.target)

if __name__ == "__main__":
    main()
