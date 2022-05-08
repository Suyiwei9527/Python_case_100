#if语句：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示
score = int(input('Please enter your score:'))
if score>100:
    print('Please enter the score less than 100')
elif score >=90:
	print('A')
elif score <60:
	print('C')
else:
	print('B')