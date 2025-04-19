import urllib.request
import os
from tqdm import tqdm

download_url = "http://192.168.100.101/Build/268.array"
save_folder = r"D:\Python_case_100\Gao"

# 回调函数，用于显示下载进度
def progress_callback(count, block_size, total_size):
    percent = int(count * block_size * 100 / total_size)
    print(f"Download progress：{percent}%")

# 保存文件
file_path = os.path.join(save_folder, "268.array")
urllib.request.urlretrieve(download_url, file_path, progress_callback)

print(f"文件已下载到：{file_path}")