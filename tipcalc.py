bill=int(input("Please enter bill cost:"))
print(bill)
tip=input("Enter if the service was bad, okay, good, or great:")
bad=bill*0
okay=bill*0.15
good=bill*0.2
great=bill*0.25
print("This is your tip:")
if tip == bad:
    print(bad)
if tip == okay:
    print(okay)
if tip == good:
    print(good)
if tip == great:
    print(great)
