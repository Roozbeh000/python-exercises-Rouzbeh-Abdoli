# Question 08

balance=int(input("Enter your balance:"))
withdraw=int(input("Enter your withdraw:"))
if withdraw <= 0:
    print("Error: Your withdraw must be greater than 0.")
elif withdraw <= balance:
    balance = balance - withdraw
    print("Withdraw successful.")
    print("Remaning balance:", balance)
else:
    print("Error: Insufficient Balance.")