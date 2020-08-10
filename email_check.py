email = input()
a = email.index(".") 
b = email.find(" ") 
c = email.find("@")
if b == -1 and c != -1 and (a + 1 != c) and (a - 1 != c):
    print("true")
    print(a)
    print(b)
    print(c)
else:
   print("trueeda")
   print(a)
   print(b)
   print(c)