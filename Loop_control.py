y = 0
x = int(input())
while y < x:
    if x % y != 0:
        y += 1
        continue
    else:
       print("This number is not prime")
       break
else:
    print("This number is prime")
