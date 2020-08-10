# lower = str.lower(str(input()))
name = str.lower(input())
print(name.replace(",", "").replace(".", "").replace("!", "").replace("?", ""))