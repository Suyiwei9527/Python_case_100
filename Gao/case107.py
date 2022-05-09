#创建自定义函数 is_number() 方法来判断字符串是否为数字
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        for i in s:
            unicodedata.numeric(i)
        return True
    except (TypeError , ValueError):
        pass
    return False