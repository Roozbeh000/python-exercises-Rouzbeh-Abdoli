time=int(input("Enter a time:"))
if time <0 or time > 23:
    print("Invalid time")
elif time <= 11:
    print("Morning")
elif time <= 15:
    print("Noon")
elif time <= 18:
    print("Afternoon")
else:
    print("Night")