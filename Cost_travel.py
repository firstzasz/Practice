due = int(input('duration in days : '))
food = int(input('total food cost per a day : '))
flight = 2*int(input('one-way flight cost : '))
hotel = int(input('cost of one night in a hotel : '))
print(due * (food)
+ flight
+ ((due-1) * (hotel))
)
