income = int(input())
if income <= 15527:
    percent = 0
elif income <= 42707:
    percent = 15
elif income <= 132406:
    percent = 25
elif income >= 132407:
    percent = 28
calculated_tax = round(percent / 100 * income)
print(f'The tax for {income} is {percent}%. That is {calculated_tax} dollars!')
