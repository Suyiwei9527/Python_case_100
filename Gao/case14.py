i =int (input('Please input integer:'))
if i == 1:
    print("1")
while i not in [1] :
    for n in range (2, i+1):
        if i % n == 0:
            i = i // n
            if i == 1:
                print(n)
            else:
                print('{} *' .format(n), end=" ")
            break