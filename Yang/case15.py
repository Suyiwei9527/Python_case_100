#利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
score=float(input("please input score:"))
if score>90: grade='A'
if score>60 and score<89:grade='B'
if score<60: grade='c'#python3 定义字符串要带引号
print("The grade of %f points is %s"%(score,grade))