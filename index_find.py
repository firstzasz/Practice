spell = "Wingardium Leviosa"
a = input()
print(spell.index(a))


email = "my_email@something.com"
print(email.endswith("@", 5, 8))  # False
print(email.endswith("@", 5, 9))  # True
print(email.find("@"))