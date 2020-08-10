def check_email(string):
    a = string.index(".")
    b = string.find(" ") 
    c = string.find("@")
    if b == -1 and c != -1 and (a + 1 != c) and (a - 1 != c):
        return True
    else:
        return False
print(check_email(input()))