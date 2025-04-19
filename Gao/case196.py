import binascii
import socket

def hex_to_decimal(hex_string):
    decimal = int(hex_string, 16)
    return decimal

def decimal_to_hex(decimal):
    hex_string = hex(decimal)[2:]
    if len(hex_string) % 2 != 0:
        hex_string = '0' + hex_string
    return hex_string

def host_to_network(hex_string):
    byte_string = binascii.unhexlify(hex_string)
    network_byte_string = socket.htonl(int.from_bytes(byte_string, byteorder='big'))
    network_hex_string = network_byte_string.hex()
    return network_hex_string

def network_to_host(hex_string):
    byte_string = binascii.unhexlify(hex_string)
    host_byte_string = socket.ntohl(int.from_bytes(byte_string, byteorder='big'))
    host_hex_string = host_byte_string.hex()
    return host_hex_string

# 示例用法
host_hex_string = '01020304'
network_hex_string = host_to_network(host_hex_string)
network_decimal = hex_to_decimal(network_hex_string)
print("Network Hex: ", network_hex_string)
print("Network Decimal: ", network_decimal)

host_hex_string = network_to_host(network_hex_string)
host_decimal = hex_to_decimal(host_hex_string)
print("Host Hex: ", host_hex_string)
print("Host Decimal: ", host_decimal)
