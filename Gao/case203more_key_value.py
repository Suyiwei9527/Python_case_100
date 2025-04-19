import random
import string

def write_to_file(content):
    with open("Gao/h2_header_more.txt" , "w+",encoding="utf-8") as file:
        file.write(content)

def generate_random_string(length):
    chars = string.digits + string.ascii_letters + "-*/;,/"
    return ''.join(random.choice(chars) for _ in range(length))

def generate_headers_dict(num_dicts, num_keys, num_chars):
    all_header = ""
    for i in range(1, num_dicts + 1):
        headers = {}
        for j in range(1, num_keys + 1):
            sub_key = f'headers{i}_{j}'
            value = generate_random_string(num_chars)
            headers[sub_key] = value
        dic_header =  f'headers{i} = {headers}' + "\n"
        all_header += dic_header
        #print(all_header)
        write_to_file(all_header)

generate_headers_dict(100, 50, 3)