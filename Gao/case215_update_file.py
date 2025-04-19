import os
import datetime
now = datetime.datetime.now().strftime("%Y-%m-%d")

def rewrite_last_line(file_path, new_content):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    if lines:
        lines[-1] = new_content

    with open(file_path, 'w') as file:
        file.writelines(lines)

# 用法示例
file_path = 'D:\Build\Auto_Download_Build List.txt'
new_content = "Updated on " + now
rewrite_last_line(file_path, new_content)