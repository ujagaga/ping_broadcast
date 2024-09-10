#!/usr/bin/python3

import subprocess
import platform
import threading
import ipaddress
import sys
import argparse


def is_host_reachable(host, timeout=2):
    os_type = platform.system()

    # Set the ping command based on the OS
    if os_type == "Windows":
        # For Windows, use '-w' for timeout in milliseconds
        command = ['ping', '-n', '1', '-w', str(timeout * 1000), host]
    else:
        # For Linux/Mac, use '-W' for timeout in seconds
        command = ['ping', '-c', '1', '-W', str(timeout), host]

    try:
        output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return output.returncode == 0
    except Exception as e:
        return False


def scan_ip_range(start_ip, timeout):
    ip = ipaddress.ip_address(start_ip)
    threads = []

    # Start a thread for each IP address
    for i in range(1, 254):
        thread = threading.Thread(target=scan_ip, args=(str(ip + i), timeout))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()


def scan_ip(ip, timeout):
    global host_found_flag

    if is_host_reachable(ip, timeout):
        print(f"\n{ip}", end="", flush=True)
        


def scan_wide(ip_addr, timeout):
    ip_parts = ip_addr.split(".")
    if len(ip_parts) != 4:
        sys.exit("Invalid IP address specified")

    ip_addr_prefix = f"{ip_parts[0]}.{ip_parts[1]}"
    for j in range(0, 254):
        target = f"{ip_addr_prefix}.{j}.1"
        scan_ip_range(target, 2)
        print(".", end="", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan a 16 bit range of IP addresses to check if hosts are reachable.")
    parser.add_argument("-i", "--ip_addr", help="Any IP address in the scan range.", required=True)
    parser.add_argument("-t", "--timeout", type=int, default=2,
                        help="Ping timeout in seconds (default: 2 seconds).", required=False)

    args = parser.parse_args()

    # Call the function to scan the range
    scan_wide(args.ip_addr, args.timeout)
