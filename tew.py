x = int(input())
if x < 100:
    print('x < 100')
    print("x less than 100")
else:
    if x == 100:
        print('x = 100')
    else:
        print('x > 100')
    print('This will be printed only because x >= 100')
    input('confirm ?')
print('This will be printed only because x < 100')    