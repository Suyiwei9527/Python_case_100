#一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
target=int(input('pleasr intput a number with five digits:'))
digits=[]
while target>=1:
    digits.append(target%10)
    target=int(target/10)
if digits[4]==digits[0] and digits[3]==digits[1]: print('it is huiwenshu')
else : print('it is not huiwenshu')