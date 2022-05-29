#一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
target=input('please input a number with five digit:')
if target[0]==target[4] and target[1]==target[3]: print('it is a huiwenshu')
else: print('it is not a huiwenshu')