#BMI
height=float(input('Please enter  your height(Metric):'))
weight=float(input('Please enter your weight:'))
bmi=float(weight / (height * height))
print('Your bmi is:%.2f' % bmi)
if bmi > 32:
    print('U are Savere Obesity')    
elif bmi >= 28:
    print('U are Obesity')    
elif bmi >= 25:
    print('U are Too Heavy')   
elif bmi >= 18.5:
    print('U are normal')
else:
    print('U are Too light')  