import os
import time
import urllib.request
import threading

download_url = "http://192.168.100.101/Build/268.array"
save_folder = "/Test"

# 回调函数，用于显示下载进度
def progress_callback(count, block_size, total_size):
    percent = int(count * block_size * 100 / total_size)
    print(f"下载进度：{percent}%")

# 保存文件
file_path = os.path.join(save_folder, "268.array")

# 定时打印进度的函数
def print_progress():
    while True:
        # 调用回调函数获取下载进度
        progress_callback(count, block_size, total_size)
        # 每5秒打印一次进度
        time.sleep(5)

# 创建定时打印进度的线程
progress_thread = threading.Thread(target=print_progress)
progress_thread.start()

# 开始下载文件并调用回调函数
urllib.request.urlretrieve(download_url, file_path, progress_callback)

# 等待下载完成
progress_thread.join()