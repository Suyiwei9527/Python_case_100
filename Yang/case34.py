#使用函数，输出三次 RUNOOB 字符串。
'''调用自定义模块：
            1. 创建.py文件，例如test.py;
            2. 在test.py中编写函数
            3. 将test.py文件放入任意一个搜索路径中（查看搜索路径的方式： import sys
                                                                     print（sys.path)  
            4. 调用模块中的函数，调用方式：import te st
                                         test.想调用的函数名称（）
'''
import custom_module_used_by_case34
for i in range(3):
    custom_module_used_by_case34.pri_runoob()