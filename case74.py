#列表排序及连接 连接a b两个列表
if __name__ == "__main__":
    a = [123,3,545,2]
    b = [4,5,6]
    a.sort()
    print(a)
    print(a+b)
    a.extend(b)
    print(a)