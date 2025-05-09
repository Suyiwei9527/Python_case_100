#读取文件，输出行数，计算出所有数字、字母个数
n = 0
numn = 0
charnum = 0
with open('trace.log' ,'r' ,encoding = "utf-8") as f:
    for line in f:
        n += 1
        for char in line:
            if char.isdigit():
                numn += 1
            elif char.isalpha():
                charnum += 1
print(f'The file is {n} lines')
print(f'The file has {numn} digits')
print(f'The file has {charnum} alpha')