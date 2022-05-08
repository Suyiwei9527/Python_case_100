#给定一个字典，然后按键(key)或值(value)对字典进行排序
def dictionairy():
    key_value = {}
    key_value[2] = 231
    key_value[1] = 12123
    key_value[3] = 12
    print(sorted(key_value.items() , key= lambda kv:(kv[1],kv[0])))
def main():
    dictionairy()
if __name__ == "__main__":
    main()