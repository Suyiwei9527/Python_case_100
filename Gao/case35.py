#文本颜色设置
class bcolors:
    HANDER = '\033[95m'
    WEARING = '\033[93m'
    ENDC = '\033[0m'
print(bcolors.WEARING + "The Wearing colors is" + bcolors.ENDC)