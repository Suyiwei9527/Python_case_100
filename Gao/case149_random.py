import random
import os
seclength = 33
def contextRandom():
    global ItemVale
    global ItemLen
    alphabet = '1234567890abcdefghijklmnopqrstuvwxyz' * 10000000
    random_len = int(1000)
    #random_len = random.randint(1, seclength)
    print('随机值：{},type:{}'.format(random_len,type(random_len)))
    ItemLen = random_len
    #ItemLen = random_len + 31
    print('>>>secStore 随机长度是：{}'.format(ItemLen))
    ItemVale = ''.join(random.sample(alphabet, random_len))
    #ItemVale = ''.join(random.sample(alphabet, random_len)) + '123456@jodie_sec_write_read_del'
    print('>>>secStore 随机内容是：{}'.format(ItemVale))
    return ItemLen,ItemVale
contextRandom()
f = open("Gao/random1000.txt" , "w+",encoding="utf-8")
f.write(ItemVale)
f.close()