def bkdrhash(hash_str):
    HASH_MAX_STRING_LEN = 100
    hash_seed = 131  # 哈希种子值，可以根据需要进行调整
    hash_value = 0
    count = 0

    for char in hash_str:
        hash_value = hash_value * hash_seed + ord(char)
        count += 1
        if count >= HASH_MAX_STRING_LEN:
            break
    hash_value &= 0xFFFFFFFF
    print(hash_value) 
bkdrhash("172.17.1.150605661704986699")