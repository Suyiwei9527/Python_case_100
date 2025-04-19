import string
import random

# 生成随机字符串的函数
def random_string(length):
    # 定义字符集
    characters = string.ascii_letters + string.digits
    
    # 使用random.choices方法从字符集中随机抽取字符，构成长度为length的字符串
    return ''.join(random.choices(characters, k=length))

# 设置输出文件路径和大小
output_path = "3x65535"
output_size = 65535 * 3 * 1 # 100M

# 打开输出文件，以二进制写入模式打开
with open(output_path, 'wb+') as f:
    # 计算需要生成多少次100MB的块，并在最后一次中生成剩余字节数量的随机字符串
    num_blocks, remainder = divmod(output_size, 1 * 1 * 1)
    
    # 循环生成每个100MB的块
    for i in range(num_blocks):
        # 生成一个100MB的随机字符串
        block = random_string(1 * 1 * 1)
        
        # 将块写入文件
        f.write(block.encode())
    
    # 如果还有剩余字节，则生成剩余字节数量的随机字符串并写入文件
    if remainder > 0:
        block = random_string(remainder)
        f.write(block.encode())