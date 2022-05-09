#输入某年某月某日，判断这一天是这一年的第几天？
list= [0,31,59,90,120,151,181,212,243,273,304,334]
year=int (input ('请输入年份：'))
month=int (input ('请输入月份：'))
day=int (input ('请输入天：'))
print (year,month)
if month<0 and month<13:
    result=list[month]+day
    if year%4==0 and month>2:
        result=result+1
if (month<1 or month>12 or day<0 or day>31 or year<0 or (month==2 and year%4==0 and day>29) or (month==2 and year%4!=0 and day>28) or (month==4 or month==6 or month==9 or month==11 and day>30)):
    print ("date error!")