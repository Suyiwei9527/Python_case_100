#HTTP/2 RST PACKET
import binascii
def write_hex_data(num_iterations):
    prefix = '00'
    suffix = '00'
    hex2_data = ''
    hex3_data = ''
    with open('Gao/hexnum1.txt', 'wb+') as file:
        hex_data = 'AAAAAAAAAAAAAA'
        for _ in range(num_iterations):
            value = int(hex_data, 16) + 2
            hex_data =format(value, '08X')
            hex2_data =prefix + hex_data + suffix
            hex3_data += hex2_data
            binary_data = binascii.unhexlify(hex3_data)
            #print(binary_data)
            file.write(binary_data)
        print(binary_data)
write_hex_data(500)