# XOR is true if a and b are difference
print('exclsive or')
#change a and b value from TT TF FT FF to check all case
a = False
b = True
# to check if whicj one result the same as XOR with the variables' value above
print(not a or b)
print((a or b) and not (a and b))
print((a and b) or not (a or b))
print((a and not b) or (not a and b))
print(a and not b)
