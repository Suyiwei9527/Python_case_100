#请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母
first_letter=input('please input the first letter:')
if first_letter=='m' or first_letter=='M': print ('it is monday')
elif first_letter=='w' or first_letter=='W': print ('it is wednesday')
elif first_letter=='f' or first_letter=='F': print ('it is friday')
elif first_letter=='t' or first_letter=='T': 
    second_letter=input('please input the second letter:')
    if second_letter=='u' or second_letter=='U': print('it is tuesday')
    elif second_letter=='h' or second_letter=='H': print('it is thursday')
    else: print('input error')
elif first_letter=='s' or first_letter=='S': 
    second_letter=input('please input the second letter:')
    if second_letter=='a' or second_letter=='A': print('it is saturday')
    elif second_letter=='u' or second_letter=='U': print('it is sunday') 
    else: print('input error')
else: print('input error') 