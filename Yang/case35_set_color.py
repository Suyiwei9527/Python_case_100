#文本颜色设置。
'''1.设置颜色的格式'\033[显示方式；前景色(也就是字体颜色）；背景色。（可以显示方式、前景色、背景色一起设置，顺序也可以打乱，也可以只设置一个或两个）
   2.以\033[的方式设置颜色的话需要以\033[0m（关闭所有设置)结尾，否则后面输出的东西都会被设置为这个颜色
   3.表述显示方式、前景色、背景色的数值范围：
     显示方式：0 1 4 5 7 8，不同数值代表不同的显示方式
        0： 代表默认显示方式，关闭所有设置，恢复默认
        1： 高亮显示
        4： 下划线
        5： 闪烁
        7： 反显
        8： 隐藏
     前景色：30-37，不同数值代表不同的颜色
     背景色：40-47，不同数值代表不同的颜色
     黑底彩色:90-97(感觉跟前景色一样的功能，字体颜色也没啥区别)
'''
#三个属性一起设置
print("\033[4;32;45m 三个属性一起配置，下划线，前景色32，背景色45 \033[m")
#显示方式
print("下面是显示方式")
print ("\033[0m 默认显示方式，关闭所有设置，恢复默认" )
print ("\033[1m 高亮显示\033[0m" )
print ("\033[4m 下划线 \033[0m" )
print ("\033[5m 闪烁 \033[0m")
print ("\033[7m 反显 \033[0m" )
print ("\033[8m 隐藏 \033[0m" )
#前景色，也就是字体颜色
print("下面是前景色")
print("\033[30m 30 \033[0m")
print("\033[31m 31 \033[0m")
print("\033[32m 32 \033[0m")
print("\033[33m 33 \033[0m")
print("\033[34m 34 \033[0m")
print("\033[35m 35 \033[0m")
print("\033[36m 36 \033[0m")
print("\033[37m 37 \033[0m")
#背景色
print("下面是背景色")
print("\033[40m 40 \033[0m")
print("\033[41m 41 \033[0m")
print("\033[42m 42 \033[0m")
print("\033[43m 43 \033[0m")
print("\033[44m 44 \033[0m")
print("\033[45m 45 \033[0m")
print("\033[46m 46 \033[0m")
print("\033[47m 47 \033[0m")
#黑底彩色
print("下面是黑底彩色")
print("\033[90m 90 \033[0m")
print("\033[91m 91 \033[0m")
print("\033[92m 92 \033[0m")
print("\033[93m 93 \033[0m")   
print("\033[94m 94 \033[0m")
print("\033[95m 95 \033[0m")
print("\033[96m 96 \033[0m")
print("\033[97m 97 \033[0m")