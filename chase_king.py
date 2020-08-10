x = int(input())
y = int(input())
if x in (1, 8):
    if y in (1, 8):
        print('3')
    elif y != x:
        print('5')
elif y in (1, 8):
    print('5')
else: 
    print('8')
