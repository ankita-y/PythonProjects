amt = int(input("Enter the amount you want to invest: "))
duration = input("Do you want to invest monthly or yearly: ")
time = int(input("Enter the duration in {0}: ".format(duration)))
interestrate = float(input("Enter Interest rate in % : "))

if duration == 'monthly':
    amount = (amt * time * interestrate)/100
else:
    time = time * 12
    amount = (amt * time * interestrate)/100

amt = amt * time
print("Total amount invested: ",amt)
print("Total Interest: ",amount)
print("Total Return Amount: ",(amt+amount))




