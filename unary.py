to_be = True           # to_be is True
not_to_be = not to_be  # not_to_be is False
print(not_to_be)

print('lazy variable')
# division is never evaluated, because the first argument is True
lazy_or = True or (1 / 0)  # True
 
# division is never evaluated, because the first argument is False
lazy_and = False and (1 / 0)  # False