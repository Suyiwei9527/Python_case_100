import urllib.request
import os
from tqdm import tqdm

download_url = "http://192.168.100.101/Build/268.array"
save_folder = r"D:\Python_case_100\Gao"

# 保存文件
file_path = os.path.join(save_folder, "268.array")

# 进度回调函数
def progress_callback(block_num, block_size, total_size):
    progress = block_num * block_size / total_size * 100
    tqdm.write(f"下载进度：{progress:.2f}%")

# 下载文件并显示进度条
with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc="下载进度", ncols=80) as progress_bar:
    urllib.request.urlretrieve(download_url, file_path, reporthook=lambda block_num, block_size, total_size: progress_callback(block_num, block_size, total_size), data=None)
    progress_bar.update()
    
print(f"文件已下载到：{file_path}")