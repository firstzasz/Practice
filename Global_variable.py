Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x, y = 1, 2

def foo():
    global y
    #global x if global x not declar, any change to x in this.function won't affect x's value in global.
    if y == 2:
        x = 2
        y = 1
        print(x,y)

foo()    # no global x, no change to x's value.
print(x)
print(y)
if y == 1:
    x = 3
print(x)