hex_data = "12345678987654323abcdef54565"
binary_data = format(int(hex_data, 16), "08b")
with open("Gao/gao_bug.bin", "wb+") as f:
    f.write(int(binary_data, 2).to_bytes((len(binary_data) + 7) // 8, byteorder="big"))
print(binary_data)