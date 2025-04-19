import requests
import re
import os
import datetime
import urllib.request

build_version = "_APV_8_6_1_"
build_prefix_pre = "ArrayOS-"
url_suffix = "rel_apv_8_6_1.html"
build_sufix = ".array"

# 获取当前日期
now = datetime.datetime.now().strftime("%Y/%m/%d")
#now1 = datetime.datetime.now()
#delta = datetime.timedelta(days=58)
#now = (now1 - delta).strftime("%Y/%m/%d")
#print(now)
# 构造build页面的URL
url = "http://10.3.0.120/newapv/build/" + url_suffix

# 发送请求，获取页面内容
response = requests.get(url)
content = response.content.decode('iso-8859-1')

save_folder = "D:\Build"

# 使用正则表达式匹配build标题
pattern = r'(Beta|Rel){version}(\d+) \(build on (\d+)\:(\d+) {date} '.format(date=now,version=build_version)
#print(pattern)
match = re.search(pattern, content)
#f = open("Gao/url_infosec_apv.txt" , "w+",encoding="utf-8")
#f.write(content)
#f.close()
#print(match)
# 如果匹配成功
if match:
    # 获取build数字和时间信息
    build_num = match.group(2)
    build_version_prefix = match.group(1)
    build_prefix = build_prefix_pre + build_version_prefix + build_version
    
# 回调函数，用于显示下载进度
    def progress_callback(count, block_size, total_size):
        percent = int(count * block_size * 100 / total_size)
        print(f"Download progress：{percent}%")

    # 构造下载链接
    download_url = "http://10.3.0.120/newapv/build/" + build_prefix + "{}".format(build_num) + build_sufix
    #download_url = "http://192.168.100.101/Build/ArrayOS-Beta_APV_10_4_3_{}.array".format(build_num)
    # 下载文件
    file_path = os.path.join(save_folder, build_prefix + "{}".format(build_num) + build_sufix)
    if not os.path.exists(file_path):
        urllib.request.urlretrieve(download_url, file_path, progress_callback)
        print("Downloaded " + build_prefix + "{}".format(build_num) + build_sufix + " to {} successfully!".format(file_path))
    else:
        print("U have downloaded the build on {}.".format(now))
else:
    # 如果匹配失败，打印错误信息
    print("Failed to download build on {}.".format(now))