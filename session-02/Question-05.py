# Question-05

distance=float(input("Enter the distance(km):"))
if distance<=2:
    fare=20000
else:
    fare=20000 +(distance -2) * 5000
print("You need to pay:", fare)
